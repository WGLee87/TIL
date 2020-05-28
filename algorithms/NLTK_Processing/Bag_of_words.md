###### scikit-learn의 feature_extraction 서브패키지와 feature_extraction.text 서브패키지는 다음과 같은 BOW 인코더 클래스를 제공

    - CountVectorizer :
        * 문서 집합에서 단어 토큰을 생성하고 각 단어의 수를 세어 BOW인코딩 벡터를 만든다.
    - TfidfVectorizer :
        * CountVectorizer와 비슷하지만 TF_IDF방식으로 단어의 가중치를 조정한 BOW인코딩 벡터를 만든다.
    - HashingVectorizer :
        * 해시함수을 사용하여 적은 메모리와 빠른 속도로 BOW인코딩 벡터를 만든다.
        
        
###### Vectorizer 클래스 기능
    - CountVectorizer는 다음과 같은 세가지 작업을 수행
        1. 문서를 토큰 리스트로 변환
        2. 각 문서에 토큰의 출현 빈도를 셈
        3. 각 문서를 BOW 인코딩 벡터로 변환
        
        
 ###### Vectorize 클래스 사용법
     - 클래스 객체 생성
     - 말뭉치를 넣고 fit 메서드 실행
     - vocabulary_ 속성에 단어장이 자동 생성됨
     - transform 메서드로 다른 문서를 BOW 인코딩
     - BOW 인코딩 결과는 sparse 행렬로 만들어지므로 toarray메서드로 보통 행렬로 변환
     
     
 ###### Vectorizer 인수
     - stop_words :문자열 {'english'} 리스트 또는 None(디폴트)
         * stop_words 'english면 영어용 스탑워드 사용
     - max_df / min_df : 정수 또는 [0.0, 1.0]사이의 실수. 디폴트 1
         * 단어장에 포함되기 위한 최대빈도, 최소빈도
     - ngram_range : (min_n, max_n) 튜플
         * n-그램 범위
     - analyzer : 문자열{'word', 'char', 'char_wb'} 또는 함수
     - token_pattern : string > 토큰 정의용 정규 표현식
     - tokenizer : 함수 또는 디폴트
         * 토큰 생성 함수
         
         
 ###### N-그램
     - 단어의 형태소에서 토큰을 생성할 때
         * 1개의 단어로 하나의 토큰을 만들면 : 모노그램(monogram, 1-gram)
         * 2개의 단어로 하나의 토큰을 만들면 : 바이그램(bigram, 2-gram)
         * 3개의 단어로 하나의 토큰을 만들면 : 트라이그램(trigram, 3-gram)
             1. 1-gram : 'I', 'am', 'a'. 'boy'
             2.2-gram : 'I am', 'am a', 'a boy'
             3.3-gram : 'I am a', 'am a boy'


```python
# step1 : 말뭉치 만들기
corpus = {
    'This is the first document.',
    'This is the second second document',
    'And the third one',
    'Is this the first document?',
    'The last document?'
}

# step2 : 인코더 객체 생성
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
vect

# step3 : 말뭉치 학습 및 단어장 생성
vect.fit(corpus)
vect.vocabulary_ # count가 아님 index 임

# step4 : 문장을 BOW 인코딩
vect.transform(corpus).toarray()
# 말뭉치에서 학습되지 않은 단어는 불용어 처리가 됨

# step5 : 불용어 사용
vect = CountVectorizer(stop_words=['and','is','the','this']).fit(corpus)
vect.vocabulary_
vect = CountVectorizer(stop_words='english').fit(corpus)
vect.vocabulary_, vect.stop_words

# step6 : 빈도수 적용
vect = CountVectorizer(max_df=4, min_df=2).fit(corpus)
vect.vocabulary_ 

# step7 : N-그램 적용
vect = CountVectorizer(ngram_range=(1,2)).fit(corpus)
vect.vocabulary_
```




    {'and': 0,
     'the': 14,
     'third': 19,
     'one': 10,
     'and the': 1,
     'the third': 18,
     'third one': 20,
     'this': 21,
     'is': 5,
     'first': 3,
     'document': 2,
     'this is': 22,
     'is the': 6,
     'the first': 15,
     'first document': 4,
     'is this': 7,
     'this the': 23,
     'second': 11,
     'the second': 17,
     'second second': 13,
     'second document': 12,
     'last': 8,
     'the last': 16,
     'last document': 9}




```python

```

###### TF-IDF 인코딩
    - TF-IDF(Term Frequency - Inverse Document Frequency) 인코딩은 단어를 갯수 그대로 카운트하지 않고 모든 문서에 공통적으로 들어있는 단어의 경우 문서 구별 능력이 떨어진다고 보아 가중치를 축소시키는 방법이다.


```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidv = TfidfVectorizer().fit(corpus)
tfidv.transform(corpus).toarray()
```




    array([[0.55666851, 0.        , 0.        , 0.        , 0.        ,
            0.55666851, 0.        , 0.26525553, 0.55666851, 0.        ],
           [0.        , 0.38947624, 0.55775063, 0.4629834 , 0.        ,
            0.        , 0.        , 0.32941651, 0.        , 0.4629834 ],
           [0.        , 0.38947624, 0.55775063, 0.4629834 , 0.        ,
            0.        , 0.        , 0.32941651, 0.        , 0.4629834 ],
           [0.        , 0.24151532, 0.        , 0.28709733, 0.        ,
            0.        , 0.85737594, 0.20427211, 0.        , 0.28709733],
           [0.        , 0.45333103, 0.        , 0.        , 0.80465933,
            0.        , 0.        , 0.38342448, 0.        , 0.        ]])




```python

```

###### 해시트릭(Hash Trick)
    - CountVectorizer 는 모든 작업을 메모리 상에서 수행
    - 처리할 문서의 크기가 커지면 단어장 딕셔너리가 커짐
    - 실행 속도가 느려지거나 실행이 불가능해짐
    
    * HashingVectorizer를 사용하면 해ㅐ시 함수(Hash function)을 사용
    * 단어에 대한 인덱스 번호를 수식으로 생성
    * 사전 메모리가 없고 실행 시간을 줄일 수 있음
    * 단어의 충돌이 있을 수는 있다.

###### Gensim 패키지
    - Bag of Words 인코딩
    - TF-IDF 인코딩
    - 토픽 모델링


```python
pip install gensim
```

    Collecting gensim
      Downloading gensim-3.8.3-cp37-cp37m-macosx_10_9_x86_64.whl (24.2 MB)
    [K     |████████████████████████████████| 24.2 MB 17 kB/s eta 0:00:014    |█▉                              | 1.4 MB 29 kB/s eta 0:12:58     |██████████▉                     | 8.2 MB 16 kB/s eta 0:15:42
    [?25hRequirement already satisfied: scipy>=0.18.1 in /opt/anaconda3/lib/python3.7/site-packages (from gensim) (1.4.1)
    Requirement already satisfied: six>=1.5.0 in /opt/anaconda3/lib/python3.7/site-packages (from gensim) (1.14.0)
    Requirement already satisfied: numpy>=1.11.3 in /opt/anaconda3/lib/python3.7/site-packages (from gensim) (1.18.1)
    Collecting smart-open>=1.8.1
      Downloading smart_open-2.0.0.tar.gz (103 kB)
    [K     |████████████████████████████████| 103 kB 17 kB/s eta 0:00:01
    [?25hRequirement already satisfied: requests in /opt/anaconda3/lib/python3.7/site-packages (from smart-open>=1.8.1->gensim) (2.23.0)
    Collecting boto
      Downloading boto-2.49.0-py2.py3-none-any.whl (1.4 MB)
    [K     |████████████████████████████████| 1.4 MB 41 kB/s eta 0:00:01
    [?25hCollecting boto3
      Downloading boto3-1.13.12-py2.py3-none-any.whl (128 kB)
    [K     |████████████████████████████████| 128 kB 39 kB/s eta 0:00:01
    [?25hRequirement already satisfied: idna<3,>=2.5 in /opt/anaconda3/lib/python3.7/site-packages (from requests->smart-open>=1.8.1->gensim) (2.9)
    Requirement already satisfied: chardet<4,>=3.0.2 in /opt/anaconda3/lib/python3.7/site-packages (from requests->smart-open>=1.8.1->gensim) (3.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.7/site-packages (from requests->smart-open>=1.8.1->gensim) (2020.4.5.1)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/anaconda3/lib/python3.7/site-packages (from requests->smart-open>=1.8.1->gensim) (1.25.8)
    Collecting jmespath<1.0.0,>=0.7.1
      Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)
    Collecting botocore<1.17.0,>=1.16.12
      Downloading botocore-1.16.12-py2.py3-none-any.whl (6.2 MB)
    [K     |████████████████████████████████| 6.2 MB 45 kB/s eta 0:00:011
    [?25hCollecting s3transfer<0.4.0,>=0.3.0
      Downloading s3transfer-0.3.3-py2.py3-none-any.whl (69 kB)
    [K     |████████████████████████████████| 69 kB 72 kB/s eta 0:00:01
    [?25hRequirement already satisfied: python-dateutil<3.0.0,>=2.1 in /opt/anaconda3/lib/python3.7/site-packages (from botocore<1.17.0,>=1.16.12->boto3->smart-open>=1.8.1->gensim) (2.8.1)
    Collecting docutils<0.16,>=0.10
      Downloading docutils-0.15.2-py3-none-any.whl (547 kB)
    [K     |████████████████████████████████| 547 kB 47 kB/s eta 0:00:01
    [?25hBuilding wheels for collected packages: smart-open
      Building wheel for smart-open (setup.py) ... [?25ldone
    [?25h  Created wheel for smart-open: filename=smart_open-2.0.0-py3-none-any.whl size=101341 sha256=8bbf591e0e2dd0c71899654f15fea8da4f179cf566ab71b3077db5b8337820e1
      Stored in directory: /Users/wglee/Library/Caches/pip/wheels/bb/1c/9c/412ec03f6d5ac7d41f4b965bde3fc0d1bd201da5ba3e2636de
    Successfully built smart-open
    Installing collected packages: boto, jmespath, docutils, botocore, s3transfer, boto3, smart-open, gensim
    Successfully installed boto-2.49.0 boto3-1.13.12 botocore-1.16.12 docutils-0.15.2 gensim-3.8.3 jmespath-0.10.0 s3transfer-0.3.3 smart-open-2.0.0
    Note: you may need to restart the kernel to use updated packages.


###### Gensim의 BOW인코딩 기능
    - Dictionary 클래스 이용
        * token2id 속성으로 사전 저장
        * doc2bow 메서드로 BOW 인코딩
    - TfidfModel 클래스를 이용하면 TF-IDF 인코딩도 가능


```python
corpus
```




    {'And the third one',
     'Is this the first document?',
     'The last document?',
     'This is the first document.',
     'This is the second second document'}




```python
token_list = [[text for text in doc.split()] for doc in corpus]
token_list
```




    [['And', 'the', 'third', 'one'],
     ['This', 'is', 'the', 'first', 'document.'],
     ['Is', 'this', 'the', 'first', 'document?'],
     ['This', 'is', 'the', 'second', 'second', 'document'],
     ['The', 'last', 'document?']]




```python
from gensim.corpora import Dictionary
dictionary = Dictionary(token_list)
dictionary.token2id
```




    {'And': 0,
     'one': 1,
     'the': 2,
     'third': 3,
     'This': 4,
     'document.': 5,
     'first': 6,
     'is': 7,
     'Is': 8,
     'document?': 9,
     'this': 10,
     'document': 11,
     'second': 12,
     'The': 13,
     'last': 14}




```python
term_matrix = [dictionary.doc2bow(token) for token in token_list]
term_matrix
```




    [[(0, 1), (1, 1), (2, 1), (3, 1)],
     [(2, 1), (4, 1), (5, 1), (6, 1), (7, 1)],
     [(2, 1), (6, 1), (8, 1), (9, 1), (10, 1)],
     [(2, 1), (4, 1), (7, 1), (11, 1), (12, 2)],
     [(9, 1), (13, 1), (14, 1)]]




```python
# TF-IDF  인코딩 in gensim

from gensim.models import TfidfModel
tfidf = TfidfModel(term_matrix)
for doc in tfidf[term_matrix]:
    print('doc:')
    for k, v in doc:
        print(k, v)
```

    doc:
    0 0.5755093812740171
    1 0.5755093812740171
    2 0.07979258234193365
    3 0.5755093812740171
    doc:
    2 0.09824442362969368
    4 0.4034194772828018
    5 0.7085945309359098
    6 0.4034194772828018
    7 0.4034194772828018
    doc:
    2 0.08489056411237639
    6 0.3485847413542797
    8 0.6122789185961829
    9 0.3485847413542797
    10 0.6122789185961829
    doc:
    2 0.05823915489565254
    4 0.23914649358577064
    7 0.23914649358577064
    11 0.4200538322758887
    12 0.8401076645517774
    doc:
    9 0.37344696513776354
    13 0.6559486886294514
    14 0.6559486886294514



```python

```


```python

```

###### Step1 : 텍스트 데이터 다운로드


```python
from sklearn.datasets import fetch_20newsgroups

newsgroups = fetch_20newsgroups(
categories = ['comp.graphics', 'rec.sport.baseball', 'sci.med'])
```

###### Step2 명사 추출

%%time
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

tagged_list = [pos_tag(word_tokenize(doc)) for doc in newsgroups.data]
nouns_list = [[t[0] for t in doc if t[1].startswith('N')] for doc in tagged_list]

###### Step3 표제어 추출


```python
from nltk.stem import WordNetLemmatizer
lm = WordNetLemmatizer()
nouns_list = [[lm.lemmatize(w, pos='n') for w in doc] for doc in nouns_list]
```

###### Step4 불용어 제거


```python
import re
token_list = [[text.lower() for text in doc] for doc in nouns_list]
token_list = [[re.sub(r"[^A-Za-z]+", ' ' , word) for word in doc] for doc in token_list]
```


```python
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words += ['', 'subject', 'article', 'line', 'year', 'month', 'address', 'keyword', 'msg']

token_list = [[word for word in doc if (word not in stop_words) and (2 < len(word)<10)] for doc in token_list]
```

###### Step5  토픽 모델링


```python
from gensim import corpora

dictionary = corpora.Dictionary(token_list)
doc_term_matrix  = [dictionary.doc2bow(tokens) for tokens in token_list]
```


```python
from gensim.models.ldamodel import LdaModel
model = LdaModel(corpus=doc_term_matrix, id2word=dictionary, num_topics=3,)
```


```python
model.print_topics()
```




    [(0,
      '0.013*"lines" + 0.006*"image" + 0.006*"time" + 0.004*"problem" + 0.004*"people" + 0.004*"computer" + 0.004*"number" + 0.004*"anyone" + 0.003*"lot" + 0.003*"point"'),
     (1,
      '0.013*"lines" + 0.008*"file" + 0.006*"image" + 0.005*"program" + 0.005*"time" + 0.004*"game" + 0.003*"people" + 0.003*"problem" + 0.003*"disease" + 0.003*"color"'),
     (2,
      '0.010*"lines" + 0.006*"game" + 0.005*"team" + 0.004*"image" + 0.004*"time" + 0.003*"system" + 0.003*"david" + 0.003*"science" + 0.003*"player" + 0.003*"food"')]



###### Step6 토픽 시각화


```python
pip install pyLDAvis
```

    Collecting pyLDAvis
      Downloading pyLDAvis-2.1.2.tar.gz (1.6 MB)
    [K     |████████████████████████████████| 1.6 MB 64 kB/s eta 0:00:012
    [?25hRequirement already satisfied: wheel>=0.23.0 in /opt/anaconda3/lib/python3.7/site-packages (from pyLDAvis) (0.34.2)
    Requirement already satisfied: numpy>=1.9.2 in /opt/anaconda3/lib/python3.7/site-packages (from pyLDAvis) (1.18.1)
    Requirement already satisfied: scipy>=0.18.0 in /opt/anaconda3/lib/python3.7/site-packages (from pyLDAvis) (1.4.1)
    Requirement already satisfied: pandas>=0.17.0 in /opt/anaconda3/lib/python3.7/site-packages (from pyLDAvis) (1.0.3)
    Requirement already satisfied: joblib>=0.8.4 in /opt/anaconda3/lib/python3.7/site-packages (from pyLDAvis) (0.14.1)
    Requirement already satisfied: jinja2>=2.7.2 in /opt/anaconda3/lib/python3.7/site-packages (from pyLDAvis) (2.11.1)
    Collecting numexpr
      Downloading numexpr-2.7.1-cp37-cp37m-macosx_10_6_intel.whl (186 kB)
    [K     |████████████████████████████████| 186 kB 65 kB/s eta 0:00:01
    [?25hCollecting pytest
      Downloading pytest-5.4.2-py3-none-any.whl (247 kB)
    [K     |████████████████████████████████| 247 kB 64 kB/s eta 0:00:01
    [?25hRequirement already satisfied: future in /opt/anaconda3/lib/python3.7/site-packages (from pyLDAvis) (0.18.2)
    Collecting funcy
      Downloading funcy-1.14.tar.gz (548 kB)
    [K     |████████████████████████████████| 548 kB 62 kB/s eta 0:00:01
    [?25hRequirement already satisfied: pytz>=2017.2 in /opt/anaconda3/lib/python3.7/site-packages (from pandas>=0.17.0->pyLDAvis) (2019.3)
    Requirement already satisfied: python-dateutil>=2.6.1 in /opt/anaconda3/lib/python3.7/site-packages (from pandas>=0.17.0->pyLDAvis) (2.8.1)
    Requirement already satisfied: MarkupSafe>=0.23 in /opt/anaconda3/lib/python3.7/site-packages (from jinja2>=2.7.2->pyLDAvis) (1.1.1)
    Collecting packaging
      Downloading packaging-20.3-py2.py3-none-any.whl (37 kB)
    Collecting py>=1.5.0
      Downloading py-1.8.1-py2.py3-none-any.whl (83 kB)
    [K     |████████████████████████████████| 83 kB 27 kB/s eta 0:00:01
    [?25hRequirement already satisfied: attrs>=17.4.0 in /opt/anaconda3/lib/python3.7/site-packages (from pytest->pyLDAvis) (19.3.0)
    Requirement already satisfied: more-itertools>=4.0.0 in /opt/anaconda3/lib/python3.7/site-packages (from pytest->pyLDAvis) (8.2.0)
    Requirement already satisfied: wcwidth in /opt/anaconda3/lib/python3.7/site-packages (from pytest->pyLDAvis) (0.1.9)
    Requirement already satisfied: importlib-metadata>=0.12; python_version < "3.8" in /opt/anaconda3/lib/python3.7/site-packages (from pytest->pyLDAvis) (1.5.0)
    Collecting pluggy<1.0,>=0.12
      Downloading pluggy-0.13.1-py2.py3-none-any.whl (18 kB)
    Requirement already satisfied: six>=1.5 in /opt/anaconda3/lib/python3.7/site-packages (from python-dateutil>=2.6.1->pandas>=0.17.0->pyLDAvis) (1.14.0)
    Requirement already satisfied: pyparsing>=2.0.2 in /opt/anaconda3/lib/python3.7/site-packages (from packaging->pytest->pyLDAvis) (2.4.7)
    Requirement already satisfied: zipp>=0.5 in /opt/anaconda3/lib/python3.7/site-packages (from importlib-metadata>=0.12; python_version < "3.8"->pytest->pyLDAvis) (2.2.0)
    Building wheels for collected packages: pyLDAvis, funcy
      Building wheel for pyLDAvis (setup.py) ... [?25ldone
    [?25h  Created wheel for pyLDAvis: filename=pyLDAvis-2.1.2-py2.py3-none-any.whl size=97711 sha256=9c11414a59cc38a5ac73d3819a771b52e09f0cb7408b7c81a46566a21994c372
      Stored in directory: /Users/wglee/Library/Caches/pip/wheels/3b/fb/41/e32e5312da9f440d34c4eff0d2207b46dc9332a7b931ef1e89
      Building wheel for funcy (setup.py) ... [?25ldone
    [?25h  Created wheel for funcy: filename=funcy-1.14-py2.py3-none-any.whl size=32042 sha256=774da61521533dd484a01344c7bea32b6ebf355e2932481eca2f96247afaac02
      Stored in directory: /Users/wglee/Library/Caches/pip/wheels/3c/33/97/805b282e129f60bb4e87cea622338f30b65f21eaf65219971f
    Successfully built pyLDAvis funcy
    Installing collected packages: numexpr, packaging, py, pluggy, pytest, funcy, pyLDAvis
    Successfully installed funcy-1.14 numexpr-2.7.1 packaging-20.3 pluggy-0.13.1 py-1.8.1 pyLDAvis-2.1.2 pytest-5.4.2
    Note: you may need to restart the kernel to use updated packages.



```python
import pyLDAvis
import pyLDAvis.gensim

pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(model, doc_term_matrix, dictionary)
vis
```





<link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.css">


<div id="ldavis_el90791122734952483851015077"></div>
<script type="text/javascript">

var ldavis_el90791122734952483851015077_data = {"mdsDat": {"x": [0.02797044029691984, -0.025161098005714037, -0.0028093422912058024], "y": [-0.010472694686024756, -0.01442156355254139, 0.024894258238566135], "topics": [1, 2, 3], "cluster": [1, 1, 1], "Freq": [42.45713806152344, 29.165782928466797, 28.377077102661133]}, "tinfo": {"Term": ["file", "game", "disease", "color", "dyer", "compass ", "water", "program", "format", "cubs", "candida", "team", "polygon", "jpeg", "lines", "geb", "lost", "league", "scott", "fan", "roger", "new", "phillies", "player", "david", "smith", "dept", "baseball", "city", "eye", "graeme", "pittsburg", "hismanal", "sheryl", "hexagon", "spdcc com", "ima", "rayssd", "s p", "lrc edu", "renggli", "choueiry", "lausanne", "dotzlaw", "gilmete", "voronoi", "avi", "rokne", "adriana", "m c", "rhinitis", "mckay", "dyer", "spdcc", "vasomotor", "corn", "khun", "mg dl", "nosebleed", "arythmia", "linus", "polygon", "programs", "outline", "charles", "prk", "scodal", "hernia", "cfs", "recommend", "aka", "curve", "cboesel", "geb", "gordon", "number", "banks", "person", "steve", "weight", "cereal", "computer", "data", "problem", "lot", "n jxp", "lines", "chastity", "graphics", "time", "product", "image", "group", "phone", "anyone", "people", "reply to", "way", "point", "question", "graphic", "effect", "use", "patient", "thing", "version", "system", "program", "software", "case", "something", "food", "science", "game", "team", "day", "suck", "cipiti", "piano", "shapiro", "af ", "maier", "klonopin", "rauser", "mpeg play", "acsddc", "wings", "chad", "yale edu", "pistons", "mccall", "erickson", "lions", "rot qc ca", "anl", "wcarter", "belinda", "trombone", "sas ", "blocking", "soth", "gkiria", "gia", "jake", "candee", "pallis", "whi", "sosa", "mono", "idle", "timlin", "vizcaino", "bal", "thornley", "kan", "hagins", "driftwood", "wetteland", "cub", "water", "lost", "harry", "cubs", "linux", "scott", "astros", "dominance", "zisfein", "game", "eye", "hiv", "league", "rockies", "city", "team", "minnesota", "hitter", "yankees", "windows", "david", "smith", "chicago", "base", "player", "food", "research", "system", "dept", "san", "doctor", "lines", "home", "science", "baseball", "thing", "run", "kind", "fan", "thanks", "time", "image", "day", "anyone", "world", "way", "people", "number", "software", "new", "lot", "file", "program", "compass ", "clubbing", "rix", "oct", "infotrac", " scf", "op rows", "muller", "denman", "helium", "dane", "ilmenau", "reiniger", "miro", "spect", "tremor", "compass", "fopen", "sizeof", "valo", "vatti", "peterbak", "rych", " prj", "chumphre", "qed", "shippert", "fingertip", "dir", "neuharth", "cx com", "int", "row", "northern", "inhibitor", "file", "candida", "yogurt", "col", "francesa", "disease", "phils", "color", "format", "program", "jpeg", "phillies", "cview", "lines", "albicans", "email", "new", "image", "machine", "morris", "world", "roger", "point", "pain", "game", "john", "time", "problem", "thanks", "fan", "people", "baseball", "day", "version", "science", "player", "team", "software", "center", "computer", "anyone", "way", "run", "case", "thing"], "Freq": [454.0, 508.0, 220.0, 231.0, 138.0, 33.0, 125.0, 393.0, 233.0, 92.0, 81.0, 388.0, 126.0, 212.0, 1456.0, 221.0, 55.0, 161.0, 73.0, 179.0, 96.0, 229.0, 102.0, 283.0, 287.0, 106.0, 150.0, 288.0, 93.0, 82.0, 12.962959289550781, 24.031593322753906, 11.571136474609375, 4.911839485168457, 4.8881683349609375, 32.498653411865234, 15.384480476379395, 15.306600570678711, 12.061148643493652, 6.42030668258667, 3.9964826107025146, 3.9920313358306885, 3.985220193862915, 3.9883413314819336, 3.9751641750335693, 3.972447633743286, 3.967034339904785, 3.9648025035858154, 3.9565882682800293, 15.001216888427734, 7.861241817474365, 3.914350748062134, 118.17161560058594, 15.608063697814941, 7.779759407043457, 31.969472885131836, 3.883967399597168, 3.8923213481903076, 9.29710865020752, 4.635743141174316, 15.305118560791016, 103.49493408203125, 12.999799728393555, 14.440126419067383, 42.3671760559082, 13.689918518066406, 15.750040054321289, 12.74655532836914, 9.930971145629883, 10.522976875305176, 18.682954788208008, 27.534263610839844, 13.132535934448242, 145.31472778320312, 127.9456787109375, 211.80755615234375, 159.58656311035156, 77.93534851074219, 145.31790161132812, 44.32190704345703, 21.173625946044922, 212.71578979492188, 157.23728942871094, 225.281494140625, 178.2394561767578, 49.86993408203125, 659.63232421875, 49.72562789916992, 105.7835464477539, 301.20794677734375, 79.41055297851562, 320.2485656738281, 123.22808074951172, 63.21501922607422, 201.46408081054688, 212.7401123046875, 99.34831237792969, 170.6947784423828, 176.0858154296875, 138.6773223876953, 123.40072631835938, 103.99696350097656, 107.3678970336914, 113.4559097290039, 146.0304718017578, 130.4461212158203, 144.4123077392578, 159.03338623046875, 128.17990112304688, 120.4838638305664, 116.14259338378906, 123.54943084716797, 133.6913604736328, 144.46188354492188, 129.77621459960938, 121.38182830810547, 16.617023468017578, 3.957862615585327, 3.945366859436035, 6.206377983093262, 3.046143054962158, 3.0403716564178467, 6.080738067626953, 6.813746929168701, 2.9816362857818604, 3.6967484951019287, 2.9272148609161377, 4.330941677093506, 4.33200740814209, 2.886918306350708, 3.5858335494995117, 9.343905448913574, 2.8512015342712402, 10.014023780822754, 2.1309897899627686, 2.1292011737823486, 2.1278207302093506, 2.1267356872558594, 2.128164529800415, 2.126953125, 2.1268045902252197, 2.1273036003112793, 2.1271636486053467, 2.126281976699829, 2.125715494155884, 2.1211938858032227, 8.477571487426758, 5.654959201812744, 4.219173431396484, 14.72004508972168, 6.272266387939453, 6.877639293670654, 6.82541036605835, 4.81770133972168, 7.4151692390441895, 3.495786428451538, 2.813274383544922, 6.037055969238281, 28.50670051574707, 77.41938018798828, 36.28116989135742, 13.308394432067871, 56.716758728027344, 17.93560028076172, 43.42066192626953, 24.734336853027344, 13.90845775604248, 18.689083099365234, 219.71852111816406, 45.4333610534668, 37.543617248535156, 80.28724670410156, 26.82185935974121, 49.365440368652344, 161.94766235351562, 19.846031188964844, 55.94278335571289, 31.58516502380371, 47.53123092651367, 118.92070007324219, 52.423866271972656, 44.258907318115234, 56.76820373535156, 110.29910278320312, 107.81607818603516, 102.46621704101562, 120.23888397216797, 65.38075256347656, 50.57915496826172, 83.02604675292969, 341.96527099609375, 68.90911865234375, 111.22161865234375, 99.75557708740234, 104.72766876220703, 89.37773895263672, 57.98591232299805, 68.04155731201172, 91.70805358886719, 133.68687438964844, 138.77105712890625, 90.28865051269531, 101.43013000488281, 83.11187744140625, 86.82256317138672, 92.71499633789062, 78.27935028076172, 72.80951690673828, 68.68478393554688, 69.96746063232422, 72.40185546875, 71.34370422363281, 33.19236755371094, 9.206003189086914, 5.932333469390869, 8.782929420471191, 4.315537452697754, 5.713907241821289, 3.567469835281372, 3.5507590770721436, 3.5286645889282227, 3.5257184505462646, 5.624360084533691, 3.506368398666382, 3.4929873943328857, 3.4891316890716553, 6.2719340324401855, 4.142650604248047, 2.745229721069336, 2.741766929626465, 2.7393319606781006, 4.792991638183594, 2.737971544265747, 2.7363197803497314, 2.7326526641845703, 2.7326931953430176, 2.727937698364258, 2.726172685623169, 4.727548122406006, 2.6950302124023438, 6.031981468200684, 3.3501813411712646, 4.671314239501953, 20.976123809814453, 20.998289108276367, 6.5116496086120605, 10.139911651611328, 271.7298889160156, 53.503570556640625, 8.843549728393555, 20.123153686523438, 4.560119152069092, 114.66466522216797, 16.27097511291504, 114.33871459960938, 110.98564910888672, 163.05482482910156, 96.17510223388672, 52.08332443237305, 31.371225357055664, 454.87164306640625, 18.89174461364746, 49.112953186035156, 91.41752624511719, 210.22789001464844, 46.560935974121094, 44.33705520629883, 96.1295394897461, 42.36359405517578, 111.7418441772461, 54.52477264404297, 144.03245544433594, 68.18013763427734, 158.1766357421875, 118.13069152832031, 97.38146209716797, 66.2422866821289, 121.13569641113281, 91.80858612060547, 95.5751724243164, 83.92613220214844, 91.27508544921875, 81.03885650634766, 97.02962493896484, 78.8957290649414, 71.8480224609375, 90.04859161376953, 92.45662689208984, 83.54399108886719, 72.4494400024414, 70.54550170898438, 69.7427978515625], "Total": [454.0, 508.0, 220.0, 231.0, 138.0, 33.0, 125.0, 393.0, 233.0, 92.0, 81.0, 388.0, 126.0, 212.0, 1456.0, 221.0, 55.0, 161.0, 73.0, 179.0, 96.0, 229.0, 102.0, 283.0, 287.0, 106.0, 150.0, 288.0, 93.0, 82.0, 13.798477172851562, 25.738895416259766, 12.821977615356445, 5.509407997131348, 5.510273456573486, 36.753868103027344, 17.416521072387695, 17.444400787353516, 13.757383346557617, 7.323929309844971, 4.587997913360596, 4.584661483764648, 4.581199645996094, 4.586568355560303, 4.586256504058838, 4.585731029510498, 4.585104942321777, 4.58390474319458, 4.58002233505249, 17.3951358795166, 9.143956184387207, 4.57933235168457, 138.3568878173828, 18.275571823120117, 9.14077377319336, 37.608604431152344, 4.573707103729248, 4.587315082550049, 10.95743179321289, 5.481452941894531, 18.255409240722656, 126.36282348632812, 15.527073860168457, 17.374099731445312, 52.77117156982422, 16.560224533081055, 19.205577850341797, 15.426026344299316, 11.940587997436523, 12.82859992980957, 23.635433197021484, 36.212425231933594, 16.348962783813477, 221.82015991210938, 193.2184295654297, 337.39056396484375, 249.03152465820312, 114.65892791748047, 232.481689453125, 62.85445785522461, 27.593427658081055, 370.9205322265625, 265.0684509277344, 400.12762451171875, 312.2957458496094, 72.7860107421875, 1456.46923828125, 72.8028793334961, 175.3069305419922, 593.0714721679688, 126.67619323730469, 669.2474975585938, 214.9695587158203, 97.28649139404297, 395.3508605957031, 426.5908203125, 171.44943237304688, 341.06134033203125, 355.5611572265625, 266.426025390625, 233.36712646484375, 189.92181396484375, 203.74826049804688, 221.91189575195312, 320.5009460449219, 274.6512756347656, 329.0709228515625, 393.4319152832031, 279.8851318359375, 255.24029541015625, 242.0504913330078, 278.6153869628906, 336.18804931640625, 508.212890625, 388.7535095214844, 307.2456359863281, 18.295978546142578, 4.555284023284912, 4.5525078773498535, 7.286219596862793, 3.638737916946411, 3.6376430988311768, 7.284658432006836, 8.222173690795898, 3.6343798637390137, 4.531196117401123, 3.631892681121826, 5.422996520996094, 5.438803672790527, 3.6301913261413574, 4.523299217224121, 11.814956665039062, 3.6258316040039062, 12.781965255737305, 2.722411870956421, 2.722548484802246, 2.7213940620422363, 2.720329999923706, 2.7224488258361816, 2.7217090129852295, 2.7216615676879883, 2.7223031520843506, 2.722804546356201, 2.7220144271850586, 2.7220516204833984, 2.7217650413513184, 10.903351783752441, 7.290604591369629, 5.4352216720581055, 19.726734161376953, 8.232257843017578, 9.072776794433594, 9.046133041381836, 6.327085971832275, 9.95616340637207, 4.559549808502197, 3.6364989280700684, 8.112340927124023, 41.60272216796875, 125.26573181152344, 55.96498107910156, 19.051128387451172, 92.49394989013672, 27.19257926940918, 73.01568603515625, 39.21199417114258, 20.67067527770996, 29.5844669342041, 508.212890625, 82.46269989013672, 66.37936401367188, 161.44105529785156, 45.227294921875, 93.97333526611328, 388.7535095214844, 32.198951721191406, 111.84017181396484, 56.7442741394043, 93.12567138671875, 287.4051513671875, 106.62586975097656, 86.7943115234375, 119.8591079711914, 283.93609619140625, 278.6153869628906, 262.8547668457031, 329.0709228515625, 150.96066284179688, 107.97705078125, 213.85653686523438, 1456.46923828125, 170.1866912841797, 336.18804931640625, 288.25189208984375, 320.5009460449219, 254.59378051757812, 135.34481811523438, 179.75057983398438, 306.06719970703125, 593.0714721679688, 669.2474975585938, 307.2456359863281, 395.3508605957031, 276.61773681640625, 341.06134033203125, 426.5908203125, 337.39056396484375, 279.8851318359375, 229.3716278076172, 312.2957458496094, 454.8868408203125, 393.4319152832031, 33.832366943359375, 9.971091270446777, 6.668871879577637, 10.019710540771484, 5.015836715698242, 6.691263675689697, 4.185768127441406, 4.184843063354492, 4.191628932952881, 4.1905388832092285, 6.699402332305908, 4.19249153137207, 4.194969654083252, 4.1932692527771, 7.5477142333984375, 5.033802509307861, 3.3622658252716064, 3.359252452850342, 3.3573250770568848, 5.88267707824707, 3.362156391143799, 3.3636653423309326, 3.360513687133789, 3.361147403717041, 3.3635709285736084, 3.363074779510498, 5.890581130981445, 3.365257978439331, 7.573462009429932, 4.2113165855407715, 5.883683204650879, 27.909366607666016, 28.82026481628418, 8.439029693603516, 13.542276382446289, 454.8868408203125, 81.13459014892578, 11.853827476501465, 29.84036636352539, 5.911060810089111, 220.32559204101562, 24.7734375, 231.329833984375, 233.60546875, 393.4319152832031, 212.19583129882812, 102.29795837402344, 57.954742431640625, 1456.46923828125, 31.874820709228516, 106.44732666015625, 229.3716278076172, 669.2474975585938, 103.12078857421875, 98.69776916503906, 276.61773681640625, 96.08226013183594, 355.5611572265625, 136.11471557617188, 508.212890625, 185.42788696289062, 593.0714721679688, 400.12762451171875, 306.06719970703125, 179.75057983398438, 426.5908203125, 288.25189208984375, 307.2456359863281, 274.6512756347656, 336.18804931640625, 283.93609619140625, 388.7535095214844, 279.8851318359375, 234.59474182128906, 370.9205322265625, 395.3508605957031, 341.06134033203125, 254.59378051757812, 255.24029541015625, 320.5009460449219], "Category": ["Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Default", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic1", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic2", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3", "Topic3"], "logprob": [30.0, 29.0, 28.0, 27.0, 26.0, 25.0, 24.0, 23.0, 22.0, 21.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, -8.300299644470215, -7.683000087738037, -8.413900375366211, -9.270700454711914, -9.27560043334961, -7.381199836730957, -8.128999710083008, -8.134099960327148, -8.372400283813477, -9.002900123596191, -9.47700023651123, -9.478099822998047, -9.4798002243042, -9.479000091552734, -9.4822998046875, -9.482999801635742, -9.484399795532227, -9.48490047454834, -9.487000465393066, -8.154199600219727, -8.800399780273438, -9.497699737548828, -6.090199947357178, -8.11460018157959, -8.810799598693848, -7.397600173950195, -9.505499839782715, -9.503399848937988, -8.632699966430664, -9.32859992980957, -8.134200096130371, -6.222799777984619, -8.29740047454834, -8.192399978637695, -7.116000175476074, -8.245699882507324, -8.105500221252441, -8.317099571228027, -8.566699981689453, -8.50879955291748, -7.934800148010254, -7.546899795532227, -8.287300109863281, -5.883500099182129, -6.010799884796143, -5.506700038909912, -5.78980016708374, -6.506499767303467, -5.883399963378906, -7.070899963378906, -7.809599876403809, -5.502399921417236, -5.804599761962891, -5.445000171661377, -5.679200172424316, -6.953000068664551, -4.370699882507324, -6.9558000564575195, -6.201000213623047, -5.154600143432617, -6.48769998550415, -5.093299865722656, -6.048299789428711, -6.715799808502197, -5.55679988861084, -5.502299785614014, -6.263700008392334, -5.722499847412109, -5.691400051116943, -5.930200099945068, -6.046899795532227, -6.2179999351501465, -6.186100006103516, -6.13100004196167, -5.878600120544434, -5.991399765014648, -5.889699935913086, -5.793300151824951, -6.008900165557861, -6.070899963378906, -6.107600212097168, -6.0457000732421875, -5.966800212860107, -5.889400005340576, -5.996600151062012, -6.063399791717529, -7.676400184631348, -9.111200332641602, -9.114299774169922, -8.661299705505371, -9.373000144958496, -9.374899864196777, -8.681699752807617, -8.567899703979492, -9.394399642944336, -9.179400444030762, -9.412799835205078, -9.021100044250488, -9.02079963684082, -9.4266996383667, -9.20989990234375, -8.252099990844727, -9.43910026550293, -8.182900428771973, -9.730299949645996, -9.731100082397461, -9.731800079345703, -9.7322998046875, -9.731599807739258, -9.732199668884277, -9.7322998046875, -9.732000350952148, -9.732099533081055, -9.732500076293945, -9.732799530029297, -9.73490047454834, -8.34939956665039, -8.754300117492676, -9.047200202941895, -7.797699928283691, -8.650699615478516, -8.558600425720215, -8.566200256347656, -8.914600372314453, -8.48330020904541, -9.235300064086914, -9.452500343322754, -8.689000129699707, -7.13670015335083, -6.137599945068359, -6.895599842071533, -7.898499965667725, -6.448800086975098, -7.600100040435791, -6.71589994430542, -7.27869987487793, -7.854400157928467, -7.558899879455566, -5.0945000648498535, -6.670599937438965, -6.861400127410889, -6.10129976272583, -7.197700023651123, -6.587600231170654, -5.399600028991699, -7.498899936676025, -6.462500095367432, -7.034200191497803, -6.625500202178955, -5.708399772644043, -6.527500152587891, -6.696800231933594, -6.44789981842041, -5.783699989318848, -5.806399822235107, -5.8572998046875, -5.697400093078613, -6.306600093841553, -6.563300132751465, -6.067699909210205, -4.652200222015381, -6.2540998458862305, -5.775300025939941, -5.884099960327148, -5.8354997634887695, -5.99399995803833, -6.426700115203857, -6.2667999267578125, -5.968299865722656, -5.591400146484375, -5.553999900817871, -5.98390007019043, -5.867499828338623, -6.066699981689453, -6.0229997634887695, -5.957300186157227, -6.1265997886657715, -6.198999881744385, -6.257299900054932, -6.238800048828125, -6.204599857330322, -6.219399929046631, -6.957099914550781, -8.23960018157959, -8.678999900817871, -8.286600112915039, -8.997200012207031, -8.71660041809082, -9.187600135803223, -9.192299842834473, -9.19849967956543, -9.199399948120117, -8.7322998046875, -9.204899787902832, -9.208700180053711, -9.209799766540527, -8.62339973449707, -9.038100242614746, -9.449600219726562, -9.450900077819824, -9.451700210571289, -8.89229965209961, -9.452199935913086, -9.452799797058105, -9.45419979095459, -9.45419979095459, -9.455900192260742, -9.456600189208984, -8.906100273132324, -9.468000411987305, -8.662400245666504, -9.250399589538574, -8.918000221252441, -7.416100025177002, -7.414999961853027, -8.58590030670166, -8.142999649047852, -4.854599952697754, -6.479700088500977, -8.279800415039062, -7.457600116729736, -8.942099571228027, -5.717400074005127, -7.670100212097168, -5.720300197601318, -5.750100135803223, -5.3653998374938965, -5.8933000564575195, -6.5065999031066895, -7.013599872589111, -4.339399814605713, -7.520699977874756, -6.565299987792969, -5.943999767303467, -5.111299991607666, -6.61870002746582, -6.667600154876709, -5.893799781799316, -6.713200092315674, -5.743299961090088, -6.4608001708984375, -5.4893999099731445, -6.237299919128418, -5.395699977874756, -5.687699794769287, -5.880799770355225, -6.26609992980957, -5.662499904632568, -5.939799785614014, -5.899499893188477, -6.0295000076293945, -5.9456000328063965, -6.064499855041504, -5.884399890899658, -6.091300010681152, -6.184899806976318, -5.959099769592285, -5.932700157165527, -6.03410005569458, -6.176599979400635, -6.203199863433838, -6.214600086212158], "loglift": [30.0, 29.0, 28.0, 27.0, 26.0, 25.0, 24.0, 23.0, 22.0, 21.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.7942000031471252, 0.7879999876022339, 0.7540000081062317, 0.7419000267982483, 0.7368999719619751, 0.7336000204086304, 0.7325999736785889, 0.7258999943733215, 0.7250999808311462, 0.7250000238418579, 0.7185999751091003, 0.7182999849319458, 0.7172999978065491, 0.7168999910354614, 0.713699996471405, 0.713100016117096, 0.711899995803833, 0.7116000056266785, 0.7103999853134155, 0.7085999846458435, 0.7055000066757202, 0.6998000144958496, 0.6990000009536743, 0.6988999843597412, 0.6955000162124634, 0.6941999793052673, 0.6931999921798706, 0.6923999786376953, 0.6923999786376953, 0.6891000270843506, 0.680400013923645, 0.6570000052452087, 0.6790000200271606, 0.6717000007629395, 0.6370999813079834, 0.6662999987602234, 0.65829998254776, 0.6658999919891357, 0.6723999977111816, 0.6585999727249146, 0.6215000152587891, 0.5827000141143799, 0.6376000046730042, 0.43369999527931213, 0.44449999928474426, 0.3910999894142151, 0.4117000102996826, 0.4706000089645386, 0.38679999113082886, 0.5073000192642212, 0.5918999910354614, 0.30059999227523804, 0.3343999981880188, 0.28220000863075256, 0.29589998722076416, 0.47859999537467957, 0.06459999829530716, 0.47540000081062317, 0.351500004529953, 0.17919999361038208, 0.3896999955177307, 0.11959999799728394, 0.3001999855041504, 0.42559999227523804, 0.18250000476837158, 0.16089999675750732, 0.3109999895095825, 0.16449999809265137, 0.15389999747276306, 0.2037000060081482, 0.21950000524520874, 0.25440001487731934, 0.21610000729560852, 0.1858000010251999, 0.0706000030040741, 0.11209999769926071, 0.03310000151395798, -0.04910000041127205, 0.07569999992847443, 0.10599999874830246, 0.12229999899864197, 0.04349999874830246, -0.06549999862909317, -0.40119999647140503, -0.24050000309944153, -0.07199999690055847, 1.1359000205993652, 1.091599941253662, 1.0889999866485596, 1.0717999935150146, 1.0543999671936035, 1.0528000593185425, 1.0514999628067017, 1.0442999601364136, 1.0341999530792236, 1.0285999774932861, 1.0164999961853027, 1.0073000192642212, 1.0046000480651855, 1.003100037574768, 0.9998999834060669, 0.9975000023841858, 0.9918000102043152, 0.988099992275238, 0.9872000217437744, 0.9864000082015991, 0.9861000180244446, 0.9860000014305115, 0.9858999848365784, 0.9855999946594238, 0.9855999946594238, 0.9855999946594238, 0.9853000044822693, 0.9851999878883362, 0.9848999977111816, 0.9829000234603882, 0.9804999828338623, 0.9781000018119812, 0.9789000153541565, 0.9394000172615051, 0.9603000283241272, 0.9552000164985657, 0.9505000114440918, 0.9595999717712402, 0.9375, 0.9664999842643738, 0.9754999876022339, 0.9366999864578247, 0.8540999889373779, 0.7509999871253967, 0.7986999750137329, 0.8733999729156494, 0.7430999875068665, 0.8159999847412109, 0.7124000191688538, 0.771399974822998, 0.8360000252723694, 0.7728999853134155, 0.3935999870300293, 0.6360999941825867, 0.6622999906539917, 0.5335999727249146, 0.7096999883651733, 0.5884000062942505, 0.3564999997615814, 0.748199999332428, 0.5393999814987183, 0.6463000178337097, 0.5595999956130981, 0.349700003862381, 0.5221999883651733, 0.5587000250816345, 0.4848000109195709, 0.2865999937057495, 0.28279998898506165, 0.29010000824928284, 0.22540000081062317, 0.3953999876976013, 0.47380000352859497, 0.28600001335144043, -0.21690000593662262, 0.3280999958515167, 0.12600000202655792, 0.17110000550746918, 0.1137000024318695, 0.18539999425411224, 0.38449999690055847, 0.260699987411499, 0.027000000700354576, -0.25760000944137573, -0.34119999408721924, 0.007499999832361937, -0.1281999945640564, 0.02969999983906746, -0.13600000739097595, -0.29409998655319214, -0.2287999987602234, -0.1143999993801117, 0.026399999856948853, -0.263700008392334, -0.6055999994277954, -0.47519999742507935, 1.2404999732971191, 1.179800033569336, 1.1426000595092773, 1.1277999877929688, 1.1092000007629395, 1.101699948310852, 1.0997999906539917, 1.0952999591827393, 1.087399959564209, 1.0867999792099, 1.0846999883651733, 1.080899953842163, 1.0765000581741333, 1.0757999420166016, 1.0743999481201172, 1.0647000074386597, 1.0568000078201294, 1.05649995803833, 1.0562000274658203, 1.0547000169754028, 1.0542000532150269, 1.0532000064849854, 1.0528000593185425, 1.0526000261306763, 1.0500999689102173, 1.0496000051498413, 1.0396000146865845, 1.037500023841858, 1.031999945640564, 1.0307999849319458, 1.0288000106811523, 0.9739999771118164, 0.9430000185966492, 1.0003000497817993, 0.970300018787384, 0.7443000078201294, 0.8432000279426575, 0.9666000008583069, 0.8655999898910522, 1.000100016593933, 0.6065000295639038, 0.8392000198364258, 0.5548999905586243, 0.5153999924659729, 0.37880000472068787, 0.4681999981403351, 0.5845000147819519, 0.645799994468689, 0.0957999974489212, 0.7365000247955322, 0.4860999882221222, 0.33970001339912415, 0.10159999877214432, 0.4643999934196472, 0.4593000113964081, 0.20260000228881836, 0.4406999945640564, 0.10209999978542328, 0.34470000863075256, -0.0013000000035390258, 0.2590999901294708, -0.06199999898672104, 0.03959999978542328, 0.1143999993801117, 0.2612999975681305, 0.000699999975040555, 0.11550000309944153, 0.09189999848604202, 0.07400000095367432, -0.044199999421834946, 0.005799999926239252, -0.1282999962568283, -0.0066999997943639755, 0.0763000026345253, -0.15600000321865082, -0.19339999556541443, -0.14710000157356262, 0.00279999990016222, -0.026399999856948853, -0.265500009059906]}, "token.table": {"Topic": [3, 2, 3, 2, 1, 2, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 2, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 2, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 1, 2, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 2, 1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 1, 2, 3, 3, 1, 3, 1, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 2, 2, 3, 1, 1, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 2, 3, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 3, 3, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 3, 3, 1, 1, 2, 3, 1, 2, 3, 1, 3, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 1, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 2, 1, 2, 3, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 1, 3, 2, 1, 2, 3, 1, 3, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], "Freq": [0.8925523161888123, 0.14944860339164734, 0.896691620349884, 0.8827691078186035, 0.8733581900596619, 0.8244616985321045, 0.8038777709007263, 0.0846187174320221, 0.12692807614803314, 0.3137272596359253, 0.09411817789077759, 0.5960817933082581, 0.7346426844596863, 0.5084091424942017, 0.25546929240226746, 0.23270468413829803, 0.9121668934822083, 0.1824333816766739, 0.1020096018910408, 0.6375600099563599, 0.2550240159034729, 0.87239009141922, 0.11054447293281555, 0.7738112807273865, 0.11054447293281555, 0.642488956451416, 0.11243556439876556, 0.24896445870399475, 0.29200950264930725, 0.475558340549469, 0.23360760509967804, 0.3365112245082855, 0.3469187915325165, 0.31916528940200806, 0.7349174618721008, 0.7348324060440063, 0.7347398996353149, 0.18487799167633057, 0.14790239930152893, 0.665560781955719, 0.47014519572257996, 0.250744104385376, 0.2781692445278168, 0.7951574921607971, 0.061165958642959595, 0.12233191728591919, 0.4305296838283539, 0.2600228786468506, 0.30691224336624146, 0.761050820350647, 0.2174430787563324, 0.03624051436781883, 0.8374797105789185, 0.0837479680776596, 0.0837479680776596, 0.7375996112823486, 0.18439990282058716, 0.7958890795707703, 0.07579895853996277, 0.13264818489551544, 0.6867859959602356, 0.09615004062652588, 0.21977153420448303, 0.3456447720527649, 0.5069456696510315, 0.13825790584087372, 0.8724744319915771, 0.8919092416763306, 0.878101110458374, 0.2447502762079239, 0.5214245319366455, 0.23410896956920624, 0.9026093482971191, 0.16755826771259308, 0.16755826771259308, 0.6702330708503723, 0.255047082901001, 0.25072425603866577, 0.49280285835266113, 0.892255425453186, 0.9753973484039307, 0.5742470026016235, 0.18332767486572266, 0.24263957142829895, 0.8508691191673279, 0.10635863989591599, 0.05317931994795799, 0.192295104265213, 0.6970697641372681, 0.12018444389104843, 0.10811518132686615, 0.6162565350532532, 0.27028796076774597, 0.7732152938842773, 0.08284449577331543, 0.16568899154663086, 0.22431296110153198, 0.24156780540943146, 0.5349001288414001, 0.16996155679225922, 0.8498077988624573, 0.1492670476436615, 0.895602285861969, 0.5922998189926147, 0.18863052129745483, 0.21503879129886627, 0.403611421585083, 0.4140496551990509, 0.1809292584657669, 0.39382171630859375, 0.29292523860931396, 0.31245359778404236, 0.9542829394340515, 0.27159392833709717, 0.43057575821876526, 0.2980909049510956, 0.13204000890254974, 0.7922400832176208, 0.2904791831970215, 0.19062696397304535, 0.5219547748565674, 0.4442230463027954, 0.3881106376647949, 0.1683371514081955, 0.1451331377029419, 0.6772879958152771, 0.19351086020469666, 0.8721117377281189, 0.2749897837638855, 0.8249692916870117, 0.8528668284416199, 0.07950453460216522, 0.06504916399717331, 0.5475937724113464, 0.25273558497428894, 0.20008233189582825, 0.2912238538265228, 0.253646582365036, 0.4603215754032135, 0.16927696764469147, 0.761746346950531, 0.08463848382234573, 0.24253389239311218, 0.545701265335083, 0.20615381002426147, 0.2503468990325928, 0.3783019781112671, 0.36717545986175537, 0.24401673674583435, 0.1582811176776886, 0.5979509353637695, 0.8914620876312256, 0.4450579881668091, 0.3876311480998993, 0.16869132220745087, 0.8930558562278748, 0.3253348469734192, 0.1969131976366043, 0.4751601219177246, 0.16917437314987183, 0.8458718657493591, 0.2833458185195923, 0.432889461517334, 0.2833458185195923, 0.6536827087402344, 0.07663866132497787, 0.2704893946647644, 0.7345367670059204, 0.8721710443496704, 0.7346720099449158, 0.6624627113342285, 0.16044017672538757, 0.17596665024757385, 0.9421329498291016, 0.07247176766395569, 0.5270665287971497, 0.2442503422498703, 0.22710996866226196, 0.6046537756919861, 0.23387552797794342, 0.1654241532087326, 0.5721740126609802, 0.223287433385849, 0.20002831518650055, 0.2193198949098587, 0.6579596996307373, 0.20996131002902985, 0.6823742985725403, 0.10498065501451492, 0.954531192779541, 0.8427315950393677, 0.1296510100364685, 0.9073959589004517, 0.9358930587768555, 0.07799109071493149, 0.2771812677383423, 0.5007145404815674, 0.2235332727432251, 0.3464932143688202, 0.5724670886993408, 0.09038953483104706, 0.411312997341156, 0.4054371118545532, 0.1821528971195221, 0.05069262906908989, 0.7603894472122192, 0.20277051627635956, 0.9540866017341614, 0.8612512350082397, 0.05741674825549126, 0.05741674825549126, 0.4781489670276642, 0.20769596099853516, 0.31378525495529175, 0.7974741458892822, 0.22152848541736603, 0.07384283095598221, 0.7384282946586609, 0.14332106709480286, 0.10749079287052155, 0.752435564994812, 0.734749972820282, 0.4260416328907013, 0.20493142306804657, 0.36671939492225647, 0.2686198055744171, 0.27804505825042725, 0.45241227746009827, 0.10044029355049133, 0.7030820846557617, 0.10044029355049133, 0.8745641112327576, 0.2955414354801178, 0.4285350739955902, 0.27337580919265747, 0.13727480173110962, 0.8236487507820129, 0.8731337189674377, 0.297322154045105, 0.4955368936061859, 0.21060317754745483, 0.4531506597995758, 0.23481443524360657, 0.31239932775497437, 0.8216742873191833, 0.05477828532457352, 0.10955657064914703, 0.22064843773841858, 0.6619452834129333, 0.11032421886920929, 0.8273963928222656, 0.07147326320409775, 0.6432594060897827, 0.285893052816391, 0.5699725151062012, 0.2241465002298355, 0.20493394136428833, 0.8192324042320251, 0.13653872907161713, 0.862309992313385, 0.05748733505606651, 0.05748733505606651, 0.3200130760669708, 0.2230394184589386, 0.455776184797287, 0.8247098326683044, 0.8843103051185608, 0.2210775762796402, 0.8734897971153259, 0.8719697594642639, 0.1552845537662506, 0.6211382150650024, 0.21739837527275085, 0.7154322266578674, 0.1839851289987564, 0.7359405159950256, 0.1839851289987564, 0.2836943566799164, 0.26343047618865967, 0.4458054304122925, 0.8254503011703491, 0.9558303356170654, 0.6869451999664307, 0.08243342489004135, 0.23356136679649353, 0.7123662829399109, 0.30082187056541443, 0.30082187056541443, 0.3967360854148865, 0.11849703639745712, 0.11849703639745712, 0.8294792771339417, 0.8213603496551514, 0.09126225858926773, 0.09126225858926773, 0.6283518671989441, 0.23118607699871063, 0.13930442929267883, 0.09980328381061554, 0.8982295393943787, 0.9556190967559814, 0.8057971596717834, 0.057556938380002975, 0.057556938380002975, 0.2865230143070221, 0.3159100115299225, 0.4040709435939789, 0.7348172664642334, 0.5092111229896545, 0.23883351683616638, 0.2478461116552353, 0.4993075132369995, 0.21800750494003296, 0.2836441695690155, 0.680278480052948, 0.1395443081855774, 0.18315190076828003, 0.8918842077255249, 0.21505805850028992, 0.2737102508544922, 0.5083190202713013, 0.20182907581329346, 0.16146326065063477, 0.6458530426025391, 0.6475719213485718, 0.14390486478805542, 0.20557838678359985, 0.8786365985870361, 0.8264027237892151, 0.9324409365653992, 0.03885170444846153, 0.03885170444846153, 0.32753849029541016, 0.38741111755371094, 0.2852754592895508, 0.494992196559906, 0.19124698638916016, 0.31499505043029785, 0.8151131868362427, 0.04748231917619705, 0.13453324139118195, 0.8453991413116455, 0.12077131122350693, 0.5623205900192261, 0.14245454967021942, 0.2949059009552002, 0.623637318611145, 0.21314185857772827, 0.15788286924362183, 0.4041360020637512, 0.18046323955059052, 0.4143029451370239, 0.8372472524642944, 0.06440363824367523, 0.06440363824367523, 0.8920408487319946, 0.521720826625824, 0.2514769434928894, 0.22895660996437073, 0.12162233889102936, 0.8513563871383667, 0.8598747849464417, 0.057324983179569244, 0.057324983179569244, 0.8574591279029846, 0.15590165555477142, 0.07795082777738571, 0.7151422500610352, 0.8718400001525879, 0.5774297118186951, 0.1924765706062317, 0.22747232019901276, 0.3956557512283325, 0.3880469799041748, 0.2130454033613205, 0.8748948574066162, 0.10936185717582703, 0.8997023701667786, 0.11055271327495575, 0.5969846248626709, 0.3095475733280182, 0.15611623227596283, 0.3954944312572479, 0.43712544441223145, 0.8726184964179993, 0.15647046267986298, 0.7823523283004761, 0.07823523133993149, 0.13879123330116272, 0.10409342497587204, 0.7286539673805237, 0.36528778076171875, 0.34957650303840637, 0.2828034460544586, 0.892720639705658, 0.8722589015960693, 0.07268824428319931, 0.07268824428319931, 0.2778368294239044, 0.47232258319854736, 0.2593143582344055, 0.7346327304840088, 0.3985864520072937, 0.3301723599433899, 0.27068182826042175, 0.8330913186073303, 0.10413641482591629, 0.052068207412958145, 0.13695687055587769, 0.5889145731925964, 0.2602180540561676, 0.13724538683891296, 0.8234723210334778, 0.9075385332107544, 0.1697625368833542, 0.1697625368833542, 0.8488126993179321, 0.8935685157775879, 0.21570749580860138, 0.48768651485443115, 0.29073619842529297, 0.45733046531677246, 0.26082128286361694, 0.28225865960121155, 0.4792388677597046, 0.2685390114784241, 0.25201353430747986, 0.13716283440589905, 0.8229770064353943, 0.7348452210426331, 0.8754855990409851, 0.05471784994006157, 0.10943569988012314, 0.8706566691398621, 0.08162406086921692, 0.05441604182124138, 0.13249044120311737, 0.7949426770210266, 0.6237050294876099, 0.17635796964168549, 0.19786503911018372, 0.05465681850910187, 0.9291659593582153, 0.4375956356525421, 0.3646630346775055, 0.19448694586753845, 0.3344021141529083, 0.41671648621559143, 0.24951542913913727, 0.3822689950466156, 0.30058759450912476, 0.3169238567352295, 0.4555368721485138, 0.32761213183403015, 0.21840809285640717, 0.15805064141750336, 0.790253221988678, 0.15805064141750336, 0.5075273513793945, 0.22594241797924042, 0.2664097249507904, 0.24294671416282654, 0.728840172290802, 0.19865697622299194, 0.7946279048919678, 0.7352049350738525, 0.5251578688621521, 0.2503088712692261, 0.2208607792854309, 0.1699906289577484, 0.8499531745910645, 0.8751994371414185, 0.10939992964267731, 0.10939992964267731, 0.8922845125198364, 0.47332748770713806, 0.2184588462114334, 0.3058423697948456, 0.11021983623504639, 0.7715388536453247, 0.11021983623504639, 0.872270941734314, 0.2155417948961258, 0.6146932244300842, 0.16764360666275024, 0.5013760924339294, 0.2550860643386841, 0.24629001319408417, 0.7346058487892151, 0.7000299096107483, 0.1909172534942627, 0.11136839538812637, 0.1232689842581749, 0.7396138906478882, 0.1232689842581749, 0.09171491861343384, 0.7337193489074707, 0.09171491861343384, 0.2684544324874878, 0.5154325366020203, 0.2147635519504547, 0.8260155916213989, 0.3506644368171692, 0.30005306005477905, 0.3470493257045746, 0.18386396765708923, 0.7354558706283569, 0.18386396765708923, 0.26434385776519775, 0.5639335513114929, 0.17622923851013184, 0.16872186958789825, 0.08436093479394913, 0.7592484354972839, 0.16900761425495148, 0.642228901386261, 0.20280912518501282], "Term": [" prj", " scf", " scf", "acsddc", "adriana", "af ", "aka", "aka", "aka", "albicans", "albicans", "albicans", "anl", "anyone", "anyone", "anyone", "arythmia", "arythmia", "astros", "astros", "astros", "avi", "bal", "bal", "bal", "banks", "banks", "banks", "base", "base", "base", "baseball", "baseball", "baseball", "belinda", "blocking", "candee", "candida", "candida", "candida", "case", "case", "case", "cboesel", "cboesel", "cboesel", "center", "center", "center", "cereal", "cereal", "cereal", "cfs", "cfs", "cfs", "chad", "chad", "charles", "charles", "charles", "chastity", "chastity", "chastity", "chicago", "chicago", "chicago", "choueiry", "chumphre", "cipiti", "city", "city", "city", "clubbing", "col", "col", "col", "color", "color", "color", "compass", "compass ", "computer", "computer", "computer", "corn", "corn", "corn", "cub", "cub", "cub", "cubs", "cubs", "cubs", "curve", "curve", "curve", "cview", "cview", "cview", "cx com", "cx com", "dane", "dane", "data", "data", "data", "david", "david", "david", "day", "day", "day", "denman", "dept", "dept", "dept", "dir", "dir", "disease", "disease", "disease", "doctor", "doctor", "doctor", "dominance", "dominance", "dominance", "dotzlaw", "driftwood", "driftwood", "dyer", "dyer", "dyer", "effect", "effect", "effect", "email", "email", "email", "erickson", "erickson", "erickson", "eye", "eye", "eye", "fan", "fan", "fan", "file", "file", "file", "fingertip", "food", "food", "food", "fopen", "format", "format", "format", "francesa", "francesa", "game", "game", "game", "geb", "geb", "geb", "gia", "gilmete", "gkiria", "gordon", "gordon", "gordon", "graeme", "graeme", "graphic", "graphic", "graphic", "graphics", "graphics", "graphics", "group", "group", "group", "hagins", "hagins", "harry", "harry", "harry", "helium", "hernia", "hernia", "hexagon", "hismanal", "hismanal", "hitter", "hitter", "hitter", "hiv", "hiv", "hiv", "home", "home", "home", "idle", "idle", "idle", "ilmenau", "ima", "ima", "ima", "image", "image", "image", "infotrac", "inhibitor", "inhibitor", "inhibitor", "int", "int", "int", "jake", "john", "john", "john", "jpeg", "jpeg", "jpeg", "kan", "kan", "kan", "khun", "kind", "kind", "kind", "klonopin", "klonopin", "lausanne", "league", "league", "league", "lines", "lines", "lines", "linus", "linus", "linus", "linux", "linux", "linux", "lions", "lost", "lost", "lost", "lot", "lot", "lot", "lrc edu", "lrc edu", "m c", "m c", "m c", "machine", "machine", "machine", "maier", "mccall", "mccall", "mckay", "mg dl", "minnesota", "minnesota", "minnesota", "miro", "mono", "mono", "mono", "morris", "morris", "morris", "mpeg play", "muller", "n jxp", "n jxp", "n jxp", "neuharth", "new", "new", "new", "northern", "northern", "northern", "nosebleed", "nosebleed", "nosebleed", "number", "number", "number", "oct", "oct", "op rows", "outline", "outline", "outline", "pain", "pain", "pain", "pallis", "patient", "patient", "patient", "people", "people", "people", "person", "person", "person", "peterbak", "phillies", "phillies", "phillies", "phils", "phils", "phils", "phone", "phone", "phone", "piano", "pistons", "pittsburg", "pittsburg", "pittsburg", "player", "player", "player", "point", "point", "point", "polygon", "polygon", "polygon", "prk", "prk", "problem", "problem", "problem", "product", "product", "product", "program", "program", "program", "programs", "programs", "programs", "qed", "question", "question", "question", "rauser", "rauser", "rayssd", "rayssd", "rayssd", "recommend", "recommend", "recommend", "reiniger", "renggli", "reply to", "reply to", "reply to", "research", "research", "research", "rhinitis", "rhinitis", "rix", "rockies", "rockies", "rockies", "roger", "roger", "roger", "rokne", "rot qc ca", "rot qc ca", "rot qc ca", "row", "row", "row", "run", "run", "run", "rych", "s p", "s p", "s p", "san", "san", "san", "sas ", "science", "science", "science", "scodal", "scodal", "scodal", "scott", "scott", "scott", "shapiro", "shapiro", "sheryl", "shippert", "shippert", "shippert", "sizeof", "smith", "smith", "smith", "software", "software", "software", "something", "something", "something", "sosa", "sosa", "soth", "spdcc", "spdcc", "spdcc", "spdcc com", "spdcc com", "spdcc com", "spect", "spect", "steve", "steve", "steve", "suck", "suck", "system", "system", "system", "team", "team", "team", "thanks", "thanks", "thanks", "thing", "thing", "thing", "thornley", "thornley", "thornley", "time", "time", "time", "timlin", "timlin", "tremor", "tremor", "trombone", "use", "use", "use", "valo", "valo", "vasomotor", "vasomotor", "vasomotor", "vatti", "version", "version", "version", "vizcaino", "vizcaino", "vizcaino", "voronoi", "water", "water", "water", "way", "way", "way", "wcarter", "weight", "weight", "weight", "wetteland", "wetteland", "wetteland", "whi", "whi", "whi", "windows", "windows", "windows", "wings", "world", "world", "world", "yale edu", "yale edu", "yale edu", "yankees", "yankees", "yankees", "yogurt", "yogurt", "yogurt", "zisfein", "zisfein", "zisfein"]}, "R": 30, "lambda.step": 0.01, "plot.opts": {"xlab": "PC1", "ylab": "PC2"}, "topic.order": [1, 3, 2]};

function LDAvis_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(LDAvis) !== "undefined"){
   // already loaded: just create the visualization
   !function(LDAvis){
       new LDAvis("#" + "ldavis_el90791122734952483851015077", ldavis_el90791122734952483851015077_data);
   }(LDAvis);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/LDAvis
   require.config({paths: {d3: "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      LDAvis_load_lib("https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.js", function(){
        new LDAvis("#" + "ldavis_el90791122734952483851015077", ldavis_el90791122734952483851015077_data);
      });
    });
}else{
    // require.js not available: dynamically load d3 & LDAvis
    LDAvis_load_lib("https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js", function(){
         LDAvis_load_lib("https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.js", function(){
                 new LDAvis("#" + "ldavis_el90791122734952483851015077", ldavis_el90791122734952483851015077_data);
            })
         });
}
</script>




```python

```


```python

```


```python

```
