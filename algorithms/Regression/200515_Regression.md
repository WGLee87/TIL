회귀분석(Linear Regression) 공부 4일차

    1. 2019년 K리그1 데이터로 보는 회귀분석
        * 득점을 용이하게 만드는 선수들의 Key Pass는 어떠한 요인들이 가장 크게 영향력을 미칠까?
        * 패스데이터만 추출하여 키패스에 영향력, 상관관계를 보기 위한 회귀분석 실시
        * 아직 미완성임 (Unperfected)



```python
import statsmodels.api as sm

df = pd.read_excel('/Users/wglee/Desktop/K리그1.xlsx').groupby('선수 이름').sum()
is_time = df['Time played'] >= 1800
df = df[is_time]
```


```python
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
      <th>Time played</th>
      <th>Goal</th>
      <th>Assists</th>
      <th>Shots</th>
      <th>SoT</th>
      <th>Blocked Shots</th>
      <th>Shots off Target</th>
      <th>Shots inside PA</th>
      <th>Shots outside of PA</th>
      <th>Offsides</th>
      <th>...</th>
      <th>Blocks</th>
      <th>Mistakes</th>
      <th>Fouls</th>
      <th>Fouls Won</th>
      <th>Yellow Cards</th>
      <th>Red Cards</th>
      <th>Instats Index</th>
      <th>Mistakes(Ball-Lost)</th>
      <th>Ball-Recovery</th>
      <th>Fantasy Score</th>
    </tr>
    <tr>
      <th>선수 이름</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A. Taggart</th>
      <td>2778</td>
      <td>21</td>
      <td>2</td>
      <td>114</td>
      <td>40</td>
      <td>30</td>
      <td>41</td>
      <td>74</td>
      <td>40</td>
      <td>18</td>
      <td>...</td>
      <td>0</td>
      <td>40</td>
      <td>67</td>
      <td>41</td>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Aleks</th>
      <td>1821</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>10</td>
      <td>1</td>
      <td>18</td>
      <td>10</td>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>C. Melo</th>
      <td>2959</td>
      <td>15</td>
      <td>10</td>
      <td>165</td>
      <td>64</td>
      <td>42</td>
      <td>54</td>
      <td>54</td>
      <td>111</td>
      <td>4</td>
      <td>...</td>
      <td>2</td>
      <td>52</td>
      <td>37</td>
      <td>124</td>
      <td>4</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>E. Bruno</th>
      <td>1967</td>
      <td>11</td>
      <td>4</td>
      <td>79</td>
      <td>29</td>
      <td>10</td>
      <td>38</td>
      <td>64</td>
      <td>15</td>
      <td>12</td>
      <td>...</td>
      <td>2</td>
      <td>27</td>
      <td>44</td>
      <td>34</td>
      <td>4</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>M. Damasceno Santos da Cruz</th>
      <td>2343</td>
      <td>7</td>
      <td>2</td>
      <td>47</td>
      <td>14</td>
      <td>10</td>
      <td>23</td>
      <td>31</td>
      <td>16</td>
      <td>16</td>
      <td>...</td>
      <td>2</td>
      <td>29</td>
      <td>31</td>
      <td>30</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
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
      <th>한의권</th>
      <td>1815</td>
      <td>4</td>
      <td>2</td>
      <td>52</td>
      <td>14</td>
      <td>16</td>
      <td>22</td>
      <td>37</td>
      <td>15</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>15</td>
      <td>44</td>
      <td>16</td>
      <td>4</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>홍정호</th>
      <td>2277</td>
      <td>2</td>
      <td>0</td>
      <td>14</td>
      <td>6</td>
      <td>0</td>
      <td>8</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>13</td>
      <td>14</td>
      <td>26</td>
      <td>17</td>
      <td>2</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>홍철</th>
      <td>2916</td>
      <td>1</td>
      <td>4</td>
      <td>16</td>
      <td>6</td>
      <td>3</td>
      <td>7</td>
      <td>8</td>
      <td>8</td>
      <td>1</td>
      <td>...</td>
      <td>5</td>
      <td>24</td>
      <td>32</td>
      <td>40</td>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>황순민</th>
      <td>2766</td>
      <td>3</td>
      <td>3</td>
      <td>45</td>
      <td>13</td>
      <td>11</td>
      <td>21</td>
      <td>10</td>
      <td>35</td>
      <td>2</td>
      <td>...</td>
      <td>3</td>
      <td>14</td>
      <td>20</td>
      <td>31</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>황현수</th>
      <td>3167</td>
      <td>5</td>
      <td>3</td>
      <td>20</td>
      <td>8</td>
      <td>3</td>
      <td>9</td>
      <td>14</td>
      <td>6</td>
      <td>0</td>
      <td>...</td>
      <td>23</td>
      <td>15</td>
      <td>32</td>
      <td>12</td>
      <td>2</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 60 columns</p>
</div>




```python
# df_name = df.reset_index()['선수 이름']
# df_name = pd.DataFrame(df_name)

# df['Time_played'] = pd.DataFrame(round(df['Time played'] / 90,2))
# df.drop('Time played', axis=1, inplace=True)

# df.reset_index(drop=True, inplace=True)

# df_Time = pd.DataFrame(df['Time_played'])

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
      <th>Goal</th>
      <th>Assists</th>
      <th>Shots</th>
      <th>SoT</th>
      <th>Blocked Shots</th>
      <th>Shots off Target</th>
      <th>Shots inside PA</th>
      <th>Shots outside of PA</th>
      <th>Offsides</th>
      <th>Freekicks</th>
      <th>...</th>
      <th>Mistakes</th>
      <th>Fouls</th>
      <th>Fouls Won</th>
      <th>Yellow Cards</th>
      <th>Red Cards</th>
      <th>Instats Index</th>
      <th>Mistakes(Ball-Lost)</th>
      <th>Ball-Recovery</th>
      <th>Fantasy Score</th>
      <th>Time_played</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>21</td>
      <td>2</td>
      <td>114</td>
      <td>40</td>
      <td>30</td>
      <td>41</td>
      <td>74</td>
      <td>40</td>
      <td>18</td>
      <td>2</td>
      <td>...</td>
      <td>40</td>
      <td>67</td>
      <td>41</td>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>30.87</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>23</td>
      <td>...</td>
      <td>1</td>
      <td>18</td>
      <td>10</td>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>20.23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15</td>
      <td>10</td>
      <td>165</td>
      <td>64</td>
      <td>42</td>
      <td>54</td>
      <td>54</td>
      <td>111</td>
      <td>4</td>
      <td>179</td>
      <td>...</td>
      <td>52</td>
      <td>37</td>
      <td>124</td>
      <td>4</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>32.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11</td>
      <td>4</td>
      <td>79</td>
      <td>29</td>
      <td>10</td>
      <td>38</td>
      <td>64</td>
      <td>15</td>
      <td>12</td>
      <td>0</td>
      <td>...</td>
      <td>27</td>
      <td>44</td>
      <td>34</td>
      <td>4</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>21.86</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>2</td>
      <td>47</td>
      <td>14</td>
      <td>10</td>
      <td>23</td>
      <td>31</td>
      <td>16</td>
      <td>16</td>
      <td>3</td>
      <td>...</td>
      <td>29</td>
      <td>31</td>
      <td>30</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>26.03</td>
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
      <th>99</th>
      <td>4</td>
      <td>2</td>
      <td>52</td>
      <td>14</td>
      <td>16</td>
      <td>22</td>
      <td>37</td>
      <td>15</td>
      <td>5</td>
      <td>0</td>
      <td>...</td>
      <td>15</td>
      <td>44</td>
      <td>16</td>
      <td>4</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>20.17</td>
    </tr>
    <tr>
      <th>100</th>
      <td>2</td>
      <td>0</td>
      <td>14</td>
      <td>6</td>
      <td>0</td>
      <td>8</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>...</td>
      <td>14</td>
      <td>26</td>
      <td>17</td>
      <td>2</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>25.30</td>
    </tr>
    <tr>
      <th>101</th>
      <td>1</td>
      <td>4</td>
      <td>16</td>
      <td>6</td>
      <td>3</td>
      <td>7</td>
      <td>8</td>
      <td>8</td>
      <td>1</td>
      <td>85</td>
      <td>...</td>
      <td>24</td>
      <td>32</td>
      <td>40</td>
      <td>3</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>32.40</td>
    </tr>
    <tr>
      <th>102</th>
      <td>3</td>
      <td>3</td>
      <td>45</td>
      <td>13</td>
      <td>11</td>
      <td>21</td>
      <td>10</td>
      <td>35</td>
      <td>2</td>
      <td>21</td>
      <td>...</td>
      <td>14</td>
      <td>20</td>
      <td>31</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>30.73</td>
    </tr>
    <tr>
      <th>103</th>
      <td>5</td>
      <td>3</td>
      <td>20</td>
      <td>8</td>
      <td>3</td>
      <td>9</td>
      <td>14</td>
      <td>6</td>
      <td>0</td>
      <td>47</td>
      <td>...</td>
      <td>15</td>
      <td>32</td>
      <td>12</td>
      <td>2</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>35.19</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 60 columns</p>
</div>




```python
df.columns
```




    Index(['Time played', 'Goal', 'Assists', 'Shots', 'SoT', 'Blocked Shots',
           'Shots off Target', 'Shots inside PA', 'Shots outside of PA',
           'Offsides', 'Freekicks', 'Corners', 'Throw-Ins', 'Take-ons Success',
           'Take-ons Total', 'Passes Success', 'Passes Total', 'Pass Accuracy(%)',
           'Key Passes', 'Passes in Final third Area Success',
           'PassesinFinalthirdArea Total', 'Middle Area Passes Success',
           'MiddleAreaPasses Total', 'Passes in Defensive Area Success',
           'PassesinDefensiveArea Total', 'Long Pass Success', 'LongPass Total',
           'Medium Range Pass Success', 'MediumRangePass Total',
           'Short Pass Success', 'ShortPass Total', 'Forwards Pass Success',
           'ForwardsPass Total', 'Sideways Pass Success', 'SidewaysPass Total',
           'Backwards Pass Success', 'BackwardsPass Total', 'Crosses Success',
           'Crosses Total', 'Control under pressure', 'Tackles Success',
           'Tackles Total', 'Aerial Duels Success', 'AerialDuels Total',
           'Ground Duels Success', 'GroundDuels Total', 'Interceptions',
           'Clearances', 'Cut-off', 'Recovery', 'Blocks', 'Mistakes', 'Fouls',
           'Fouls Won', 'Yellow Cards', 'Red Cards', 'Instats Index',
           'Mistakes(Ball-Lost)', 'Ball-Recovery', 'Fantasy Score'],
          dtype='object')




```python
a = df['Passes in Final third Area Success'] / df['Time_played']
b = df['Middle Area Passes Success'] / df['Time_played']
c = df['Passes in Defensive Area Success'] / df['Time_played']
d = df['Long Pass Success'] / df['Time_played']
e = df['Medium Range Pass Success'] / df['Time_played']
f = df['Short Pass Success'] / df['Time_played']
g = df['Forwards Pass Success'] / df['Time_played']
h = df['Sideways Pass Success'] / df['Time_played']
i = df['Backwards Pass Success'] / df['Time_played']
i = df['Backwards Pass Success'] / df['Time_played']
j = df['Key Passes'] / df['Time_played']

df0 = pd.concat([df_name, a,b,c,d,e,f,g,h,i, j], axis=1)
df0
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
      <th>선수 이름</th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A. Taggart</td>
      <td>6.997085</td>
      <td>9.102689</td>
      <td>0.388727</td>
      <td>0.550696</td>
      <td>3.401361</td>
      <td>12.536443</td>
      <td>3.919663</td>
      <td>6.770327</td>
      <td>5.798510</td>
      <td>0.907029</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aleks</td>
      <td>0.444884</td>
      <td>25.803262</td>
      <td>14.335146</td>
      <td>4.300544</td>
      <td>17.498764</td>
      <td>18.783984</td>
      <td>16.856154</td>
      <td>18.932279</td>
      <td>4.794859</td>
      <td>0.098863</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C. Melo</td>
      <td>12.682482</td>
      <td>18.917275</td>
      <td>1.094891</td>
      <td>4.714112</td>
      <td>10.796837</td>
      <td>17.183698</td>
      <td>9.701946</td>
      <td>15.298054</td>
      <td>7.694647</td>
      <td>2.858881</td>
    </tr>
    <tr>
      <th>3</th>
      <td>E. Bruno</td>
      <td>7.182068</td>
      <td>9.652333</td>
      <td>1.143641</td>
      <td>1.189387</td>
      <td>3.522415</td>
      <td>13.266240</td>
      <td>4.757548</td>
      <td>7.136322</td>
      <td>6.084172</td>
      <td>1.646844</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M. Damasceno Santos da Cruz</td>
      <td>11.909335</td>
      <td>12.831348</td>
      <td>0.845179</td>
      <td>0.883596</td>
      <td>5.109489</td>
      <td>19.592778</td>
      <td>5.416827</td>
      <td>10.065309</td>
      <td>10.103726</td>
      <td>1.690357</td>
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
    </tr>
    <tr>
      <th>99</th>
      <td>한의권</td>
      <td>11.700545</td>
      <td>8.577095</td>
      <td>0.793257</td>
      <td>0.545364</td>
      <td>4.214179</td>
      <td>16.311353</td>
      <td>4.263758</td>
      <td>7.486366</td>
      <td>9.320773</td>
      <td>1.239465</td>
    </tr>
    <tr>
      <th>100</th>
      <td>홍정호</td>
      <td>1.106719</td>
      <td>30.118577</td>
      <td>16.877470</td>
      <td>6.126482</td>
      <td>23.241107</td>
      <td>18.735178</td>
      <td>20.434783</td>
      <td>23.083004</td>
      <td>4.584980</td>
      <td>0.316206</td>
    </tr>
    <tr>
      <th>101</th>
      <td>홍철</td>
      <td>16.604938</td>
      <td>27.808642</td>
      <td>8.240741</td>
      <td>4.567901</td>
      <td>15.216049</td>
      <td>32.870370</td>
      <td>16.975309</td>
      <td>17.746914</td>
      <td>17.932099</td>
      <td>1.944444</td>
    </tr>
    <tr>
      <th>102</th>
      <td>황순민</td>
      <td>8.590953</td>
      <td>27.074520</td>
      <td>6.801171</td>
      <td>3.449398</td>
      <td>13.830133</td>
      <td>25.187114</td>
      <td>13.439636</td>
      <td>16.889034</td>
      <td>12.137976</td>
      <td>0.943703</td>
    </tr>
    <tr>
      <th>103</th>
      <td>황현수</td>
      <td>2.614379</td>
      <td>26.115374</td>
      <td>9.008241</td>
      <td>2.983802</td>
      <td>15.373686</td>
      <td>19.380506</td>
      <td>18.755328</td>
      <td>14.492754</td>
      <td>4.489912</td>
      <td>0.511509</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 11 columns</p>
</div>




```python
dfx = df0[['선수 이름',0,1,2,3,4,5,6,7,8]]
dfx.columns = ['선수 이름','FTA_PS','MA_PS','DA_PS','LPS','MPS','SHORT_PS','FPS','SIDE_PS','BPS']
dfy = pd.DataFrame(df0[9])
dfy.columns = ['KP']
dfz = pd.concat([dfx, dfy], axis=1).set_index('선수 이름')
dfz
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
      <th>FTA_PS</th>
      <th>MA_PS</th>
      <th>DA_PS</th>
      <th>LPS</th>
      <th>MPS</th>
      <th>SHORT_PS</th>
      <th>FPS</th>
      <th>SIDE_PS</th>
      <th>BPS</th>
      <th>KP</th>
    </tr>
    <tr>
      <th>선수 이름</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A. Taggart</th>
      <td>6.997085</td>
      <td>9.102689</td>
      <td>0.388727</td>
      <td>0.550696</td>
      <td>3.401361</td>
      <td>12.536443</td>
      <td>3.919663</td>
      <td>6.770327</td>
      <td>5.798510</td>
      <td>0.907029</td>
    </tr>
    <tr>
      <th>Aleks</th>
      <td>0.444884</td>
      <td>25.803262</td>
      <td>14.335146</td>
      <td>4.300544</td>
      <td>17.498764</td>
      <td>18.783984</td>
      <td>16.856154</td>
      <td>18.932279</td>
      <td>4.794859</td>
      <td>0.098863</td>
    </tr>
    <tr>
      <th>C. Melo</th>
      <td>12.682482</td>
      <td>18.917275</td>
      <td>1.094891</td>
      <td>4.714112</td>
      <td>10.796837</td>
      <td>17.183698</td>
      <td>9.701946</td>
      <td>15.298054</td>
      <td>7.694647</td>
      <td>2.858881</td>
    </tr>
    <tr>
      <th>E. Bruno</th>
      <td>7.182068</td>
      <td>9.652333</td>
      <td>1.143641</td>
      <td>1.189387</td>
      <td>3.522415</td>
      <td>13.266240</td>
      <td>4.757548</td>
      <td>7.136322</td>
      <td>6.084172</td>
      <td>1.646844</td>
    </tr>
    <tr>
      <th>M. Damasceno Santos da Cruz</th>
      <td>11.909335</td>
      <td>12.831348</td>
      <td>0.845179</td>
      <td>0.883596</td>
      <td>5.109489</td>
      <td>19.592778</td>
      <td>5.416827</td>
      <td>10.065309</td>
      <td>10.103726</td>
      <td>1.690357</td>
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
    </tr>
    <tr>
      <th>한의권</th>
      <td>11.700545</td>
      <td>8.577095</td>
      <td>0.793257</td>
      <td>0.545364</td>
      <td>4.214179</td>
      <td>16.311353</td>
      <td>4.263758</td>
      <td>7.486366</td>
      <td>9.320773</td>
      <td>1.239465</td>
    </tr>
    <tr>
      <th>홍정호</th>
      <td>1.106719</td>
      <td>30.118577</td>
      <td>16.877470</td>
      <td>6.126482</td>
      <td>23.241107</td>
      <td>18.735178</td>
      <td>20.434783</td>
      <td>23.083004</td>
      <td>4.584980</td>
      <td>0.316206</td>
    </tr>
    <tr>
      <th>홍철</th>
      <td>16.604938</td>
      <td>27.808642</td>
      <td>8.240741</td>
      <td>4.567901</td>
      <td>15.216049</td>
      <td>32.870370</td>
      <td>16.975309</td>
      <td>17.746914</td>
      <td>17.932099</td>
      <td>1.944444</td>
    </tr>
    <tr>
      <th>황순민</th>
      <td>8.590953</td>
      <td>27.074520</td>
      <td>6.801171</td>
      <td>3.449398</td>
      <td>13.830133</td>
      <td>25.187114</td>
      <td>13.439636</td>
      <td>16.889034</td>
      <td>12.137976</td>
      <td>0.943703</td>
    </tr>
    <tr>
      <th>황현수</th>
      <td>2.614379</td>
      <td>26.115374</td>
      <td>9.008241</td>
      <td>2.983802</td>
      <td>15.373686</td>
      <td>19.380506</td>
      <td>18.755328</td>
      <td>14.492754</td>
      <td>4.489912</td>
      <td>0.511509</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 10 columns</p>
</div>



    * 데이터 전처리 끝..


```python
dfX = dfX.set_index('선수 이름')
```


```python
dfX = sm.add_constant(dfx)
dfz0 = pd.concat([dfX, dfy], axis=1)
dfz0  = dfz0.set_index('선수 이름')

dfz0
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
      <th>const</th>
      <th>FTA_PS</th>
      <th>MA_PS</th>
      <th>DA_PS</th>
      <th>LPS</th>
      <th>MPS</th>
      <th>SHORT_PS</th>
      <th>FPS</th>
      <th>SIDE_PS</th>
      <th>BPS</th>
      <th>KP</th>
    </tr>
    <tr>
      <th>선수 이름</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A. Taggart</th>
      <td>1.0</td>
      <td>6.997085</td>
      <td>9.102689</td>
      <td>0.388727</td>
      <td>0.550696</td>
      <td>3.401361</td>
      <td>12.536443</td>
      <td>3.919663</td>
      <td>6.770327</td>
      <td>5.798510</td>
      <td>0.907029</td>
    </tr>
    <tr>
      <th>Aleks</th>
      <td>1.0</td>
      <td>0.444884</td>
      <td>25.803262</td>
      <td>14.335146</td>
      <td>4.300544</td>
      <td>17.498764</td>
      <td>18.783984</td>
      <td>16.856154</td>
      <td>18.932279</td>
      <td>4.794859</td>
      <td>0.098863</td>
    </tr>
    <tr>
      <th>C. Melo</th>
      <td>1.0</td>
      <td>12.682482</td>
      <td>18.917275</td>
      <td>1.094891</td>
      <td>4.714112</td>
      <td>10.796837</td>
      <td>17.183698</td>
      <td>9.701946</td>
      <td>15.298054</td>
      <td>7.694647</td>
      <td>2.858881</td>
    </tr>
    <tr>
      <th>E. Bruno</th>
      <td>1.0</td>
      <td>7.182068</td>
      <td>9.652333</td>
      <td>1.143641</td>
      <td>1.189387</td>
      <td>3.522415</td>
      <td>13.266240</td>
      <td>4.757548</td>
      <td>7.136322</td>
      <td>6.084172</td>
      <td>1.646844</td>
    </tr>
    <tr>
      <th>M. Damasceno Santos da Cruz</th>
      <td>1.0</td>
      <td>11.909335</td>
      <td>12.831348</td>
      <td>0.845179</td>
      <td>0.883596</td>
      <td>5.109489</td>
      <td>19.592778</td>
      <td>5.416827</td>
      <td>10.065309</td>
      <td>10.103726</td>
      <td>1.690357</td>
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
    </tr>
    <tr>
      <th>한의권</th>
      <td>1.0</td>
      <td>11.700545</td>
      <td>8.577095</td>
      <td>0.793257</td>
      <td>0.545364</td>
      <td>4.214179</td>
      <td>16.311353</td>
      <td>4.263758</td>
      <td>7.486366</td>
      <td>9.320773</td>
      <td>1.239465</td>
    </tr>
    <tr>
      <th>홍정호</th>
      <td>1.0</td>
      <td>1.106719</td>
      <td>30.118577</td>
      <td>16.877470</td>
      <td>6.126482</td>
      <td>23.241107</td>
      <td>18.735178</td>
      <td>20.434783</td>
      <td>23.083004</td>
      <td>4.584980</td>
      <td>0.316206</td>
    </tr>
    <tr>
      <th>홍철</th>
      <td>1.0</td>
      <td>16.604938</td>
      <td>27.808642</td>
      <td>8.240741</td>
      <td>4.567901</td>
      <td>15.216049</td>
      <td>32.870370</td>
      <td>16.975309</td>
      <td>17.746914</td>
      <td>17.932099</td>
      <td>1.944444</td>
    </tr>
    <tr>
      <th>황순민</th>
      <td>1.0</td>
      <td>8.590953</td>
      <td>27.074520</td>
      <td>6.801171</td>
      <td>3.449398</td>
      <td>13.830133</td>
      <td>25.187114</td>
      <td>13.439636</td>
      <td>16.889034</td>
      <td>12.137976</td>
      <td>0.943703</td>
    </tr>
    <tr>
      <th>황현수</th>
      <td>1.0</td>
      <td>2.614379</td>
      <td>26.115374</td>
      <td>9.008241</td>
      <td>2.983802</td>
      <td>15.373686</td>
      <td>19.380506</td>
      <td>18.755328</td>
      <td>14.492754</td>
      <td>4.489912</td>
      <td>0.511509</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 11 columns</p>
</div>




```python
sns.pairplot(dfz0[['FTA_PS', 'KP']])
plt.show()

sns.regplot(x="FTA_PS", y="KP", data=dfz0)
```


<img width="361" alt="output_9_0" src="https://user-images.githubusercontent.com/59719711/82029782-6d57f180-96d2-11ea-966a-d7c8bc89b46a.png">




    <matplotlib.axes._subplots.AxesSubplot at 0x1a2ce4e8d0>




<img width="393" alt="output_9_2" src="https://user-images.githubusercontent.com/59719711/82029817-79dc4a00-96d2-11ea-99c6-2a0d19fa4b27.png">



```python
dfX
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
      <th>const</th>
      <th>선수 이름</th>
      <th>FTA_PS</th>
      <th>MA_PS</th>
      <th>DA_PS</th>
      <th>LPS</th>
      <th>MPS</th>
      <th>SHORT_PS</th>
      <th>FPS</th>
      <th>SIDE_PS</th>
      <th>BPS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>A. Taggart</td>
      <td>6.997085</td>
      <td>9.102689</td>
      <td>0.388727</td>
      <td>0.550696</td>
      <td>3.401361</td>
      <td>12.536443</td>
      <td>3.919663</td>
      <td>6.770327</td>
      <td>5.798510</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>Aleks</td>
      <td>0.444884</td>
      <td>25.803262</td>
      <td>14.335146</td>
      <td>4.300544</td>
      <td>17.498764</td>
      <td>18.783984</td>
      <td>16.856154</td>
      <td>18.932279</td>
      <td>4.794859</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>C. Melo</td>
      <td>12.682482</td>
      <td>18.917275</td>
      <td>1.094891</td>
      <td>4.714112</td>
      <td>10.796837</td>
      <td>17.183698</td>
      <td>9.701946</td>
      <td>15.298054</td>
      <td>7.694647</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>E. Bruno</td>
      <td>7.182068</td>
      <td>9.652333</td>
      <td>1.143641</td>
      <td>1.189387</td>
      <td>3.522415</td>
      <td>13.266240</td>
      <td>4.757548</td>
      <td>7.136322</td>
      <td>6.084172</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>M. Damasceno Santos da Cruz</td>
      <td>11.909335</td>
      <td>12.831348</td>
      <td>0.845179</td>
      <td>0.883596</td>
      <td>5.109489</td>
      <td>19.592778</td>
      <td>5.416827</td>
      <td>10.065309</td>
      <td>10.103726</td>
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
    </tr>
    <tr>
      <th>99</th>
      <td>1.0</td>
      <td>한의권</td>
      <td>11.700545</td>
      <td>8.577095</td>
      <td>0.793257</td>
      <td>0.545364</td>
      <td>4.214179</td>
      <td>16.311353</td>
      <td>4.263758</td>
      <td>7.486366</td>
      <td>9.320773</td>
    </tr>
    <tr>
      <th>100</th>
      <td>1.0</td>
      <td>홍정호</td>
      <td>1.106719</td>
      <td>30.118577</td>
      <td>16.877470</td>
      <td>6.126482</td>
      <td>23.241107</td>
      <td>18.735178</td>
      <td>20.434783</td>
      <td>23.083004</td>
      <td>4.584980</td>
    </tr>
    <tr>
      <th>101</th>
      <td>1.0</td>
      <td>홍철</td>
      <td>16.604938</td>
      <td>27.808642</td>
      <td>8.240741</td>
      <td>4.567901</td>
      <td>15.216049</td>
      <td>32.870370</td>
      <td>16.975309</td>
      <td>17.746914</td>
      <td>17.932099</td>
    </tr>
    <tr>
      <th>102</th>
      <td>1.0</td>
      <td>황순민</td>
      <td>8.590953</td>
      <td>27.074520</td>
      <td>6.801171</td>
      <td>3.449398</td>
      <td>13.830133</td>
      <td>25.187114</td>
      <td>13.439636</td>
      <td>16.889034</td>
      <td>12.137976</td>
    </tr>
    <tr>
      <th>103</th>
      <td>1.0</td>
      <td>황현수</td>
      <td>2.614379</td>
      <td>26.115374</td>
      <td>9.008241</td>
      <td>2.983802</td>
      <td>15.373686</td>
      <td>19.380506</td>
      <td>18.755328</td>
      <td>14.492754</td>
      <td>4.489912</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 11 columns</p>
</div>




```python
from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True).fit(dfX, dfy)
predicted = model.predict(dfX)
print(model.coef_ , model.intercept_)
plt.scatter(dfy, predicted, s=10)
plt.xlabel("Key Passes")
plt.ylabel("Predicted K.P")
plt.title("K.P 예측결과")
plt.show()
```

    [[ 0.          0.10882897 -0.01628515 -0.06078463  0.0427565   0.01455489
      -0.0255522   0.01466758  0.03398377 -0.01689216]] [0.5024628]



<img width="402" alt="output_11_1" src="https://user-images.githubusercontent.com/59719711/82029851-895b9300-96d2-11ea-9268-cd7823af80b2.png">



```python
model = sm.OLS.from_formula("KP ~ FTA_PS+MA_PS+DA_PS+LPS+MPS+SHORT_PS+FPS+SIDE_PS+BPS", data=dfz0)
# model = sm.OLS(dfy, dfX)
result = model.fit()
print(result.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                     KP   R-squared:                       0.804
    Model:                            OLS   Adj. R-squared:                  0.790
    Method:                 Least Squares   F-statistic:                     56.23
    Date:                Fri, 15 May 2020   Prob (F-statistic):           3.36e-31
    Time:                        17:29:57   Log-Likelihood:                -15.150
    No. Observations:                 104   AIC:                             46.30
    Df Residuals:                      96   BIC:                             67.45
    Df Model:                           7                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept      0.5025      0.113      4.456      0.000       0.279       0.726
    FTA_PS         0.1088      0.011      9.624      0.000       0.086       0.131
    MA_PS         -0.0163      0.006     -2.557      0.012      -0.029      -0.004
    DA_PS         -0.0608      0.008     -7.267      0.000      -0.077      -0.044
    LPS            0.0428      0.015      2.896      0.005       0.013       0.072
    MPS            0.0146      0.012      1.171      0.244      -0.010       0.039
    SHORT_PS      -0.0256      0.009     -2.767      0.007      -0.044      -0.007
    FPS            0.0147      0.010      1.513      0.133      -0.005       0.034
    SIDE_PS        0.0340      0.010      3.314      0.001       0.014       0.054
    BPS           -0.0169      0.014     -1.249      0.215      -0.044       0.010
    ==============================================================================
    Omnibus:                        2.841   Durbin-Watson:                   1.617
    Prob(Omnibus):                  0.242   Jarque-Bera (JB):                2.212
    Skew:                           0.293   Prob(JB):                        0.331
    Kurtosis:                       3.410   Cond. No.                     4.79e+16
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The smallest eigenvalue is 8.39e-29. This might indicate that there are
    strong multicollinearity problems or that the design matrix is singular.


    * 스케일링 작업


```python
feature_names = list(dfz.columns)
feature_names = ['scale({})'.format(name) for name in feature_names]
feature_names
model3 = sm.OLS.from_formula("KP ~ " + "+".join(feature_names), data=dfz0)
result3 = model3.fit()
print(result3.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                     KP   R-squared:                       1.000
    Model:                            OLS   Adj. R-squared:                  1.000
    Method:                 Least Squares   F-statistic:                 8.400e+30
    Date:                Fri, 15 May 2020   Prob (F-statistic):               0.00
    Time:                        17:30:00   Log-Likelihood:                 3474.2
    No. Observations:                 104   AIC:                            -6930.
    Df Residuals:                      95   BIC:                            -6907.
    Df Model:                           8                                         
    Covariance Type:            nonrobust                                         
    ===================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
    -----------------------------------------------------------------------------------
    Intercept           0.7871   7.71e-17   1.02e+16      0.000       0.787       0.787
    scale(FTA_PS)    1.665e-16   2.59e-16      0.644      0.521   -3.47e-16     6.8e-16
    scale(MA_PS)    -1.943e-16   9.74e-17     -1.995      0.049   -3.88e-16    -9.4e-19
    scale(DA_PS)     6.939e-18   1.84e-16      0.038      0.970   -3.58e-16    3.72e-16
    scale(LPS)       8.327e-17    1.2e-16      0.693      0.490   -1.55e-16    3.22e-16
    scale(MPS)       1.249e-16   2.11e-16      0.591      0.556   -2.94e-16    5.44e-16
    scale(SHORT_PS) -4.163e-17   1.73e-16     -0.240      0.811   -3.86e-16    3.02e-16
    scale(FPS)      -1.388e-17    1.5e-16     -0.092      0.927   -3.12e-16    2.85e-16
    scale(SIDE_PS)  -5.551e-17   1.65e-16     -0.336      0.738   -3.84e-16    2.73e-16
    scale(BPS)       1.943e-16   2.01e-16      0.969      0.335   -2.04e-16    5.92e-16
    scale(KP)           0.6321   1.74e-16   3.63e+15      0.000       0.632       0.632
    ==============================================================================
    Omnibus:                       10.601   Durbin-Watson:                   2.003
    Prob(Omnibus):                  0.005   Jarque-Bera (JB):                7.182
    Skew:                          -0.506   Prob(JB):                       0.0276
    Kurtosis:                       2.203   Cond. No.                     1.30e+16
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The smallest eigenvalue is 2.74e-30. This might indicate that there are
    strong multicollinearity problems or that the design matrix is singular.


    부분회귀 플롯으로 살펴본 FTA_PS 와 종속변수와의 상관관계
            1. 이 플롯의 가로축의 값은 독립변수 자체의 값이 아니라 어떤 독립변수에서 다른 독립변수의 영향을 제거한 일종의 '순수한 독립변수 성분'을 뜻함


```python
others = list(set(dfz.columns).difference(set(["KP", "FTA_PS"])))
p, resids = sm.graphics.plot_partregress(
    "KP", "FTA_PS", others, data=dfz, obs_labels=False, ret_coords=True
)
plt.show()
```


<img width="399" alt="output_16_0" src="https://user-images.githubusercontent.com/59719711/82029884-95dfeb80-96d2-11ea-96c6-6d56b6cf540a.png">


    sm.graphics.plot_partregress_grid 명령을 쓰면 전체 데이터에 대해 한번에 부분회귀 플롯을 그릴 수 있다.
    (전혀 상관이 없는거처럼 나왔네 아마도 데이터가 잘못된 상태일거야)


```python
fig = plt.figure(figsize=(10, 20))
sm.graphics.plot_partregress_grid(result, fig=fig)
fig.suptitle("")
plt.show()
```


<img width="707" alt="output_18_0" src="https://user-images.githubusercontent.com/59719711/82029915-a09a8080-96d2-11ea-964a-b72a5f441629.png">



```python
sm.graphics.plot_ccpr(result, "FTA_PS")
plt.show()
```

<img width="398" alt="output_19_0" src="https://user-images.githubusercontent.com/59719711/82029949-af813300-96d2-11ea-9818-0f2daad08bad.png">



```python
fig = plt.figure(figsize=(10,20))
sm.graphics.plot_ccpr_grid(result, fig=fig)
plt.show()
```


<img width="708" alt="output_20_0" src="https://user-images.githubusercontent.com/59719711/82029964-bad45e80-96d2-11ea-932d-bcceaf95588e.png">



```python
fig = plt.figure(figsize=(12,6))
sm.graphics.plot_regress_exog(result, 'FTA_PS', fig=fig)
plt.tight_layout(pad=4, h_pad=0.5, w_pad=0.5)
plt.show()
```


<img width="782" alt="output_21_0" src="https://user-images.githubusercontent.com/59719711/82030010-ccb60180-96d2-11ea-9e93-a52930d1d921.png">



```python
dfz1 = dfz0.reset_index(drop=True)
dfz1 = dfz1.reset_index()
dfz1.columns = ['PLAYERS','const','FTA_PS','MA_PS','DA_PS','LPS','MPS','SHORT_PS',	'FPS','SIDE_PS','BPS','KP']
dfz1
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
      <th>PLAYERS</th>
      <th>const</th>
      <th>FTA_PS</th>
      <th>MA_PS</th>
      <th>DA_PS</th>
      <th>LPS</th>
      <th>MPS</th>
      <th>SHORT_PS</th>
      <th>FPS</th>
      <th>SIDE_PS</th>
      <th>BPS</th>
      <th>KP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1.0</td>
      <td>6.997085</td>
      <td>9.102689</td>
      <td>0.388727</td>
      <td>0.550696</td>
      <td>3.401361</td>
      <td>12.536443</td>
      <td>3.919663</td>
      <td>6.770327</td>
      <td>5.798510</td>
      <td>0.907029</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1.0</td>
      <td>0.444884</td>
      <td>25.803262</td>
      <td>14.335146</td>
      <td>4.300544</td>
      <td>17.498764</td>
      <td>18.783984</td>
      <td>16.856154</td>
      <td>18.932279</td>
      <td>4.794859</td>
      <td>0.098863</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1.0</td>
      <td>12.682482</td>
      <td>18.917275</td>
      <td>1.094891</td>
      <td>4.714112</td>
      <td>10.796837</td>
      <td>17.183698</td>
      <td>9.701946</td>
      <td>15.298054</td>
      <td>7.694647</td>
      <td>2.858881</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1.0</td>
      <td>7.182068</td>
      <td>9.652333</td>
      <td>1.143641</td>
      <td>1.189387</td>
      <td>3.522415</td>
      <td>13.266240</td>
      <td>4.757548</td>
      <td>7.136322</td>
      <td>6.084172</td>
      <td>1.646844</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>1.0</td>
      <td>11.909335</td>
      <td>12.831348</td>
      <td>0.845179</td>
      <td>0.883596</td>
      <td>5.109489</td>
      <td>19.592778</td>
      <td>5.416827</td>
      <td>10.065309</td>
      <td>10.103726</td>
      <td>1.690357</td>
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
    </tr>
    <tr>
      <th>99</th>
      <td>99</td>
      <td>1.0</td>
      <td>11.700545</td>
      <td>8.577095</td>
      <td>0.793257</td>
      <td>0.545364</td>
      <td>4.214179</td>
      <td>16.311353</td>
      <td>4.263758</td>
      <td>7.486366</td>
      <td>9.320773</td>
      <td>1.239465</td>
    </tr>
    <tr>
      <th>100</th>
      <td>100</td>
      <td>1.0</td>
      <td>1.106719</td>
      <td>30.118577</td>
      <td>16.877470</td>
      <td>6.126482</td>
      <td>23.241107</td>
      <td>18.735178</td>
      <td>20.434783</td>
      <td>23.083004</td>
      <td>4.584980</td>
      <td>0.316206</td>
    </tr>
    <tr>
      <th>101</th>
      <td>101</td>
      <td>1.0</td>
      <td>16.604938</td>
      <td>27.808642</td>
      <td>8.240741</td>
      <td>4.567901</td>
      <td>15.216049</td>
      <td>32.870370</td>
      <td>16.975309</td>
      <td>17.746914</td>
      <td>17.932099</td>
      <td>1.944444</td>
    </tr>
    <tr>
      <th>102</th>
      <td>102</td>
      <td>1.0</td>
      <td>8.590953</td>
      <td>27.074520</td>
      <td>6.801171</td>
      <td>3.449398</td>
      <td>13.830133</td>
      <td>25.187114</td>
      <td>13.439636</td>
      <td>16.889034</td>
      <td>12.137976</td>
      <td>0.943703</td>
    </tr>
    <tr>
      <th>103</th>
      <td>103</td>
      <td>1.0</td>
      <td>2.614379</td>
      <td>26.115374</td>
      <td>9.008241</td>
      <td>2.983802</td>
      <td>15.373686</td>
      <td>19.380506</td>
      <td>18.755328</td>
      <td>14.492754</td>
      <td>4.489912</td>
      <td>0.511509</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 12 columns</p>
</div>




```python
model_category = sm.OLS.from_formula('KP ~ C(PLAYERS) + 0', dfz1).fit()
print(model_category.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                     KP   R-squared:                       1.000
    Model:                            OLS   Adj. R-squared:                    nan
    Method:                 Least Squares   F-statistic:                       nan
    Date:                Fri, 15 May 2020   Prob (F-statistic):                nan
    Time:                        17:31:27   Log-Likelihood:                    inf
    No. Observations:                 104   AIC:                              -inf
    Df Residuals:                       0   BIC:                              -inf
    Df Model:                         103                                         
    Covariance Type:            nonrobust                                         
    ===================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
    -----------------------------------------------------------------------------------
    C(PLAYERS)[0]       0.9070        nan        nan        nan         nan         nan
    C(PLAYERS)[1]       0.0989        nan        nan        nan         nan         nan
    C(PLAYERS)[2]       2.8589        nan        nan        nan         nan         nan
    C(PLAYERS)[3]       1.6468        nan        nan        nan         nan         nan
    C(PLAYERS)[4]       1.6904        nan        nan        nan         nan         nan
    C(PLAYERS)[5]       1.5765        nan        nan        nan         nan         nan
    C(PLAYERS)[6]       0.5366        nan        nan        nan         nan         nan
    C(PLAYERS)[7]       1.2879        nan        nan        nan         nan         nan
    C(PLAYERS)[8]       0.9104        nan        nan        nan         nan         nan
    C(PLAYERS)[9]       0.4872        nan        nan        nan         nan         nan
    C(PLAYERS)[10]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[11]      0.7013        nan        nan        nan         nan         nan
    C(PLAYERS)[12]      1.0230        nan        nan        nan         nan         nan
    C(PLAYERS)[13]      1.0710        nan        nan        nan         nan         nan
    C(PLAYERS)[14]      0.0608        nan        nan        nan         nan         nan
    C(PLAYERS)[15]      0.6717        nan        nan        nan         nan         nan
    C(PLAYERS)[16]      0.0628        nan        nan        nan         nan         nan
    C(PLAYERS)[17]      0.1082        nan        nan        nan         nan         nan
    C(PLAYERS)[18]      1.6010        nan        nan        nan         nan         nan
    C(PLAYERS)[19]      0.5337        nan        nan        nan         nan         nan
    C(PLAYERS)[20]      0.1904        nan        nan        nan         nan         nan
    C(PLAYERS)[21]      0.0775        nan        nan        nan         nan         nan
    C(PLAYERS)[22]      1.2965        nan        nan        nan         nan         nan
    C(PLAYERS)[23]      0.8130        nan        nan        nan         nan         nan
    C(PLAYERS)[24]      1.8854        nan        nan        nan         nan         nan
    C(PLAYERS)[25]      2.1829        nan        nan        nan         nan         nan
    C(PLAYERS)[26]      1.2417        nan        nan        nan         nan         nan
    C(PLAYERS)[27]      0.3139        nan        nan        nan         nan         nan
    C(PLAYERS)[28]      0.4444        nan        nan        nan         nan         nan
    C(PLAYERS)[29]      0.6825        nan        nan        nan         nan         nan
    C(PLAYERS)[30]      0.3040        nan        nan        nan         nan         nan
    C(PLAYERS)[31]      0.9569        nan        nan        nan         nan         nan
    C(PLAYERS)[32]      0.1307        nan        nan        nan         nan         nan
    C(PLAYERS)[33]      0.1493        nan        nan        nan         nan         nan
    C(PLAYERS)[34]      0.7005        nan        nan        nan         nan         nan
    C(PLAYERS)[35]      1.6603        nan        nan        nan         nan         nan
    C(PLAYERS)[36]      0.6917        nan        nan        nan         nan         nan
    C(PLAYERS)[37]      1.0335        nan        nan        nan         nan         nan
    C(PLAYERS)[38]      1.9589        nan        nan        nan         nan         nan
    C(PLAYERS)[39]      1.0721        nan        nan        nan         nan         nan
    C(PLAYERS)[40]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[41]      1.0757        nan        nan        nan         nan         nan
    C(PLAYERS)[42]      0.0632        nan        nan        nan         nan         nan
    C(PLAYERS)[43]      1.9376        nan        nan        nan         nan         nan
    C(PLAYERS)[44]      0.9946        nan        nan        nan         nan         nan
    C(PLAYERS)[45]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[46]      0.1062        nan        nan        nan         nan         nan
    C(PLAYERS)[47]      0.3660        nan        nan        nan         nan         nan
    C(PLAYERS)[48]      0.6584        nan        nan        nan         nan         nan
    C(PLAYERS)[49]      1.8886        nan        nan        nan         nan         nan
    C(PLAYERS)[50]      0.9237        nan        nan        nan         nan         nan
    C(PLAYERS)[51]      0.9758        nan        nan        nan         nan         nan
    C(PLAYERS)[52]      0.2336        nan        nan        nan         nan         nan
    C(PLAYERS)[53]      1.2715        nan        nan        nan         nan         nan
    C(PLAYERS)[54]      1.7718        nan        nan        nan         nan         nan
    C(PLAYERS)[55]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[56]      0.6342        nan        nan        nan         nan         nan
    C(PLAYERS)[57]      0.5669        nan        nan        nan         nan         nan
    C(PLAYERS)[58]      0.4771        nan        nan        nan         nan         nan
    C(PLAYERS)[59]      1.1311        nan        nan        nan         nan         nan
    C(PLAYERS)[60]      0.4095        nan        nan        nan         nan         nan
    C(PLAYERS)[61]      1.0849        nan        nan        nan         nan         nan
    C(PLAYERS)[62]      0.3330        nan        nan        nan         nan         nan
    C(PLAYERS)[63]      0.0914        nan        nan        nan         nan         nan
    C(PLAYERS)[64]      0.3334        nan        nan        nan         nan         nan
    C(PLAYERS)[65]      1.8844        nan        nan        nan         nan         nan
    C(PLAYERS)[66]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[67]      0.3669        nan        nan        nan         nan         nan
    C(PLAYERS)[68]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[69]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[70]      1.7517        nan        nan        nan         nan         nan
    C(PLAYERS)[71]      0.0925        nan        nan        nan         nan         nan
    C(PLAYERS)[72]      1.6155        nan        nan        nan         nan         nan
    C(PLAYERS)[73]      0.8716        nan        nan        nan         nan         nan
    C(PLAYERS)[74]      0.4621        nan        nan        nan         nan         nan
    C(PLAYERS)[75]      0.9886        nan        nan        nan         nan         nan
    C(PLAYERS)[76]      0.6920        nan        nan        nan         nan         nan
    C(PLAYERS)[77]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[78]      0.9017        nan        nan        nan         nan         nan
    C(PLAYERS)[79]      1.5005        nan        nan        nan         nan         nan
    C(PLAYERS)[80]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[81]      0.8477        nan        nan        nan         nan         nan
    C(PLAYERS)[82]      0.8485        nan        nan        nan         nan         nan
    C(PLAYERS)[83]      1.0993        nan        nan        nan         nan         nan
    C(PLAYERS)[84]      0.0962        nan        nan        nan         nan         nan
    C(PLAYERS)[85]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[86]      1.4854        nan        nan        nan         nan         nan
    C(PLAYERS)[87]      1.0064        nan        nan        nan         nan         nan
    C(PLAYERS)[88]      0.6310        nan        nan        nan         nan         nan
    C(PLAYERS)[89]      0.1633        nan        nan        nan         nan         nan
    C(PLAYERS)[90]      0.5721        nan        nan        nan         nan         nan
    C(PLAYERS)[91]           0        nan        nan        nan         nan         nan
    C(PLAYERS)[92]      0.9491        nan        nan        nan         nan         nan
    C(PLAYERS)[93]      1.1517        nan        nan        nan         nan         nan
    C(PLAYERS)[94]      0.1330        nan        nan        nan         nan         nan
    C(PLAYERS)[95]      1.7536        nan        nan        nan         nan         nan
    C(PLAYERS)[96]      1.3037        nan        nan        nan         nan         nan
    C(PLAYERS)[97]      0.0683        nan        nan        nan         nan         nan
    C(PLAYERS)[98]      0.7222        nan        nan        nan         nan         nan
    C(PLAYERS)[99]      1.2395        nan        nan        nan         nan         nan
    C(PLAYERS)[100]     0.3162        nan        nan        nan         nan         nan
    C(PLAYERS)[101]     1.9444        nan        nan        nan         nan         nan
    C(PLAYERS)[102]     0.9437        nan        nan        nan         nan         nan
    C(PLAYERS)[103]     0.5115        nan        nan        nan         nan         nan
    ==============================================================================
    Omnibus:                      506.990   Durbin-Watson:                     nan
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               39.000
    Skew:                           0.000   Prob(JB):                     3.40e-09
    Kurtosis:                       0.000   Cond. No.                         1.00
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


    /opt/anaconda3/lib/python3.7/site-packages/statsmodels/regression/linear_model.py:1698: RuntimeWarning: divide by zero encountered in true_divide
      return 1 - (np.divide(self.nobs - self.k_constant, self.df_resid)
    /opt/anaconda3/lib/python3.7/site-packages/statsmodels/regression/linear_model.py:1699: RuntimeWarning: invalid value encountered in double_scalars
      * (1 - self.rsquared))
    /opt/anaconda3/lib/python3.7/site-packages/statsmodels/regression/linear_model.py:889: RuntimeWarning: divide by zero encountered in log
      llf = -nobs2*np.log(2*np.pi) - nobs2*np.log(ssr / nobs) - nobs2
    /opt/anaconda3/lib/python3.7/site-packages/statsmodels/stats/stattools.py:46: RuntimeWarning: invalid value encountered in double_scalars
      dw = np.sum(diff_resids**2, axis=axis) / np.sum(resids**2, axis=axis)
    /opt/anaconda3/lib/python3.7/site-packages/statsmodels/regression/linear_model.py:1620: RuntimeWarning: invalid value encountered in double_scalars
      return np.dot(wresid, wresid) / self.df_resid
    /opt/anaconda3/lib/python3.7/site-packages/scipy/stats/_distn_infrastructure.py:903: RuntimeWarning: invalid value encountered in greater
      return (a < x) & (x < b)
    /opt/anaconda3/lib/python3.7/site-packages/scipy/stats/_distn_infrastructure.py:903: RuntimeWarning: invalid value encountered in less
      return (a < x) & (x < b)
    /opt/anaconda3/lib/python3.7/site-packages/scipy/stats/_distn_infrastructure.py:1912: RuntimeWarning: invalid value encountered in less_equal
      cond2 = cond0 & (x <= _a)



```python
print(model_category.t_test('C(PLAYERS)[2] = C(PLAYERS)[5]'))
```

                                 Test for Constraints                             
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    c0             1.2824        nan        nan        nan         nan         nan
    ==============================================================================


라운딩


```python
rooms = np.arange(3, 10)
labels = [str(r) for r in rooms[:-1]]
df_boston["CAT_RM"] = np.round(df_boston.RM)

sns.barplot(x="CAT_RM", y="MEDV", data=df_boston)
plt.show()
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
# 레버리지
plt.figure(figsize=(14,6))
plt.scatter(dfx['Passes in Final third Area Success'], dfy, s=30)
plt.xlabel('Passes in Final third Area Success')
plt.ylabel('Key Passes')
plt.title("서드지역과 키패스 회귀분석용 데이터")
plt.show()
```


<img width="836" alt="output_33_0" src="https://user-images.githubusercontent.com/59719711/82030071-e5beb280-96d2-11ea-8eee-8129ab46f304.png">



```python
xx = dfx['Passes in Final third Area Success']
xx1 = sm.add_constant(xx)
model = sm.OLS(dfy, xx1)
result = model.fit()
print(result.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:             Key Passes   R-squared:                       0.717
    Model:                            OLS   Adj. R-squared:                  0.714
    Method:                 Least Squares   F-statistic:                     258.1
    Date:                Fri, 15 May 2020   Prob (F-statistic):           1.06e-29
    Time:                        14:11:06   Log-Likelihood:                -381.17
    No. Observations:                 104   AIC:                             766.3
    Df Residuals:                     102   BIC:                             771.6
    Df Model:                           1                                         
    Covariance Type:            nonrobust                                         
    ======================================================================================================
                                             coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------------------------------
    const                                  2.1866      1.493      1.465      0.146      -0.775       5.148
    Passes in Final third Area Success     0.1012      0.006     16.067      0.000       0.089       0.114
    ==============================================================================
    Omnibus:                       44.976   Durbin-Watson:                   1.714
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):              191.518
    Skew:                           1.354   Prob(JB):                     2.58e-42
    Kurtosis:                       9.072   Cond. No.                         378.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
influence = result.get_influence()
hat = influence.hat_matrix_diag

plt.figure(figsize=(14,6))
plt. stem(hat)
plt.axhline(0.03, c = 'g', ls = '--') # c = color , ls = linestyle
plt.title('각 데이터의 레버리지 값')
plt.show()
```

    /opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:5: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the "use_line_collection" keyword argument to True.
      """



<img width="831" alt="output_35_1" src="https://user-images.githubusercontent.com/59719711/82030105-f111de00-96d2-11ea-9eea-bb0322998687.png">



```python
plt.figure(figsize=(14,6))
ax = plt.subplot()
plt.scatter(xx, dfy, s=30)
sm.graphics.abline_plot(model_results=result, ax=ax)

idx = hat >= 0.03
plt.scatter(xx[idx], dfy[idx], s=300, c="r", alpha=0.5)
plt.title("회귀분석 결과와 레버리지 포인트")
plt.show()
```


<img width="828" alt="output_36_0" src="https://user-images.githubusercontent.com/59719711/82030129-fa9b4600-96d2-11ea-8090-fd29c48b8373.png">



```python
# 아웃라이어
plt.figure(figsize=(14, 6))
plt.stem(result.resid)
plt.axhline(20, c='g', ls='--')
plt.axhline(-20, c='g', ls='--')
plt.title("각 데이터의 잔차")
plt.show()
```

    /opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:3: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the "use_line_collection" keyword argument to True.
      This is separate from the ipykernel package so we can avoid doing imports until



<img width="826" alt="output_37_1" src="https://user-images.githubusercontent.com/59719711/82030172-071f9e80-96d3-11ea-93c7-4a61e53477b0.png">



```python
plt.figure(figsize=(14,6))
sm.graphics.plot_leverage_resid2(result)
plt.show()

# sm.graphics.influence_plot(result)
# plt.show()
```


    <Figure size 1008x432 with 0 Axes>



<img width="404" alt="output_38_1" src="https://user-images.githubusercontent.com/59719711/82030192-0dae1600-96d3-11ea-851d-39ba05cdc451.png">


##### 학습데이터, 검증데이터 로 나누어 회귀분석


```python
dfz = dfz.reset_index(drop=True)
```


```python
N = len(dfz)
ratio = 0.7
np.random.seed(0)
idx_train = np.random.choice(np.arange(N), np.int(ratio * N))
idx_test = list(set(np.arange(N)).difference(idx_train))

df_train = dfz.iloc[idx_train]
df_test = dfz.iloc[idx_test]

df_train.shape, df_test.shape
```




    ((72, 10), (52, 10))



    학습용 데이터로 만든 회귀모형


```python
np.array(dfz.columns)
```




    array(['Passes in Final third Area Success', 'Middle Area Passes Success',
           'Passes in Defensive Area Success', 'Long Pass Success',
           'Medium Range Pass Success', 'Short Pass Success',
           'Forwards Pass Success', 'Sideways Pass Success',
           'Backwards Pass Success', 'Key Passes'], dtype=object)




```python
model = sm.OLS.from_formula("Key Passes ~ " + "+".join(np.array(dfz.columns)), data=df_train)
result = model.fit()
print(result.summary())
```


    Traceback (most recent call last):


      File "/opt/anaconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3331, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)


      File "<ipython-input-273-2edd23d21593>", line 1, in <module>
        model = sm.OLS.from_formula("Key Passes ~ " + "+".join(np.array(dfz.columns)), data=df_train)


      File "/opt/anaconda3/lib/python3.7/site-packages/statsmodels/base/model.py", line 169, in from_formula
        missing=missing)


      File "/opt/anaconda3/lib/python3.7/site-packages/statsmodels/formula/formulatools.py", line 65, in handle_formula_data
        NA_action=na_action)


      File "/opt/anaconda3/lib/python3.7/site-packages/patsy/highlevel.py", line 310, in dmatrices
        NA_action, return_type)


      File "/opt/anaconda3/lib/python3.7/site-packages/patsy/highlevel.py", line 165, in _do_highlevel_design
        NA_action)


      File "/opt/anaconda3/lib/python3.7/site-packages/patsy/highlevel.py", line 70, in _try_incr_builders
        NA_action)


      File "/opt/anaconda3/lib/python3.7/site-packages/patsy/build.py", line 689, in design_matrix_builders
        factor_states = _factors_memorize(all_factors, data_iter_maker, eval_env)


      File "/opt/anaconda3/lib/python3.7/site-packages/patsy/build.py", line 354, in _factors_memorize
        which_pass = factor.memorize_passes_needed(state, eval_env)


      File "/opt/anaconda3/lib/python3.7/site-packages/patsy/eval.py", line 474, in memorize_passes_needed
        subset_names = [name for name in ast_names(self.code)


      File "/opt/anaconda3/lib/python3.7/site-packages/patsy/eval.py", line 474, in <listcomp>
        subset_names = [name for name in ast_names(self.code)


      File "/opt/anaconda3/lib/python3.7/site-packages/patsy/eval.py", line 105, in ast_names
        for node in ast.walk(ast.parse(code)):


      File "/opt/anaconda3/lib/python3.7/ast.py", line 35, in parse
        return compile(source, filename, mode, PyCF_ONLY_AST)


      File "<unknown>", line 1
        Backwards Pass Success
                     ^
    SyntaxError: invalid syntax



    검증용 데이터의 회귀모형


```python
pred = result.predict(df_test)
pred

# rss = ((df_test['Key Passes'] - pred) ** 2).sum()
# tss = ((df_test['Key Passes'] - df_test['Key Passes'].mean())** 2).sum()
# rsquared = 1 - rss / tss
# rsquared
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-258-c56032d76bcc> in <module>
    ----> 1 pred = result.predict(df_test)
          2 pred
          3 
          4 # rss = ((df_test['Key Passes'] - pred) ** 2).sum()
          5 # tss = ((df_test['Key Passes'] - df_test['Key Passes'].mean())** 2).sum()


    /opt/anaconda3/lib/python3.7/site-packages/statsmodels/base/model.py in predict(self, exog, transform, *args, **kwargs)
       1098 
       1099         predict_results = self.model.predict(self.params, exog, *args,
    -> 1100                                              **kwargs)
       1101 
       1102         if exog_index is not None and not hasattr(predict_results,


    /opt/anaconda3/lib/python3.7/site-packages/statsmodels/regression/linear_model.py in predict(self, params, exog)
        378             exog = self.exog
        379 
    --> 380         return np.dot(exog, params)
        381 
        382     def get_distribution(self, params, scale, exog=None, dist_class=None):


    <__array_function__ internals> in dot(*args, **kwargs)


    ValueError: shapes (52,10) and (9,) not aligned: 10 (dim 1) != 9 (dim 0)



```python

```


```python
from sklearn.datasets import load_boston

boston = load_boston()
dfX = pd.DataFrame(boston.data, columns=boston.feature_names)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])
df = pd.concat([dfX, dfy], axis=1)

N = len(df)
ratio = 0.7
np.random.seed(0)
idx_train = np.random.choice(np.arange(N), np.int(ratio * N))
idx_test = list(set(np.arange(N)).difference(idx_train))

df_train = df.iloc[idx_train]
df_test = df.iloc[idx_test]
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
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
      <th>MEDV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>172</th>
      <td>0.13914</td>
      <td>0.0</td>
      <td>4.05</td>
      <td>0.0</td>
      <td>0.510</td>
      <td>5.572</td>
      <td>88.5</td>
      <td>2.5961</td>
      <td>5.0</td>
      <td>296.0</td>
      <td>16.6</td>
      <td>396.90</td>
      <td>14.69</td>
      <td>23.1</td>
    </tr>
    <tr>
      <th>47</th>
      <td>0.22927</td>
      <td>0.0</td>
      <td>6.91</td>
      <td>0.0</td>
      <td>0.448</td>
      <td>6.030</td>
      <td>85.5</td>
      <td>5.6894</td>
      <td>3.0</td>
      <td>233.0</td>
      <td>17.9</td>
      <td>392.74</td>
      <td>18.80</td>
      <td>16.6</td>
    </tr>
    <tr>
      <th>117</th>
      <td>0.15098</td>
      <td>0.0</td>
      <td>10.01</td>
      <td>0.0</td>
      <td>0.547</td>
      <td>6.021</td>
      <td>82.6</td>
      <td>2.7474</td>
      <td>6.0</td>
      <td>432.0</td>
      <td>17.8</td>
      <td>394.51</td>
      <td>10.30</td>
      <td>19.2</td>
    </tr>
    <tr>
      <th>192</th>
      <td>0.08664</td>
      <td>45.0</td>
      <td>3.44</td>
      <td>0.0</td>
      <td>0.437</td>
      <td>7.178</td>
      <td>26.3</td>
      <td>6.4798</td>
      <td>5.0</td>
      <td>398.0</td>
      <td>15.2</td>
      <td>390.49</td>
      <td>2.87</td>
      <td>36.4</td>
    </tr>
    <tr>
      <th>323</th>
      <td>0.28392</td>
      <td>0.0</td>
      <td>7.38</td>
      <td>0.0</td>
      <td>0.493</td>
      <td>5.708</td>
      <td>74.3</td>
      <td>4.7211</td>
      <td>5.0</td>
      <td>287.0</td>
      <td>19.6</td>
      <td>391.13</td>
      <td>11.74</td>
      <td>18.5</td>
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
    </tr>
    <tr>
      <th>80</th>
      <td>0.04113</td>
      <td>25.0</td>
      <td>4.86</td>
      <td>0.0</td>
      <td>0.426</td>
      <td>6.727</td>
      <td>33.5</td>
      <td>5.4007</td>
      <td>4.0</td>
      <td>281.0</td>
      <td>19.0</td>
      <td>396.90</td>
      <td>5.29</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>446</th>
      <td>6.28807</td>
      <td>0.0</td>
      <td>18.10</td>
      <td>0.0</td>
      <td>0.740</td>
      <td>6.341</td>
      <td>96.4</td>
      <td>2.0720</td>
      <td>24.0</td>
      <td>666.0</td>
      <td>20.2</td>
      <td>318.01</td>
      <td>17.79</td>
      <td>14.9</td>
    </tr>
    <tr>
      <th>136</th>
      <td>0.32264</td>
      <td>0.0</td>
      <td>21.89</td>
      <td>0.0</td>
      <td>0.624</td>
      <td>5.942</td>
      <td>93.5</td>
      <td>1.9669</td>
      <td>4.0</td>
      <td>437.0</td>
      <td>21.2</td>
      <td>378.25</td>
      <td>16.90</td>
      <td>17.4</td>
    </tr>
    <tr>
      <th>189</th>
      <td>0.08370</td>
      <td>45.0</td>
      <td>3.44</td>
      <td>0.0</td>
      <td>0.437</td>
      <td>7.185</td>
      <td>38.9</td>
      <td>4.5667</td>
      <td>5.0</td>
      <td>398.0</td>
      <td>15.2</td>
      <td>396.90</td>
      <td>5.39</td>
      <td>34.9</td>
    </tr>
    <tr>
      <th>129</th>
      <td>0.88125</td>
      <td>0.0</td>
      <td>21.89</td>
      <td>0.0</td>
      <td>0.624</td>
      <td>5.637</td>
      <td>94.7</td>
      <td>1.9799</td>
      <td>4.0</td>
      <td>437.0</td>
      <td>21.2</td>
      <td>396.90</td>
      <td>18.34</td>
      <td>14.3</td>
    </tr>
  </tbody>
</table>
<p>354 rows × 14 columns</p>
</div>




```python
model = sm.OLS.from_formula("MEDV ~ " + "+".join(boston.feature_names), data=df_train)
result = model.fit()
print(result.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                   MEDV   R-squared:                       0.757
    Model:                            OLS   Adj. R-squared:                  0.747
    Method:                 Least Squares   F-statistic:                     81.31
    Date:                Fri, 15 May 2020   Prob (F-statistic):           7.22e-96
    Time:                        14:46:05   Log-Likelihood:                -1057.6
    No. Observations:                 354   AIC:                             2143.
    Df Residuals:                     340   BIC:                             2197.
    Df Model:                          13                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept     40.6105      6.807      5.966      0.000      27.222      53.999
    CRIM          -0.0801      0.040     -2.012      0.045      -0.158      -0.002
    ZN             0.0438      0.016      2.777      0.006       0.013       0.075
    INDUS          0.0978      0.076      1.287      0.199      -0.052       0.247
    CHAS           2.7905      1.120      2.491      0.013       0.587       4.994
    NOX          -21.4614      4.919     -4.363      0.000     -31.136     -11.787
    RM             3.7948      0.532      7.128      0.000       2.748       4.842
    AGE            0.0006      0.016      0.036      0.971      -0.030       0.031
    DIS           -1.6910      0.256     -6.605      0.000      -2.195      -1.187
    RAD            0.2730      0.079      3.447      0.001       0.117       0.429
    TAX           -0.0097      0.004     -2.215      0.027      -0.018      -0.001
    PTRATIO       -1.1651      0.167     -6.983      0.000      -1.493      -0.837
    B              0.0134      0.004      3.815      0.000       0.006       0.020
    LSTAT         -0.5490      0.062     -8.908      0.000      -0.670      -0.428
    ==============================================================================
    Omnibus:                      129.426   Durbin-Watson:                   1.979
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):              603.605
    Skew:                           1.498   Prob(JB):                    8.49e-132
    Kurtosis:                       8.652   Cond. No.                     1.64e+04
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 1.64e+04. This might indicate that there are
    strong multicollinearity or other numerical problems.



```python
pred = result.predict(df_test)

rss = ((df_test.MEDV - pred) ** 2).sum()
tss = ((df_test.MEDV - df_test.MEDV.mean())** 2).sum()
rsquared = 1 - rss / tss
rsquared
```




    0.688373412498711




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
