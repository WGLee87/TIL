#!/usr/bin/env python
# coding: utf-8

# In[112]:


import matplotlib
from matplotlib import font_manager, rc
import platform

try :
    if platform.system() == 'windows':
        # windows의 경우
        font_name = font_manager.FomntProperties(fname="c:/Windows/Font")
        rc('font', family = font_name)
    else:
        # mac의 경우
        rc('font', family = 'AppleGothic')
except :
    pass

matplotlib.rcParams['axes.unicode_minus'] = False


# In[82]:


# !pip install tensorflow


# In[4]:


import tensorflow as tf
tf.__version__


# In[14]:


a = tf.constant([1, 2, 3, 4, 5, 6])
a


# In[16]:


b = tf.constant([[1, 2, 3], [4, 5, 6]])


# In[17]:


tf.reshape(a, (2,3))


# In[26]:


a = tf.range(6, dtype=tf.int32)
b = 2 * tf.ones(6, dtype=tf.int32)

a.numpy(), b.numpy()


# In[28]:


tf.add(a,b), tf.add(a,b).numpy(), (a + b).numpy()


# ###### 선형회귀모형 with tensorflow

# In[41]:


w0 = tf.constant([[3.0], [5.0]])
w0.numpy()


# In[42]:


X = tf.concat([tf.ones((10, 1)), tf.random.normal((10, 1))], 1)
X.numpy()


# In[46]:


y_target = tf.matmul(X, w0) + tf.random.normal((10, 1))
y_target.numpy()


# In[47]:


w = tf.constant([[0.0], [0.0]])
y_predict = tf.matmul(X, w)
y_predict.numpy()


# In[48]:


plt.plot(X[:, 1], y_target, "ro")
plt.plot(X[:, 1], y_predict, "b-")
plt.show()


# In[50]:


loss = tf.reduce_sum(tf.square(y_target - y_predict))
loss.numpy()


# In[59]:


w = tf.constant([[3.0], [3.0]])
y_predict = tf.matmul(X, w)
y_predict.numpy()


# In[60]:


loss = tf.reduce_sum(tf.square(y_target - y_predict))
loss.numpy()


# In[61]:


plt.plot(X[:, 1], y_target, "ro")
plt.plot(X[:, 1], y_predict, "b-")
plt.show()


# In[62]:


w = tf.constant([[3.0], [5.0]])
y_predict = tf.matmul(X, w)
y_predict.numpy()


# In[64]:


loss = tf.reduce_sum(tf.square(y_target - y_predict))
loss.numpy()


# In[65]:


plt.plot(X[:, 1], y_target, "ro")
plt.plot(X[:, 1], y_predict, "b-")
plt.show()


# In[81]:


w_hat = tf.linalg.inv(tf.matmul(tf.transpose(X),X))*tf.matmul(tf.transpose(X),y_target)
w_hat


# In[ ]:





# In[ ]:





# In[ ]:


x = tf.Variable(tf.constant(1.0))

with tf.GradientTape() as tape:
    y = tf.multiply(5, x)

gradient = tape.gradient(y, x) 
gradient.numpy()


# In[ ]:


x1 = tf.Variable(tf.constant(1.0))
x2 = tf.Variable(tf.constant(1.0))

with tf.GradientTape() as tape:
    y = tf.multiply(x1, x2)

gradients = tape.gradient(y, [x1, x2]) 
gradients[0].numpy(), gradients[1].numpy()


# In[ ]:





# In[ ]:





# * 최적화

# In[85]:


x = tf.constant(5.0)  # x = 5
w = tf.Variable(tf.constant(0.0))  # w의 초깃값

@tf.function
def train_step():
    with tf.GradientTape() as tape:
        y = tf.multiply(w, x)
        loss = tf.square(tf.subtract(y, 50))

    gradient = tape.gradient(loss, w)
    mu = 0.01
    w.assign_sub(mu * gradient)


# In[86]:


for i in range(10):
    train_step()
    print("{:1}:{:4.3}".format(i, w.numpy()))


# In[90]:


from tensorflow import keras

optimizer = keras.optimizers.SGD()

x = tf.constant(5.0)  # x = 5
w = tf.Variable(tf.constant(0.0))  # w의 초깃값

@tf.function
def train_step():
    with tf.GradientTape() as tape:
        y = tf.multiply(w, x)
        loss = tf.square(tf.subtract(y, 50))

    gradient = tape.gradient(loss, w)
    optimizer.apply_gradients([(gradient, w)])
    
for i in range(10):
    train_step()
    print("{:1}:{:4.3}".format(i, w.numpy()))


# In[96]:


x = tf.Variable(tf.constant(5.0))  # x = 5
w = tf.Variable(tf.constant(0.0))  # w의 초깃값
b = tf.Variable(tf.constant(0.0))  # b의 초깃값

@tf.function
def train_step():
    with tf.GradientTape() as tape:
        y = tf.add(tf.multiply(x, w), b)
        loss = tf.square(tf.subtract(y, 50))

    variables = [w, b]
    gradients = tape.gradient(loss, variables)
    optimizer.apply_gradients(zip(gradients, variables))
    return loss

for i in range(15):
    loss = train_step()
    print("{:2}:w={:6.5f}, b={:6.5f}, loss={:10.5f}".format(i, w.numpy(), b.numpy(), loss.numpy()))


# ###### 선형회귀 모형

# In[110]:


# 가중치 변수
w = tf.Variable(tf.random.normal((2, 1)))

@tf.function
def model_predict(X):
    return tf.matmul(X, w)
    
@tf.function
def train_step(X, y_target):
    with tf.GradientTape() as tape:
        y_predict = model_predict(X)
        loss = tf.reduce_sum(tf.square(y_target - y_predict))

    gradient = tape.gradient(loss, w)
    optimizer.apply_gradients([(gradient, w)])
    return loss


# 정답인 가중치 벡터
w0 = tf.constant([[3.0], [5.0]])

# 입력 데이터 행렬
X = tf.concat([tf.ones((10, 1)), tf.random.normal((10, 1))], 1)

# 목표값 벡터
y_target = tf.matmul(X, w0) + tf.random.normal((10, 1))

losses = []
w_0s = []
w_1s = []
for i in range(20):
    loss_value = train_step(X, y_target)
    losses.append(loss_value)
    
    w_0 = w.numpy()[0][0]
    w_1 = w.numpy()[1][0]
    w_0s.append(w_0)
    w_1s.append(w_1)
    
    print(f"[{i:02d}] loss: {loss_value:7.3f}, w_0: {w_0:3.2f}, w_1: {w_1:3.2f}")


# ###### 보스턴 주택가격으로

# In[117]:


from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['const'] = np.ones(df.shape[0])
# 자료형을 float로 통일
X = tf.constant(df.values, dtype=tf.float32)
y_target = tf.constant(boston.target.reshape(-1, 1), dtype=tf.float32)

# 가중치 변수
w = tf.Variable(tf.zeros((X.shape[1], 1)))

@tf.function
def model_predict(X):
    return tf.matmul(X, w)

optimizer = keras.optimizers.SGD(learning_rate=6e-9)
@tf.function
def train_step(X, y_target):
    with tf.GradientTape() as tape:
        y_predict = model_predict(X)
        loss = tf.reduce_sum(tf.square(y_target - y_predict))

    gradient = tape.gradient(loss, w)
    optimizer.apply_gradients([(gradient, w)])
    return loss

for i in range(100000):
    loss_value = train_step(X, y_target)
    if (i % 10000 == 0):
        print(f"[{i:05d}] loss: {loss_value:10.3f}")

predictions = model_predict(X)
plt.scatter(boston.target, predictions)
plt.xlabel(u"실제 집값")
plt.ylabel(u"집값 예측치")
plt.title("집값 예측치와 실제 집값의 관계")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[123]:


import tensorflow as tf
from tensorflow import keras
tf.__version__, keras.__version__


# In[128]:


mnist = keras.datasets.mnist
(X_train0, y_train0), (X_test0, y_test0) = mnist.load_data()
# import matplotlib.pylab as plt

# plt.figure(figsize=(6, 1))
# for i in range(36):
#     plt.subplot(3, 12, i+1)
#     plt.imshow(X_train0[i], cmap="gray")
#     plt.axis("off")
# plt.show()


# In[129]:


print(X_train0.shape, X_train0.dtype)
print(y_train0.shape, y_train0.dtype)
print(X_test0.shape, X_test0.dtype)
print(y_test0.shape, y_test0.dtype)


# In[130]:


X_train = X_train0.reshape(60000, 784).astype('float32') / 255.0
X_test = X_test0.reshape(10000, 784).astype('float32') / 255.0
print(X_train.shape, X_train.dtype)


# In[134]:


from tensorflow.keras.utils import to_categorical

Y_train = to_categorical(y_train0, 10)
Y_test = to_categorical(y_test0, 10)
Y_train[:5]


# ###### keras를 활용한 신경망 구현

# In[135]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

tf.random.set_seed(0)

model = Sequential()
model.add(Dense(15, input_dim=784, activation="sigmoid"))
model.add(Dense(10, activation="sigmoid"))
model.compile(optimizer=SGD(lr=0.2), loss='mean_squared_error', metrics=["accuracy"])


# In[136]:


model.summary()


# In[137]:


l1 = model.layers[0]
l2 = model.layers[1]

print(l1.name, type(l1), l1.output_shape, l1.activation.__name__, l1.count_params())
print(l2.name, type(l1), l2.output_shape, l2.activation.__name__, l2.count_params())


# In[138]:


get_ipython().run_cell_magic('time', '', 'hist = model.fit(X_train, Y_train,\n                 epochs=10, batch_size=100,\n                 validation_data=(X_test, Y_test),\n                 verbose=2)')


# In[139]:


plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.plot(hist.history['loss'])
plt.title("loss")
plt.subplot(1, 2, 2)
plt.title("accuracy")
plt.plot(hist.history['accuracy'], 'b-', label="training")
plt.plot(hist.history['val_accuracy'], 'r:', label="validation")
plt.legend()
plt.tight_layout()
plt.show()


# In[140]:


# 첫번째 레이어
w1 = l1.get_weights()
w1[0].shape, w1[1].shape


# In[141]:


# 두번째 레이어
w2 = l2.get_weights()
w2[0].shape, w2[1].shape


# In[167]:


model.predict(X_test[:1, :])


# In[168]:


model.predict_classes(X_test[:1, :], verbose=0)


# In[166]:


plt.figure(figsize=(1, 1))
plt.imshow(X_test0[0], cmap=plt.cm.bone_r)
plt.grid(False)
plt.axis("off")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




