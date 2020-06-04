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
df = pd.read_csv('/Users/wglee/Desktop/k1.csv').groupby('선수 이름').sum()
df1 = pd.read_csv('/Users/wglee/Desktop/k2.csv').groupby('선수 이름').sum()
df['league'], df1['league'] = '0', '1'
df['Game played'] = round(df['Time played'] / 90,2)
df1['Game played'] = round(df1['Time played'] / 90,2)
is_time = df['Game played'] >= 20
is_time2 = df1['Game played'] >= 20
df = df[is_time]
df1 = df1[is_time2]
del df['Time played']
del df1['Time played']
    
df[['Goal', 'Assists', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target','Shots inside PA', 'Shots outside of PA', 'Offsides', 'Freekicks',\
    'Corners', 'Throw-Ins', 'Take-ons Success', 'Take-ons Total', 'Passes Success', 'Passes Total', 'Pass Accuracy(%)', 'Key Passes',\
    'Passes in Final third Area Success', 'PassesinFinalthirdArea Total','Middle Area Passes Success', 'MiddleAreaPasses Total',\
    'Passes in Defensive Area Success', 'PassesinDefensiveArea Total','Long Pass Success', 'LongPass Total', 'Medium Range Pass Success',\
    'MediumRangePass Total', 'Short Pass Success', 'ShortPass Total','Forwards Pass Success', 'ForwardsPass Total', \
    'Sideways Pass Success','SidewaysPass Total', 'Backwards Pass Success', 'BackwardsPass Total','Crosses Success', 'Crosses Total', \
    'Control under pressure','Tackles Success', 'Tackles Total', 'Aerial Duels Success','AerialDuels Total', 'Ground Duels Success', \
    'GroundDuels Total','Interceptions', 'Clearances', 'Cut-off', 'Recovery', 'Blocks','Mistakes', 'Fouls', 'Fouls Won', 'Yellow Cards',\
    'Red Cards']] = \
round(df[['Goal', 'Assists', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target', 'Shots inside PA', 'Shots outside of PA', 'Offsides', \
          'Freekicks','Corners', 'Throw-Ins', 'Take-ons Success', 'Take-ons Total','Passes Success', 'Passes Total', 'Pass Accuracy(%)', \
          'Key Passes','Passes in Final third Area Success', 'PassesinFinalthirdArea Total','Middle Area Passes Success', \
          'MiddleAreaPasses Total','Passes in Defensive Area Success', 'PassesinDefensiveArea Total','Long Pass Success', 'LongPass Total', \
          'Medium Range Pass Success','MediumRangePass Total', 'Short Pass Success', 'ShortPass Total','Forwards Pass Success', \
          'ForwardsPass Total', 'Sideways Pass Success','SidewaysPass Total', 'Backwards Pass Success', 'BackwardsPass Total',\
          'Crosses Success', 'Crosses Total', 'Control under pressure','Tackles Success', 'Tackles Total', 'Aerial Duels Success',\
          'AerialDuels Total', 'Ground Duels Success', 'GroundDuels Total','Interceptions', 'Clearances', 'Cut-off', 'Recovery', 'Blocks',\
          'Mistakes', 'Fouls', 'Fouls Won', 'Yellow Cards', 'Red Cards']].div(df['Game played'], axis=0),2)


df1[['Goal', 'Assists', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target','Shots inside PA', 'Shots outside of PA', 'Offsides', 'Freekicks',\
    'Corners', 'Throw-Ins', 'Take-ons Success', 'Take-ons Total', 'Passes Success', 'Passes Total', 'Pass Accuracy(%)', 'Key Passes',\
    'Passes in Final third Area Success', 'PassesinFinalthirdArea Total','Middle Area Passes Success', 'MiddleAreaPasses Total',\
    'Passes in Defensive Area Success', 'PassesinDefensiveArea Total','Long Pass Success', 'LongPass Total', 'Medium Range Pass Success',\
    'MediumRangePass Total', 'Short Pass Success', 'ShortPass Total','Forwards Pass Success', 'ForwardsPass Total', \
    'Sideways Pass Success','SidewaysPass Total', 'Backwards Pass Success', 'BackwardsPass Total','Crosses Success', 'Crosses Total', \
    'Control under pressure','Tackles Success', 'Tackles Total', 'Aerial Duels Success','AerialDuels Total', 'Ground Duels Success', \
    'GroundDuels Total','Interceptions', 'Clearances', 'Cut-off', 'Recovery', 'Blocks','Mistakes', 'Fouls', 'Fouls Won', 'Yellow Cards',\
    'Red Cards']] = \
round(df1[['Goal', 'Assists', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target', 'Shots inside PA', 'Shots outside of PA', 'Offsides', \
          'Freekicks','Corners', 'Throw-Ins', 'Take-ons Success', 'Take-ons Total','Passes Success', 'Passes Total', 'Pass Accuracy(%)', \
          'Key Passes','Passes in Final third Area Success', 'PassesinFinalthirdArea Total','Middle Area Passes Success', \
          'MiddleAreaPasses Total','Passes in Defensive Area Success', 'PassesinDefensiveArea Total','Long Pass Success', 'LongPass Total', \
          'Medium Range Pass Success','MediumRangePass Total', 'Short Pass Success', 'ShortPass Total','Forwards Pass Success', \
          'ForwardsPass Total', 'Sideways Pass Success','SidewaysPass Total', 'Backwards Pass Success', 'BackwardsPass Total',\
          'Crosses Success', 'Crosses Total', 'Control under pressure','Tackles Success', 'Tackles Total', 'Aerial Duels Success',\
          'AerialDuels Total', 'Ground Duels Success', 'GroundDuels Total','Interceptions', 'Clearances', 'Cut-off', 'Recovery', 'Blocks',\
          'Mistakes', 'Fouls', 'Fouls Won', 'Yellow Cards', 'Red Cards']].div(df1['Game played'], axis=0),2)
```


```python
is_atk = df['Goal'] >= 0.35
df = df[is_atk]
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
      <th>Cut-off</th>
      <th>Recovery</th>
      <th>Blocks</th>
      <th>Mistakes</th>
      <th>Fouls</th>
      <th>Fouls Won</th>
      <th>Yellow Cards</th>
      <th>Red Cards</th>
      <th>league</th>
      <th>Game played</th>
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
      <td>0.68</td>
      <td>0.06</td>
      <td>3.69</td>
      <td>1.30</td>
      <td>0.97</td>
      <td>1.33</td>
      <td>2.40</td>
      <td>1.30</td>
      <td>0.58</td>
      <td>0.06</td>
      <td>...</td>
      <td>0.81</td>
      <td>4.15</td>
      <td>0.00</td>
      <td>1.30</td>
      <td>2.17</td>
      <td>1.33</td>
      <td>0.10</td>
      <td>0.0</td>
      <td>0</td>
      <td>30.87</td>
    </tr>
    <tr>
      <th>C. Melo</th>
      <td>0.46</td>
      <td>0.30</td>
      <td>5.02</td>
      <td>1.95</td>
      <td>1.28</td>
      <td>1.64</td>
      <td>1.64</td>
      <td>3.38</td>
      <td>0.12</td>
      <td>5.44</td>
      <td>...</td>
      <td>1.46</td>
      <td>5.54</td>
      <td>0.06</td>
      <td>1.58</td>
      <td>1.13</td>
      <td>3.77</td>
      <td>0.12</td>
      <td>0.0</td>
      <td>0</td>
      <td>32.88</td>
    </tr>
    <tr>
      <th>E. Bruno</th>
      <td>0.50</td>
      <td>0.18</td>
      <td>3.61</td>
      <td>1.33</td>
      <td>0.46</td>
      <td>1.74</td>
      <td>2.93</td>
      <td>0.69</td>
      <td>0.55</td>
      <td>0.00</td>
      <td>...</td>
      <td>1.46</td>
      <td>3.71</td>
      <td>0.09</td>
      <td>1.24</td>
      <td>2.01</td>
      <td>1.56</td>
      <td>0.18</td>
      <td>0.0</td>
      <td>0</td>
      <td>21.86</td>
    </tr>
    <tr>
      <th>O. Aanderson</th>
      <td>0.41</td>
      <td>0.19</td>
      <td>2.69</td>
      <td>1.01</td>
      <td>0.57</td>
      <td>1.09</td>
      <td>1.39</td>
      <td>1.30</td>
      <td>0.24</td>
      <td>1.79</td>
      <td>...</td>
      <td>4.00</td>
      <td>6.09</td>
      <td>0.14</td>
      <td>1.41</td>
      <td>1.36</td>
      <td>2.26</td>
      <td>0.05</td>
      <td>0.0</td>
      <td>0</td>
      <td>36.79</td>
    </tr>
    <tr>
      <th>S. Mugoša</th>
      <td>0.49</td>
      <td>0.14</td>
      <td>3.85</td>
      <td>1.23</td>
      <td>1.09</td>
      <td>1.54</td>
      <td>2.28</td>
      <td>1.58</td>
      <td>0.42</td>
      <td>0.63</td>
      <td>...</td>
      <td>0.88</td>
      <td>3.89</td>
      <td>0.14</td>
      <td>0.56</td>
      <td>0.95</td>
      <td>2.07</td>
      <td>0.07</td>
      <td>0.0</td>
      <td>0</td>
      <td>28.56</td>
    </tr>
    <tr>
      <th>U. Đerić</th>
      <td>0.61</td>
      <td>0.04</td>
      <td>3.00</td>
      <td>1.18</td>
      <td>0.53</td>
      <td>1.26</td>
      <td>2.31</td>
      <td>0.69</td>
      <td>0.28</td>
      <td>0.00</td>
      <td>...</td>
      <td>1.87</td>
      <td>3.45</td>
      <td>0.20</td>
      <td>1.06</td>
      <td>1.71</td>
      <td>1.10</td>
      <td>0.08</td>
      <td>0.0</td>
      <td>0</td>
      <td>24.63</td>
    </tr>
    <tr>
      <th>김보경</th>
      <td>0.40</td>
      <td>0.25</td>
      <td>1.31</td>
      <td>0.62</td>
      <td>0.29</td>
      <td>0.40</td>
      <td>0.94</td>
      <td>0.36</td>
      <td>0.07</td>
      <td>0.69</td>
      <td>...</td>
      <td>2.83</td>
      <td>7.40</td>
      <td>0.11</td>
      <td>1.27</td>
      <td>1.31</td>
      <td>1.60</td>
      <td>0.18</td>
      <td>0.0</td>
      <td>0</td>
      <td>27.58</td>
    </tr>
    <tr>
      <th>김인성</th>
      <td>0.35</td>
      <td>0.13</td>
      <td>2.04</td>
      <td>0.87</td>
      <td>0.57</td>
      <td>0.61</td>
      <td>1.57</td>
      <td>0.48</td>
      <td>0.65</td>
      <td>0.04</td>
      <td>...</td>
      <td>3.96</td>
      <td>7.35</td>
      <td>0.09</td>
      <td>0.65</td>
      <td>1.57</td>
      <td>1.30</td>
      <td>0.13</td>
      <td>0.0</td>
      <td>0</td>
      <td>22.99</td>
    </tr>
    <tr>
      <th>문선민</th>
      <td>0.47</td>
      <td>0.43</td>
      <td>2.79</td>
      <td>1.13</td>
      <td>0.80</td>
      <td>0.85</td>
      <td>2.17</td>
      <td>0.61</td>
      <td>0.14</td>
      <td>0.09</td>
      <td>...</td>
      <td>1.18</td>
      <td>5.20</td>
      <td>0.00</td>
      <td>0.99</td>
      <td>1.51</td>
      <td>1.47</td>
      <td>0.05</td>
      <td>0.0</td>
      <td>0</td>
      <td>21.16</td>
    </tr>
    <tr>
      <th>박용지</th>
      <td>0.44</td>
      <td>0.11</td>
      <td>1.98</td>
      <td>0.80</td>
      <td>0.66</td>
      <td>0.51</td>
      <td>1.39</td>
      <td>0.59</td>
      <td>0.33</td>
      <td>0.00</td>
      <td>...</td>
      <td>1.43</td>
      <td>3.33</td>
      <td>0.15</td>
      <td>1.17</td>
      <td>1.54</td>
      <td>2.45</td>
      <td>0.07</td>
      <td>0.0</td>
      <td>0</td>
      <td>27.34</td>
    </tr>
    <tr>
      <th>박주영</th>
      <td>0.38</td>
      <td>0.22</td>
      <td>1.98</td>
      <td>0.83</td>
      <td>0.61</td>
      <td>0.54</td>
      <td>0.93</td>
      <td>1.06</td>
      <td>0.54</td>
      <td>3.01</td>
      <td>...</td>
      <td>1.41</td>
      <td>4.23</td>
      <td>0.19</td>
      <td>0.77</td>
      <td>1.22</td>
      <td>1.41</td>
      <td>0.06</td>
      <td>0.0</td>
      <td>0</td>
      <td>31.24</td>
    </tr>
    <tr>
      <th>염기훈</th>
      <td>0.42</td>
      <td>0.17</td>
      <td>2.01</td>
      <td>0.84</td>
      <td>0.54</td>
      <td>0.59</td>
      <td>0.67</td>
      <td>1.34</td>
      <td>0.00</td>
      <td>2.09</td>
      <td>...</td>
      <td>1.88</td>
      <td>7.08</td>
      <td>0.17</td>
      <td>0.84</td>
      <td>0.46</td>
      <td>2.05</td>
      <td>0.04</td>
      <td>0.0</td>
      <td>0</td>
      <td>23.88</td>
    </tr>
    <tr>
      <th>윤일록</th>
      <td>0.35</td>
      <td>0.16</td>
      <td>2.47</td>
      <td>1.27</td>
      <td>0.67</td>
      <td>0.54</td>
      <td>1.55</td>
      <td>0.92</td>
      <td>0.22</td>
      <td>0.16</td>
      <td>...</td>
      <td>2.76</td>
      <td>8.71</td>
      <td>0.00</td>
      <td>1.33</td>
      <td>1.87</td>
      <td>1.33</td>
      <td>0.13</td>
      <td>0.0</td>
      <td>0</td>
      <td>31.57</td>
    </tr>
    <tr>
      <th>이영재</th>
      <td>0.39</td>
      <td>0.29</td>
      <td>2.57</td>
      <td>1.11</td>
      <td>0.53</td>
      <td>0.82</td>
      <td>0.77</td>
      <td>1.79</td>
      <td>0.10</td>
      <td>2.37</td>
      <td>...</td>
      <td>2.95</td>
      <td>8.13</td>
      <td>0.15</td>
      <td>0.92</td>
      <td>0.92</td>
      <td>1.94</td>
      <td>0.05</td>
      <td>0.0</td>
      <td>0</td>
      <td>20.66</td>
    </tr>
    <tr>
      <th>주니오</th>
      <td>0.72</td>
      <td>0.19</td>
      <td>3.87</td>
      <td>1.63</td>
      <td>1.18</td>
      <td>1.03</td>
      <td>2.85</td>
      <td>1.03</td>
      <td>0.76</td>
      <td>0.15</td>
      <td>...</td>
      <td>1.78</td>
      <td>3.49</td>
      <td>0.11</td>
      <td>1.25</td>
      <td>1.75</td>
      <td>0.87</td>
      <td>0.08</td>
      <td>0.0</td>
      <td>0</td>
      <td>26.34</td>
    </tr>
    <tr>
      <th>페시치</th>
      <td>0.48</td>
      <td>0.10</td>
      <td>2.66</td>
      <td>1.26</td>
      <td>0.53</td>
      <td>0.87</td>
      <td>2.17</td>
      <td>0.48</td>
      <td>0.82</td>
      <td>0.10</td>
      <td>...</td>
      <td>0.77</td>
      <td>3.72</td>
      <td>0.05</td>
      <td>1.50</td>
      <td>1.26</td>
      <td>1.55</td>
      <td>0.05</td>
      <td>0.0</td>
      <td>0</td>
      <td>20.71</td>
    </tr>
  </tbody>
</table>
<p>16 rows × 57 columns</p>
</div>



###### K리그1 내 경기당 득점 0.35 이상의 선수에 대한 공격, 패스, 수비, 기여도, 실수 index 추출


```python
df_atk = df[['Goal', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target', 'Shots inside PA', 'Shots outside of PA', 'Freekicks']]
df_atk[['Goal', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target', 'Shots inside PA', 'Shots outside of PA', 'Freekicks']] *= 1.79
df_atk

df_dist = df[['Assists', 'Key Passes', 'Passes Success', 'Passes in Final third Area Success', 'Forwards Pass Success', 'Crosses Success']]
df_dist[['Assists', 'Key Passes', 'Passes Success', 'Passes in Final third Area Success', 'Forwards Pass Success', 'Crosses Success']] *= 3.78
df_dist

df_def = df[['Tackles Success', 'Interceptions', 'Clearances', 'Blocks']]
df_def[['Tackles Success', 'Interceptions', 'Clearances', 'Blocks']] * 4.67
df_def

df_cont = df[['Take-ons Success', 'Control under pressure', 'Aerial Duels Success', 'Ground Duels Success']]
df_cont[['Take-ons Success', 'Control under pressure', 'Aerial Duels Success', 'Ground Duels Success']] *= 3.86
df_cont

df_mis = df[['Mistakes', 'Yellow Cards', 'Red Cards', 'Fouls']]
df_mis[['Mistakes', 'Yellow Cards', 'Red Cards', 'Fouls']] *= 1.67

a = pd.concat([df_atk, df_dist], axis=1)
b = pd.concat([a, df_def], axis=1)
c = pd.concat([b, df_cont], axis=1)
d = pd.concat([c, df_mis], axis=1)
d['league'] = 0
d
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
      <th>Shots</th>
      <th>SoT</th>
      <th>Blocked Shots</th>
      <th>Shots off Target</th>
      <th>Shots inside PA</th>
      <th>Shots outside of PA</th>
      <th>Freekicks</th>
      <th>Assists</th>
      <th>Key Passes</th>
      <th>...</th>
      <th>Blocks</th>
      <th>Take-ons Success</th>
      <th>Control under pressure</th>
      <th>Aerial Duels Success</th>
      <th>Ground Duels Success</th>
      <th>Mistakes</th>
      <th>Yellow Cards</th>
      <th>Red Cards</th>
      <th>Fouls</th>
      <th>league</th>
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
      <td>1.2172</td>
      <td>6.6051</td>
      <td>2.3270</td>
      <td>1.7363</td>
      <td>2.3807</td>
      <td>4.2960</td>
      <td>2.3270</td>
      <td>0.1074</td>
      <td>0.2268</td>
      <td>3.4398</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.7334</td>
      <td>0.0000</td>
      <td>8.1446</td>
      <td>2.7406</td>
      <td>2.1710</td>
      <td>0.1670</td>
      <td>0.0</td>
      <td>3.6239</td>
      <td>0</td>
    </tr>
    <tr>
      <th>C. Melo</th>
      <td>0.8234</td>
      <td>8.9858</td>
      <td>3.4905</td>
      <td>2.2912</td>
      <td>2.9356</td>
      <td>2.9356</td>
      <td>6.0502</td>
      <td>9.7376</td>
      <td>1.1340</td>
      <td>10.8108</td>
      <td>...</td>
      <td>0.06</td>
      <td>2.0072</td>
      <td>0.6948</td>
      <td>2.4704</td>
      <td>5.0566</td>
      <td>2.6386</td>
      <td>0.2004</td>
      <td>0.0</td>
      <td>1.8871</td>
      <td>0</td>
    </tr>
    <tr>
      <th>E. Bruno</th>
      <td>0.8950</td>
      <td>6.4619</td>
      <td>2.3807</td>
      <td>0.8234</td>
      <td>3.1146</td>
      <td>5.2447</td>
      <td>1.2351</td>
      <td>0.0000</td>
      <td>0.6804</td>
      <td>6.2370</td>
      <td>...</td>
      <td>0.09</td>
      <td>0.8878</td>
      <td>0.5404</td>
      <td>33.8908</td>
      <td>3.3582</td>
      <td>2.0708</td>
      <td>0.3006</td>
      <td>0.0</td>
      <td>3.3567</td>
      <td>0</td>
    </tr>
    <tr>
      <th>O. Aanderson</th>
      <td>0.7339</td>
      <td>4.8151</td>
      <td>1.8079</td>
      <td>1.0203</td>
      <td>1.9511</td>
      <td>2.4881</td>
      <td>2.3270</td>
      <td>3.2041</td>
      <td>0.7182</td>
      <td>5.9724</td>
      <td>...</td>
      <td>0.14</td>
      <td>2.2002</td>
      <td>0.5404</td>
      <td>4.9408</td>
      <td>9.7658</td>
      <td>2.3547</td>
      <td>0.0835</td>
      <td>0.0</td>
      <td>2.2712</td>
      <td>0</td>
    </tr>
    <tr>
      <th>S. Mugoša</th>
      <td>0.8771</td>
      <td>6.8915</td>
      <td>2.2017</td>
      <td>1.9511</td>
      <td>2.7566</td>
      <td>4.0812</td>
      <td>2.8282</td>
      <td>1.1277</td>
      <td>0.5292</td>
      <td>3.4398</td>
      <td>...</td>
      <td>0.14</td>
      <td>0.9650</td>
      <td>0.4246</td>
      <td>11.2326</td>
      <td>2.1616</td>
      <td>0.9352</td>
      <td>0.1169</td>
      <td>0.0</td>
      <td>1.5865</td>
      <td>0</td>
    </tr>
    <tr>
      <th>U. Đerić</th>
      <td>1.0919</td>
      <td>5.3700</td>
      <td>2.1122</td>
      <td>0.9487</td>
      <td>2.2554</td>
      <td>4.1349</td>
      <td>1.2351</td>
      <td>0.0000</td>
      <td>0.1512</td>
      <td>1.8522</td>
      <td>...</td>
      <td>0.20</td>
      <td>0.1544</td>
      <td>0.4632</td>
      <td>22.0792</td>
      <td>2.0458</td>
      <td>1.7702</td>
      <td>0.1336</td>
      <td>0.0</td>
      <td>2.8557</td>
      <td>0</td>
    </tr>
    <tr>
      <th>김보경</th>
      <td>0.7160</td>
      <td>2.3449</td>
      <td>1.1098</td>
      <td>0.5191</td>
      <td>0.7160</td>
      <td>1.6826</td>
      <td>0.6444</td>
      <td>1.2351</td>
      <td>0.9450</td>
      <td>7.1442</td>
      <td>...</td>
      <td>0.11</td>
      <td>0.9650</td>
      <td>0.2702</td>
      <td>2.3932</td>
      <td>6.5620</td>
      <td>2.1209</td>
      <td>0.3006</td>
      <td>0.0</td>
      <td>2.1877</td>
      <td>0</td>
    </tr>
    <tr>
      <th>김인성</th>
      <td>0.6265</td>
      <td>3.6516</td>
      <td>1.5573</td>
      <td>1.0203</td>
      <td>1.0919</td>
      <td>2.8103</td>
      <td>0.8592</td>
      <td>0.0716</td>
      <td>0.4914</td>
      <td>3.6288</td>
      <td>...</td>
      <td>0.09</td>
      <td>0.5018</td>
      <td>0.0000</td>
      <td>3.8600</td>
      <td>8.3762</td>
      <td>1.0855</td>
      <td>0.2171</td>
      <td>0.0</td>
      <td>2.6219</td>
      <td>0</td>
    </tr>
    <tr>
      <th>문선민</th>
      <td>0.8413</td>
      <td>4.9941</td>
      <td>2.0227</td>
      <td>1.4320</td>
      <td>1.5215</td>
      <td>3.8843</td>
      <td>1.0919</td>
      <td>0.1611</td>
      <td>1.6254</td>
      <td>7.3332</td>
      <td>...</td>
      <td>0.00</td>
      <td>2.0072</td>
      <td>0.9264</td>
      <td>2.5476</td>
      <td>2.5476</td>
      <td>1.6533</td>
      <td>0.0835</td>
      <td>0.0</td>
      <td>2.5217</td>
      <td>0</td>
    </tr>
    <tr>
      <th>박용지</th>
      <td>0.7876</td>
      <td>3.5442</td>
      <td>1.4320</td>
      <td>1.1814</td>
      <td>0.9129</td>
      <td>2.4881</td>
      <td>1.0561</td>
      <td>0.0000</td>
      <td>0.4158</td>
      <td>2.4948</td>
      <td>...</td>
      <td>0.15</td>
      <td>1.6984</td>
      <td>0.2702</td>
      <td>5.5198</td>
      <td>2.8178</td>
      <td>1.9539</td>
      <td>0.1169</td>
      <td>0.0</td>
      <td>2.5718</td>
      <td>0</td>
    </tr>
    <tr>
      <th>박주영</th>
      <td>0.6802</td>
      <td>3.5442</td>
      <td>1.4857</td>
      <td>1.0919</td>
      <td>0.9666</td>
      <td>1.6647</td>
      <td>1.8974</td>
      <td>5.3879</td>
      <td>0.8316</td>
      <td>7.1442</td>
      <td>...</td>
      <td>0.19</td>
      <td>0.2316</td>
      <td>0.1158</td>
      <td>16.9454</td>
      <td>3.9372</td>
      <td>1.2859</td>
      <td>0.1002</td>
      <td>0.0</td>
      <td>2.0374</td>
      <td>0</td>
    </tr>
    <tr>
      <th>염기훈</th>
      <td>0.7518</td>
      <td>3.5979</td>
      <td>1.5036</td>
      <td>0.9666</td>
      <td>1.0561</td>
      <td>1.1993</td>
      <td>2.3986</td>
      <td>3.7411</td>
      <td>0.6426</td>
      <td>7.1064</td>
      <td>...</td>
      <td>0.17</td>
      <td>0.3088</td>
      <td>1.3124</td>
      <td>17.2928</td>
      <td>6.7936</td>
      <td>1.4028</td>
      <td>0.0668</td>
      <td>0.0</td>
      <td>0.7682</td>
      <td>0</td>
    </tr>
    <tr>
      <th>윤일록</th>
      <td>0.6265</td>
      <td>4.4213</td>
      <td>2.2733</td>
      <td>1.1993</td>
      <td>0.9666</td>
      <td>2.7745</td>
      <td>1.6468</td>
      <td>0.2864</td>
      <td>0.6048</td>
      <td>6.1236</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.7334</td>
      <td>0.0000</td>
      <td>3.7828</td>
      <td>5.7514</td>
      <td>2.2211</td>
      <td>0.2171</td>
      <td>0.0</td>
      <td>3.1229</td>
      <td>0</td>
    </tr>
    <tr>
      <th>이영재</th>
      <td>0.6981</td>
      <td>4.6003</td>
      <td>1.9869</td>
      <td>0.9487</td>
      <td>1.4678</td>
      <td>1.3783</td>
      <td>3.2041</td>
      <td>4.2423</td>
      <td>1.0962</td>
      <td>5.6700</td>
      <td>...</td>
      <td>0.15</td>
      <td>0.9264</td>
      <td>0.1930</td>
      <td>3.3582</td>
      <td>3.3582</td>
      <td>1.5364</td>
      <td>0.0835</td>
      <td>0.0</td>
      <td>1.5364</td>
      <td>0</td>
    </tr>
    <tr>
      <th>주니오</th>
      <td>1.2888</td>
      <td>6.9273</td>
      <td>2.9177</td>
      <td>2.1122</td>
      <td>1.8437</td>
      <td>5.1015</td>
      <td>1.8437</td>
      <td>0.2685</td>
      <td>0.7182</td>
      <td>3.5910</td>
      <td>...</td>
      <td>0.11</td>
      <td>0.7334</td>
      <td>0.0000</td>
      <td>10.1132</td>
      <td>2.7792</td>
      <td>2.0875</td>
      <td>0.1336</td>
      <td>0.0</td>
      <td>2.9225</td>
      <td>0</td>
    </tr>
    <tr>
      <th>페시치</th>
      <td>0.8592</td>
      <td>4.7614</td>
      <td>2.2554</td>
      <td>0.9487</td>
      <td>1.5573</td>
      <td>3.8843</td>
      <td>0.8592</td>
      <td>0.1790</td>
      <td>0.3780</td>
      <td>4.9140</td>
      <td>...</td>
      <td>0.05</td>
      <td>2.0458</td>
      <td>0.3860</td>
      <td>12.3134</td>
      <td>4.2846</td>
      <td>2.5050</td>
      <td>0.0835</td>
      <td>0.0</td>
      <td>2.1042</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>16 rows × 27 columns</p>
</div>




```python
is_atk1 = df1['Goal'] >= 0.35
df1 = df1[is_atk1]
df1
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
      <th>Cut-off</th>
      <th>Recovery</th>
      <th>Blocks</th>
      <th>Mistakes</th>
      <th>Fouls</th>
      <th>Fouls Won</th>
      <th>Yellow Cards</th>
      <th>Red Cards</th>
      <th>league</th>
      <th>Game played</th>
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
      <th>C. Egbuchulam</th>
      <td>0.69</td>
      <td>0.03</td>
      <td>4.37</td>
      <td>1.72</td>
      <td>1.13</td>
      <td>1.51</td>
      <td>2.89</td>
      <td>1.48</td>
      <td>0.79</td>
      <td>0.03</td>
      <td>...</td>
      <td>1.79</td>
      <td>5.98</td>
      <td>0.00</td>
      <td>1.27</td>
      <td>1.86</td>
      <td>0.48</td>
      <td>0.10</td>
      <td>0.00</td>
      <td>1</td>
      <td>29.08</td>
    </tr>
    <tr>
      <th>F. Silva</th>
      <td>0.69</td>
      <td>0.12</td>
      <td>2.60</td>
      <td>1.30</td>
      <td>0.28</td>
      <td>1.02</td>
      <td>2.20</td>
      <td>0.41</td>
      <td>0.37</td>
      <td>0.04</td>
      <td>...</td>
      <td>2.80</td>
      <td>5.85</td>
      <td>0.04</td>
      <td>0.77</td>
      <td>1.79</td>
      <td>1.46</td>
      <td>0.12</td>
      <td>0.04</td>
      <td>1</td>
      <td>24.60</td>
    </tr>
    <tr>
      <th>M. Jesús</th>
      <td>0.44</td>
      <td>0.13</td>
      <td>4.15</td>
      <td>1.77</td>
      <td>0.57</td>
      <td>1.81</td>
      <td>2.47</td>
      <td>1.68</td>
      <td>0.49</td>
      <td>0.04</td>
      <td>...</td>
      <td>1.19</td>
      <td>3.89</td>
      <td>0.09</td>
      <td>1.28</td>
      <td>2.12</td>
      <td>2.03</td>
      <td>0.31</td>
      <td>0.00</td>
      <td>1</td>
      <td>22.64</td>
    </tr>
    <tr>
      <th>고무열</th>
      <td>0.55</td>
      <td>0.14</td>
      <td>2.77</td>
      <td>1.20</td>
      <td>0.28</td>
      <td>1.29</td>
      <td>1.62</td>
      <td>1.15</td>
      <td>0.09</td>
      <td>0.14</td>
      <td>...</td>
      <td>1.94</td>
      <td>5.12</td>
      <td>0.00</td>
      <td>0.92</td>
      <td>1.06</td>
      <td>1.29</td>
      <td>0.14</td>
      <td>0.00</td>
      <td>1</td>
      <td>21.66</td>
    </tr>
    <tr>
      <th>알렉스</th>
      <td>0.44</td>
      <td>0.04</td>
      <td>2.24</td>
      <td>1.08</td>
      <td>0.48</td>
      <td>0.68</td>
      <td>1.36</td>
      <td>0.88</td>
      <td>0.56</td>
      <td>0.48</td>
      <td>...</td>
      <td>1.92</td>
      <td>5.20</td>
      <td>0.00</td>
      <td>1.28</td>
      <td>1.32</td>
      <td>0.96</td>
      <td>0.04</td>
      <td>0.00</td>
      <td>1</td>
      <td>24.99</td>
    </tr>
    <tr>
      <th>윌리안</th>
      <td>0.39</td>
      <td>0.10</td>
      <td>2.20</td>
      <td>0.88</td>
      <td>0.64</td>
      <td>0.69</td>
      <td>1.32</td>
      <td>0.88</td>
      <td>0.34</td>
      <td>0.05</td>
      <td>...</td>
      <td>6.02</td>
      <td>10.87</td>
      <td>0.39</td>
      <td>1.08</td>
      <td>2.40</td>
      <td>2.06</td>
      <td>0.15</td>
      <td>0.00</td>
      <td>1</td>
      <td>20.43</td>
    </tr>
    <tr>
      <th>이동준</th>
      <td>0.41</td>
      <td>0.22</td>
      <td>2.00</td>
      <td>0.92</td>
      <td>0.48</td>
      <td>0.60</td>
      <td>1.55</td>
      <td>0.44</td>
      <td>0.29</td>
      <td>0.00</td>
      <td>...</td>
      <td>2.76</td>
      <td>4.40</td>
      <td>0.06</td>
      <td>1.55</td>
      <td>1.27</td>
      <td>3.23</td>
      <td>0.03</td>
      <td>0.00</td>
      <td>1</td>
      <td>31.56</td>
    </tr>
    <tr>
      <th>이정협</th>
      <td>0.60</td>
      <td>0.14</td>
      <td>2.12</td>
      <td>1.15</td>
      <td>0.23</td>
      <td>0.74</td>
      <td>1.80</td>
      <td>0.32</td>
      <td>0.69</td>
      <td>0.05</td>
      <td>...</td>
      <td>0.69</td>
      <td>3.41</td>
      <td>0.05</td>
      <td>0.83</td>
      <td>1.38</td>
      <td>1.57</td>
      <td>0.28</td>
      <td>0.00</td>
      <td>1</td>
      <td>21.67</td>
    </tr>
    <tr>
      <th>조규성</th>
      <td>0.49</td>
      <td>0.14</td>
      <td>3.18</td>
      <td>0.92</td>
      <td>0.74</td>
      <td>1.52</td>
      <td>2.15</td>
      <td>1.02</td>
      <td>0.60</td>
      <td>0.00</td>
      <td>...</td>
      <td>1.48</td>
      <td>3.88</td>
      <td>0.11</td>
      <td>1.41</td>
      <td>2.05</td>
      <td>2.58</td>
      <td>0.11</td>
      <td>0.04</td>
      <td>1</td>
      <td>28.33</td>
    </tr>
    <tr>
      <th>호물로</th>
      <td>0.41</td>
      <td>0.10</td>
      <td>3.26</td>
      <td>1.03</td>
      <td>0.99</td>
      <td>1.23</td>
      <td>0.89</td>
      <td>2.37</td>
      <td>0.03</td>
      <td>6.27</td>
      <td>...</td>
      <td>3.50</td>
      <td>8.91</td>
      <td>0.27</td>
      <td>0.45</td>
      <td>1.10</td>
      <td>2.02</td>
      <td>0.10</td>
      <td>0.00</td>
      <td>1</td>
      <td>29.17</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 57 columns</p>
</div>




```python
df1_atk = df1[['Goal', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target', 'Shots inside PA', 'Shots outside of PA', 'Freekicks']]
df1_atk[['Goal', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target', 'Shots inside PA', 'Shots outside of PA', 'Freekicks']] *= 1.29
df1_atk

df1_dist = df1[['Assists', 'Key Passes', 'Passes Success', 'Passes in Final third Area Success', 'Forwards Pass Success', 'Crosses Success']]
df1_dist[['Assists', 'Key Passes', 'Passes Success', 'Passes in Final third Area Success', 'Forwards Pass Success', 'Crosses Success']] *= 3.28
df1_dist

df1_def = df1[['Tackles Success', 'Interceptions', 'Clearances', 'Blocks']]
df1_def[['Tackles Success', 'Interceptions', 'Clearances', 'Blocks']] * 4.17
df1_def

df1_cont = df1[['Take-ons Success', 'Control under pressure', 'Aerial Duels Success', 'Ground Duels Success']]
df1_cont[['Take-ons Success', 'Control under pressure', 'Aerial Duels Success', 'Ground Duels Success']] *= 3.36
df1_cont

df1_mis = df1[['Mistakes', 'Yellow Cards', 'Red Cards', 'Fouls']]
df1_mis[['Mistakes', 'Yellow Cards', 'Red Cards', 'Fouls']] *= 2.17
```


```python
e = pd.concat([df1_atk, df1_dist], axis=1)
f = pd.concat([e, df1_def], axis=1)
g = pd.concat([f, df1_cont], axis=1)
h = pd.concat([g, df1_mis], axis=1)
h['league'] = 1
h
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
      <th>Shots</th>
      <th>SoT</th>
      <th>Blocked Shots</th>
      <th>Shots off Target</th>
      <th>Shots inside PA</th>
      <th>Shots outside of PA</th>
      <th>Freekicks</th>
      <th>Assists</th>
      <th>Key Passes</th>
      <th>...</th>
      <th>Blocks</th>
      <th>Take-ons Success</th>
      <th>Control under pressure</th>
      <th>Aerial Duels Success</th>
      <th>Ground Duels Success</th>
      <th>Mistakes</th>
      <th>Yellow Cards</th>
      <th>Red Cards</th>
      <th>Fouls</th>
      <th>league</th>
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
      <th>C. Egbuchulam</th>
      <td>0.8901</td>
      <td>5.6373</td>
      <td>2.2188</td>
      <td>1.4577</td>
      <td>1.9479</td>
      <td>3.7281</td>
      <td>1.9092</td>
      <td>0.0387</td>
      <td>0.0984</td>
      <td>3.5096</td>
      <td>...</td>
      <td>0.00</td>
      <td>1.0416</td>
      <td>0.0000</td>
      <td>6.5856</td>
      <td>3.9312</td>
      <td>2.7559</td>
      <td>0.2170</td>
      <td>0.0000</td>
      <td>4.0362</td>
      <td>1</td>
    </tr>
    <tr>
      <th>F. Silva</th>
      <td>0.8901</td>
      <td>3.3540</td>
      <td>1.6770</td>
      <td>0.3612</td>
      <td>1.3158</td>
      <td>2.8380</td>
      <td>0.5289</td>
      <td>0.0516</td>
      <td>0.3936</td>
      <td>4.0016</td>
      <td>...</td>
      <td>0.04</td>
      <td>0.2688</td>
      <td>0.2688</td>
      <td>19.1184</td>
      <td>4.2336</td>
      <td>1.6709</td>
      <td>0.2604</td>
      <td>0.0868</td>
      <td>3.8843</td>
      <td>1</td>
    </tr>
    <tr>
      <th>M. Jesús</th>
      <td>0.5676</td>
      <td>5.3535</td>
      <td>2.2833</td>
      <td>0.7353</td>
      <td>2.3349</td>
      <td>3.1863</td>
      <td>2.1672</td>
      <td>0.0516</td>
      <td>0.4264</td>
      <td>3.0504</td>
      <td>...</td>
      <td>0.09</td>
      <td>0.7392</td>
      <td>0.0000</td>
      <td>17.3712</td>
      <td>3.9984</td>
      <td>2.7776</td>
      <td>0.6727</td>
      <td>0.0000</td>
      <td>4.6004</td>
      <td>1</td>
    </tr>
    <tr>
      <th>고무열</th>
      <td>0.7095</td>
      <td>3.5733</td>
      <td>1.5480</td>
      <td>0.3612</td>
      <td>1.6641</td>
      <td>2.0898</td>
      <td>1.4835</td>
      <td>0.1806</td>
      <td>0.4592</td>
      <td>4.9856</td>
      <td>...</td>
      <td>0.00</td>
      <td>1.8480</td>
      <td>0.4704</td>
      <td>7.7616</td>
      <td>4.9728</td>
      <td>1.9964</td>
      <td>0.3038</td>
      <td>0.0000</td>
      <td>2.3002</td>
      <td>1</td>
    </tr>
    <tr>
      <th>알렉스</th>
      <td>0.5676</td>
      <td>2.8896</td>
      <td>1.3932</td>
      <td>0.6192</td>
      <td>0.8772</td>
      <td>1.7544</td>
      <td>1.1352</td>
      <td>0.6192</td>
      <td>0.1312</td>
      <td>4.4608</td>
      <td>...</td>
      <td>0.00</td>
      <td>0.6720</td>
      <td>0.4032</td>
      <td>5.5104</td>
      <td>4.1664</td>
      <td>2.7776</td>
      <td>0.0868</td>
      <td>0.0000</td>
      <td>2.8644</td>
      <td>1</td>
    </tr>
    <tr>
      <th>윌리안</th>
      <td>0.5031</td>
      <td>2.8380</td>
      <td>1.1352</td>
      <td>0.8256</td>
      <td>0.8901</td>
      <td>1.7028</td>
      <td>1.1352</td>
      <td>0.0645</td>
      <td>0.3280</td>
      <td>2.2632</td>
      <td>...</td>
      <td>0.39</td>
      <td>2.4528</td>
      <td>0.0000</td>
      <td>12.6672</td>
      <td>6.4176</td>
      <td>2.3436</td>
      <td>0.3255</td>
      <td>0.0000</td>
      <td>5.2080</td>
      <td>1</td>
    </tr>
    <tr>
      <th>이동준</th>
      <td>0.5289</td>
      <td>2.5800</td>
      <td>1.1868</td>
      <td>0.6192</td>
      <td>0.7740</td>
      <td>1.9995</td>
      <td>0.5676</td>
      <td>0.0000</td>
      <td>0.7216</td>
      <td>3.8376</td>
      <td>...</td>
      <td>0.06</td>
      <td>1.0752</td>
      <td>0.2016</td>
      <td>5.0064</td>
      <td>4.3680</td>
      <td>3.3635</td>
      <td>0.0651</td>
      <td>0.0000</td>
      <td>2.7559</td>
      <td>1</td>
    </tr>
    <tr>
      <th>이정협</th>
      <td>0.7740</td>
      <td>2.7348</td>
      <td>1.4835</td>
      <td>0.2967</td>
      <td>0.9546</td>
      <td>2.3220</td>
      <td>0.4128</td>
      <td>0.0645</td>
      <td>0.4592</td>
      <td>4.3952</td>
      <td>...</td>
      <td>0.05</td>
      <td>0.1680</td>
      <td>0.0000</td>
      <td>13.3392</td>
      <td>1.8480</td>
      <td>1.8011</td>
      <td>0.6076</td>
      <td>0.0000</td>
      <td>2.9946</td>
      <td>1</td>
    </tr>
    <tr>
      <th>조규성</th>
      <td>0.6321</td>
      <td>4.1022</td>
      <td>1.1868</td>
      <td>0.9546</td>
      <td>1.9608</td>
      <td>2.7735</td>
      <td>1.3158</td>
      <td>0.0000</td>
      <td>0.4592</td>
      <td>3.4768</td>
      <td>...</td>
      <td>0.11</td>
      <td>0.7056</td>
      <td>0.1344</td>
      <td>18.1440</td>
      <td>4.9728</td>
      <td>3.0597</td>
      <td>0.2387</td>
      <td>0.0868</td>
      <td>4.4485</td>
      <td>1</td>
    </tr>
    <tr>
      <th>호물로</th>
      <td>0.5289</td>
      <td>4.2054</td>
      <td>1.3287</td>
      <td>1.2771</td>
      <td>1.5867</td>
      <td>1.1481</td>
      <td>3.0573</td>
      <td>8.0883</td>
      <td>0.3280</td>
      <td>5.0512</td>
      <td>...</td>
      <td>0.27</td>
      <td>0.7056</td>
      <td>0.3360</td>
      <td>1.1424</td>
      <td>5.6448</td>
      <td>0.9765</td>
      <td>0.2170</td>
      <td>0.0000</td>
      <td>2.3870</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 27 columns</p>
</div>




```python
new_df = pd.concat([d,h])
new_df

new_dfX = new_df[['Goal', 'Shots', 'SoT', 'Blocked Shots', 'Shots off Target',
       'Shots inside PA', 'Shots outside of PA', 'Freekicks', 'Assists',
       'Key Passes', 'Passes Success', 'Passes in Final third Area Success',
       'Forwards Pass Success', 'Crosses Success', 'Tackles Success',
       'Interceptions', 'Clearances', 'Blocks', 'Take-ons Success',
       'Control under pressure', 'Aerial Duels Success',
       'Ground Duels Success', 'Mistakes', 'Yellow Cards', 'Red Cards',
       'Fouls',]]
new_dfy = new_df['league']
```


```python
x_new = [0.81, 4.13, 2.05, 1.12, 3.35, 2.01, 3.13, 0.21, 1.45, 4.54, 43.23, 22.12, 13.22, 2.12, 0.56, 0.38, 0.31, 0.05, 2.22, 0.71, 6.53,\
         1.46, 3.15, 0.24, 0, 2.46]
```


```python
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import VotingClassifier

model_logics= LogisticRegression(random_state=1)
model_qda = QuadraticDiscriminantAnalysis()
model_gnb = GaussianNB()

ensemble = VotingClassifier(estimators=[('lr', model_logics), ('qda', model_qda), ('gnb', model_gnb)], voting='soft')

probas = [c.fit(new_dfX, new_dfy).predict_proba([x_new]) for c in (model_logics, model_qda, model_gnb, ensemble)]
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]

ind = np.arange(4)
width = 0.35  # bar width
p1 = plt.bar(ind, np.hstack(([class1_1[:-1], [0]])), width, color='green')
p2 = plt.bar(ind + width, np.hstack(([class2_1[:-1], [0]])), width, color='lightgreen')
p3 = plt.bar(ind, [0, 0, 0, class1_1[-1]], width, color='blue')
p4 = plt.bar(ind + width, [0, 0, 0, class2_1[-1]], width, color='steelblue')

plt.xticks(ind + 0.5 * width, ['로지스틱 회귀 모형', 'QDA 모형', '가우시안 나이브베이즈', '소프트 다수결 모형'])
plt.ylim([0, 1.1])
plt.title('세가지 다른 분류 모형과 소프트 다수결 모형의 분류 결과')
plt.legend([p1[0], p2[0]], ['클래스 1', '클래스 2'], loc='upper left')
plt.show()
```

    /opt/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/_logistic.py:940: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/discriminant_analysis.py:691: UserWarning: Variables are collinear
      warnings.warn("Variables are collinear")
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/_logistic.py:940: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/discriminant_analysis.py:691: UserWarning: Variables are collinear
      warnings.warn("Variables are collinear")



<img width="381" alt="output_10_1" src="https://user-images.githubusercontent.com/59719711/83753395-2b084b80-a6a5-11ea-98c4-5d5a4aa62adb.png">



```python
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import VotingClassifier

model1 = LogisticRegression(random_state=1)
model2 = QuadraticDiscriminantAnalysis()
model3 = LinearDiscriminantAnalysis()
model4 = GaussianNB()
model5 = BernoulliNB()
model6 = MultinomialNB()
model7 = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)

ensemble = VotingClassifier(estimators=[('lr', model1), ('qda', model2), ('lda', model3), ('gnb', model4), ('bern', model5), \
                           ('mnb', model6), ('tree', model7)], voting='soft')

ens_model = ensemble.fit(new_dfX, new_dfy)

# # 예측된 y값
y_pred = ens_model.predict(new_dfX)

from sklearn.model_selection import cross_val_score, KFold
cv = KFold(5, shuffle=True, random_state=0)
cross_val_score(ens_model, new_dfX, new_dfy, scoring='accuracy', cv=cv).mean()
```

    /opt/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/_logistic.py:940: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/discriminant_analysis.py:691: UserWarning: Variables are collinear
      warnings.warn("Variables are collinear")
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/_logistic.py:940: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/discriminant_analysis.py:691: UserWarning: Variables are collinear
      warnings.warn("Variables are collinear")
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/_logistic.py:940: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/discriminant_analysis.py:691: UserWarning: Variables are collinear
      warnings.warn("Variables are collinear")
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/_logistic.py:940: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/discriminant_analysis.py:691: UserWarning: Variables are collinear
      warnings.warn("Variables are collinear")
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/_logistic.py:940: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/discriminant_analysis.py:691: UserWarning: Variables are collinear
      warnings.warn("Variables are collinear")
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/_logistic.py:940: ConvergenceWarning: lbfgs failed to converge (status=1):
    STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
    
    Increase the number of iterations (max_iter) or scale the data as shown in:
        https://scikit-learn.org/stable/modules/preprocessing.html
    Please also refer to the documentation for alternative solver options:
        https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
      extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
    /opt/anaconda3/lib/python3.7/site-packages/sklearn/discriminant_analysis.py:691: UserWarning: Variables are collinear
      warnings.warn("Variables are collinear")





    0.7666666666666666




```python
from sklearn.ensemble import BaggingClassifier
model1 = DecisionTreeClassifier(max_depth=5, random_state=0).fit(new_dfX, new_dfy)
model2 = BaggingClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=100, random_state=0).fit(new_dfX, new_dfy)

cv = KFold(5, shuffle=True, random_state=0)
model1_cross = cross_val_score(model1, new_dfX, new_dfy, scoring='accuracy', cv=cv)
model2_cross = cross_val_score(model2, new_dfX, new_dfy, scoring='accuracy', cv=cv)

print('개별모형의 성능점수(평균) : {} '.format(model1_cross.mean()))
print('개별모형의 성능점수(표준편차) : {} '.format(model1_cross.std()))
print('Bagging모형의 성능점수(평균) : {}'.format(model2_cross.mean()))
print('Bagging모형의 성능점수(표준편차) : {}'.format(model2_cross.std()))
```

    개별모형의 성능점수(평균) : 0.6799999999999999 
    개별모형의 성능점수(표준편차) : 0.20396078054371142 
    Bagging모형의 성능점수(평균) : 0.5666666666666667
    Bagging모형의 성능점수(표준편차) : 0.20439612955674524



```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

model_rf = RandomForestClassifier(max_depth=10, n_estimators=100, random_state=0).fit(new_dfX, new_dfy)
model_rf0 = ExtraTreesClassifier(n_estimators=100, random_state=0).fit(new_dfX, new_dfy)
cv = KFold(5, shuffle=True, random_state=0)
print(cross_val_score(model_rf, new_dfX, new_dfy, scoring='accuracy', cv=cv).mean())
print(cross_val_score(model_rf0, new_dfX, new_dfy, scoring='accuracy', cv=cv).mean())
```

    0.7200000000000001
    0.76



```python
# 특성 중요도
idx = np.argsort(model_rf.feature_importances_)
names = new_df.columns[idx]
values = model_rf.feature_importances_[idx]

plt.figure(figsize=(12,6))
plt.barh(names, values)
plt.title('Breast Cancer Feature Importance')
plt.show()
```


<img width="863" alt="output_14_0" src="https://user-images.githubusercontent.com/59719711/83753424-3c515800-a6a5-11ea-90ed-26448af75842.png">



```python
probas_1 = model1.predict([x_new])
probas_2 = model2.predict([x_new])
probas_3 = model_logics.predict([x_new])
print(probas_1, probas_2, probas_3)
```

    [1] [0] [1]

