```python
pip install soynlp
```


```python
!brew install wget
```


```python
!wget https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt -O 2016-10-20.txt
```


```python
from soynlp import DoublespaceLineCorpus

# corpus = DoublespaceLineCorpus('2016-10-20.txt') # 문서의 갯수
# len(corpus)

corpus = DoublespaceLineCorpus('2016-10-20.txt', iter_sent=True) #문장의 갯수
len(corpus)
```




    223357




```python
i = 0
for d in corpus:
    print(i, d)
    i += 1
    if i > 7:
        break
```

    0 19
    1 1990
    2 52 1 22
    3 오패산터널 총격전 용의자 검거 서울 연합뉴스 경찰 관계자들이 19일 오후 서울 강북구 오패산 터널 인근에서 사제 총기를 발사해 경찰을 살해한 용의자 성모씨를 검거하고 있다 성씨는 검거 당시 서바이벌 게임에서 쓰는 방탄조끼에 헬멧까지 착용한 상태였다 독자제공 영상 캡처 연합뉴스
    4 서울 연합뉴스 김은경 기자 사제 총기로 경찰을 살해한 범인 성모 46 씨는 주도면밀했다
    5 경찰에 따르면 성씨는 19일 오후 강북경찰서 인근 부동산 업소 밖에서 부동산업자 이모 67 씨가 나오기를 기다렸다 이씨와는 평소에도 말다툼을 자주 한 것으로 알려졌다
    6 이씨가 나와 걷기 시작하자 성씨는 따라가면서 미리 준비해온 사제 총기를 이씨에게 발사했다 총알이 빗나가면서 이씨는 도망갔다 그 빗나간 총알은 지나가던 행인 71 씨의 배를 스쳤다
    7 성씨는 강북서 인근 치킨집까지 이씨 뒤를 쫓으며 실랑이하다 쓰러뜨린 후 총기와 함께 가져온 망치로 이씨 머리를 때렸다


###### 단어 추출


```python
from soynlp.word import WordExtractor

word_extractor = WordExtractor()
word_extractor.train(corpus)
```

    training was done. used memory 0.942 Gbse memory 0.910 Gb



```python
word_score = word_extractor.extract()
```

    all cohesion probabilities was computed. # words = 223348
    all branching entropies was computed # words = 360721
    all accessor variety was computed # words = 360721



```python

```

###### cohesion


```python
print(word_score['연합'].cohesion_forward)
print(word_score['연합뉴'].cohesion_forward)
print(word_score['연합뉴스'].cohesion_forward)
print(word_score['연합뉴스는'].cohesion_forward)
```

    0.1943363253634125
    0.43154839105434084
    0.5710254410737682
    0.1535595043355021


###### branching entropy


```python
print(word_score['연합'].right_branching_entropy)
print(word_score['연합뉴'].right_branching_entropy) #연합뉴 다음에는 항상 '스'만 나옴. 그래서 엔트로피값이 0 (좋은거임)
print(word_score['연합뉴스'].right_branching_entropy)
print(word_score['연합뉴스는'].right_branching_entropy)
```

    0.42721236711742844
    -0.0
    3.8967810761022053
    0.410116318288409


###### Accessor Variety


```python
print(word_score['연합'].right_accessor_variety)
print(word_score['연합뉴'].right_accessor_variety)
print(word_score['연합뉴스'].right_accessor_variety)
print(word_score['연합뉴스는'].right_accessor_variety)
```

    42
    1
    158
    2


###### L-토큰화
    한국어의 경우 공백(띄어쓰기)으로 분리된 하나의 문자열은 'L토큰 + R토큰' 구조인 경우가 많다. 왼쪽에 오는 L토큰은 체언(명사, 대명사)이나, 동사, 형용사 등이고 오른쪽에 오는 R토큰은 조사, 동사, 형용사 등이다. 여러가지 길이의 L토큰의 점수를 비교하여 가장 점수가 높은 L단어를 찾는 것이 L토큰화이다 soynlp에서는 LTokenizer 클래스로 제공한다.


```python
from soynlp.tokenizer import LTokenizer
scores = {word:score.cohesion_forward for word, score in word_score.items()}
l_tokenizer = LTokenizer(scores=scores)

l_tokenizer.tokenize('안정성에 문제있는 스마트폰을 휴대하고 탑승할 경우에 압수한다.', flatten=False)
```




    [('안정성', '에'),
     ('문제', '있는'),
     ('스마트폰', '을'),
     ('휴대', '하고'),
     ('탑승', '할'),
     ('경우', '에'),
     ('압수', '한다.')]




```python

```

###### 연습문제


```python
import nltk
# nltk.download('movie_reviews')

from nltk.corpus import movie_reviews
sentences = [list(s) for s in movie_reviews.sents()]
sentences[:10]
```




    [['plot',
      ':',
      'two',
      'teen',
      'couples',
      'go',
      'to',
      'a',
      'church',
      'party',
      ',',
      'drink',
      'and',
      'then',
      'drive',
      '.'],
     ['they', 'get', 'into', 'an', 'accident', '.'],
     ['one',
      'of',
      'the',
      'guys',
      'dies',
      ',',
      'but',
      'his',
      'girlfriend',
      'continues',
      'to',
      'see',
      'him',
      'in',
      'her',
      'life',
      ',',
      'and',
      'has',
      'nightmares',
      '.'],
     ['what', "'", 's', 'the', 'deal', '?'],
     ['watch', 'the', 'movie', 'and', '"', 'sorta', '"', 'find', 'out', '.'],
     ['.'],
     ['.'],
     ['critique',
      ':',
      'a',
      'mind',
      '-',
      'fuck',
      'movie',
      'for',
      'the',
      'teen',
      'generation',
      'that',
      'touches',
      'on',
      'a',
      'very',
      'cool',
      'idea',
      ',',
      'but',
      'presents',
      'it',
      'in',
      'a',
      'very',
      'bad',
      'package',
      '.'],
     ['which',
      'is',
      'what',
      'makes',
      'this',
      'review',
      'an',
      'even',
      'harder',
      'one',
      'to',
      'write',
      ',',
      'since',
      'i',
      'generally',
      'applaud',
      'films',
      'which',
      'attempt',
      'to',
      'break',
      'the',
      'mold',
      ',',
      'mess',
      'with',
      'your',
      'head',
      'and',
      'such',
      '(',
      'lost',
      'highway',
      '&',
      'memento',
      ')',
      ',',
      'but',
      'there',
      'are',
      'good',
      'and',
      'bad',
      'ways',
      'of',
      'making',
      'all',
      'types',
      'of',
      'films',
      ',',
      'and',
      'these',
      'folks',
      'just',
      'didn',
      "'",
      't',
      'snag',
      'this',
      'one',
      'correctly',
      '.'],
     ['they',
      'seem',
      'to',
      'have',
      'taken',
      'this',
      'pretty',
      'neat',
      'concept',
      ',',
      'but',
      'executed',
      'it',
      'terribly',
      '.']]




```python
from gensim.models.word2vec import Word2Vec

model = Word2Vec(sentences)
model.init_sims(replace=True)
```


```python
model.wv.similarity('actor', 'actress')
```




    0.89180624




```python
model.wv.similarity('actor', 'she')
```




    0.25650415




```python
model.wv.most_similar('accident')
```




    [('church', 0.9030872583389282),
     ('plane', 0.8886701464653015),
     ('building', 0.878474771976471),
     ('corpse', 0.8646252155303955),
     ('village', 0.8575769066810608),
     ('abandoned', 0.8549262285232544),
     ('bed', 0.8544203042984009),
     ('boat', 0.8525615334510803),
     ('hospital', 0.8522876501083374),
     ('meeting', 0.8493953347206116)]




```python

```
