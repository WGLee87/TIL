###### 1. 연구배경 (The background of Research)

1. <img width="753" alt="스크린샷 2020-06-02 오후 6 20 58" src="https://user-images.githubusercontent.com/59719711/83503397-f4dc9780-a4fd-11ea-93ec-59a53ec72fb3.png">

2. <img width="752" alt="스크린샷 2020-06-02 오후 6 22 15" src="https://user-images.githubusercontent.com/59719711/83503455-0c1b8500-a4fe-11ea-8b56-7267c354f7b2.png">

###### 2. 선행 연구

###### 참고연구 목록
    : 연구 주제 관련 직, 간접적 관련 선행연구 및 참고자료 (총 22건)

```
1) 이종우(2014), 실업팀 선수의 연봉 결정요인 분석 : 개인종목을 중심으로. 서울대학교 대학원
2) 권병진(2005). 미국 프로야구 Major League 선수들의 노동생산성과 연봉에 관한 연구. 서강대학교 대학원
3) 송종우(2008). 한국 프로스포츠 선수들의 연봉에 대한 다변량적분석. 응용통계연구, 21(3), 441-45
4) 승희배, 강기훈(2012). 한국 프로야구 선수들의 경기력과 연봉의 관계 분석. 한국데이터정보과학회지, 23(2), 285-298.
5) 신문선(2003). 한국 프로축구 선수의 연봉산정 모델 개발. 국내박사학위논문, 세종대학교 대학원, 서울.
6) 오광모, 이장택(2003). 데이터마이닝을 이용한 한국프로야구 선수들이 연봉에 관한 모형연구. 한국스포츠사회학회지,16(2), 295-309.
7) 한동섭, 김정기, 김종(2007). 스포츠 스타의 이미지와 소속 팀, 보증 제품 및 사회 이미지의 관계에 관한 연구. 한국스포츠산업.경영학회지, 12(3), 155-168.
8) 최명일(2002). 스포츠 스타 이미지 구성요인에 관한 연구. 국내석사학위논문, 한양대학교 대학원, 서울.
9) 손동만(2018). NBA 선수 연봉구조와 선수 스타파워가 팀 퍼포먼스에 미치는 영향. 서울대학교 대학원
10) 황선욱(2019). 주성분 기법을 활용한 NBA선수 포지션별 선수평가지수 및 연봉예측모델 개발. 동국대학교 대학원
11) Yunus Koloğlu(2018). A Multiple Linear Regression Approach For Estimating the Market Value of Football Players in Forward Position
12) Edward Nsolo(2018), Player valuation in European football
13) Daniel Bratulić(2019). Predicting 2018–19 NBA’s Most Valuable Player using Machine Learning
14) Shubham Maurya(2018). Can Linear Models predict a Footballer’s Value?
15) Yaldo, L.(2017). Computational Estimation of Football Player Wages
16) Oliver Müller(2017). BEYOND CROWD JUDGMENTS: DATA-DRIVEN ESTIMATION OF MARKET VALUE IN ASSOCIATION FOOTBALL
17) Martin, I. M. & Eroglu, S. (1993).  Measuring a Multi-Dimensional Construct: Country Image
18) J. David Singer(2007). 국가역량 종합지수(Composite Index of National Capability, CNIC)
19) US News(2020). US News 최고의 나라 지수
20) 강지원(2020). Why do Instagram Users Tag Friends in Comments
```

###### 참고연구 분류 및 시사점

    **1. 데이터 측면**

    - 해외 축구에 대한 국내 연구는 거의 전무한 상태. 더군다나 ML알고리즘을 활용한 연구는 현재까지 발견하지 못함
    - 해외 축구에 대한 해외 연구는 회귀, ML알고리즘 활용한 연구가 다수 있어, 비교 연구하기에 적절.
        - (대상 데이터셋은 유사하나, 방법론 측면(선형회귀, ML알고리즘 각각 1건씩)에서 다른 논문 2건 발견)

**2. 방법 측면 : 최근 연구에서 ML 방법론의 연구가 두드러지나, 동시에 크롤링 데이터를 토대로 한 회귀 연구도 함께 활발히 진행 중**

###### 선행연구 검토에서 얻은 시사점

###### 2. 문제정의 (The definition of Issue)

주목한 배경 : European football market 전반의 개별 선수의 능력치에 대한 적절한 시장가치를 예측하는 연구의 한계
* 각 시즌 별, 각 리그 별 세부 연구들 존재. 하지만 전반을 통합한 연구는 부족하고 방법론에서 한정됨
   
###### 연구 문제 : European football market 전반의 개별 선수의 능력치에 대한 적절한 시장가치를 예측 모델 연구
* 대상 데이터 : 주요 리그 통합, 대상 기간 : 최소 5시즌 통합, 방법론 : 선형회귀 및 머신러닝 모델(결합 모형 포함)

###### 회귀 모델

1) 종속변수 : 유럽 주요리그 500명의 시장평가가격

2) 독립변수

    경기력 요인 : performance, ability stats
    비경기력 요인 : 개인별 인지도 및 시장영향력(SNS, 위키피디아 등)
   
3) 사용모델 : 단순 선형회귀, 정규화 선형회귀
    
    

#### 제한점 (Limitation)
    1. 2개의 다른 사이트에서 데이터 merge 과정에서 동일 독립변수임에도 불구하고 다르게 기재되어 있음 -> 고생하여 해결...
    2. 위키피디아 데이터 크롤링 제한
    3. 모든 선수의 몸값 시장가치 데이터 갯수 제한 (1,600만 유로 이하 시장가격 데이터 부재)


###### api-football 데이터


```python
from pandas.io.json import json_normalize

n = 0

headers= {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "aeda90b38bmsh068bc2e3a0bb552p19cf54jsnea18b745c09e"
}
payload = {}
data = pd.DataFrame()

for i in range(270, 280+1):
    response = requests.request("GET","https://api-football-v1.p.rapidapi.com/v2/players/player/{}".format(i), \
                                headers=headers, data=payload)
    json_object = response.json()
    df = json_normalize(json_object['api']['players'])
    data = data.append(df, ignore_index = True)

    i += 1
# data['Name'] = data[['firstname','lastname']].apply(lambda x: ' '.join(x), axis=1)
data
```

    /opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:16: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead
      app.launch_new_instance()





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
      <th>player_id</th>
      <th>player_name</th>
      <th>firstname</th>
      <th>lastname</th>
      <th>number</th>
      <th>position</th>
      <th>age</th>
      <th>birth_date</th>
      <th>birth_place</th>
      <th>birth_country</th>
      <th>...</th>
      <th>penalty.commited</th>
      <th>penalty.success</th>
      <th>penalty.missed</th>
      <th>penalty.saved</th>
      <th>games.appearences</th>
      <th>games.minutes_played</th>
      <th>games.lineups</th>
      <th>substitutes.in</th>
      <th>substitutes.out</th>
      <th>substitutes.bench</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>270</td>
      <td>S. N&amp;apos;Soki</td>
      <td>Stanley</td>
      <td>N'Soki</td>
      <td>None</td>
      <td>Defender</td>
      <td>21</td>
      <td>09/04/1999</td>
      <td>Poissy</td>
      <td>France</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>17</td>
      <td>1272</td>
      <td>14</td>
      <td>3</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>270</td>
      <td>S. N&amp;apos;Soki</td>
      <td>Stanley</td>
      <td>N'Soki</td>
      <td>None</td>
      <td>Defender</td>
      <td>21</td>
      <td>09/04/1999</td>
      <td>Poissy</td>
      <td>France</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>697</td>
      <td>8</td>
      <td>4</td>
      <td>3</td>
      <td>19</td>
    </tr>
    <tr>
      <th>2</th>
      <td>270</td>
      <td>S. N&amp;apos;Soki</td>
      <td>Stanley</td>
      <td>N'Soki</td>
      <td>None</td>
      <td>Defender</td>
      <td>21</td>
      <td>09/04/1999</td>
      <td>Poissy</td>
      <td>France</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>25</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>270</td>
      <td>S. N&amp;apos;Soki</td>
      <td>Stanley</td>
      <td>N'Soki</td>
      <td>None</td>
      <td>Defender</td>
      <td>21</td>
      <td>09/04/1999</td>
      <td>Poissy</td>
      <td>France</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>270</td>
      <td>S. N&amp;apos;Soki</td>
      <td>Stanley</td>
      <td>N'Soki</td>
      <td>None</td>
      <td>Defender</td>
      <td>21</td>
      <td>09/04/1999</td>
      <td>Poissy</td>
      <td>France</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>249</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>418</th>
      <td>280</td>
      <td>Alisson</td>
      <td>Alisson Ramsés</td>
      <td>Becker</td>
      <td>None</td>
      <td>Goalkeeper</td>
      <td>28</td>
      <td>02/10/1992</td>
      <td>Novo Hamburgo</td>
      <td>Brazil</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>136</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>419</th>
      <td>280</td>
      <td>Alisson</td>
      <td>Alisson Ramsés</td>
      <td>Becker</td>
      <td>None</td>
      <td>Goalkeeper</td>
      <td>28</td>
      <td>02/10/1992</td>
      <td>Novo Hamburgo</td>
      <td>Brazil</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>270</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>420</th>
      <td>280</td>
      <td>Alisson</td>
      <td>Alisson Ramsés</td>
      <td>Becker</td>
      <td>None</td>
      <td>Goalkeeper</td>
      <td>28</td>
      <td>02/10/1992</td>
      <td>Novo Hamburgo</td>
      <td>Brazil</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>421</th>
      <td>280</td>
      <td>Alisson</td>
      <td>Alisson Ramsés</td>
      <td>Becker</td>
      <td>None</td>
      <td>Goalkeeper</td>
      <td>28</td>
      <td>02/10/1992</td>
      <td>Novo Hamburgo</td>
      <td>Brazil</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>422</th>
      <td>280</td>
      <td>Alisson</td>
      <td>Alisson Ramsés</td>
      <td>Becker</td>
      <td>None</td>
      <td>Goalkeeper</td>
      <td>28</td>
      <td>02/10/1992</td>
      <td>Novo Hamburgo</td>
      <td>Brazil</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>401</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>423 rows × 51 columns</p>
</div>



###### 트랜스퍼 마켓 데이터 크롤링


```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

dataFrame= pd.DataFrame(columns=['Name', 'Values'])

for i in range(1,2):
    url = 'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?ajax=yw1&page=' + str(i)
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    chrome_driver = '/Users/wglee/Desktop/DATA ANALYSIS/Chromedriver'
    driver = webdriver.Chrome(chrome_driver, options=options)
    driver.implicitly_wait(3)
    driver.get(url)

    src = driver.page_source

    driver.close()

    resp = BeautifulSoup(src, "html.parser")
    values_data = resp.select('table')
    table_html = str(values_data)
    num = 0
    name = ' '
    value = ' '
    for index, row in pd.read_html(table_html)[1].iterrows():
        if index%3 == 0:
            num = row['#']
            value = row['Market value']
        elif index%3 == 1:
            name = row['Player']
        else : 
            dataFrame.loc[num] = [name, value]
dataFrame
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
      <th>Name</th>
      <th>Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1.0</th>
      <td>Kylian Mbappé</td>
      <td>€180.00m</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>Raheem Sterling</td>
      <td>€128.00m</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>Neymar</td>
      <td>€128.00m</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>Sadio Mané</td>
      <td>€120.00m</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>Mohamed Salah</td>
      <td>€120.00m</td>
    </tr>
    <tr>
      <th>6.0</th>
      <td>Harry Kane</td>
      <td>€120.00m</td>
    </tr>
    <tr>
      <th>7.0</th>
      <td>Kevin De Bruyne</td>
      <td>€120.00m</td>
    </tr>
    <tr>
      <th>8.0</th>
      <td>Jadon Sancho</td>
      <td>€117.00m</td>
    </tr>
    <tr>
      <th>9.0</th>
      <td>Lionel Messi</td>
      <td>€112.00m</td>
    </tr>
    <tr>
      <th>10.0</th>
      <td>Trent Alexander-Arnold</td>
      <td>€99.00m</td>
    </tr>
    <tr>
      <th>11.0</th>
      <td>Antoine Griezmann</td>
      <td>€96.00m</td>
    </tr>
    <tr>
      <th>12.0</th>
      <td>João Félix</td>
      <td>€81.00m</td>
    </tr>
    <tr>
      <th>13.0</th>
      <td>Kai Havertz</td>
      <td>€81.00m</td>
    </tr>
    <tr>
      <th>14.0</th>
      <td>Bernardo Silva</td>
      <td>€80.00m</td>
    </tr>
    <tr>
      <th>15.0</th>
      <td>N'Golo Kanté</td>
      <td>€80.00m</td>
    </tr>
    <tr>
      <th>16.0</th>
      <td>Leroy Sané</td>
      <td>€80.00m</td>
    </tr>
    <tr>
      <th>17.0</th>
      <td>Virgil van Dijk</td>
      <td>€80.00m</td>
    </tr>
    <tr>
      <th>18.0</th>
      <td>Paul Pogba</td>
      <td>€80.00m</td>
    </tr>
    <tr>
      <th>19.0</th>
      <td>Jan Oblak</td>
      <td>€80.00m</td>
    </tr>
    <tr>
      <th>20.0</th>
      <td>Eden Hazard</td>
      <td>€80.00m</td>
    </tr>
    <tr>
      <th>21.0</th>
      <td>Erling Haaland</td>
      <td>€72.00m</td>
    </tr>
    <tr>
      <th>22.0</th>
      <td>Frenkie de Jong</td>
      <td>€72.00m</td>
    </tr>
    <tr>
      <th>23.0</th>
      <td>Paulo Dybala</td>
      <td>€72.00m</td>
    </tr>
    <tr>
      <th>24.0</th>
      <td>Serge Gnabry</td>
      <td>€72.00m</td>
    </tr>
    <tr>
      <th>25.0</th>
      <td>Saúl Ñíguez</td>
      <td>€72.00m</td>
    </tr>
  </tbody>
</table>
</div>



###### 인스타그램 크롤링


```python
ul = dataFrame['Name'].tolist()
userList = ul[0:30]
userList
```


```python
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re

# userList= ['chris eriksen', 'cristiano ronaldo', 'lionel messi', 'wglee87']

url = 'https://www.instagram.com/'
driver = webdriver.Chrome('/Users/wglee/Desktop/DATA ANALYSIS/Chromedriver')
driver.get(url)
driver.implicitly_wait(3)

id = '' #Instagram ID
pw = '' #Instagram PW

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(id)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(pw)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()

driver.implicitly_wait(3)


def checkInstaFollowers(user):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(user)
    driver.implicitly_wait(7)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div').click()

    r = requests.get(driver.current_url).text
    followers = re.search('"edge_followed_by":{"count":([0-9]+)}',r).group(1)

    if (r.find('"is_verified":true')!=-1):
        print('{} : {}'.format(user, followers))
    else:
        print('{} : user not verified'.format(user))

for a in userList:
    try:
        checkInstaFollowers(a)
    except AttributeError:
        print("{}'s top search is returned as hashtag. Continue to next item".format(a))
```

    Kylian Mbappé : 40806283
    Raheem Sterling : 7015289
    Neymar : 139023864
    Sadio Mané : 7300478
    Mohamed Salah : 7300478
    Harry Kane : 9645324
    Kevin De Bruyne : 11100685
    Jadon Sancho : 4252976
    Lionel Messi's top search is returned as hashtag. Continue to next item
    Trent Alexander-Arnold : 4359769
    Antoine Griezmann : 30243317
    João Félix : 3266543
    Kai Havertz : 767217
    Bernardo Silva's top search is returned as hashtag. Continue to next item
    N'Golo Kanté : 7000069
    Leroy Sané : 5114492
    Virgil van Dijk : 5114492
    Paul Pogba : 41084625
    Jan Oblak : 1301539
    Eden Hazard : 1301540



    ---------------------------------------------------------------------------

    StaleElementReferenceException            Traceback (most recent call last)

    <ipython-input-7-734d65108619> in <module>
         36 for a in userList:
         37     try:
    ---> 38         checkInstaFollowers(a)
         39     except AttributeError:
         40         print("{}'s top search is returned as hashtag. Continue to next item".format(a))


    <ipython-input-7-734d65108619> in checkInstaFollowers(user)
         24     driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(user)
         25     driver.implicitly_wait(7)
    ---> 26     driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div').click()
         27 
         28     r = requests.get(driver.current_url).text


    /opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webelement.py in click(self)
         78     def click(self):
         79         """Clicks the element."""
    ---> 80         self._execute(Command.CLICK_ELEMENT)
         81 
         82     def submit(self):


    /opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webelement.py in _execute(self, command, params)
        631             params = {}
        632         params['id'] = self._id
    --> 633         return self._parent.execute(command, params)
        634 
        635     def find_element(self, by=By.ID, value=None):


    /opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py in execute(self, driver_command, params)
        319         response = self.command_executor.execute(driver_command, params)
        320         if response:
    --> 321             self.error_handler.check_response(response)
        322             response['value'] = self._unwrap_value(
        323                 response.get('value', None))


    /opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/errorhandler.py in check_response(self, response)
        240                 alert_text = value['alert'].get('text')
        241             raise exception_class(message, screen, stacktrace, alert_text)
    --> 242         raise exception_class(message, screen, stacktrace)
        243 
        244     def _value_or_default(self, obj, key, default):


    StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
      (Session info: chrome=83.0.4103.61)




```python

```
