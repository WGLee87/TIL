###### API로 날씨 정보 가져오기
    - darksky.net 서비스를 사용
    - 회원가입 및 로그인
        - id : pdj1224@gmail.com
        - pw : qwer1234


```python
KEY = '1181bba0a7d7f1ec6799a80846a2a98f'
lat, lng = 37.8267, -122.4233
url = 'https://api.darksky.net/forecast/{}/{},{}'.format(KEY, lat, lng)

response = requests.get(url)
response.text
datas = response.json()
datas
datas['timezone'], datas['hourly']['summary']
```




    ('America/Los_Angeles', 'Partly cloudy throughout the day.')




```python
def forecast(lat, lng):
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(KEY, lat, lng)
    response = requests.get(url)
    datas = response.json()
    return datas['timezone'], datas['hourly']['summary']
```


```python
forecast(37.5650, 126.9780)
```




    ('Asia/Seoul', 'Partly cloudy throughout the day.')




```python
# 데이터프레임으로 가져오기
from pandas.io.json import json_normalize
datas
df = json_normalize(datas)
df
```

    /opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:4: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead
      after removing the cwd from sys.path.





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
      <th>latitude</th>
      <th>longitude</th>
      <th>timezone</th>
      <th>offset</th>
      <th>currently.time</th>
      <th>currently.summary</th>
      <th>currently.icon</th>
      <th>currently.nearestStormDistance</th>
      <th>currently.nearestStormBearing</th>
      <th>currently.precipIntensity</th>
      <th>...</th>
      <th>minutely.data</th>
      <th>hourly.summary</th>
      <th>hourly.icon</th>
      <th>hourly.data</th>
      <th>daily.summary</th>
      <th>daily.icon</th>
      <th>daily.data</th>
      <th>flags.sources</th>
      <th>flags.nearest-station</th>
      <th>flags.units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37.8267</td>
      <td>-122.4233</td>
      <td>America/Los_Angeles</td>
      <td>-7</td>
      <td>1592545449</td>
      <td>Clear</td>
      <td>clear-night</td>
      <td>7</td>
      <td>297</td>
      <td>0</td>
      <td>...</td>
      <td>[{'time': 1592545440, 'precipIntensity': 0, 'p...</td>
      <td>Partly cloudy throughout the day.</td>
      <td>partly-cloudy-day</td>
      <td>[{'time': 1592542800, 'summary': 'Clear', 'ico...</td>
      <td>No precipitation throughout the week.</td>
      <td>clear-day</td>
      <td>[{'time': 1592463600, 'summary': 'Clear throug...</td>
      <td>[nwspa, cmc, gfs, hrrr, icon, isd, madis, nam,...</td>
      <td>2.582</td>
      <td>us</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 35 columns</p>
</div>




```python
datas['timezone'], datas['hourly']['summary']

payload = {}
data = pd.DataFrame()

for i in range(1, 100):
    url = 'https://api.darksky.net/forecast/1181bba0a7d7f1ec6799a80846a2a98f/{},-122.4233'.format(KEY, i)
    response = requests.get(url, data=payload)
    datas = response.json()

    i += 1
# data['Name'] = data[['firstname','lastname']].apply(lambda x: ' '.join(x), axis=1)
datas
```




    {'code': 400, 'error': 'Poorly formatted request'}


