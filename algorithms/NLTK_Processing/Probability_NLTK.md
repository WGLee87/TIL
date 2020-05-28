```python
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
```

###### NLTK 패키지의 바이그램 모형
    - ngram 명령으로 문장을 바이그램 분해
    - ConditionalFreqDist 클래스로 각 문맥 별 단어 빈도를 측정
    - ConditionalProbDist 클래스로 조건부 확률을 추정

###### 실습 : NLTK로 바이그램 모형 제작

    Step1 말뭉치 바이그램 토큰화


```python
from nltk.corpus import movie_reviews
from nltk.util import ngrams

sentences = []
for tokens in movie_reviews.sents():
    bigram = ngrams(tokens, 2, pad_left=True, pad_right=True, left_pad_symbol='SS', right_pad_symbol='SE')
    sentences += [t for t in bigram]
    
sentences[:17]
```




    [('SS', 'plot'),
     ('plot', ':'),
     (':', 'two'),
     ('two', 'teen'),
     ('teen', 'couples'),
     ('couples', 'go'),
     ('go', 'to'),
     ('to', 'a'),
     ('a', 'church'),
     ('church', 'party'),
     ('party', ','),
     (',', 'drink'),
     ('drink', 'and'),
     ('and', 'then'),
     ('then', 'drive'),
     ('drive', '.'),
     ('.', 'SE')]



    Step2 ConditionalFreqDist 클래스 객체 생성


```python
from nltk import ConditionalFreqDist
cfd = ConditionalFreqDist(sentences)

cfd['SS'].most_common(5)
```




    [('the', 8071), ('.', 3173), ('it', 3136), ('i', 2471), ('but', 1814)]




```python
cfd['SS'].plot(5, title='문장의 첫단어 분포')
plt.show()
```

<img width="404" alt="output_7_0" src="https://user-images.githubusercontent.com/59719711/82319797-2c7f1600-9a0d-11ea-855e-0d111d76115a.png">


    Step3 조건부 확률 추정


```python
from nltk.probability import ConditionalProbDist, MLEProbDist
cpd = ConditionalProbDist(cfd, MLEProbDist)
```




    <ConditionalProbDist with 39769 conditions>




```python
cpd['i'].prob('am')
```




    0.018562267971650354




```python
cpd['she'].prob('is')
```




    0.1174785100286533




```python
cpd['we'].prob('are')
```




    0.08504504504504505




```python
cpd['you'].prob('are')
```




    0.031790820165538



    Step4 문장 확률 계산


```python
def sentence_score(s):
    p = 0.0
    for i in range(len(s) - 1):
        c = s[i]
        w= s[i+1]
        p += np.log(cpd[c].prob(w) + np.finfo(float).eps)   # 0이 나오면 에러이며 실수에서 가장 작은 값을 넣어주는 코드 eps 어쩌어쩌
    return np.exp(p)
```


```python
test_sentence = ['i',' like', 'the', 'movie', '.']
sentence_score(test_sentence)
```




    1.9222494746876606e-34




```python
test_sentence = ['do','i', 'like', 'the', 'movie', '.']
sentence_score(test_sentence)
```




    4.293625275307985e-08




```python
test_sentence = ['like','i', 'the', 'movie', '.']
sentence_score(test_sentence)
```




    1.0088151944997699e-20



    Step5 무작위 문장 생성


```python
def generate_sentence(seed=None):
    if seed is not None:
        import random
        random.seed(seed)
    c = 'SS'
    sentence = []
    while True:
        if c not in cpd:
            break
        w = cpd[c].generate()
        
        if w == 'SE':
            break
        else:
            w2 = w
        
        if c == 'SS':
            sentence.append(w2.title())
        else:
            sentence.append(' ' + w2)
        
        c = w
    return ''.join(sentence)
```


```python
generate_sentence()
```




    'Cameron hopes to maintain their unctuous european film , with government and tommy lee miller , and i half feet of princeton university professor finds it stands some interaction between the screen , of all , raising cain and i found people .'



###### 한글로 해보기


```python
!wget -nc -q https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt
```


```python
import codecs
with codecs.open('ratings_train.txt', encoding='utf-8') as f:
    data = [line.split('\t') for line in f.read().splitlines()]
    data = data[1:]
    
docs = [row[1] for row in data]
len(docs)
```




    150000




```python
import warnings
warnings.simplefilter('ignore')

from konlpy.tag import Okt
tagger = Okt()

def tokenize(doc):
    tokens = [' \ '.join(t) for t in tagger.pos(doc)]
    return tokens
tokenize('그 영화는 정말 재밌었어요.')
```




    ['그 \\ Noun',
     '영화 \\ Noun',
     '는 \\ Josa',
     '정말 \\ Noun',
     '재밌었어요 \\ Adjective',
     '. \\ Punctuation']




```python
from tqdm import tqdm
sentences = []
for d in tqdm(docs):
    tokens = tokenize(d)
    bigram = ngrams(tokens,2, pad_left=True, pad_right=True, left_pad_symbol='SS', right_pad_symbol='SE')
    sentences += [t for t in bigram]
```

    100%|██████████| 150000/150000 [12:08<00:00, 205.89it/s]



```python
sentences[:10]
```




    [('SS', '아 \\ Exclamation'),
     ('아 \\ Exclamation', '더빙 \\ Noun'),
     ('더빙 \\ Noun', '.. \\ Punctuation'),
     ('.. \\ Punctuation', '진짜 \\ Noun'),
     ('진짜 \\ Noun', '짜증나네요 \\ Adjective'),
     ('짜증나네요 \\ Adjective', '목소리 \\ Noun'),
     ('목소리 \\ Noun', 'SE'),
     ('SS', '흠 \\ Noun'),
     ('흠 \\ Noun', '... \\ Punctuation'),
     ('... \\ Punctuation', '포스터 \\ Noun')]




```python
cfd = ConditionalFreqDist(sentences)
cpd = ConditionalProbDist(cfd, MLEProbDist)

def korean_most_common(c, n, pos=None):
    if pos is None:
        return cfd[tokenize(c)[0]].most_common(n)
    else:
        return cfd['/'.join([c, pos])].most_common(n)
```


```python
korean_most_common('나', 10)
```




    [('는 \\ Josa', 831),
     ('의 \\ Josa', 339),
     ('만 \\ Josa', 213),
     ('에게 \\ Josa', 148),
     ('에겐 \\ Josa', 84),
     ('랑 \\ Josa', 81),
     ('한테 \\ Josa', 50),
     ('참 \\ Verb', 45),
     ('이 \\ Determiner', 44),
     ('와도 \\ Josa', 43)]




```python
korean_most_common('의', 10)
```




    [('영화 \\ Noun', 19),
     ('연기 \\ Noun', 14),
     ('구심 \\ Noun', 12),
     ('모습 \\ Noun', 9),
     ('감독 \\ Noun', 8),
     ('매력 \\ Noun', 7),
     ('감동 \\ Noun', 7),
     ('흐름 \\ Noun', 6),
     ('그 \\ Noun', 6),
     ('이야기 \\ Noun', 6)]




```python
def korean_bigram_prob(c,w):
    context = tokenize(c)[0]
    word = tokenize(w)[0]
    return cpd[context].prob(word)
```


```python
korean_bigram_prob('이', '영화')
```




    0.4010748656417948




```python
korean_bigram_prob('영화', '이')
```




    0.00015767585785521414




```python
def korean_generate_sentence(seed=None, debug=False):
    if seed is not None:
        import random
        random.seed(seed)
    c = 'SS'
    sentence = []
    while True:
        if c not in cpd:
            break
            
        w = cpd[c].generate()
        
        if w =='SE':
            break
            
        w2 = w.split("/")[0]
        pos = w.split("/")[1]
        
        if c == 'SS':
            sentence.append(w2.title())
        elif c in ["`", "\"", "(", "'"]:
            sentence.append(w2)
        elif w2 in ["'", ".", ",", ")", ":", ";", "?"]:
            sentence.append(w2)
        elif pos in ['Josa', 'Punctuation', 'Suffix']:
            sentence.append(w2)
        elif w in ['임/Noun', '것/Noun', '는걸/Noun', '릴때/Noun','되다/Verb','이다/Verb', '하다/verb', '이다/Adjective']:
            sentence.append(w2)
        else:
            sentence.append(" " + w2)
        c = w
                   
        if debug:
                   print(w)
    return " ".join(sentence)
```


```python
korean_generate_sentence(0)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-97-145068f2c552> in <module>
    ----> 1 korean_generate_sentence(0)
    

    <ipython-input-96-a2308fdd4467> in korean_generate_sentence(seed, debug)
         15 
         16         w2 = w.split("/")[0]
    ---> 17         pos = w.split("/")[1]
         18 
         19         if c == 'SS':


    IndexError: list index out of range



```python
korean_generate_sentence(1)
```


```python

```


```python

```
