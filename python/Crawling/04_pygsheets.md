```python
import zigbang as zb
```


```python
items_df = zb.crawling_apt('광교동')
items_df.tail(2)
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
      <th>itemId</th>
      <th>apartmentName</th>
      <th>buildingFloor</th>
      <th>groupedItemFloor</th>
      <th>lat</th>
      <th>lng</th>
      <th>sales</th>
      <th>itemTitle</th>
      <th>m2</th>
      <th>p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>337</th>
      <td>21866496</td>
      <td>서원마을3단지아이파크</td>
      <td>20</td>
      <td>저층</td>
      <td>37.308180</td>
      <td>127.080468</td>
      <td>63000</td>
      <td>전체 올수리된집, 심곡초품아, 남향,</td>
      <td>113</td>
      <td>34</td>
    </tr>
    <tr>
      <th>338</th>
      <td>19972453</td>
      <td>한국2차</td>
      <td>6</td>
      <td>고층</td>
      <td>37.267459</td>
      <td>127.051121</td>
      <td>49000</td>
      <td>주인거주하여 상태 깨끗 대지지분넓은 저층아파트  방3구조 굿</td>
      <td>85</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



###### 구글 스프레드 시트에 저장
    - oauth 개념
    - oauth 인증 파일 생성
        - https://console.developers.google.com
        - 프로젝트 생성
        - 라이브러리 탭 선택: Google Drive API,cGoogle Sheets API 사용설정
        - Oauth 동의화면
            - 어플리케이션 이름 설정
            - Google API 범위 추가 : drive, spreadsheets (../auth/drive, ../auth/spreadsheets)
            - 저장
        - 사용자 인증정보
            - Oauth 클라이언트 ID 선택
        - pygsheets
            - conda install -c marta -sd pygsheets
            - pip install pygsheets
    - 스프레드 시트에 크롤링한 데이터 저장 및 로드


```python
import pygsheets
```


```python
# access token 얻기
gc = pygsheets.authorize(client_secret='client_secret.json', no_cache=True)
```

    Please go to this URL and finish the authentication flow: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=980382924424-mee4sn2k37359lccmcrcd1qqh2h44ask.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fspreadsheets+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&state=AgjT63XZmF1BwEUxas04m4IGoR0D7n&prompt=consent&access_type=offline
    Enter the authorization code: 4/1AHG8jbG6cBJyXBtt5mGWbEAcJhsNUWw0w8H-Y4-o2oe4lLij14SC4I



```python
gc
```




    <pygsheets.client.Client at 0x7fca79a23f10>




```python
# 스프레드 시트 파일 열기
s_file = gc.open('zigbang')
s_file
```




    <Spreadsheet 'zigbang' Sheets:6>




```python
# 붓꽃 데이터 로드
iris_df = sns.load_dataset('iris')
iris_df.tail(1)
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>virginica</td>
    </tr>
  </tbody>
</table>
</div>




```python
# iris 시트 만들기
iris_sheet = s_file.add_worksheet('iris')
```


```python
# iris 시트에 데이터프레임 저장
iris_sheet.set_dataframe(iris_df, 'A1', copy_index=False)
```


```python
# 시트 삭제
s_file.del_worksheet(s_file[0])
```


```python

```


```python
# 직방 데이터를 크롤링 후 저장
addrs = ['연남동', '망원동', '송도동', '광교동']
for addr in addrs:
    print(addr)
    df = zb.crawling_apt(addr)
    sheet = s_file.add_worksheet(addr)
    sheet.set_dataframe(df, 'A1', copy_index=False)
```

    연남동
    망원동
    송도동
    광교동



```python
 # 데이터 가져오기
sheet = s_file.worksheet_by_title('광교동')
load_df = sheet.get_as_df()
load_df.tail(3)
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
      <th>itemId</th>
      <th>apartmentName</th>
      <th>buildingFloor</th>
      <th>groupedItemFloor</th>
      <th>lat</th>
      <th>lng</th>
      <th>sales</th>
      <th>itemTitle</th>
      <th>m2</th>
      <th>p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>336</th>
      <td>22029384</td>
      <td>서원마을현대홈타운</td>
      <td>20</td>
      <td>고층</td>
      <td>37.309308</td>
      <td>127.081566</td>
      <td>58000</td>
      <td>올수리, 밝고 컨디션좋은집, 심곡초품아</td>
      <td>108</td>
      <td>32</td>
    </tr>
    <tr>
      <th>337</th>
      <td>21866496</td>
      <td>서원마을3단지아이파크</td>
      <td>20</td>
      <td>저층</td>
      <td>37.308180</td>
      <td>127.080468</td>
      <td>63000</td>
      <td>전체 올수리된집, 심곡초품아, 남향,</td>
      <td>113</td>
      <td>34</td>
    </tr>
    <tr>
      <th>338</th>
      <td>19972453</td>
      <td>한국2차</td>
      <td>6</td>
      <td>고층</td>
      <td>37.267459</td>
      <td>127.051121</td>
      <td>49000</td>
      <td>주인거주하여 상태 깨끗 대지지분넓은 저층아파트  방3구조 굿</td>
      <td>85</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
