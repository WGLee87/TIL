###### daum에서 환율정보 크롤링
    - https://finance.daum.net/exchanges
    - fake_useragent
        - pip install fake_useragent


```python
from fake_useragent import UserAgent
```


```python
UserAgent().chrome
```




    'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36'




```python

```


```python

```


```python
url = 'https://finance.daum.net/api/exchanges/summaries'

headers = {
    'user-agent' : UserAgent().chrome,
    'referer' : 'https://finance.daum.net/exchanges'
}
response = requests.get(url, headers=headers)
datas = response.json()['data']
result = pd.DataFrame(datas)
result.tail(2)
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
      <th>symbolCode</th>
      <th>date</th>
      <th>currencyCode</th>
      <th>currencyName</th>
      <th>currencyUnit</th>
      <th>country</th>
      <th>region</th>
      <th>name</th>
      <th>recurrenceCount</th>
      <th>basePrice</th>
      <th>...</th>
      <th>changeRate</th>
      <th>cashBuyingPrice</th>
      <th>cashSellingPrice</th>
      <th>ttBuyingPrice</th>
      <th>ttSellingPrice</th>
      <th>tcBuyingPrice</th>
      <th>fcSellingPrice</th>
      <th>exchangeCommission</th>
      <th>usDollarRate</th>
      <th>chartImageUrl</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40</th>
      <td>FRX.KRWQAR</td>
      <td>2020-06-23 17:59:27</td>
      <td>QAR</td>
      <td>리얄</td>
      <td>1</td>
      <td>카타르</td>
      <td>{'korName': '중동', 'engName': 'Middle East'}</td>
      <td>카타르 (KRW/QAR)</td>
      <td>607</td>
      <td>332.05</td>
      <td>...</td>
      <td>0.004109</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>None</td>
      <td>None</td>
      <td>2.185</td>
      <td>0.2746</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>FRX.KRWTRY</td>
      <td>2020-06-23 17:59:28</td>
      <td>TRY</td>
      <td>리라</td>
      <td>1</td>
      <td>터키</td>
      <td>{'korName': '중동', 'engName': 'Middle East'}</td>
      <td>터키 (KRW/TRY)</td>
      <td>607</td>
      <td>176.30</td>
      <td>...</td>
      <td>0.004292</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>174.37</td>
      <td>178.23</td>
      <td>None</td>
      <td>None</td>
      <td>13.675</td>
      <td>0.1458</td>
      <td>{'day': 'https://t1.daumcdn.net/finance/chart/...</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 22 columns</p>
</div>




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


```python

```


```python

```


```python

```


```python

```
