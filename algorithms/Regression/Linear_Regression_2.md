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

##### 스케일링

<img width="542" alt="스크린샷 2020-05-13 오후 6 20 21" src="https://user-images.githubusercontent.com/59719711/81794987-8af85000-9546-11ea-80c2-df81105e3ee1.png">

```python

```

    이 summary report는 어제 보스턴 집값 데이터를 활용하여 선형회귀분석을 한 결과값이야. 아랫부분의 Cond. No. 라고 쓰여져 있는 부분인데 조건수(conditional number)는 가장 큰 고유치와 가장 작은 고유치의 비율을 뜻해.


```python
from sklearn.datasets import load_boston

boston = load_boston()

dfx = pd.DataFrame(boston.data, columns=boston.feature_names)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])
df = pd.concat([dfx,dfy],axis=1)
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
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0.0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1.0</td>
      <td>296.0</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2.0</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>392.83</td>
      <td>4.03</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3.0</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
      <td>36.2</td>
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
      <th>501</th>
      <td>0.06263</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.593</td>
      <td>69.1</td>
      <td>2.4786</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>391.99</td>
      <td>9.67</td>
      <td>22.4</td>
    </tr>
    <tr>
      <th>502</th>
      <td>0.04527</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.120</td>
      <td>76.7</td>
      <td>2.2875</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>9.08</td>
      <td>20.6</td>
    </tr>
    <tr>
      <th>503</th>
      <td>0.06076</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.976</td>
      <td>91.0</td>
      <td>2.1675</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>5.64</td>
      <td>23.9</td>
    </tr>
    <tr>
      <th>504</th>
      <td>0.10959</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.794</td>
      <td>89.3</td>
      <td>2.3889</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>393.45</td>
      <td>6.48</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>505</th>
      <td>0.04741</td>
      <td>0.0</td>
      <td>11.93</td>
      <td>0.0</td>
      <td>0.573</td>
      <td>6.030</td>
      <td>80.8</td>
      <td>2.5050</td>
      <td>1.0</td>
      <td>273.0</td>
      <td>21.0</td>
      <td>396.90</td>
      <td>7.88</td>
      <td>11.9</td>
    </tr>
  </tbody>
</table>
<p>506 rows × 14 columns</p>
</div>



    이것은 일부러 TAX변수를 크게 만들어 조건수를 증폭시켜본 데이터야


```python
import statsmodels.api as sm
dfX = sm.add_constant(dfx)
dfX2 = dfX.copy()
dfX2["TAX"] *= 1e13
df2 = pd.concat([dfX2, dfy], axis=1)
model2 = sm.OLS.from_formula("MEDV ~ " + "+".join(boston.feature_names), data=df2)
result2 = model2.fit()
print(result2.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                   MEDV   R-squared:                       0.333
    Model:                            OLS   Adj. R-squared:                  0.329
    Method:                 Least Squares   F-statistic:                     83.39
    Date:                Wed, 13 May 2020   Prob (F-statistic):           8.62e-44
    Time:                        16:03:11   Log-Likelihood:                -1737.9
    No. Observations:                 506   AIC:                             3484.
    Df Residuals:                     502   BIC:                             3501.
    Df Model:                           3                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept     -0.0038      0.000     -8.543      0.000      -0.005      -0.003
    CRIM          -0.1567      0.046     -3.376      0.001      -0.248      -0.066
    ZN             0.1273      0.016      7.752      0.000       0.095       0.160
    INDUS         -0.1971      0.019    -10.433      0.000      -0.234      -0.160
    CHAS           0.0034      0.000     12.430      0.000       0.003       0.004
    NOX           -0.0023      0.000     -9.285      0.000      -0.003      -0.002
    RM             0.0267      0.002     14.132      0.000       0.023       0.030
    AGE            0.1410      0.017      8.443      0.000       0.108       0.174
    DIS           -0.0286      0.004     -7.531      0.000      -0.036      -0.021
    RAD            0.1094      0.018      6.163      0.000       0.075       0.144
    TAX         1.077e-15   2.66e-16      4.051      0.000    5.55e-16     1.6e-15
    PTRATIO       -0.1124      0.011    -10.390      0.000      -0.134      -0.091
    B              0.0516      0.003     19.916      0.000       0.046       0.057
    LSTAT         -0.6569      0.056    -11.790      0.000      -0.766      -0.547
    ==============================================================================
    Omnibus:                       39.447   Durbin-Watson:                   0.863
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               46.611
    Skew:                           0.704   Prob(JB):                     7.56e-11
    Kurtosis:                       3.479   Cond. No.                     1.19e+17
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 1.19e+17. This might indicate that there are
    strong multicollinearity or other numerical problems.


    조건수(Conditional No.)가 1000조 수준으로 증가한 것을 볼 수 있지? 오른쪽 제일 상단에 보이는 R-squared라는 값으로 표시되는 성능지표도 크게 감소한것을 볼 수 있어. R-squared 는 이 모델 성능에 대해 몇점인지를 알려주는 기능이라고 보면 되(0.333으로 나왔으니 100점 만점에 33.3점이라는 소리야)
    
    statsmodels에서는  scale() 이라는 명령을 사용하여 스케일링을 할 수 있는데, 이 방식으로 스케일을 하면 스케일링에 사용된 평균과 표준편차를 저장하였다가 나중에 predict() 라는 명령을 사용할 때도 같은 스케일을 사용하기 때문에 편리한 것을 알 수 있어. 다만! 스케일링을 할 때에는 카테고리 변수, 즉 범주형 데이터는 스케일링을 하지 않는다는 것에 주의 해주면 되.


```python
feature_names = list(boston.feature_names)
feature_names.remove("CHAS") 
feature_names = ['scale({})'.format(name) for name in feature_names] + ['CHAS']
model3 = sm.OLS.from_formula("MEDV ~ " + "+".join(feature_names), data=df2)
result3 = model3.fit()
print(result3.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                   MEDV   R-squared:                       0.741
    Model:                            OLS   Adj. R-squared:                  0.734
    Method:                 Least Squares   F-statistic:                     108.1
    Date:                Wed, 13 May 2020   Prob (F-statistic):          6.72e-135
    Time:                        16:11:05   Log-Likelihood:                -1498.8
    No. Observations:                 506   AIC:                             3026.
    Df Residuals:                     492   BIC:                             3085.
    Df Model:                          13                                         
    Covariance Type:            nonrobust                                         
    ==================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
    ----------------------------------------------------------------------------------
    Intercept         22.3470      0.219    101.943      0.000      21.916      22.778
    scale(CRIM)       -0.9281      0.282     -3.287      0.001      -1.483      -0.373
    scale(ZN)          1.0816      0.320      3.382      0.001       0.453       1.710
    scale(INDUS)       0.1409      0.421      0.334      0.738      -0.687       0.969
    scale(NOX)        -2.0567      0.442     -4.651      0.000      -2.926      -1.188
    scale(RM)          2.6742      0.293      9.116      0.000       2.098       3.251
    scale(AGE)         0.0195      0.371      0.052      0.958      -0.710       0.749
    scale(DIS)        -3.1040      0.420     -7.398      0.000      -3.928      -2.280
    scale(RAD)         2.6622      0.577      4.613      0.000       1.528       3.796
    scale(TAX)        -2.0768      0.633     -3.280      0.001      -3.321      -0.833
    scale(PTRATIO)    -2.0606      0.283     -7.283      0.000      -2.617      -1.505
    scale(B)           0.8493      0.245      3.467      0.001       0.368       1.331
    scale(LSTAT)      -3.7436      0.362    -10.347      0.000      -4.454      -3.033
    CHAS               2.6867      0.862      3.118      0.002       0.994       4.380
    ==============================================================================
    Omnibus:                      178.041   Durbin-Watson:                   1.078
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):              783.126
    Skew:                           1.521   Prob(JB):                    8.84e-171
    Kurtosis:                       8.281   Cond. No.                         10.6
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


    독립변수 데이터를 스케일링한것만으로 조건수의 수치가 확 내려간 것을 볼 수 있어. 어때? 쉽지?

    조건수를 될 수 있으면 낮춰주는게 각 독립변수의 오차범위를 줄여줄 수 있다고 해. 그래서 큰 값의 데이터들은 스케일링을 통해 사이즈를 줄여주는 거지.

##### 범주형 독립변수의 회귀분석

    이번에는 연속형 데이터가 아닌 범주형 데이터의 회귀분석을 하는 방법에 대해 알아보자! 범주형 데이터는 측정 결과가 몇 개의 범주 또는 향목의 형태로 나타나는 자료를 말하는데 그것을 숫자로 표현한 것이라고 할 수 있어. 예를 들면 남자는 1 여자는 0 이런식이지!
    
    아무튼..

    여기서 다룰 학습은 그러한 범주형 독립변수(데이터)의 회귀분석 모델링 시 에는 앞서 배운 더미변수화가 필수라는 거야. 풀랭크(full-rank) 방식과 축소랭크(reduced-rank) 방식이 있는데 풀랭크방식에서는 더미변수의 값을 원핫인코딩(one-hot-encoding) 방식으로 지정을 하는거야
    
    예를 들어서..
    
    남자는 1 이고 여자는 0 이면 
    남자 : d1=1, d2=0
    여자 : d1=0, d2=1 이런식으로 쓴다는 거지
 
    축소랭크 방식에서는 특정한 하나의 범주값을 기준값(reference, baseline)으로 하고 기준값에 대응하는 더미변수의 가중치는 항상 1으로 놓아 계산 하는 방법이지
    
    무슨 말인지 어렵지? 그럼 실 데이터로 예를 들어보도록 할게.
    
    아래의 데이터는 1920년부터 1939년까지 영국 노팅험 지역의 기온을 나타낸 데이터야. 이 데이터에서 독립 변수는 월(monath)이며 범주값으로 처리를 할거야 그리고 value로 표기된 값이 종속변수인 해당 월의 평균 기온이라고 할 수 있지. 분석의 목적은 독립변수인 월 값을 이용하여 종속변수인 월 평균 기온을 예측하는 것이야.


```python
import datetime
from calendar import isleap

def convert_partial_year(number):
   #연 단위 숫자에서 날짜를 계산하는 코드
    year = int(number)
    d = datetime.timedelta(days=(number - year) * (365 + isleap(year)))
    day_one = datetime.datetime(year, 1, 1)
    date = d + day_one
    return date

df_nottem = sm.datasets.get_rdataset("nottem").data

df_nottem["date0"] = df_nottem[["time"]].applymap(convert_partial_year)
df_nottem["date"] = pd.DatetimeIndex(df_nottem["date0"]).round('60min') + datetime.timedelta(seconds=3600*24)
df_nottem["month"] = df_nottem["date"].dt.strftime("%m").astype('category')
del df_nottem["date0"], df_nottem["date"]
df_nottem
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
      <th>time</th>
      <th>value</th>
      <th>month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1920.000000</td>
      <td>40.6</td>
      <td>01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1920.083333</td>
      <td>40.8</td>
      <td>02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1920.166667</td>
      <td>44.4</td>
      <td>03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1920.250000</td>
      <td>46.7</td>
      <td>04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1920.333333</td>
      <td>54.1</td>
      <td>05</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>235</th>
      <td>1939.583333</td>
      <td>61.8</td>
      <td>08</td>
    </tr>
    <tr>
      <th>236</th>
      <td>1939.666667</td>
      <td>58.2</td>
      <td>09</td>
    </tr>
    <tr>
      <th>237</th>
      <td>1939.750000</td>
      <td>46.7</td>
      <td>10</td>
    </tr>
    <tr>
      <th>238</th>
      <td>1939.833333</td>
      <td>46.6</td>
      <td>11</td>
    </tr>
    <tr>
      <th>239</th>
      <td>1939.916667</td>
      <td>37.8</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
<p>240 rows × 3 columns</p>
</div>



    박스플롯을 통해 해당 월에 종속변수데이터가 어디에 주로 모여있는지 확인을 해보는거야


```python
df_nottem.boxplot("value", "month")
plt.show()
```


<img width="382" alt="output_14_0" src="https://user-images.githubusercontent.com/59719711/81795405-0a861f00-9547-11ea-8d19-a3c30dfdf966.png">


    %% 범주형 독립변수의 경우 앞서 시행한 회귀분석에서 추가해준 상수항(add_constant)을 추가하지 않아.


```python
# 풀랭크 방식
model = sm.OLS.from_formula("value ~ C(month) + 0", df_nottem)
result = model.fit()
print(result.summary())

# C()로 카테고리로 처리
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  value   R-squared:                       0.930
    Model:                            OLS   Adj. R-squared:                  0.927
    Method:                 Least Squares   F-statistic:                     277.3
    Date:                Wed, 13 May 2020   Prob (F-statistic):          2.96e-125
    Time:                        16:28:22   Log-Likelihood:                -535.82
    No. Observations:                 240   AIC:                             1096.
    Df Residuals:                     228   BIC:                             1137.
    Df Model:                          11                                         
    Covariance Type:            nonrobust                                         
    ================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
    --------------------------------------------------------------------------------
    C(month)[01]    39.6950      0.518     76.691      0.000      38.675      40.715
    C(month)[02]    39.1900      0.518     75.716      0.000      38.170      40.210
    C(month)[03]    42.1950      0.518     81.521      0.000      41.175      43.215
    C(month)[04]    46.2900      0.518     89.433      0.000      45.270      47.310
    C(month)[05]    52.5600      0.518    101.547      0.000      51.540      53.580
    C(month)[06]    58.0400      0.518    112.134      0.000      57.020      59.060
    C(month)[07]    61.9000      0.518    119.592      0.000      60.880      62.920
    C(month)[08]    60.5200      0.518    116.926      0.000      59.500      61.540
    C(month)[09]    56.4800      0.518    109.120      0.000      55.460      57.500
    C(month)[10]    49.4950      0.518     95.625      0.000      48.475      50.515
    C(month)[11]    42.5800      0.518     82.265      0.000      41.560      43.600
    C(month)[12]    39.5300      0.518     76.373      0.000      38.510      40.550
    ==============================================================================
    Omnibus:                        5.430   Durbin-Watson:                   1.529
    Prob(Omnibus):                  0.066   Jarque-Bera (JB):                5.299
    Skew:                          -0.281   Prob(JB):                       0.0707
    Kurtosis:                       3.463   Cond. No.                         1.00
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
model = sm.OLS.from_formula("value ~ C(month)", df_nottem)
result = model.fit()
print(result.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  value   R-squared:                       0.930
    Model:                            OLS   Adj. R-squared:                  0.927
    Method:                 Least Squares   F-statistic:                     277.3
    Date:                Wed, 13 May 2020   Prob (F-statistic):          2.96e-125
    Time:                        16:32:20   Log-Likelihood:                -535.82
    No. Observations:                 240   AIC:                             1096.
    Df Residuals:                     228   BIC:                             1137.
    Df Model:                          11                                         
    Covariance Type:            nonrobust                                         
    ==================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
    ----------------------------------------------------------------------------------
    Intercept         39.6950      0.518     76.691      0.000      38.675      40.715
    C(month)[T.02]    -0.5050      0.732     -0.690      0.491      -1.947       0.937
    C(month)[T.03]     2.5000      0.732      3.415      0.001       1.058       3.942
    C(month)[T.04]     6.5950      0.732      9.010      0.000       5.153       8.037
    C(month)[T.05]    12.8650      0.732     17.575      0.000      11.423      14.307
    C(month)[T.06]    18.3450      0.732     25.062      0.000      16.903      19.787
    C(month)[T.07]    22.2050      0.732     30.335      0.000      20.763      23.647
    C(month)[T.08]    20.8250      0.732     28.450      0.000      19.383      22.267
    C(month)[T.09]    16.7850      0.732     22.931      0.000      15.343      18.227
    C(month)[T.10]     9.8000      0.732     13.388      0.000       8.358      11.242
    C(month)[T.11]     2.8850      0.732      3.941      0.000       1.443       4.327
    C(month)[T.12]    -0.1650      0.732     -0.225      0.822      -1.607       1.277
    ==============================================================================
    Omnibus:                        5.430   Durbin-Watson:                   1.529
    Prob(Omnibus):                  0.066   Jarque-Bera (JB):                5.299
    Skew:                          -0.281   Prob(JB):                       0.0707
    Kurtosis:                       3.463   Cond. No.                         12.9
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


    축소랭크 방식 ( +0 제거) - '기준이 되는 데이터 값에서  다른 범주형 데이터 값이 얼마나 다르냐' 의 의미로 보면 됨, 즉 1월을 기준으로 2월에는 차이가 얼마나 있느냐 를 나타내는거야. 풀랭크 방식과 축소랭크 방식의 차이를 조금은 알 수 있게된거같아.
    
    이 이상은 내가 이해를 못했기 때문에 넘어가도록 할게.

##### 부분회귀

    만약 회귀분석을 한 후에 새로운 독립변수를 추가하여 다시 회귀분석을 한다면 그 전에 회귀분석으로 구했던 가중치의 값은 변할까 변하지 않을까? 예를 들어  𝑥1 이라는 독립변수만으로 회귀분석한 결과가 다음과 같다고 하자.

<img width="202" alt="스크린샷 2020-05-13 오후 4 49 48" src="https://user-images.githubusercontent.com/59719711/81795180-cdba2800-9546-11ea-9243-aeeca5cda269.png">

    이 때 새로운 독립변수  𝑥2 를 추가하여 회귀분석을 하게 되면 이 때 나오는  𝑥1 에 대한 가중치  𝑤′1 가 원래의  𝑤1 과 같을까 다를까?

<img width="307" alt="스크린샷 2020-05-13 오후 4 49 52" src="https://user-images.githubusercontent.com/59719711/81795240-de6a9e00-9546-11ea-9ef1-5bd349d3ec8a.png">

    답부터 말하자면

    일반적으로  𝑤′1 의 값은 원래의  𝑤1 의 값과 다르다.


```python
from sklearn.datasets import load_boston

boston = load_boston()

dfX0 = pd.DataFrame(boston.data, columns=boston.feature_names)
dfX = sm.add_constant(dfX0)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])
df = pd.concat([dfX, dfy], axis=1)

model_boston = sm.OLS(dfy, dfX)
result_boston = model_boston.fit()
print(result_boston.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                   MEDV   R-squared:                       0.741
    Model:                            OLS   Adj. R-squared:                  0.734
    Method:                 Least Squares   F-statistic:                     108.1
    Date:                Wed, 13 May 2020   Prob (F-statistic):          6.72e-135
    Time:                        18:01:08   Log-Likelihood:                -1498.8
    No. Observations:                 506   AIC:                             3026.
    Df Residuals:                     492   BIC:                             3085.
    Df Model:                          13                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const         36.4595      5.103      7.144      0.000      26.432      46.487
    CRIM          -0.1080      0.033     -3.287      0.001      -0.173      -0.043
    ZN             0.0464      0.014      3.382      0.001       0.019       0.073
    INDUS          0.0206      0.061      0.334      0.738      -0.100       0.141
    CHAS           2.6867      0.862      3.118      0.002       0.994       4.380
    NOX          -17.7666      3.820     -4.651      0.000     -25.272     -10.262
    RM             3.8099      0.418      9.116      0.000       2.989       4.631
    AGE            0.0007      0.013      0.052      0.958      -0.025       0.027
    DIS           -1.4756      0.199     -7.398      0.000      -1.867      -1.084
    RAD            0.3060      0.066      4.613      0.000       0.176       0.436
    TAX           -0.0123      0.004     -3.280      0.001      -0.020      -0.005
    PTRATIO       -0.9527      0.131     -7.283      0.000      -1.210      -0.696
    B              0.0093      0.003      3.467      0.001       0.004       0.015
    LSTAT         -0.5248      0.051    -10.347      0.000      -0.624      -0.425
    ==============================================================================
    Omnibus:                      178.041   Durbin-Watson:                   1.078
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):              783.126
    Skew:                           1.521   Prob(JB):                    8.84e-171
    Kurtosis:                       8.281   Cond. No.                     1.51e+04
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 1.51e+04. This might indicate that there are
    strong multicollinearity or other numerical problems.


    이렇게 보면 AGE는 집값을 결정하는데 음의 상관관계를 가진다고 볼 수 있다고 할 수 있어


```python
sns.regplot(x="AGE", y="MEDV", data=df)
plt.show()
```


<img width="389" alt="output_25_0" src="https://user-images.githubusercontent.com/59719711/81795459-1c67c200-9547-11ea-9580-72d65bfab466.png">


    plot_partregress(endog, exog_i, exog_others, data=None, obs_labels=True, ret_coords=False)

    endog: 종속변수 문자열
    exog_i: 분석 대상이 되는 독립변수 문자열
    exog_others: 나머지 독립변수 문자열의 리스트
    data: 모든 데이터가 있는 데이터프레임
    obs_labels: 데이터 라벨링 여부
    ret_coords: 잔차 데이터 반환 여부

    하지만! 다른 독립변수에 영향을 받은 AGE가 집값에 영향을 미쳤는지에 대한 부분을 확인해보면 그래프는 다음과 같아.
    AGE 데이터에 대한 부분회귀인셈이지.


```python
others = list(set(df.columns).difference(set(["MEDV", "AGE"])))
p, resids = sm.graphics.plot_partregress(
    "MEDV", "AGE", others, data=df, obs_labels=False, ret_coords=True
)
plt.show()

# 크게 상관이 없다는 거로 나오게 되
```

<img width="395" alt="output_29_0" src="https://user-images.githubusercontent.com/59719711/81795521-2be70b00-9547-11ea-9d31-c7d0f66eedab.png">


    sm.graphics.plot_partregress_grid 명령을 쓰면 전체 데이터에 대해 한번에 부분회귀 플롯을 그릴 수 있어.

    plot_partregress_grid(result, fig)
    
    result: 회귀분석 결과 객체
    fig: plt.figure 객체


```python
fig = plt.figure(figsize=(8, 20))
sm.graphics.plot_partregress_grid(result_boston, fig=fig)
fig.suptitle("")
plt.show()
```

<img width="563" alt="output_32_0" src="https://user-images.githubusercontent.com/59719711/81795567-399c9080-9547-11ea-8128-fc56699f56a0.png">


    CCPR 플롯
    CCPR(Component-Component plus Residual) 플롯도 부분회귀 플롯과 마찬가지로 특정한 하나의 변수의 영향을 살펴보기 위한 것이야
    
    부분회귀분석과 비슷하지만 다른점이 하나 있는데 그것은 위에서 언급한 다른 변수에 영향을 받은 AGE가 아니라 AGE 데이터 그 자체와 집값의 상관관계를 보기위한 방법이라고 보면 되


```python
sm.graphics.plot_ccpr(result_boston, "AGE")
plt.show()
```

<img width="395" alt="output_34_0" src="https://user-images.githubusercontent.com/59719711/81795631-49b47000-9547-11ea-9b2d-70d08594dd10.png">


    CCPR 플롯에서는 부분회귀 플롯과 달리 독립변수가 원래의 값 그대로 나타난다는 점을 다시 한번 상기 시켜줄게


```python
fig = plt.figure(figsize=(8, 15))
sm.graphics.plot_ccpr_grid(result_boston, fig=fig)
fig.suptitle("")
plt.show()
```

<img width="564" alt="output_36_0" src="https://user-images.githubusercontent.com/59719711/81795667-533dd800-9547-11ea-8b7d-5ca07cf8a5ed.png">


    plot_regress_exog(result, exog_idx)

    result: 회귀분석 결과 객체
    exog_idx: 분석 대상이 되는 독립변수 문자열


```python
fig = sm.graphics.plot_regress_exog(result_boston, "AGE")
plt.tight_layout(pad=4, h_pad=0.5, w_pad=0.5)
plt.show()
```


<img width="356" alt="output_38_0" src="https://user-images.githubusercontent.com/59719711/81795721-62248a80-9547-11ea-9e1f-12d645504968.png">
