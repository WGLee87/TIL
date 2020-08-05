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
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target
df.tail()
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
      <th>age</th>
      <th>sex</th>
      <th>bmi</th>
      <th>bp</th>
      <th>s1</th>
      <th>s2</th>
      <th>s3</th>
      <th>s4</th>
      <th>s5</th>
      <th>s6</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>437</th>
      <td>0.041708</td>
      <td>0.050680</td>
      <td>0.019662</td>
      <td>0.059744</td>
      <td>-0.005697</td>
      <td>-0.002566</td>
      <td>-0.028674</td>
      <td>-0.002592</td>
      <td>0.031193</td>
      <td>0.007207</td>
      <td>178.0</td>
    </tr>
    <tr>
      <th>438</th>
      <td>-0.005515</td>
      <td>0.050680</td>
      <td>-0.015906</td>
      <td>-0.067642</td>
      <td>0.049341</td>
      <td>0.079165</td>
      <td>-0.028674</td>
      <td>0.034309</td>
      <td>-0.018118</td>
      <td>0.044485</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>439</th>
      <td>0.041708</td>
      <td>0.050680</td>
      <td>-0.015906</td>
      <td>0.017282</td>
      <td>-0.037344</td>
      <td>-0.013840</td>
      <td>-0.024993</td>
      <td>-0.011080</td>
      <td>-0.046879</td>
      <td>0.015491</td>
      <td>132.0</td>
    </tr>
    <tr>
      <th>440</th>
      <td>-0.045472</td>
      <td>-0.044642</td>
      <td>0.039062</td>
      <td>0.001215</td>
      <td>0.016318</td>
      <td>0.015283</td>
      <td>-0.028674</td>
      <td>0.026560</td>
      <td>0.044528</td>
      <td>-0.025930</td>
      <td>220.0</td>
    </tr>
    <tr>
      <th>441</th>
      <td>-0.045472</td>
      <td>-0.044642</td>
      <td>-0.073030</td>
      <td>-0.081414</td>
      <td>0.083740</td>
      <td>0.027809</td>
      <td>0.173816</td>
      <td>-0.039493</td>
      <td>-0.004220</td>
      <td>0.003064</td>
      <td>57.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.pairplot(df[["target", "bmi"]])
plt.show()
```


<img width="378" alt="output_2_0" src="https://user-images.githubusercontent.com/59719711/89396986-3b42b280-d74a-11ea-8c75-65137d58c43e.png">


```python
import statsmodels.api as sm
model = sm.OLS.from_formula('target ~ age + bmi + bp + s1 + s2 + s3 + s4 + s5 + s6',\
                           data=df)
result = model.fit()
print(result.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                 target   R-squared:                       0.501
    Model:                            OLS   Adj. R-squared:                  0.490
    Method:                 Least Squares   F-statistic:                     48.11
    Date:                Wed, 05 Aug 2020   Prob (F-statistic):           8.80e-60
    Time:                        18:25:47   Log-Likelihood:                -2393.7
    No. Observations:                 442   AIC:                             4807.
    Df Residuals:                     432   BIC:                             4848.
    Df Model:                           9                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept    152.1335      2.618     58.105      0.000     146.987     157.280
    age          -33.1791     60.435     -0.549      0.583    -151.962      85.604
    bmi          557.0556     66.936      8.322      0.000     425.495     688.617
    bp           276.0860     65.307      4.227      0.000     147.727     404.445
    s1          -712.8060    423.044     -1.685      0.093   -1544.287     118.675
    s2           420.5672    344.309      1.221      0.223    -256.162    1097.296
    s3           139.5107    215.802      0.646      0.518    -284.641     563.662
    s4           126.2804    163.605      0.772      0.441    -195.280     447.841
    s5           756.3691    174.728      4.329      0.000     412.947    1099.791
    s6            48.9170     66.895      0.731      0.465     -82.563     180.397
    ==============================================================================
    Omnibus:                        5.600   Durbin-Watson:                   2.018
    Prob(Omnibus):                  0.061   Jarque-Bera (JB):                4.045
    Skew:                           0.094   Prob(JB):                        0.132
    Kurtosis:                       2.571   Cond. No.                         227.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
result.params
result.resid
```




    0     -55.117070
    1       6.927652
    2     -35.884060
    3      39.082034
    4       6.540158
             ...    
    437   -15.018028
    438     2.948301
    439    10.774945
    440     8.141105
    441     3.551810
    Length: 442, dtype: float64




```python
result.resid.plot(style="o")
plt.title("잔차 벡터")
plt.xlabel("데이터 번호")
plt.ylabel("잔차")
plt.show()
```


<img width="402" alt="output_5_0" src="https://user-images.githubusercontent.com/59719711/89397083-5ad9db00-d74a-11ea-9ba7-5272a65285e0.png">


###### sklearn으로 하는 선형회귀분석


```python
dfy = df['target']
dfX = df.drop(columns=['target'])
```


```python
from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True).fit(dfX, dfy)
predicted = model.predict(dfX)
print(model.coef_ , model.intercept_)

plt.scatter(dfy, predicted, s=20)
plt.xlabel("실제 위험도")
plt.ylabel("예측 위험도")
plt.title("당뇨병 진행 예측결과")
plt.show()

plt.figure(figsize=(16,6))
plt.plot(dfy)
plt.plot(predicted)
plt.xlabel("실제 위험도")
plt.ylabel("예측 위험도")
plt.title("선형회귀분석을 활용한 당뇨병 진행 예측결과 예측결과")
plt.show()
```

    [ -10.01219782 -239.81908937  519.83978679  324.39042769 -792.18416163
      476.74583782  101.04457032  177.06417623  751.27932109   67.62538639] 152.1334841628965



<img width="397" alt="output_8_1" src="https://user-images.githubusercontent.com/59719711/89397120-662d0680-d74a-11ea-8c5b-04a9009d24df.png">


<img width="955" alt="output_8_2" src="https://user-images.githubusercontent.com/59719711/89397150-704f0500-d74a-11ea-9d95-8701515cfcdf.png">


```python

```
