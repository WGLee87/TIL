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


```python
conda install nltk # NLTK
```

    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    ## Package Plan ##
    
      environment location: /opt/anaconda3
    
      added / updated specs:
        - nltk
    
    
    The following NEW packages will be INSTALLED:
    
      nltk               pkgs/main/osx-64::nltk-3.4.5-py37_0
    
    The following packages will be SUPERSEDED by a higher-priority channel:
    
      ca-certificates    conda-forge::ca-certificates-2020.4.5~ --> pkgs/main::ca-certificates-2020.1.1-0
      certifi            conda-forge::certifi-2020.4.5.1-py37h~ --> pkgs/main::certifi-2020.4.5.1-py37_0
      conda              conda-forge::conda-4.8.3-py37hc8dfbb8~ --> pkgs/main::conda-4.8.3-py37_0
      openssl            conda-forge::openssl-1.1.1g-h0b31af3_0 --> pkgs/main::openssl-1.1.1g-h1de35cc_0
    
    
    Proceed ([y]/n)? ^C
    
    CondaSystemExit: 
    Operation aborted.  Exiting.
    


###### 말뭉치
    - 말뭉치(Corpus)
        - 텍스트 분석에 필요한 텍스트 데이터
    - 웹 크롤링 등으로 수집
    - 텍스트 처리 패키지에서 제공하는 샘플 말뭉치 사용


```python
import nltk
nltk.download('book', quiet=True)
from nltk.book import *
```


```python
nltk.download('movie_reviews')
```

    [nltk_data] Downloading package movie_reviews to
    [nltk_data]     /Users/wglee/nltk_data...
    [nltk_data]   Package movie_reviews is already up-to-date!





    True




```python
nltk.download('punkt')
```

    [nltk_data] Downloading package punkt to /Users/wglee/nltk_data...
    [nltk_data]   Package punkt is already up-to-date!





    True




```python
nltk.download('stopwords')
```

    [nltk_data] Downloading package stopwords to /Users/wglee/nltk_data...
    [nltk_data]   Package stopwords is already up-to-date!





    True



###### step2 : 구텐베르그 말뭉치 목록


```python
nltk.corpus.gutenberg.fileids()
```




    ['austen-emma.txt',
     'austen-persuasion.txt',
     'austen-sense.txt',
     'bible-kjv.txt',
     'blake-poems.txt',
     'bryant-stories.txt',
     'burgess-busterbrown.txt',
     'carroll-alice.txt',
     'chesterton-ball.txt',
     'chesterton-brown.txt',
     'chesterton-thursday.txt',
     'edgeworth-parents.txt',
     'melville-moby_dick.txt',
     'milton-paradise.txt',
     'shakespeare-caesar.txt',
     'shakespeare-hamlet.txt',
     'shakespeare-macbeth.txt',
     'whitman-leaves.txt']




```python
emma_raw = nltk.corpus.gutenberg.raw('austen-emma.txt')
print(emma_raw[:500])
```

    [Emma by Jane Austen 1816]
    
    VOLUME I
    
    CHAPTER I
    
    
    Emma Woodhouse, handsome, clever, and rich, with a comfortable home
    and happy disposition, seemed to unite some of the best blessings
    of existence; and had lived nearly twenty-one years in the world
    with very little to distress or vex her.
    
    She was the youngest of the two daughters of a most affectionate,
    indulgent father; and had, in consequence of her sister's marriage,
    been mistress of his house from a very early period.  Her mother
    had died t


###### 토큰화
    - 토큰화(Tokenizing)
        - 말뭉치(텍스트 데이터)를 '토큰'이라고 불리는 작은 단위로 나누는 행위 (사용자정의에 의해 토큰의 범위는 달라질 수 있음 - 문장을 토큰으로 or 단어를 토큰으로 or 영어의 경우 단어를 토큰으로 쓰는 경우가 가장 일반적임)
    
    - 토큰(Token)
        - 문장, 단어, 형태소 등 분석에 있어서 의미를 가지는 단위
        
    - 토큰의 명칭
        - 토큰의 이름은 실제 토큰의 활용과 관계가 없다.
        - 숫자 혹은 기호로 나타내거나 품사 등을 덧붙여서 쓰는 경우도 있음
        
      
 ###### 토큰의 종류
    - 영어 : 의미가 같은 정규화된 단어
        ex. I am a boy. > I + am + a + boy +.
        
    - 한국어 : 의미가 같은 정규화된 형태소
        ex. 나는 소년이다. > 나 + 는 + 소년 + 이 + 다 +.
        
        
    * 형태소(morpheme)
        - 의미를 가진 가장 작은 말의 단위
    * 한국어 형태소
        - 자립 형태소 : 체언(명사, 대명사, 수사), 수식언(관형사, 부사), 감탄사 등
        - 의존 형태소 : 접사, 어미, 조사, 어간 등

###### 정규화(Normalization)
    - 의미와 쓰임이 같은 단어를 같은 토큰으로 표시
    
        * 대소문자 통합 (case removal)
        * 어간 추출 (stemming)
        * 표제어 추출 (lemmaization)
        * 품사 부착 (Part-of-sppech tagging)
        * 불용어 (stopwords)
        
        
###### 어간추출
    - 단어를 어간과 접사로 분리하여 단순히 접사를 삭제하거나 교체
        - 어간(stem) : 단어의 의미를 담고 있는 핵심 부분
        - 접사(affix) : 단어에 부가적인 의미를 주는 부분
    - 단순 알고리즘 사용
        - 포터(porter) 알고리즘
        - 랭케스터(lancaster) 알고리즘
        
        
###### 표제어 추출(lemmatization)
    -  기본 사전형 단어로 변형
        * ex) is, am, are, was, were, been > be  // has, had > have
    -  사전 정보(Wordnet) 사용
    
    
###### 품사 부착
    - 품사(POS - Part_Of_Speech)
        - 단어의 쓰임에 따른 구분
    - 동일한 철자의 단어가 다른 의미나 다른 품사로 쓰이는 경우
        - 다른 토큰으로 토큰화 해야 한다
            * ex) Permit : 허가하다, 허가증   / refuse : 거부하다, 쓰레기
            
            
###### 불용어
    - 분석의 필요성이 없는 단어
    - 모든 문서에서 너무 자주 쓰이는 단어
    - 너무 드물게 나타나는 단어

###### step1 토큰화
    - nltk의 word_tokenize 함수 사용


```python
# word_tokenize
sent = emma_raw[50:196]
print(sent)

from nltk.tokenize import word_tokenize
word_tokenize(sent)
```

    Emma Woodhouse, handsome, clever, and rich, with a comfortable home
    and happy disposition, seemed to unite some of the best blessings
    of existence





    ['Emma',
     'Woodhouse',
     ',',
     'handsome',
     ',',
     'clever',
     ',',
     'and',
     'rich',
     ',',
     'with',
     'a',
     'comfortable',
     'home',
     'and',
     'happy',
     'disposition',
     ',',
     'seemed',
     'to',
     'unite',
     'some',
     'of',
     'the',
     'best',
     'blessings',
     'of',
     'existence']



###### 어간 추출
    - nltk의 porterstemmer, lancasterstemmer 사용


```python
from nltk.stem import PorterStemmer, LancasterStemmer

st1 = PorterStemmer()
st2 = LancasterStemmer()

words = ['fly', 'flies', 'flying', 'flew', ' flown']
print('Porter Stemmer :', [st1.stem(w) for w in words])
print('Lancaster Stemmer :', [st2.stem(w) for w in words])
```

    Porter Stemmer : ['fli', 'fli', 'fli', 'flew', ' flown']
    Lancaster Stemmer : ['fly', 'fli', 'fly', 'flew', ' flown']


###### 표제어 추출
    - nltk의 WordNetLemmatizer 사용


```python
from nltk.stem import WordNetLemmatizer

lm = WordNetLemmatizer()
[lm.lemmatize(w, pos='v') for w in words]
```




    ['fly', 'fly', 'fly', 'fly', ' flown']



###### nltk의 pos_tag 사용


```python
from nltk.tag import pos_tag

sentence = "Emma refused to permit us to obtain the refuse permit"

tag_list = pos_tag(word_tokenize(sentence))
tag_list
```




    [('Emma', 'NNP'),
     ('refused', 'VBD'),
     ('to', 'TO'),
     ('permit', 'VB'),
     ('us', 'PRP'),
     ('to', 'TO'),
     ('obtain', 'VB'),
     ('the', 'DT'),
     ('refuse', 'NN'),
     ('permit', 'NN')]




```python
def tokenizer(sentence):
    return ['/'.join(p) for p in tag_list]

tokenizer(sentence)
```




    ['Emma/NNP',
     'refused/VBD',
     'to/TO',
     'permit/VB',
     'us/PRP',
     'to/TO',
     'obtain/VB',
     'the/DT',
     'refuse/NN',
     'permit/NN']




```python
from nltk.corpus import stopwords
stopwords.words('english')[:10]
```




    ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're"]




```python

```

###### NLTK의 빈도 분석
    - 두 가지 클래스를 사용
        - Text 클래스
        - FreqDist 클래스
        
        
###### Text 클래스
    - NLTK의 Text 클래스는 문서 분석에 유용한 여러가지 메서드를 제공
        * plot : 단어 빈도 그래프
        * dispersion_plot : 단어 위치 그래프
        * concordance : 단어 문맥 인쇄
        * similar : 유사 단어 검색

    * Step1. 클래스 객체 생성
    * Step2. 단어 빈도 그래프 (plot)
    * Step3. 단어 위치 그래프 (dispersion_plot)
    * Step4. 단어 문맥 인쇄 (concordance)
    * Step5. 유사 단어 검색 (similar)
    * Step6. 공통 문맥 인쇄 (common_contexts)


```python
from nltk import Text

# step1
text = Text(word_tokenize(emma_raw))
text

# step2
text.plot(20)
plt.show()

# step3
text.dispersion_plot(['Emma', 'Knightley', 'Frank', 'Jane', 'Harriet', 'Robert'])

# step4
text.concordance('Emma')

# step5
text.similar('Emma',1)

# step6
text.common_contexts(['Emma', 'she'], 1)
```


<img width="412" alt="output_25_0" src="https://user-images.githubusercontent.com/59719711/82319239-2a688780-9a0c-11ea-91bf-3701a2105814.png">



<img width="424" alt="output_25_1" src="https://user-images.githubusercontent.com/59719711/82319259-33f1ef80-9a0c-11ea-9109-797c8fa708be.png">



    Displaying 25 of 855 matches:
    [ Emma by Jane Austen 1816 ] VOLUME I CHAPT
    ane Austen 1816 ] VOLUME I CHAPTER I Emma Woodhouse , handsome , clever , and 
    both daughters , but particularly of Emma . Between _them_ it was more the int
     friend very mutually attached , and Emma doing just what she liked ; highly e
    r own . The real evils , indeed , of Emma 's situation were the power of havin
    ding-day of this beloved friend that Emma first sat in mournful thought of any
    ing only half a mile from them ; but Emma was aware that great must be the dif
    y . It was a melancholy change ; and Emma could not but sigh over it , and wis
     the rest of her life at Hartfield . Emma smiled and chatted as cheerfully as 
    able to tell her how we all are . '' Emma spared no exertions to maintain this
     ' I have a great regard for you and Emma ; but when it comes to the question 
    ful , troublesome creature ! '' said Emma playfully . `` That is what you have
    e few people who could see faults in Emma Woodhouse , and the only one who eve
    is was not particularly agreeable to Emma herself , she knew it would be so mu
    g thought perfect by every body . `` Emma knows I never flatter her , '' said 
    t be a gainer . '' `` Well , '' said Emma , willing to let it pass -- '' you w
    re of meeting every day . '' `` Dear Emma bears every thing so well , '' said 
    ss her more than she thinks for . '' Emma turned away her head , divided betwe
    nd smiles . `` It is impossible that Emma should not miss such a companion , '
    en one matter of joy to me , '' said Emma , '' and a very considerable one -- 
    od to them , by interference . '' `` Emma never thinks of herself , if she can
    etter thing . Invite him to dinner , Emma , and help him to the best of the fi
     could not think , without pain , of Emma 's losing a single pleasure , or suf
     of her companionableness : but dear Emma was of no feeble character ; she was
    , was so just and so apparent , that Emma , well as she knew her father , was 
    she
    said_i



```python

```

###### FreqDist 클래스
    - FreqDist 클래스는 문서에 사용된 단어(토큰)의 사용빈도 정보를 담는 클래스
    - Text 클래스의 vocab 메서드로 추출할 수 있음
    - 토큰 리스트를 넣어서 직접 만들 수도 있음
    
        * 빈도 분석에 유용한 여러가지 메서드를 제공한다.
            - N : 빈도(횟수)
            - freq : 빈도(퍼센트)
            - most_common : 가장 많이 나오는 단어
            - plot : 가장 많이 나오는 단어 플롯

    Step1. Text클래스에서 생성
    Step2. 토큰 리스트에서 생성
    Step3. 단어 빈도 분석


```python
fd = text.vocab()
type(fd)

from nltk import FreqDist
stopwords = ['Mr.', 'Mrs.', 'Miss', 'Mr', 'Mrs', 'Dear']
tokens = pos_tag(word_tokenize(emma_raw))
names = [t[0] for t in tokens if t[1] =='NNP' and t[0] not in stopwords]
fd_names = FreqDist(names)
fd_names
```




    FreqDist({'Emma': 829, 'Harriet': 477, 'Weston': 429, 'Elton': 374, 'Knightley': 373, 'Woodhouse': 307, 'Jane': 295, 'Fairfax': 232, 'Churchill': 213, 'Frank': 207, ...})




```python
# step3. 단어빈도분석
fd_names.N(), fd_names['Emma'], round(fd_names.freq('Emma'),2)
```




    (6924, 829, 0.12)




```python
fd_names.most_common(5)
```




    [('Emma', 829),
     ('Harriet', 477),
     ('Weston', 429),
     ('Elton', 374),
     ('Knightley', 373)]




```python
fd_names.plot(30)
plt.show()
```


<img width="392" alt="output_32_0" src="https://user-images.githubusercontent.com/59719711/82319301-42d8a200-9a0c-11ea-9d51-c9db66248fe3.png">


###### 워드클라우드


```python
!pip install wordcloud
```

    Collecting wordcloud
      Downloading wordcloud-1.7.0-cp37-cp37m-macosx_10_6_x86_64.whl (160 kB)
    [K     |████████████████████████████████| 160 kB 231 kB/s eta 0:00:01
    [?25hRequirement already satisfied: numpy>=1.6.1 in /opt/anaconda3/lib/python3.7/site-packages (from wordcloud) (1.18.1)
    Requirement already satisfied: matplotlib in /opt/anaconda3/lib/python3.7/site-packages (from wordcloud) (3.2.1)
    Requirement already satisfied: pillow in /opt/anaconda3/lib/python3.7/site-packages (from wordcloud) (7.0.0)
    Requirement already satisfied: cycler>=0.10 in /opt/anaconda3/lib/python3.7/site-packages (from matplotlib->wordcloud) (0.10.0)
    Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /opt/anaconda3/lib/python3.7/site-packages (from matplotlib->wordcloud) (2.4.7)
    Requirement already satisfied: python-dateutil>=2.1 in /opt/anaconda3/lib/python3.7/site-packages (from matplotlib->wordcloud) (2.8.1)
    Requirement already satisfied: kiwisolver>=1.0.1 in /opt/anaconda3/lib/python3.7/site-packages (from matplotlib->wordcloud) (1.2.0)
    Requirement already satisfied: six in /opt/anaconda3/lib/python3.7/site-packages (from cycler>=0.10->matplotlib->wordcloud) (1.14.0)
    Installing collected packages: wordcloud
    Successfully installed wordcloud-1.7.0



```python
conda install wordcloud -c conda-forge
```

    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    ## Package Plan ##
    
      environment location: /opt/anaconda3
    
      added / updated specs:
        - wordcloud
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        wordcloud-1.7.0            |   py37h9bfed18_0         172 KB  conda-forge
        ------------------------------------------------------------
                                               Total:         172 KB
    
    The following NEW packages will be INSTALLED:
    
      wordcloud          conda-forge/osx-64::wordcloud-1.7.0-py37h9bfed18_0
    
    
    
    Downloading and Extracting Packages
    wordcloud-1.7.0      | 172 KB    | ##################################### | 100% 
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    
    Note: you may need to restart the kernel to use updated packages.



```python
from wordcloud import WordCloud

wc = WordCloud(width=1000, height=800, background_color='white', random_state=1)
plt.imshow(wc.generate_from_frequencies(fd_names))
plt.axis(False)
plt.show() 
```


<img width="286" alt="output_36_0" src="https://user-images.githubusercontent.com/59719711/82319321-51bf5480-9a0c-11ea-94a0-b2ad6856e3ef.png">



```python

```


```python

```

###### 연습문제(과제)


```python
nltk.corpus.gutenberg.fileids()
```




    ['austen-emma.txt',
     'austen-persuasion.txt',
     'austen-sense.txt',
     'bible-kjv.txt',
     'blake-poems.txt',
     'bryant-stories.txt',
     'burgess-busterbrown.txt',
     'carroll-alice.txt',
     'chesterton-ball.txt',
     'chesterton-brown.txt',
     'chesterton-thursday.txt',
     'edgeworth-parents.txt',
     'melville-moby_dick.txt',
     'milton-paradise.txt',
     'shakespeare-caesar.txt',
     'shakespeare-hamlet.txt',
     'shakespeare-macbeth.txt',
     'whitman-leaves.txt']




```python
# # 구텐베르그 말뭉치 에시 불러오기
# carroll_raw = nltk.corpus.gutenberg.raw('carroll-alice.txt')
# print(carroll_raw)

# # 단어들의 토큰화
# from nltk.tokenize import word_tokenize
# word_tokenize(carroll_raw)[:20]

from nltk.tag import pos_tag
tag_list = pos_tag(word_tokenize(carroll_raw[:100]))
tag_list

def tokens(sentence):
    return [' : '.join(t) for t in tag_list]
tokens(carroll_raw[:100])

# nltk 빈도분석
from nltk import Text
text = Text(word_tokenize(carroll_raw))
text

# text.plot(20)
# plt.show()

from nltk import FreqDist
stopwords = ['Mr.', 'Mrs.', 'Miss', 'Mr', 'Mrs', 'Dear']
tokens = pos_tag(word_tokenize(carroll_raw))
names = [p[0] for p in tokens if p[1] == 'NNP' and p[0] not in stopwords]
fd_names = FreqDist(names)
fd_names

fd_names.plot(20)
plt.show()
```

<img width="397" alt="output_41_0" src="https://user-images.githubusercontent.com/59719711/82319432-859a7a00-9a0c-11ea-8f19-cec2cae3de98.png">


```python
from wordcloud import WordCloud

wc = WordCloud(width=1200, height=1000, background_color='white', random_state=0)
plt.imshow(wc.generate_from_frequencies(fd_names))
plt.axis(False)
plt.show()
```


<img width="275" alt="output_42_0" src="https://user-images.githubusercontent.com/59719711/82319466-94812c80-9a0c-11ea-95a0-2a184c117a8e.png">


###### 한글 자연어 처리
    - KoNLPy 패키지
        * 윈도우에서는 JAVA 1.7 이상 및 JPype1 패키지를 먼저 설치
            * pip install Jpype1-0.5.7-cp27-none-win_amd64.whl 혹은 pip install Jpype1
            * pip intall konlpy


```python
pip install konlpy
```

    Collecting konlpy
      Downloading konlpy-0.5.2-py2.py3-none-any.whl (19.4 MB)
    [K     |████████████████████████████████| 19.4 MB 9.5 MB/s eta 0:00:01
    [?25hCollecting colorama
      Downloading colorama-0.4.3-py2.py3-none-any.whl (15 kB)
    Collecting beautifulsoup4==4.6.0
      Downloading beautifulsoup4-4.6.0-py3-none-any.whl (86 kB)
    [K     |████████████████████████████████| 86 kB 2.1 MB/s eta 0:00:011
    [?25hCollecting tweepy>=3.7.0
      Downloading tweepy-3.8.0-py2.py3-none-any.whl (28 kB)
    Collecting JPype1>=0.7.0
      Downloading JPype1-0.7.5-cp37-cp37m-macosx_10_9_x86_64.whl (299 kB)
    [K     |████████████████████████████████| 299 kB 9.9 MB/s eta 0:00:01
    [?25hRequirement already satisfied: numpy>=1.6 in /opt/anaconda3/lib/python3.7/site-packages (from konlpy) (1.18.1)
    Requirement already satisfied: lxml>=4.1.0 in /opt/anaconda3/lib/python3.7/site-packages (from konlpy) (4.5.0)
    Requirement already satisfied: PySocks>=1.5.7 in /opt/anaconda3/lib/python3.7/site-packages (from tweepy>=3.7.0->konlpy) (1.7.1)
    Requirement already satisfied: six>=1.10.0 in /opt/anaconda3/lib/python3.7/site-packages (from tweepy>=3.7.0->konlpy) (1.14.0)
    Requirement already satisfied: requests>=2.11.1 in /opt/anaconda3/lib/python3.7/site-packages (from tweepy>=3.7.0->konlpy) (2.23.0)
    Requirement already satisfied: requests-oauthlib>=0.7.0 in /opt/anaconda3/lib/python3.7/site-packages (from tweepy>=3.7.0->konlpy) (1.3.0)
    Requirement already satisfied: chardet<4,>=3.0.2 in /opt/anaconda3/lib/python3.7/site-packages (from requests>=2.11.1->tweepy>=3.7.0->konlpy) (3.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.7/site-packages (from requests>=2.11.1->tweepy>=3.7.0->konlpy) (2020.4.5.1)
    Requirement already satisfied: idna<3,>=2.5 in /opt/anaconda3/lib/python3.7/site-packages (from requests>=2.11.1->tweepy>=3.7.0->konlpy) (2.9)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/anaconda3/lib/python3.7/site-packages (from requests>=2.11.1->tweepy>=3.7.0->konlpy) (1.25.8)
    Requirement already satisfied: oauthlib>=3.0.0 in /opt/anaconda3/lib/python3.7/site-packages (from requests-oauthlib>=0.7.0->tweepy>=3.7.0->konlpy) (3.1.0)
    Installing collected packages: colorama, beautifulsoup4, tweepy, JPype1, konlpy
      Attempting uninstall: beautifulsoup4
        Found existing installation: beautifulsoup4 4.8.0
        Uninstalling beautifulsoup4-4.8.0:
          Successfully uninstalled beautifulsoup4-4.8.0
    Successfully installed JPype1-0.7.5 beautifulsoup4-4.6.0 colorama-0.4.3 konlpy-0.5.2 tweepy-3.8.0
    Note: you may need to restart the kernel to use updated packages.


###### KoNLPy 기능
    - 샘플 말뭉치
        - kolaw : 헌법 말뭉치
        - kobill : 법안 말뭉치
        
    - 한글 형태소 분석기
        - KoNLPy는 다양한 형태소 분석, 태킹 라이브러리를 파이썬에서 쉽게 사용할 수 있도록 모아 놓음
            * Hannanum : 한나눔 (카이스트 개발)
            * kkma : 꼬꼬마 (서울대학교 개발)
            * Komoran : 코모란 / 잘 안될 수도 있음
            * Mecab : 메카브 (일본어용 형태소 분석기 인데 한글로 번형한 형태) / 잘 안될수도 있음
            * Open Korean Text : 오픈 소스 한국어 분석기
            
       

###### Step1. 헌법 말뭉치


```python
from konlpy.corpus import kolaw
kolaw.fileids()

c = kolaw.open('constitution.txt').read()
print(c[:200])
```

    대한민국헌법
    
    유구한 역사와 전통에 빛나는 우리 대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에 항거한 4·19민주이념을 계승하고, 조국의 민주개혁과 평화적 통일의 사명에 입각하여 정의·인도와 동포애로써 민족의 단결을 공고히 하고, 모든 사회적 폐습과 불의를 타파하며, 자율과 조화를 바탕으로 자유민주적 기본질서를 더욱 확고히 하여 정치·경제


###### Step2.법안 말뭉치


```python
from konlpy.corpus import kobill
kobill.fileids()

d = kobill.open('1809890.txt').read()
print(d[:200])
```

    지방공무원법 일부개정법률안
    
    (정의화의원 대표발의 )
    
     의 안
     번 호
    
    9890
    
    발의연월일 : 2010.  11.  12.  
    
    발  의  자 : 정의화․이명수․김을동 
    
    이사철․여상규․안규백
    
    황영철․박영아․김정훈
    
    김학송 의원(10인)
    
    제안이유 및 주요내용
    
      초등학교 저학년의 경우에도 부모의 따뜻한 사랑과 보살핌이 필요
    
    한 나이이나, 현재 


###### step3. 형태소 분석기 생성


```python
from konlpy.tag import *

hannanum = Hannanum()
kkma = Kkma()
okt = Okt()
```

###### Step4. 명사 추출


```python
hannanum.nouns(c[:40]) # 40번째 글자까지 명사만 추출
```




    ['대한민국헌법', '유구', '역사', '전통', '빛', '우리', '대한국민', '3·1운동']




```python
kkma.nouns(c[:40])
```




    ['대한',
     '대한민국',
     '대한민국헌법',
     '민국',
     '헌법',
     '유구',
     '역사',
     '전통',
     '우리',
     '국민',
     '3',
     '1',
     '1운동',
     '운동']




```python
okt.nouns(c[:40])
```




    ['대한민국', '헌법', '유구', '역사', '전통', '우리', '국민', '운동']



###### Step.5 형태소 추출
    명사뿐만 아니라 모든 품사의 형태소를 알아내려면 morphs 메서드 사용


```python
hannanum.morphs(c[:40])
```




    ['대한민국헌법',
     '유구',
     '하',
     'ㄴ',
     '역사',
     '와',
     '전통',
     '에',
     '빛',
     '나는',
     '우리',
     '대한국민',
     '은',
     '3·1운동',
     '으로']




```python
kkma.morphs(c[:40])
```




    ['대한민국',
     '헌법',
     '유구',
     '하',
     'ㄴ',
     '역사',
     '와',
     '전통',
     '에',
     '빛나',
     '는',
     '우리',
     '대하',
     'ㄴ',
     '국민',
     '은',
     '3',
     '·',
     '1',
     '운동',
     '으로']




```python
okt.morphs(c[:40])
```




    ['대한민국',
     '헌법',
     '\n\n',
     '유구',
     '한',
     '역사',
     '와',
     '전통',
     '에',
     '빛나는',
     '우리',
     '대',
     '한',
     '국민',
     '은',
     '3',
     '·',
     '1',
     '운동',
     '으로']



###### Step.6 품사 부착
    pos명령을 사용하여 품사 부착
    한국어 품사 태그세트로는 형태소 분석기마다 사용하는 품사 태그가 다르므로 각 형태소 분석기에 대한 문서를 참조한다.
    부착되는 품사 태그의 기호와 의미는 tagset 속성으로 확인할 수 있다.


```python
hannanum.pos(c[:40])
```




    [('대한민국헌법', 'N'),
     ('유구', 'N'),
     ('하', 'X'),
     ('ㄴ', 'E'),
     ('역사', 'N'),
     ('와', 'J'),
     ('전통', 'N'),
     ('에', 'J'),
     ('빛', 'N'),
     ('나는', 'J'),
     ('우리', 'N'),
     ('대한국민', 'N'),
     ('은', 'J'),
     ('3·1운동', 'N'),
     ('으로', 'J')]




```python
hannanum.tagset
```




    {'E': '어미',
     'EC': '연결 어미',
     'EF': '종결 어미',
     'EP': '선어말어미',
     'ET': '전성 어미',
     'F': '외국어',
     'I': '독립언',
     'II': '감탄사',
     'J': '관계언',
     'JC': '격조사',
     'JP': '서술격 조사',
     'JX': '보조사',
     'M': '수식언',
     'MA': '부사',
     'MM': '관형사',
     'N': '체언',
     'NB': '의존명사',
     'NC': '보통명사',
     'NN': '수사',
     'NP': '대명사',
     'NQ': '고유명사',
     'P': '용언',
     'PA': '형용사',
     'PV': '동사',
     'PX': '보조 용언',
     'S': '기호',
     'X': '접사',
     'XP': '접두사',
     'XS': '접미사'}




```python
kkma.pos(c[:40])
```




    [('대한민국', 'NNG'),
     ('헌법', 'NNG'),
     ('유구', 'NNG'),
     ('하', 'XSV'),
     ('ㄴ', 'ETD'),
     ('역사', 'NNG'),
     ('와', 'JC'),
     ('전통', 'NNG'),
     ('에', 'JKM'),
     ('빛나', 'VV'),
     ('는', 'ETD'),
     ('우리', 'NNM'),
     ('대하', 'VV'),
     ('ㄴ', 'ETD'),
     ('국민', 'NNG'),
     ('은', 'JX'),
     ('3', 'NR'),
     ('·', 'SP'),
     ('1', 'NR'),
     ('운동', 'NNG'),
     ('으로', 'JKM')]




```python
kkma.tagset
```




    {'EC': '연결 어미',
     'ECD': '의존적 연결 어미',
     'ECE': '대등 연결 어미',
     'ECS': '보조적 연결 어미',
     'EF': '종결 어미',
     'EFA': '청유형 종결 어미',
     'EFI': '감탄형 종결 어미',
     'EFN': '평서형 종결 어미',
     'EFO': '명령형 종결 어미',
     'EFQ': '의문형 종결 어미',
     'EFR': '존칭형 종결 어미',
     'EP': '선어말 어미',
     'EPH': '존칭 선어말 어미',
     'EPP': '공손 선어말 어미',
     'EPT': '시제 선어말 어미',
     'ET': '전성 어미',
     'ETD': '관형형 전성 어미',
     'ETN': '명사형 전성 어미',
     'IC': '감탄사',
     'JC': '접속 조사',
     'JK': '조사',
     'JKC': '보격 조사',
     'JKG': '관형격 조사',
     'JKI': '호격 조사',
     'JKM': '부사격 조사',
     'JKO': '목적격 조사',
     'JKQ': '인용격 조사',
     'JKS': '주격 조사',
     'JX': '보조사',
     'MA': '부사',
     'MAC': '접속 부사',
     'MAG': '일반 부사',
     'MD': '관형사',
     'MDN': '수 관형사',
     'MDT': '일반 관형사',
     'NN': '명사',
     'NNB': '일반 의존 명사',
     'NNG': '보통명사',
     'NNM': '단위 의존 명사',
     'NNP': '고유명사',
     'NP': '대명사',
     'NR': '수사',
     'OH': '한자',
     'OL': '외국어',
     'ON': '숫자',
     'SE': '줄임표',
     'SF': '마침표, 물음표, 느낌표',
     'SO': '붙임표(물결,숨김,빠짐)',
     'SP': '쉼표,가운뎃점,콜론,빗금',
     'SS': '따옴표,괄호표,줄표',
     'SW': '기타기호 (논리수학기호,화폐기호)',
     'UN': '명사추정범주',
     'VA': '형용사',
     'VC': '지정사',
     'VCN': "부정 지정사, 형용사 '아니다'",
     'VCP': "긍정 지정사, 서술격 조사 '이다'",
     'VV': '동사',
     'VX': '보조 용언',
     'VXA': '보조 형용사',
     'VXV': '보조 동사',
     'XP': '접두사',
     'XPN': '체언 접두사',
     'XPV': '용언 접두사',
     'XR': '어근',
     'XSA': '형용사 파생 접미사',
     'XSN': '명사파생 접미사',
     'XSV': '동사 파생 접미사'}




```python
okt.pos(c[:40])
```




    [('대한민국', 'Noun'),
     ('헌법', 'Noun'),
     ('\n\n', 'Foreign'),
     ('유구', 'Noun'),
     ('한', 'Josa'),
     ('역사', 'Noun'),
     ('와', 'Josa'),
     ('전통', 'Noun'),
     ('에', 'Josa'),
     ('빛나는', 'Verb'),
     ('우리', 'Noun'),
     ('대', 'Modifier'),
     ('한', 'Modifier'),
     ('국민', 'Noun'),
     ('은', 'Josa'),
     ('3', 'Number'),
     ('·', 'Punctuation'),
     ('1', 'Number'),
     ('운동', 'Noun'),
     ('으로', 'Josa')]




```python
okt.tagset
```




    {'Adjective': '형용사',
     'Adverb': '부사',
     'Alpha': '알파벳',
     'Conjunction': '접속사',
     'Determiner': '관형사',
     'Eomi': '어미',
     'Exclamation': '감탄사',
     'Foreign': '외국어, 한자 및 기타기호',
     'Hashtag': '트위터 해쉬태그',
     'Josa': '조사',
     'KoreanParticle': '(ex: ㅋㅋ)',
     'Noun': '명사',
     'Number': '숫자',
     'PreEomi': '선어말어미',
     'Punctuation': '구두점',
     'ScreenName': '트위터 아이디',
     'Suffix': '접미사',
     'Unknown': '미등록어',
     'Verb': '동사'}




```python

```


```python
a = pd.DataFrame(hannanum.tagset.keys(), columns = ['Hannanum-기호'])
b = pd.DataFrame(hannanum.tagset.values(), columns = ['Hannanum-품사'])
hannanum_df = pd.concat([a,b], axis=1)
hannanum_df

c = pd.DataFrame(kkma.tagset.keys(), columns = ['Kkma-기호'])
d = pd.DataFrame(kkma.tagset.values(), columns = ['Kkma-품사'])
kkma_df = pd.concat([c,d], axis=1)
kkma_df

e = pd.DataFrame(okt.tagset.keys(), columns = ['Okt-기호'])
f = pd.DataFrame(okt.tagset.values(), columns = ['Okt-품사'])
okt_df = pd.concat([e,f], axis=1)

df = pd.concat([hannanum_df, kkma_df, okt_df], axis=1)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Hannanum-기호</th>
      <th>Hannanum-품사</th>
      <th>Kkma-기호</th>
      <th>Kkma-품사</th>
      <th>Okt-기호</th>
      <th>Okt-품사</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>E</td>
      <td>어미</td>
      <td>EC</td>
      <td>연결 어미</td>
      <td>Adjective</td>
      <td>형용사</td>
    </tr>
    <tr>
      <th>1</th>
      <td>EC</td>
      <td>연결 어미</td>
      <td>ECD</td>
      <td>의존적 연결 어미</td>
      <td>Adverb</td>
      <td>부사</td>
    </tr>
    <tr>
      <th>2</th>
      <td>EF</td>
      <td>종결 어미</td>
      <td>ECE</td>
      <td>대등 연결 어미</td>
      <td>Alpha</td>
      <td>알파벳</td>
    </tr>
    <tr>
      <th>3</th>
      <td>EP</td>
      <td>선어말어미</td>
      <td>ECS</td>
      <td>보조적 연결 어미</td>
      <td>Conjunction</td>
      <td>접속사</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ET</td>
      <td>전성 어미</td>
      <td>EF</td>
      <td>종결 어미</td>
      <td>Determiner</td>
      <td>관형사</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>62</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>XPV</td>
      <td>용언 접두사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>63</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>XR</td>
      <td>어근</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>64</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>XSA</td>
      <td>형용사 파생 접미사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>65</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>XSN</td>
      <td>명사파생 접미사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>66</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>XSV</td>
      <td>동사 파생 접미사</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>67 rows × 6 columns</p>
</div>



###### Step7. 빈도 분석
    nltk의 기능을 사용하여 한국어 빈도 분석 가능


```python
from nltk import Text
kolaw = Text(hannanum.nouns(c))

kolaw.plot(30)
plt.show()
```


<img width="397" alt="output_70_0" src="https://user-images.githubusercontent.com/59719711/82319517-b37fbe80-9a0c-11ea-8f34-a6d43d8f17fa.png">



```python
from wordcloud import WordCloud

# 폰트설정
font_path = '/Users/wglee/Library/Fonts/koverwatch.ttf'

wc = WordCloud(width = 1000, height=800, background_color = 'white', font_path=font_path)
plt.imshow(wc.generate_from_frequencies(kolaw.vocab()))
plt.grid(False)
plt.show()
```


<img width="318" alt="output_71_0" src="https://user-images.githubusercontent.com/59719711/82319613-d7430480-9a0c-11ea-8e83-db0fa2c4024c.png">



```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
