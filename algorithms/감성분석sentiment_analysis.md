```python
!rm -f ratings_train.txt ratings_test.txt
!wget -nc https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt
!wget -nc https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt
```

    --2020-05-28 12:56:32--  https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.228.133
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.228.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 14628807 (14M) [text/plain]
    Saving to: ‘ratings_train.txt’
    
    ratings_train.txt   100%[===================>]  13.95M  3.12MB/s    in 5.4s    
    
    2020-05-28 12:56:38 (2.59 MB/s) - ‘ratings_train.txt’ saved [14628807/14628807]
    
    --2020-05-28 12:56:38--  https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.228.133
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.228.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 4893335 (4.7M) [text/plain]
    Saving to: ‘ratings_test.txt’
    
    ratings_test.txt    100%[===================>]   4.67M  1.34MB/s    in 3.5s    
    
    2020-05-28 12:56:42 (1.34 MB/s) - ‘ratings_test.txt’ saved [4893335/4893335]
    



```python
import codecs
with codecs.open("ratings_train.txt", encoding='utf-8') as f:
    data = [line.split('\t') for line in f.read().splitlines()]
    data = data[1:] 
```

    이 데이터는 번호, 내용, 평점으로 이루져 있으므로 내용을 X, 평점을 y로 저장한다


```python
from pprint import pprint
pprint(data[0])
```

    ['9976970', '아 더빙.. 진짜 짜증나네요 목소리', '0']



```python
X = list(zip(*data))[1]
y = np.array(list(zip(*data))[2], dtype=int)
```

    이제 이 데이터를 다항 나이브 베이즈 모형으로 학습시킨다.


```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

model1 = Pipeline([
    ('vect':CountVectorizer()),
    ('mb':MultinomialNB())
])
```


```python
model1.fit(X, y)
```




    Pipeline(memory=None,
             steps=[('vect',
                     CountVectorizer(analyzer='word', binary=False,
                                     decode_error='strict',
                                     dtype=<class 'numpy.int64'>, encoding='utf-8',
                                     input='content', lowercase=True, max_df=1.0,
                                     max_features=None, min_df=1,
                                     ngram_range=(1, 1), preprocessor=None,
                                     stop_words=None, strip_accents=None,
                                     token_pattern='(?u)\\b\\w\\w+\\b',
                                     tokenizer=None, vocabulary=None)),
                    ('mb',
                     MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True))],
             verbose=False)



모형의 성능을 보기 위해 테스트 데이터도 읽어들인다.


```python
import codecs
with codecs.open("ratings_test.txt", encoding='utf-8') as f:
    data_test = [line.split('\t') for line in f.read().splitlines()]
    data_test = data[1:]
```


```python
X_test = list(zip(*data_test))[1]
y_test = np.array(list(zip(*data_test))[2], dtype=int)
```


```python
print(classification_report(y_test, model1.predict(X_test)))
```

                  precision    recall  f1-score   support
    
               0       0.81      0.84      0.83     24827
               1       0.84      0.81      0.82     25172
    
        accuracy                           0.83     49999
       macro avg       0.83      0.83      0.83     49999
    weighted avg       0.83      0.83      0.83     49999
    


    Tfidf모델 사용


```python
from sklearn.feature_extraction.text import TfidfVectorizer

model2 = Pipeline([
    ('vect', TfidfVectorizer()),
    ('mb', MultinomialNB())
])
```


```python
model2.fit(X, y)
```




    Pipeline(memory=None,
             steps=[('vect',
                     TfidfVectorizer(analyzer='word', binary=False,
                                     decode_error='strict',
                                     dtype=<class 'numpy.float64'>,
                                     encoding='utf-8', input='content',
                                     lowercase=True, max_df=1.0, max_features=None,
                                     min_df=1, ngram_range=(1, 1), norm='l2',
                                     preprocessor=None, smooth_idf=True,
                                     stop_words=None, strip_accents=None,
                                     sublinear_tf=False,
                                     token_pattern='(?u)\\b\\w\\w+\\b',
                                     tokenizer=None, use_idf=True,
                                     vocabulary=None)),
                    ('mb',
                     MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True))],
             verbose=False)




```python
# 테스트 데이터로 예측
print(classification_report(y_test, model2.predict(X_test)))
```

                  precision    recall  f1-score   support
    
               0       0.81      0.84      0.83     24827
               1       0.84      0.81      0.83     25172
    
        accuracy                           0.83     49999
       macro avg       0.83      0.83      0.83     49999
    weighted avg       0.83      0.83      0.83     49999
    


    이번에는 형태소 분석기를 사용한 결과와 비교한다.


```python
from konlpy.tag import Okt
pos_tagger = Okt()

def tokenize_pos(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc)]
```


```python
model3 = Pipeline([
    ('vect', CountVectorizer(tokenizer=tokenize_pos)),
    ('mb', MultinomialNB()),
])
```


```python
model3.fit(X, y)
```




    Pipeline(memory=None,
             steps=[('vect',
                     CountVectorizer(analyzer='word', binary=False,
                                     decode_error='strict',
                                     dtype=<class 'numpy.int64'>, encoding='utf-8',
                                     input='content', lowercase=True, max_df=1.0,
                                     max_features=None, min_df=1,
                                     ngram_range=(1, 1), preprocessor=None,
                                     stop_words=None, strip_accents=None,
                                     token_pattern='(?u)\\b\\w\\w+\\b',
                                     tokenizer=<function tokenize_pos at 0x1a2a9ae440>,
                                     vocabulary=None)),
                    ('mb',
                     MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True))],
             verbose=False)




```python
print(classification_report(y_test, model3.predict(X_test)))
```

                  precision    recall  f1-score   support
    
               0       0.85      0.86      0.85     24827
               1       0.86      0.85      0.85     25172
    
        accuracy                           0.85     49999
       macro avg       0.85      0.85      0.85     49999
    weighted avg       0.85      0.85      0.85     49999
    


    -gram 을 사용하면 성능이 더 개선되는 것을 볼 수 있다.


```python
model4 = Pipeline([
    ('vect', TfidfVectorizer(tokenizer=tokenize_pos, ngram_range=(1, 2))),
    ('mb', MultinomialNB()),
])
```


```python
model4.fit(X, y)
```




    Pipeline(memory=None,
             steps=[('vect',
                     TfidfVectorizer(analyzer='word', binary=False,
                                     decode_error='strict',
                                     dtype=<class 'numpy.float64'>,
                                     encoding='utf-8', input='content',
                                     lowercase=True, max_df=1.0, max_features=None,
                                     min_df=1, ngram_range=(1, 2), norm='l2',
                                     preprocessor=None, smooth_idf=True,
                                     stop_words=None, strip_accents=None,
                                     sublinear_tf=False,
                                     token_pattern='(?u)\\b\\w\\w+\\b',
                                     tokenizer=<function tokenize_pos at 0x1a2a9ae440>,
                                     use_idf=True, vocabulary=None)),
                    ('mb',
                     MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True))],
             verbose=False)




```python
print(classification_report(y_test, model4.predict(X_test)))
```

                  precision    recall  f1-score   support
    
               0       0.86      0.87      0.87     24827
               1       0.87      0.86      0.87     25172
    
        accuracy                           0.87     49999
       macro avg       0.87      0.87      0.87     49999
    weighted avg       0.87      0.87      0.87     49999
    


    연습 문제 1¶
    위에서 만든 감성분석 모형에 다양한 문장을 넣어서 결과를 테스트해보자.


```python
model1.predict(['멋있는데?'])
```




    array([0])




```python
model2.predict(['멋있는데?'])
```




    array([0])




```python
model3.predict(['멋있는데?'])
```




    array([0])




```python
model4.predict(['멋있는데?'])
```




    array([0])




```python
model4.predict(['재밌음'])
```




    array([1])


