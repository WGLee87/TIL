---
title: 선형회귀분석 정리
date: 2020-05-12 18:28:55
tags:
---

선형회귀분석 정리
오늘의 데이터 사이언스 스쿨에서는 본격적으로 제대로 된 선형회귀분석에 대해 배울 수 있었어. 또 배운 내용을 바탕으로 파이썬을 이용하여 패키지를 이용해 직접 구현해볼 수도 있었는데, 요약된 정보들이 가지는 함축적인 의미가 있어. 길고, 어려운 내용들이었지만 간신히 맥락은 잡고 있는 것 같아 잊기 전에 빠른 정리를 통해 복습을 하려고 해. listen.

우선 선형회귀분석이란, 종속 변수 y와 한 개 이상의 독립 변수 x와의 선형 관계를 모델링하는 방법이야. 사실 이런 단어들을 이용해 설명하면 쉬운 것도 어렵게 느껴지기 마련인데, 내가 수업시간에 깨달은 선형회귀분석 내용은 아래와 같아.

<img width="1214" alt="스크린샷 2020-05-12 오후 6 31 31" src="https://user-images.githubusercontent.com/59719711/81667918-e4954780-947e-11ea-9b8c-4591666ce580.png">

seaborn 데이터셋에 있는 tip 데이터를 가져와봤어. 총 지출 비용, 팁의 금액, 팁을 준 사람의 성별과 흡연 여부, 요일 시간, 함께 온 인원들의 정보 나열되어 있네. 막무가내로 서로 연관성 없이 나열되어 있는 것 같은 이 데이터들 속에서 그 어떤 상관성이 있을까?
가령, 식사 인원이 많으면 많을 수록 팁의 비용이 커지거나, 저녁 타임에 오는 손님이 팁을 더 많이 준다 등 데이터를 통해 이러한 인사이트를 얻어 내야 하는 것인데, 이러한 선형회귀분석은 이러한 데이터의 성별, 흡연여부, 식사 시간대 등과 같은 데이터(독립변수, x)들이 팁(종속변수, y)에 영향을 주는지, 혹은 영향을 주지 않는지, 영향을 주면 어떤 항목이 가장 영향을 많이 주는지 알 수 있는 방법 중에 하나라고 할 수 있지.

그렇다면 팁 데이터를 벡터값 y로 놓고 나머지 벡터들, 즉 나머지 행렬 데이터를 x로 놓고 일반적으로 알고 있는 'y = wx'를  만들 수 있겠지? 여기서 기울기에 해당하는 'w'가 바로 우리가 알고 싶어 하는 가중치라는 것이야. 
x의 항목들(성별, 흡연여부, 식사시간대 등) 중 어떤 항목이 팁이 많고 적음에 상관이 있는지, 즉 팁에 긍정적인 영향을 미쳐서 팁의 금액이 올라가게 하는지, 혹은 부정적인 영향을 미쳐서 팁의 금액을 내려가게 하는지, 혹은 전혀 상관이 없는지 말야.

이 때 wx를 x에 대한 함수로 나타난다면 y와 x 의 관계는 이렇게 정리할 수 있어.

![image](https://user-images.githubusercontent.com/59719711/81668790-1fe44600-9480-11ea-9fc9-3e84c3effece.png)   
(어렵다 참)

아무튼!

여기서 y 위의 ^와 물결표가 붙으면서 좀 더 깊게 들어가게 되는데, ^가 붙은 y를 y hat이라고 해. y는 우리가 마주하고 있는 현실 세계에서 일어난 실제 데이터이고, y hat은 예측한 가중치, w의 영향을 받은 '예측값'이라고 할 수 있어. 때문에 우리가 원하는 것은 어떤 값을 가질 지 모르는 가중치 w의 값을 조정하여 우리가 예측한 예측치 y hat과 실제 발생한 데이터 값 y의 차이(잔차)를 줄이는 것이라고 할 수 있지.

![image (1)](https://user-images.githubusercontent.com/59719711/81669155-c2042e00-9480-11ea-9862-63dcd2791f4c.png)

언급했던 y, y hat, w 모두는 스칼라 값이 아니라 벡터 혹은 행렬의 형태를 갖추고 있어. 위의 사진에서 가중치 값 w는 이 선형회귀 모형의 모수 즉 parameter 야. 그리고 x1, x2 ... 는 tip 데이터에서는 종속 변수 tip데이터를 제외한 나머지, 즉 성별, 흡연여부, 식사 시간대 등이 되는거야.

우선 선형회귀분석에 결정론적 방법과 확률론적 방법이라는 2가지 방법이 있어. 결정론적 방법은 단순하게 독립변수 x에 대응하는 종속변수 y 값을 계산하는 함수를 만들어 내는 것인 반면 확률론적 방법은 이름 그대로 x, y 뒤에 어떤 '확률 모형'이 숨어져 있다는 가정이 '추가'되는데, 이 가정이 추가됨으로써 결정론적 방법보다 더 많은 정보를 가지고 시작하게 된다고 할 수 있지.(비록 가정이라 할지라도) 더 많은 정보를 가지고 시작함으로써 결정론적 방법보다 조금 더 깊은 인사이트를 도출할 수 있어.




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




```python
sns.pairplot(df[['MEDV','RM']])
```




    <seaborn.axisgrid.PairGrid at 0x1a2a600f90>




<img width="361" alt="output_3_1" src="https://user-images.githubusercontent.com/59719711/81673250-4dcc8900-9486-11ea-98f7-683760804f5c.png">




```python
sns.pairplot(df[['MEDV','CRIM']])
```




    <seaborn.axisgrid.PairGrid at 0x1a2a60d0d0>




<img width="361" alt="output_4_1" src="https://user-images.githubusercontent.com/59719711/81673306-68066700-9486-11ea-8088-860245701f6e.png">



```python
sns.pairplot(df[['MEDV','AGE']])
```




    <seaborn.axisgrid.PairGrid at 0x1a2adfd150>




<img width="370" alt="output_5_1" src="https://user-images.githubusercontent.com/59719711/81673336-76548300-9486-11ea-9485-ba132d64d474.png">


```python
sns.pairplot(df[['MEDV','CHAS']])
```




    <seaborn.axisgrid.PairGrid at 0x1a2b239d50>




<img width="365" alt="output_6_1" src="https://user-images.githubusercontent.com/59719711/81673361-82404500-9486-11ea-88e0-0472e2c33a37.png">



```python
from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(dfx, dfy)
predicted = model.predict(dfx)
plt.scatter(dfy, predicted, s=10)
plt.xlabel("실제 가격")
plt.ylabel("예측 가격")
plt.title("보스턴 주택가격 예측결과")
plt.show()
```


<img width="389" alt="output_7_0" src="https://user-images.githubusercontent.com/59719711/81673398-8c624380-9486-11ea-9678-bac5f9e74d4c.png">



```python
import statsmodels.api as sm
```


```python
model = sm.OLS(dfy, dfx)
result = model.fit()
result.params
```




    CRIM      -0.092897
    ZN         0.048715
    INDUS     -0.004060
    CHAS       2.853999
    NOX       -2.868436
    RM         5.928148
    AGE       -0.007269
    DIS       -0.968514
    RAD        0.171151
    TAX       -0.009396
    PTRATIO   -0.392191
    B          0.014906
    LSTAT     -0.416304
    dtype: float64




```python
print(result.summary())
```

                                     OLS Regression Results                                
    =======================================================================================
    Dep. Variable:                   MEDV   R-squared (uncentered):                   0.959
    Model:                            OLS   Adj. R-squared (uncentered):              0.958
    Method:                 Least Squares   F-statistic:                              891.3
    Date:                Tue, 12 May 2020   Prob (F-statistic):                        0.00
    Time:                        19:14:28   Log-Likelihood:                         -1523.8
    No. Observations:                 506   AIC:                                      3074.
    Df Residuals:                     493   BIC:                                      3128.
    Df Model:                          13                                                  
    Covariance Type:            nonrobust                                                  
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    CRIM          -0.0929      0.034     -2.699      0.007      -0.161      -0.025
    ZN             0.0487      0.014      3.382      0.001       0.020       0.077
    INDUS         -0.0041      0.064     -0.063      0.950      -0.131       0.123
    CHAS           2.8540      0.904      3.157      0.002       1.078       4.630
    NOX           -2.8684      3.359     -0.854      0.394      -9.468       3.731
    RM             5.9281      0.309     19.178      0.000       5.321       6.535
    AGE           -0.0073      0.014     -0.526      0.599      -0.034       0.020
    DIS           -0.9685      0.196     -4.951      0.000      -1.353      -0.584
    RAD            0.1712      0.067      2.564      0.011       0.040       0.302
    TAX           -0.0094      0.004     -2.395      0.017      -0.017      -0.002
    PTRATIO       -0.3922      0.110     -3.570      0.000      -0.608      -0.176
    B              0.0149      0.003      5.528      0.000       0.010       0.020
    LSTAT         -0.4163      0.051     -8.197      0.000      -0.516      -0.317
    ==============================================================================
    Omnibus:                      204.082   Durbin-Watson:                   0.999
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1374.225
    Skew:                           1.609   Prob(JB):                    3.90e-299
    Kurtosis:                      10.404   Cond. No.                     8.50e+03
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 8.5e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.

