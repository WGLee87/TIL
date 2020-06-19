###### scraping & crawling & spider & bot
    - scraping : 데이터를 수집하는 작업
    - crawling : 여러 페이지의 특정 데이터들을 수집하고 분류하는 작업
    - spider : 웹 데이터를 수집하는 소프트웨어
    - bot : 인터넷 상에서 자동화된 작업을 실행하는 소프트웨어 


```python

```

###### web crawling
    - 1. requests : json : 동적페이지(URL 변경 없이 데이터를 수정 및 추가)
    - 2. requests : html : 정적페이지(URL 변경으로 데이터를 수정 및 추가)
    - 3. selenium : web browser : 1,2번 방법을 사용하지 못할때 사용


```python

```

###### 1. 네이버 주식 데이터 크롤링
    - 코스피 데이터 수집
    - 코스탁 데이터 수집
    - USD 환율 데이터 수집
    - 그래프, 상관계수 확인

###### 크롤링 절차
    - 1. 웹 서비스 분석 : URL 확인
    - 2. request, response : json 데이터(문자열)를 얻기
    - 3. json 데이터(문자열) > dict(파싱) > 데이터프레임


```python
# 1.웹서비스 분석 : URL 찾기
code, page_size, page = 'KOSPI', 20, 1
url = 'https://m.stock.naver.com/api/json/sise/dailySiseIndexListJson.nhn?\
code={}&pageSize={}&page={}'.format(code, page_size, page)
url
```




    'https://m.stock.naver.com/api/json/sise/dailySiseIndexListJson.nhn?code=KOSPI&pageSize=20&page=1'




```python
# 2. request, response : JSON(str)
response = requests.get(url)
response
```




    <Response [200]>




```python
# 3.JSON(str) > JSON(dict) > df
# response.text
datas = response.json()['result']['siseList']
kospi_df = pd.DataFrame(datas)
kospi_df.tail(3)
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
      <th>cd</th>
      <th>dt</th>
      <th>ncv</th>
      <th>cv</th>
      <th>cr</th>
      <th>ov</th>
      <th>hv</th>
      <th>lv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17</th>
      <td>KOSPI</td>
      <td>20200527</td>
      <td>2031.20</td>
      <td>1.42</td>
      <td>0.07</td>
      <td>2027.90</td>
      <td>2043.44</td>
      <td>2019.82</td>
    </tr>
    <tr>
      <th>18</th>
      <td>KOSPI</td>
      <td>20200526</td>
      <td>2029.78</td>
      <td>35.18</td>
      <td>1.76</td>
      <td>2001.00</td>
      <td>2029.89</td>
      <td>1997.94</td>
    </tr>
    <tr>
      <th>19</th>
      <td>KOSPI</td>
      <td>20200525</td>
      <td>1994.60</td>
      <td>24.47</td>
      <td>1.24</td>
      <td>1980.51</td>
      <td>1994.90</td>
      <td>1967.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 함수로 만들기
def get_stock_data(code, page_size=20, page=1):
    url = 'https://m.stock.naver.com/api/json/sise/dailySiseIndexListJson.nhn?\
code={}&pageSize={}&page={}'.format(code, page_size, page)
    response = requests.get(url)
    datas = response.json()['result']['siseList']
    return pd.DataFrame(datas)
```


```python
kospi_df = get_stock_data('KOSPI', 100)
kospi_df.tail(3)
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
      <th>cd</th>
      <th>dt</th>
      <th>ncv</th>
      <th>cv</th>
      <th>cr</th>
      <th>ov</th>
      <th>hv</th>
      <th>lv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>97</th>
      <td>KOSPI</td>
      <td>20200130</td>
      <td>2148.00</td>
      <td>-37.28</td>
      <td>-1.71</td>
      <td>2181.54</td>
      <td>2187.45</td>
      <td>2139.72</td>
    </tr>
    <tr>
      <th>98</th>
      <td>KOSPI</td>
      <td>20200129</td>
      <td>2185.28</td>
      <td>8.56</td>
      <td>0.39</td>
      <td>2188.18</td>
      <td>2195.45</td>
      <td>2172.33</td>
    </tr>
    <tr>
      <th>99</th>
      <td>KOSPI</td>
      <td>20200128</td>
      <td>2176.72</td>
      <td>-69.41</td>
      <td>-3.09</td>
      <td>2192.22</td>
      <td>2199.93</td>
      <td>2166.23</td>
    </tr>
  </tbody>
</table>
</div>




```python
kosdaq_df = get_stock_data('KOSDAQ', 100)
kosdaq_df.tail(3)
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
      <th>cd</th>
      <th>dt</th>
      <th>ncv</th>
      <th>cv</th>
      <th>cr</th>
      <th>ov</th>
      <th>hv</th>
      <th>lv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>97</th>
      <td>KOSDAQ</td>
      <td>20200130</td>
      <td>656.39</td>
      <td>-13.79</td>
      <td>-2.06</td>
      <td>670.65</td>
      <td>673.17</td>
      <td>652.42</td>
    </tr>
    <tr>
      <th>98</th>
      <td>KOSDAQ</td>
      <td>20200129</td>
      <td>670.18</td>
      <td>5.48</td>
      <td>0.82</td>
      <td>671.08</td>
      <td>671.98</td>
      <td>664.09</td>
    </tr>
    <tr>
      <th>99</th>
      <td>KOSDAQ</td>
      <td>20200128</td>
      <td>664.70</td>
      <td>-20.87</td>
      <td>-3.04</td>
      <td>660.79</td>
      <td>668.22</td>
      <td>658.78</td>
    </tr>
  </tbody>
</table>
</div>




```python
#### USD달러 크롤링
# code, page_size, page = 'FX_USDKRW', 100, 1
# url = 'https://m.stock.naver.com/api/json/marketindex/marketIndexDay.nhn?\
# marketIndexCd={}&pageSize={}&page={}'.format(code, page_size, page)

# # 쿠키데이터 추가 > 요청
# params = {
#     'cookie': 'NNB=L52X2EQ2BHWF4; nid_inf=-1419637409; NID_AUT=/qEuJQvawi8l5RlC+Bg6I1s71CcylErEwdF2v/4jVKWsYvLOZpBKDD9WNDxSaLKL; NID_JKL=OvyTRV7VW3sIWyIs00Gem3XD1T8CswIgLzHeuQr/p+Y=; nx_ssl=2; NRTK=ag#30s_gr#4_ma#2_si#2_en#2_sp#2; page_uid=UXwFGwprvN8ssiPBbVsssssstGw-521104; NID_SES=AAABgAgVa8N8ddr/Eazth8mqFKoxPDxp2HMWOVnPck7bb3nSxNEHj5BGDD2XqAYZKTZhUkSNOcRhAM1+uWIPo4CHMQ2o3QynwB+jlDKirsHc8wnbSb+u7jJ6rQou1/8UMDu0qpfZ5gWX21qpQkohjhJy6CN4bjQNFLXTGk55Tfc1a/48n64rr2mH93OqNMnju/HnnQYGF67aCQYRIoRoRYwUirUOVKzWPRj+g0+XzRULgnihhUAwwYkh4dZ/4X7WkUH5TzZWBqokpdrqF5dSN+GzCyTs+Schq4i0zTGBFl2JtjKrkxNsxgshFxFb/F2TwsO0A1FUCELCCsn1rqZJrPT2csqOz75RHIrzLLqvaeypohyzj/sCYZ59esfgBd+gi2DkUu061KN9DpsCX2Y0mHmxRDlxxGDIcGSstXQJvasJbbCKIoMoCkAR2O7equBz76TE4/LFmkgLr3fZaxqs17eZ1hAQv9qWKl/+XD/b49+CDuXqEiOlYENqstVyByg+j7YGSA==; XSRF-TOKEN=892541ee-3189-4746-accc-8daec33d1da4; JSESSIONID=954A83CB40D65F60FF60891B93DEDCE6; BMR='
# }

# response = requests.get(url, headers=params)
# datas = response.json()['result']['marketIndexDay']
# datas
# usd_df = pd.DataFrame(datas)
# usd_df.tail(3)
```


```python
# 통화데이터 함수로 만들기
def get_currency_data(code, page_size=100, page=1):
    url = 'https://m.stock.naver.com/api/json/marketindex/marketIndexDay.nhn?\
marketIndexCd={}&pageSize={}&page={}'.format(code, page_size, page)
    params = {
    'cookie': 'NNB=L52X2EQ2BHWF4; nid_inf=-1419637409; NID_AUT=/qEuJQvawi8l5RlC+Bg6I1s71CcylErEwdF2v/4jVKWsYvLOZpBKDD9WNDxSaLKL; NID_JKL=OvyTRV7VW3sIWyIs00Gem3XD1T8CswIgLzHeuQr/p+Y=; nx_ssl=2; NRTK=ag#30s_gr#4_ma#2_si#2_en#2_sp#2; page_uid=UXwFGwprvN8ssiPBbVsssssstGw-521104; NID_SES=AAABgAgVa8N8ddr/Eazth8mqFKoxPDxp2HMWOVnPck7bb3nSxNEHj5BGDD2XqAYZKTZhUkSNOcRhAM1+uWIPo4CHMQ2o3QynwB+jlDKirsHc8wnbSb+u7jJ6rQou1/8UMDu0qpfZ5gWX21qpQkohjhJy6CN4bjQNFLXTGk55Tfc1a/48n64rr2mH93OqNMnju/HnnQYGF67aCQYRIoRoRYwUirUOVKzWPRj+g0+XzRULgnihhUAwwYkh4dZ/4X7WkUH5TzZWBqokpdrqF5dSN+GzCyTs+Schq4i0zTGBFl2JtjKrkxNsxgshFxFb/F2TwsO0A1FUCELCCsn1rqZJrPT2csqOz75RHIrzLLqvaeypohyzj/sCYZ59esfgBd+gi2DkUu061KN9DpsCX2Y0mHmxRDlxxGDIcGSstXQJvasJbbCKIoMoCkAR2O7equBz76TE4/LFmkgLr3fZaxqs17eZ1hAQv9qWKl/+XD/b49+CDuXqEiOlYENqstVyByg+j7YGSA==; XSRF-TOKEN=892541ee-3189-4746-accc-8daec33d1da4; JSESSIONID=954A83CB40D65F60FF60891B93DEDCE6; BMR='
}

    response = requests.get(url, headers=params)
    datas = response.json()['result']['marketIndexDay']
    return pd.DataFrame(datas)
```


```python
usd_df = get_currency_data('FX_USDKRW')
usd_df.tail(3)
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
      <th>dt</th>
      <th>nv</th>
      <th>cv</th>
      <th>cr</th>
      <th>cbv</th>
      <th>csv</th>
      <th>sv</th>
      <th>rv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>97</th>
      <td>20200130</td>
      <td>1189.0</td>
      <td>10.0</td>
      <td>0.85</td>
      <td>1209.80</td>
      <td>1168.20</td>
      <td>1200.6</td>
      <td>1177.4</td>
    </tr>
    <tr>
      <th>98</th>
      <td>20200129</td>
      <td>1179.0</td>
      <td>-0.5</td>
      <td>-0.04</td>
      <td>1199.63</td>
      <td>1158.37</td>
      <td>1190.5</td>
      <td>1167.5</td>
    </tr>
    <tr>
      <th>99</th>
      <td>20200128</td>
      <td>1179.5</td>
      <td>11.5</td>
      <td>0.98</td>
      <td>1200.14</td>
      <td>1158.86</td>
      <td>1191.0</td>
      <td>1168.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(usd_df.dt.values)
print(kospi_df.dt.values)
```

    ['20200619' '20200618' '20200617' '20200616' '20200615' '20200612'
     '20200611' '20200610' '20200609' '20200608' '20200605' '20200604'
     '20200603' '20200602' '20200601' '20200529' '20200528' '20200527'
     '20200526' '20200525' '20200522' '20200521' '20200520' '20200519'
     '20200518' '20200515' '20200514' '20200513' '20200512' '20200511'
     '20200508' '20200507' '20200506' '20200504' '20200429' '20200428'
     '20200427' '20200424' '20200423' '20200422' '20200421' '20200420'
     '20200417' '20200416' '20200414' '20200413' '20200410' '20200409'
     '20200408' '20200407' '20200406' '20200403' '20200402' '20200401'
     '20200331' '20200330' '20200327' '20200326' '20200325' '20200324'
     '20200323' '20200320' '20200319' '20200318' '20200317' '20200316'
     '20200313' '20200312' '20200311' '20200310' '20200309' '20200306'
     '20200305' '20200304' '20200303' '20200302' '20200228' '20200227'
     '20200226' '20200225' '20200224' '20200221' '20200220' '20200219'
     '20200218' '20200217' '20200214' '20200213' '20200212' '20200211'
     '20200210' '20200207' '20200206' '20200205' '20200204' '20200203'
     '20200131' '20200130' '20200129' '20200128']
    ['20200619' '20200618' '20200617' '20200616' '20200615' '20200612'
     '20200611' '20200610' '20200609' '20200608' '20200605' '20200604'
     '20200603' '20200602' '20200601' '20200529' '20200528' '20200527'
     '20200526' '20200525' '20200522' '20200521' '20200520' '20200519'
     '20200518' '20200515' '20200514' '20200513' '20200512' '20200511'
     '20200508' '20200507' '20200506' '20200504' '20200429' '20200428'
     '20200427' '20200424' '20200423' '20200422' '20200421' '20200420'
     '20200417' '20200416' '20200414' '20200413' '20200410' '20200409'
     '20200408' '20200407' '20200406' '20200403' '20200402' '20200401'
     '20200331' '20200330' '20200327' '20200326' '20200325' '20200324'
     '20200323' '20200320' '20200319' '20200318' '20200317' '20200316'
     '20200313' '20200312' '20200311' '20200310' '20200309' '20200306'
     '20200305' '20200304' '20200303' '20200302' '20200228' '20200227'
     '20200226' '20200225' '20200224' '20200221' '20200220' '20200219'
     '20200218' '20200217' '20200214' '20200213' '20200212' '20200211'
     '20200210' '20200207' '20200206' '20200205' '20200204' '20200203'
     '20200131' '20200130' '20200129' '20200128']



```python
# 데이터 합치기
# merge_df_1 = pd.merge(kospi_df, kosdaq_df, left_on='dt', right_on='dt')
merge_df_1 = pd.merge(kospi_df, kosdaq_df, on='dt', how='inner')
merge_df_1 = merge_df_1.rename(columns={'ncv_x':'ncv_kospi', 'ncv_y':'ncv_kosdaq'})
merge_df_1 = merge_df_1[['dt','ncv_kospi', 'ncv_kosdaq']]
merge_df_1
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
      <th>dt</th>
      <th>ncv_kospi</th>
      <th>ncv_kosdaq</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20200619</td>
      <td>2126.08</td>
      <td>739.69</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20200618</td>
      <td>2133.48</td>
      <td>737.33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20200617</td>
      <td>2141.05</td>
      <td>735.40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20200616</td>
      <td>2138.05</td>
      <td>735.38</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20200615</td>
      <td>2030.82</td>
      <td>693.15</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>20200203</td>
      <td>2118.88</td>
      <td>646.85</td>
    </tr>
    <tr>
      <th>96</th>
      <td>20200131</td>
      <td>2119.01</td>
      <td>642.48</td>
    </tr>
    <tr>
      <th>97</th>
      <td>20200130</td>
      <td>2148.00</td>
      <td>656.39</td>
    </tr>
    <tr>
      <th>98</th>
      <td>20200129</td>
      <td>2185.28</td>
      <td>670.18</td>
    </tr>
    <tr>
      <th>99</th>
      <td>20200128</td>
      <td>2176.72</td>
      <td>664.70</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 3 columns</p>
</div>




```python
merge_df = pd.merge(merge_df_1, usd_df, on='dt', how='inner')[['dt','ncv_kospi', 'ncv_kosdaq', 'nv']]
merge_df
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
      <th>dt</th>
      <th>ncv_kospi</th>
      <th>ncv_kosdaq</th>
      <th>nv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20200619</td>
      <td>2126.08</td>
      <td>739.69</td>
      <td>1211.7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20200618</td>
      <td>2133.48</td>
      <td>737.33</td>
      <td>1209.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20200617</td>
      <td>2141.05</td>
      <td>735.40</td>
      <td>1213.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20200616</td>
      <td>2138.05</td>
      <td>735.38</td>
      <td>1212.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20200615</td>
      <td>2030.82</td>
      <td>693.15</td>
      <td>1215.5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>20200203</td>
      <td>2118.88</td>
      <td>646.85</td>
      <td>1194.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>20200131</td>
      <td>2119.01</td>
      <td>642.48</td>
      <td>1194.5</td>
    </tr>
    <tr>
      <th>97</th>
      <td>20200130</td>
      <td>2148.00</td>
      <td>656.39</td>
      <td>1189.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>20200129</td>
      <td>2185.28</td>
      <td>670.18</td>
      <td>1179.0</td>
    </tr>
    <tr>
      <th>99</th>
      <td>20200128</td>
      <td>2176.72</td>
      <td>664.70</td>
      <td>1179.5</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 4 columns</p>
</div>




```python
# import plotly.express as px
# fig = px.line(merge_df, x='dt', y='ncv_kospi')
# fig.show()
```


```python
# 그래프 그리기
plt.figure(figsize=(18,6))
plt.plot(merge_df.dt, merge_df.ncv_kospi, 'r*:', label='kospi')
plt.plot(merge_df.dt, merge_df.ncv_kosdaq, 'bo--', label='kosdaq')
plt.plot(merge_df.dt, merge_df.nv, 'g^-', label='dollors')

# xtick이 항상 10개 출력 되도록
step = len(merge_df) // 10
plt.xticks(merge_df[::step]['dt'])

plt.title('The effect of Kospi and Kosdaq with US DOLLORS')
plt.legend()
plt.show()
```


<img width="1053" alt="output_19_0" src="https://user-images.githubusercontent.com/59719711/85102292-53647e00-b23f-11ea-9410-cc9e804f450a.png">


    정규화 (Normalization)
    z = (x - min(x)) / (max(x) - min(x))


```python
from sklearn import preprocessing
```


```python
preprocessing.minmax_scale(merge_df['ncv_kospi'])
```




    array([0.85048667, 0.85990203, 0.86953369, 0.86571665, 0.72928303,
           0.85840066, 0.91499459, 0.93905465, 0.93044087, 0.92454991,
           0.92147083, 0.88242255, 0.87710414, 0.80100515, 0.77287359,
           0.72773077, 0.72638209, 0.72976652, 0.72795979, 0.68319868,
           0.65206438, 0.68791908, 0.67688784, 0.66539856, 0.61005153,
           0.59754437, 0.59459253, 0.61426299, 0.59104269, 0.60787582,
           0.62113366, 0.59923659, 0.59942744, 0.55694383, 0.62334754,
           0.60620905, 0.59180609, 0.54885171, 0.58157644, 0.55793626,
           0.53659902, 0.56074814, 0.58132197, 0.50821299, 0.50822571,
           0.46837585, 0.51283161, 0.48167186, 0.44468478, 0.46562758,
           0.42526878, 0.34073414, 0.33999618, 0.28986577, 0.37788663,
           0.33014823, 0.33092436, 0.2908582 , 0.31442204, 0.1938164 ,
           0.03157962, 0.13806222, 0.        , 0.16993447, 0.27329983,
           0.32727273, 0.39926204, 0.47927985, 0.57335708, 0.64290349,
           0.63252115, 0.74124308, 0.79854953, 0.76555761, 0.70807303,
           0.69326293, 0.67354157, 0.75990839, 0.78774731, 0.82189707,
           0.79063554, 0.8972581 , 0.9388129 , 0.95769451, 0.95583689,
           0.99819327, 1.        , 0.98647497, 0.99337108, 0.97395509,
           0.94589987, 0.95974299, 0.98008779, 0.90080794, 0.89097271,
           0.84132578, 0.84149119, 0.87837649, 0.92580953, 0.91491825])




```python
plt.figure(figsize=(18,6))
plt.plot(merge_df['dt'], preprocessing.minmax_scale(merge_df['ncv_kospi']), 'r*:', label='kospi')
plt.plot(merge_df['dt'], preprocessing.minmax_scale(merge_df['ncv_kosdaq']), 'bo--', label='kosdaq')
plt.plot(merge_df['dt'], preprocessing.minmax_scale(merge_df['nv']), 'g^-', label='usd')
# xtick이 항상 10개 출력 되도록
step = len(merge_df) // 10
plt.xticks(merge_df[::step]['dt'])

plt.legend()
plt.show()
```


<img width="1044" alt="output_23_0" src="https://user-images.githubusercontent.com/59719711/85102471-b48c5180-b23f-11ea-960c-59930e0a45dc.png">



```python
# 상관계수
```


```python
print(np.corrcoef(merge_df['ncv_kospi'], merge_df['ncv_kosdaq'])[0,1])
print(np.corrcoef(merge_df['ncv_kospi'], merge_df['nv'])[0,1])
print(np.corrcoef(merge_df['ncv_kosdaq'], merge_df['nv'])[0,1])
```

    0.8433394279395071
    -0.7604155843262883
    -0.41380572460261045



```python

```


```python
# 중국(코로나) 위안화 데이터 가져와서 전처리 후 kospi, kosdaq 과의 insight 분석하기
chn_df = get_currency_data('FX_CNYKRW')
merge_df_chn = pd.merge(merge_df_1, chn_df[['dt','nv']], on='dt', how='inner')
merge_df_chn
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
      <th>dt</th>
      <th>ncv_kospi</th>
      <th>ncv_kosdaq</th>
      <th>nv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20200619</td>
      <td>2126.08</td>
      <td>739.69</td>
      <td>171.24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20200618</td>
      <td>2133.48</td>
      <td>737.33</td>
      <td>170.97</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20200617</td>
      <td>2141.05</td>
      <td>735.40</td>
      <td>171.41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20200616</td>
      <td>2138.05</td>
      <td>735.38</td>
      <td>171.45</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20200615</td>
      <td>2030.82</td>
      <td>693.15</td>
      <td>171.36</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>20200203</td>
      <td>2118.88</td>
      <td>646.85</td>
      <td>170.17</td>
    </tr>
    <tr>
      <th>96</th>
      <td>20200131</td>
      <td>2119.01</td>
      <td>642.48</td>
      <td>171.02</td>
    </tr>
    <tr>
      <th>97</th>
      <td>20200130</td>
      <td>2148.00</td>
      <td>656.39</td>
      <td>170.06</td>
    </tr>
    <tr>
      <th>98</th>
      <td>20200129</td>
      <td>2185.28</td>
      <td>670.18</td>
      <td>169.36</td>
    </tr>
    <tr>
      <th>99</th>
      <td>20200128</td>
      <td>2176.72</td>
      <td>664.70</td>
      <td>168.89</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 4 columns</p>
</div>




```python
plt.figure(figsize=(18,6))
plt.plot(merge_df_chn['dt'], preprocessing.minmax_scale(merge_df_chn['ncv_kospi']), 'r*:', label='kospi')
plt.plot(merge_df_chn['dt'], preprocessing.minmax_scale(merge_df_chn['ncv_kosdaq']), 'bo--', label='kosdaq')
plt.plot(merge_df_chn['dt'], preprocessing.minmax_scale(merge_df_chn['nv']), 'g^-', label='chn')
# xtick이 항상 10개 출력 되도록
step = len(merge_df_chn) // 10
plt.xticks(merge_df_chn[::step]['dt'])

plt.legend()
plt.show()
```


<img width="1044" alt="output_28_0" src="https://user-images.githubusercontent.com/59719711/85102521-cb32a880-b23f-11ea-8443-e307377c7dfc.png">



```python
print(np.corrcoef(merge_df_chn['ncv_kospi'], merge_df_chn['nv'])[0,1])
print(np.corrcoef(merge_df_chn['ncv_kosdaq'], merge_df_chn['nv'])[0,1])
```

    -0.8379584847254301
    -0.6721809453863601



```python

```


```python

```


```python

```


```python

```


```python
# from pandas.io.json import json_normalize

# key ='HKjlKoD96KLVmmxm%2ByoE5Qy9Hxa2zd0c79rL%2BpZSqtxHOFnUl8usHgST2yl%2FbCyqUsXXd68dsHcJcVmHjYRBOg%3D%3D'
# url = 'http://apis.data.go.kr/1360000/RoadWthrInfoService/getStdNodeLinkRoadWw?\
# serviceKey={}&numOfRows=10&pageNo=1&stdLinkId=2370012300&hhCode=00'.format(key)

# payload = {}
# headers= {}

# response = requests.request("GET", url, headers=headers, data = payload)
# response
# # response.json()
```


```python

```
