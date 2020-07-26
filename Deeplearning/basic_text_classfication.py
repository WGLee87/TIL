#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install tf-nightly')


# In[2]:


import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization

print(tf.__version__)


# ###### Download and explore the IMDB dataset

# In[3]:


url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

dataset = tf.keras.utils.get_file("aclImdb_v1.tar.gz", url,
                                    untar=True, cache_dir='.',
                                    cache_subdir='')

dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')


# In[4]:


os.listdir(dataset_dir)


# In[5]:


train_dir = os.path.join(dataset_dir, 'train')
os.listdir(train_dir)


# In[10]:


sample_file = os.path.join(train_dir, 'pos/1181_9.txt')
with open(sample_file) as f:
    print(f.read())


# ###### Load the dataset

# In[11]:


remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)


# In[12]:


batch_size = 32
seed = 42

raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/train', 
    batch_size=batch_size, 
    validation_split=0.2, 
    subset='training', 
    seed=seed)


# In[13]:


for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(3):
        print("Review", text_batch.numpy()[i])
        print("Label", label_batch.numpy()[i])


# In[14]:


print("Label 0 corresponds to", raw_train_ds.class_names[0])
print("Label 1 corresponds to", raw_train_ds.class_names[1])


# In[15]:


raw_val_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/train', 
    batch_size=batch_size, 
    validation_split=0.2, 
    subset='validation', 
    seed=seed)


# In[16]:


raw_test_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/test', 
    batch_size=batch_size)


# ###### Prepare the dataset for training

# In[18]:


def custom_standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
    return tf.strings.regex_replace(stripped_html,
                                  '[%s]' % re.escape(string.punctuation),
                                  '')


# In[19]:


max_features = 10000
sequence_length = 250

vectorize_layer = TextVectorization(
    standardize=custom_standardization,
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length)


# In[20]:


# Make a text-only dataset (without labels), then call adapt
train_text = raw_train_ds.map(lambda x, y: x)
vectorize_layer.adapt(train_text)


# In[22]:


def vectorize_text(text, label):
    text = tf.expand_dims(text, -1)
    return vectorize_layer(text), label


# In[23]:


# retrieve a batch (of 32 reviews and labels) from the dataset
text_batch, label_batch = next(iter(raw_train_ds))
first_review, first_label = text_batch[0], label_batch[0]
print("Review", first_review)
print("Label", raw_train_ds.class_names[first_label])
print("Vectorized review", vectorize_text(first_review, first_label))


# In[24]:


print("1287 ---> ",vectorize_layer.get_vocabulary()[1287])
print(" 313 ---> ",vectorize_layer.get_vocabulary()[313])
print('Vocabulary size: {}'.format(len(vectorize_layer.get_vocabulary())))


# In[25]:


train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)


# ###### Configure the dataset for performance

# In[26]:


AUTOTUNE = tf.data.experimental.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)


# ###### Create the model
#     It's time to create our neural network:

# In[27]:


embedding_dim = 16


# In[28]:


model = tf.keras.Sequential([
  layers.Embedding(max_features + 1, embedding_dim),
  layers.Dropout(0.2),
  layers.GlobalAveragePooling1D(),
  layers.Dropout(0.2),
  layers.Dense(1)])

model.summary()


# ###### Loss function and optimizer

# In[29]:


model.compile(loss=losses.BinaryCrossentropy(from_logits=True), optimizer='adam', metrics=tf.metrics.BinaryAccuracy(threshold=0.0))


# ###### Train the model

# In[31]:


epochs = 10
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs)


# ###### Evaluate the model

# In[32]:


loss, accuracy = model.evaluate(test_ds)

print("Loss: ", loss)
print("Accuracy: ", accuracy)


# ###### Create a plot of accuracy and loss over time

# In[33]:


history_dict = history.history
history_dict.keys()


# In[40]:


acc = history_dict['binary_accuracy']
val_acc = history_dict['val_binary_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

# "bo" is for "blue dot"
plt.plot(epochs, loss, 'bo', label='Training loss')
# b is for "solid blue line"
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()


# In[35]:


plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')

plt.show()


# ###### Export the model

# In[41]:


export_model = tf.keras.Sequential([
  vectorize_layer, model, layers.Activation('sigmoid')])

export_model.compile(
    loss=losses.BinaryCrossentropy(from_logits=False), optimizer="adam", metrics=['accuracy']
)

# Test it with `raw_test_ds`, which yields raw strings
loss, accuracy = export_model.evaluate(raw_test_ds)
print(accuracy)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 연습문제

# In[ ]:


get_ipython().system('pip install tf-nightly')


# In[ ]:


import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization


print(tf.__version__)


# ###### Download the BigQuery dataset

# In[55]:


url = "http://storage.googleapis.com/download.tensorflow.org/data/stack_overflow_16k.tar.gz"

dataset = tf.keras.utils.get_file("stack_overflow_16k.tar.gz", url,
                                    untar=True, cache_dir='.',
                                    cache_subdir='')


# In[113]:


batch_size = 32

raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'train', batch_size=batch_size, validation_split=0.2, subset='training', seed=42)

raw_val_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'train', batch_size=batch_size, validation_split=0.2, subset='validation', seed=42)

raw_test_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'test', batch_size=batch_size)


# ###### Explore the data

# In[114]:


print(raw_train_ds.class_names)


# In[126]:


for text_batch, label_batch in raw_train_ds.take(1):
    for i in range(3):
        print("Review", text_batch.numpy()[i])
        print("Label", label_batch.numpy()[i])


# ###### Prepare data for training

# In[116]:


max_features = 5000
embedding_dim = 128
sequence_length = 500

vectorize_layer = TextVectorization(
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length)


# In[117]:


# Make a text-only dataset (no labels) and call adapt
text_ds = raw_train_ds.map(lambda x, y: x)
vectorize_layer.adapt(text_ds)


# ###### Vectorize the data

# In[119]:


def vectorize_text(text, label):
    text = tf.expand_dims(text, -1)
    return vectorize_layer(text), label

train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)


# ###### Configure the dataset for performance

# In[120]:


AUTOTUNE = tf.data.experimental.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)


# ###### Build the model¶
#     This model has not be tuned in any way, the goal is to show you the mechanics.

# In[104]:


model = tf.keras.Sequential([
  layers.Embedding(max_features + 1, embedding_dim),
  layers.Dropout(0.2),
  layers.GlobalAveragePooling1D(),
  layers.Dropout(0.2),
  layers.Dense(4)]) # 위의 예제와 여기서 차이를 보임 0,1 일땐 2 이지만 여기서는 4가지의 언어기 때문에 4


# In[121]:


model.compile(
    loss=losses.SparseCategoricalCrossentropy(from_logits=True), 
    optimizer='adam', 
    metrics=['accuracy'])


# ###### Train the model

# In[122]:


history = model.fit(
    train_ds, validation_data=val_ds, epochs=5)


# ###### Evaluate the model

# In[123]:


loss, accuracy = model.evaluate(test_ds)

print("Loss: ", loss)
print("Accuracy: ", accuracy)

