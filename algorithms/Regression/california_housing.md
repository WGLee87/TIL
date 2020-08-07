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
import statsmodels.api as sm
from sklearn.datasets import fetch_california_housing
```


```python
cal_data = fetch_california_housing()
dfx = pd.DataFrame(cal_data.data, columns=cal_data.feature_names)
dfy = pd.DataFrame(cal_data.target, columns=['Price'])
df = pd.concat([dfx,dfy], axis=1)
df.tail(2)
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
      <th>MedInc</th>
      <th>HouseAge</th>
      <th>AveRooms</th>
      <th>AveBedrms</th>
      <th>Population</th>
      <th>AveOccup</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20638</th>
      <td>1.8672</td>
      <td>18.0</td>
      <td>5.329513</td>
      <td>1.171920</td>
      <td>741.0</td>
      <td>2.123209</td>
      <td>39.43</td>
      <td>-121.32</td>
      <td>0.847</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>2.3886</td>
      <td>16.0</td>
      <td>5.254717</td>
      <td>1.162264</td>
      <td>1387.0</td>
      <td>2.616981</td>
      <td>39.37</td>
      <td>-121.24</td>
      <td>0.894</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfX = sm.add_constant(dfx)
dfX.tail(2)
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
      <th>MedInc</th>
      <th>HouseAge</th>
      <th>AveRooms</th>
      <th>AveBedrms</th>
      <th>Population</th>
      <th>AveOccup</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20638</th>
      <td>1.0</td>
      <td>1.8672</td>
      <td>18.0</td>
      <td>5.329513</td>
      <td>1.171920</td>
      <td>741.0</td>
      <td>2.123209</td>
      <td>39.43</td>
      <td>-121.32</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>1.0</td>
      <td>2.3886</td>
      <td>16.0</td>
      <td>5.254717</td>
      <td>1.162264</td>
      <td>1387.0</td>
      <td>2.616981</td>
      <td>39.37</td>
      <td>-121.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
model = sm.OLS.from_formula("Price ~ " + "+".join(cal_data.feature_names), data=df)
# model = sm.OLS(dfy, dfX)

result = model.fit()
print(result.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  Price   R-squared:                       0.606
    Model:                            OLS   Adj. R-squared:                  0.606
    Method:                 Least Squares   F-statistic:                     3970.
    Date:                Fri, 07 Aug 2020   Prob (F-statistic):               0.00
    Time:                        14:01:41   Log-Likelihood:                -22624.
    No. Observations:               20640   AIC:                         4.527e+04
    Df Residuals:                   20631   BIC:                         4.534e+04
    Df Model:                           8                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept    -36.9419      0.659    -56.067      0.000     -38.233     -35.650
    MedInc         0.4367      0.004    104.054      0.000       0.428       0.445
    HouseAge       0.0094      0.000     21.143      0.000       0.009       0.010
    AveRooms      -0.1073      0.006    -18.235      0.000      -0.119      -0.096
    AveBedrms      0.6451      0.028     22.928      0.000       0.590       0.700
    Population -3.976e-06   4.75e-06     -0.837      0.402   -1.33e-05    5.33e-06
    AveOccup      -0.0038      0.000     -7.769      0.000      -0.005      -0.003
    Latitude      -0.4213      0.007    -58.541      0.000      -0.435      -0.407
    Longitude     -0.4345      0.008    -57.682      0.000      -0.449      -0.420
    ==============================================================================
    Omnibus:                     4393.650   Durbin-Watson:                   0.885
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):            14087.596
    Skew:                           1.082   Prob(JB):                         0.00
    Kurtosis:                       6.420   Cond. No.                     2.38e+05
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 2.38e+05. This might indicate that there are
    strong multicollinearity or other numerical problems.



```python
feature_names = list(cal_data.feature_names)
feature_names = ['scale({})'.format(name) for name in feature_names]

model_scaled = sm.OLS.from_formula('Price ~' + '+'.join(feature_names) , data=df)
result_scaled = model_scaled.fit()
print(result_scaled.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                  Price   R-squared:                       0.606
    Model:                            OLS   Adj. R-squared:                  0.606
    Method:                 Least Squares   F-statistic:                     3970.
    Date:                Fri, 07 Aug 2020   Prob (F-statistic):               0.00
    Time:                        14:01:03   Log-Likelihood:                -22624.
    No. Observations:               20640   AIC:                         4.527e+04
    Df Residuals:                   20631   BIC:                         4.534e+04
    Df Model:                           8                                         
    Covariance Type:            nonrobust                                         
    =====================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
    -------------------------------------------------------------------------------------
    Intercept             2.0686      0.005    410.326      0.000       2.059       2.078
    scale(MedInc)         0.8296      0.008    104.054      0.000       0.814       0.845
    scale(HouseAge)       0.1188      0.006     21.143      0.000       0.108       0.130
    scale(AveRooms)      -0.2655      0.015    -18.235      0.000      -0.294      -0.237
    scale(AveBedrms)      0.3057      0.013     22.928      0.000       0.280       0.332
    scale(Population)    -0.0045      0.005     -0.837      0.402      -0.015       0.006
    scale(AveOccup)      -0.0393      0.005     -7.769      0.000      -0.049      -0.029
    scale(Latitude)      -0.8999      0.015    -58.541      0.000      -0.930      -0.870
    scale(Longitude)     -0.8705      0.015    -57.682      0.000      -0.900      -0.841
    ==============================================================================
    Omnibus:                     4393.650   Durbin-Watson:                   0.885
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):            14087.596
    Skew:                           1.082   Prob(JB):                         0.00
    Kurtosis:                       6.420   Cond. No.                         6.67
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
data = sm.datasets.get_rdataset('Diamonds', package='Stat2Data')

df = data.data
dfx = df['Carat']
dfy = df['TotalPrice']
dfX = sm.add_constant(dfx)
df.tail(2)
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
      <th>Carat</th>
      <th>Color</th>
      <th>Clarity</th>
      <th>Depth</th>
      <th>PricePerCt</th>
      <th>TotalPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>349</th>
      <td>1.52</td>
      <td>F</td>
      <td>VS1</td>
      <td>70.4</td>
      <td>7634.3</td>
      <td>11604.1</td>
    </tr>
    <tr>
      <th>350</th>
      <td>1.72</td>
      <td>G</td>
      <td>VS1</td>
      <td>69.1</td>
      <td>8081.1</td>
      <td>13899.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
model = sm.OLS.from_formula('TotalPrice ~ Carat', data=df)
result = model.fit()
print(result.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:             TotalPrice   R-squared:                       0.863
    Model:                            OLS   Adj. R-squared:                  0.863
    Method:                 Least Squares   F-statistic:                     2204.
    Date:                Fri, 07 Aug 2020   Prob (F-statistic):          7.20e-153
    Time:                        14:02:18   Log-Likelihood:                -3293.1
    No. Observations:                 351   AIC:                             6590.
    Df Residuals:                     349   BIC:                             6598.
    Df Model:                           1                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept  -7181.2981    347.537    -20.663      0.000   -7864.828   -6497.769
    Carat       1.464e+04    311.815     46.946      0.000     1.4e+04    1.53e+04
    ==============================================================================
    Omnibus:                      159.724   Durbin-Watson:                   1.237
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1205.436
    Skew:                           1.734   Prob(JB):                    1.75e-262
    Kurtosis:                      11.390   Cond. No.                         4.31
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
model2 = sm.OLS.from_formula('TotalPrice ~ Carat + I(Carat **2)', data = df)
result2 = model2.fit()
print(result2.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:             TotalPrice   R-squared:                       0.926
    Model:                            OLS   Adj. R-squared:                  0.925
    Method:                 Least Squares   F-statistic:                     2168.
    Date:                Fri, 07 Aug 2020   Prob (F-statistic):          3.43e-197
    Time:                        14:02:28   Log-Likelihood:                -3186.0
    No. Observations:                 351   AIC:                             6378.
    Df Residuals:                     348   BIC:                             6390.
    Df Model:                           2                                         
    Covariance Type:            nonrobust                                         
    =================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
    ---------------------------------------------------------------------------------
    Intercept      -522.7021    466.292     -1.121      0.263   -1439.807     394.403
    Carat          2385.9862    752.545      3.171      0.002     905.878    3866.094
    I(Carat ** 2)  4498.2062    263.039     17.101      0.000    3980.860    5015.553
    ==============================================================================
    Omnibus:                      125.710   Durbin-Watson:                   1.864
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1166.009
    Skew:                           1.214   Prob(JB):                    6.37e-254
    Kurtosis:                      11.592   Cond. No.                         18.3
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
model3 = sm.OLS.from_formula('TotalPrice ~ Carat + I(Carat **2)+Depth', data = df)
result3 = model3.fit()
print(result3.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:             TotalPrice   R-squared:                       0.931
    Model:                            OLS   Adj. R-squared:                  0.930
    Method:                 Least Squares   F-statistic:                     1555.
    Date:                Fri, 07 Aug 2020   Prob (F-statistic):          8.83e-201
    Time:                        14:02:38   Log-Likelihood:                -3173.7
    No. Observations:                 351   AIC:                             6355.
    Df Residuals:                     347   BIC:                             6371.
    Df Model:                           3                                         
    Covariance Type:            nonrobust                                         
    =================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
    ---------------------------------------------------------------------------------
    Intercept      6343.0918   1436.487      4.416      0.000    3517.775    9168.408
    Carat          2950.0367    736.110      4.008      0.000    1502.237    4397.836
    I(Carat ** 2)  4430.3574    254.653     17.398      0.000    3929.499    4931.216
    Depth          -114.0769     22.662     -5.034      0.000    -158.649     -69.505
    ==============================================================================
    Omnibus:                       97.132   Durbin-Watson:                   2.036
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1252.377
    Skew:                           0.741   Prob(JB):                    1.12e-272
    Kurtosis:                      12.134   Cond. No.                         850.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
model4 = sm.OLS.from_formula('TotalPrice ~ Carat + I(Carat **2)+Depth+C(Color)+0', data = df)
result4 = model4.fit()
print(result4.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:             TotalPrice   R-squared:                       0.940
    Model:                            OLS   Adj. R-squared:                  0.939
    Method:                 Least Squares   F-statistic:                     595.7
    Date:                Fri, 07 Aug 2020   Prob (F-statistic):          1.28e-202
    Time:                        14:02:59   Log-Likelihood:                -3148.0
    No. Observations:                 351   AIC:                             6316.
    Df Residuals:                     341   BIC:                             6355.
    Df Model:                           9                                         
    Covariance Type:            nonrobust                                         
    =================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
    ---------------------------------------------------------------------------------
    C(Color)[D]    7298.8418   1367.466      5.337      0.000    4609.110    9988.573
    C(Color)[E]    6962.8167   1372.642      5.073      0.000    4262.905    9662.729
    C(Color)[F]    7550.5039   1386.740      5.445      0.000    4822.862    1.03e+04
    C(Color)[G]    6925.7723   1397.264      4.957      0.000    4177.431    9674.113
    C(Color)[H]    5591.5172   1429.135      3.913      0.000    2780.487    8402.547
    C(Color)[I]    3974.5666   1424.379      2.790      0.006    1172.892    6776.242
    C(Color)[J]    4931.2735   1721.706      2.864      0.004    1544.773    8317.774
    Carat          3896.8539    720.120      5.411      0.000    2480.417    5313.290
    I(Carat ** 2)  4172.6227    243.831     17.113      0.000    3693.020    4652.225
    Depth          -132.7053     21.527     -6.165      0.000    -175.048     -90.362
    ==============================================================================
    Omnibus:                       89.268   Durbin-Watson:                   1.992
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1250.277
    Skew:                           0.605   Prob(JB):                    3.21e-272
    Kurtosis:                      12.167   Cond. No.                     2.27e+03
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 2.27e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.



```python
model4 = sm.OLS.from_formula('TotalPrice ~ Carat+I(Carat **2)+Depth+C(Color)+0+C(Clarity)', data = df)
result4 = model4.fit()
print(result4.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:             TotalPrice   R-squared:                       0.963
    Model:                            OLS   Adj. R-squared:                  0.961
    Method:                 Least Squares   F-statistic:                     540.6
    Date:                Fri, 07 Aug 2020   Prob (F-statistic):          1.14e-227
    Time:                        14:03:21   Log-Likelihood:                -3064.6
    No. Observations:                 351   AIC:                             6163.
    Df Residuals:                     334   BIC:                             6229.
    Df Model:                          16                                         
    Covariance Type:            nonrobust                                         
    ======================================================================================
                             coef    std err          t      P>|t|      [0.025      0.975]
    --------------------------------------------------------------------------------------
    C(Color)[D]         1.009e+04   1167.587      8.638      0.000    7788.686    1.24e+04
    C(Color)[E]         1.014e+04   1190.425      8.519      0.000    7799.893    1.25e+04
    C(Color)[F]         1.023e+04   1195.910      8.551      0.000    7874.093    1.26e+04
    C(Color)[G]         9223.8155   1193.304      7.730      0.000    6876.477    1.16e+04
    C(Color)[H]         7934.6179   1220.097      6.503      0.000    5534.574    1.03e+04
    C(Color)[I]         6386.7296   1205.387      5.298      0.000    4015.622    8757.838
    C(Color)[J]         8452.9956   1451.292      5.824      0.000    5598.171    1.13e+04
    C(Clarity)[T.SI1]  -3074.6096    475.020     -6.473      0.000   -4009.018   -2140.201
    C(Clarity)[T.SI2]  -5427.2405    625.742     -8.673      0.000   -6658.133   -4196.348
    C(Clarity)[T.SI3]  -6846.8673   1169.744     -5.853      0.000   -9147.861   -4545.874
    C(Clarity)[T.VS1]   -976.5625    425.411     -2.296      0.022   -1813.385    -139.740
    C(Clarity)[T.VS2]  -1692.6303    431.115     -3.926      0.000   -2540.673    -844.587
    C(Clarity)[T.VVS1]   619.5188    482.109      1.285      0.200    -328.834    1567.871
    C(Clarity)[T.VVS2]  -823.9503    470.761     -1.750      0.081   -1749.980     102.080
    Carat               6232.4639    620.649     10.042      0.000    5011.589    7453.338
    I(Carat ** 2)       3555.0137    206.643     17.204      0.000    3148.529    3961.499
    Depth               -177.3032     17.545    -10.106      0.000    -211.816    -142.790
    ==============================================================================
    Omnibus:                      134.300   Durbin-Watson:                   1.914
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1368.675
    Skew:                           1.291   Prob(JB):                    6.25e-298
    Kurtosis:                      12.323   Cond. No.                     2.47e+03
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 2.47e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.



```python
fig = plt.figure(figsize=(16,8))
sm.graphics.plot_regress_exog(result, "Carat", fig=fig)
plt.tight_layout(pad=4, h_pad=0.5, w_pad=0.5)
plt.show()
```


<img width="1072" alt="output_12_0" src="https://user-images.githubusercontent.com/59719711/89611800-0acd5680-d8b9-11ea-8b79-f699f210b2f1.png">


```python
fig = plt.figure(figsize=(16,8))
sm.graphics.plot_regress_exog(result3, "Depth", fig=fig)
plt.tight_layout(pad=4, h_pad=0.5, w_pad=0.5)
plt.show()
```


<img width="1072" alt="output_13_0" src="https://user-images.githubusercontent.com/59719711/89611827-1caef980-d8b9-11ea-883b-4fd84b4637d1.png">


```python
cal_data = fetch_california_housing()
X = cal_data.data
y = cal_data.target
```

###### 최적 정규화 - 검증 성능 곡선


```python
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve

alphas = np.logspace(-4, 0, 200)

train_scores = []
test_scores = []
for alpha in alphas:
    model = Lasso(alpha=alpha)
    train_score = -mean_squared_error(y, model.fit(X, y).predict(X))
    test_score = np.mean(cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=10))
    train_scores.append(train_score)
    test_scores.append(test_score)

optimal_alpha = alphas[np.argmax(test_scores)]
optimal_score = np.max(test_scores)

plt.plot(alphas, test_scores, "-", label="검증 성능")
plt.plot(alphas, train_scores, "--", label="학습 성능")
plt.axhline(optimal_score, linestyle=':')
plt.axvline(optimal_alpha, linestyle=':')
plt.scatter(optimal_alpha, optimal_score)
plt.title("최적 정규화")
plt.ylabel('성능')
plt.xlabel('정규화 가중치')
plt.legend()
plt.show()
```


<img width="399" alt="output_16_0" src="https://user-images.githubusercontent.com/59719711/89611848-2afd1580-d8b9-11ea-9d84-033dd2f69717.png">


###### 다항회귀의 차수 결정


```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

n_samples = 100
np.random.seed(0)
X = np.sort(np.random.rand(n_samples))
y = np.sin(2 * np.pi * X) + np.random.randn(n_samples) * 0.5
X = X[:, np.newaxis]


model = Pipeline([("poly", PolynomialFeatures()),
                  ("lreg", LinearRegression())])

degrees = np.arange(1, 15)
train_scores, test_scores = validation_curve(
    model, X, y, "poly__degree", degrees, cv=100,
    scoring="neg_mean_squared_error")

plt.plot(degrees, test_scores.mean(axis=1), "o-", label="검증성능 평균")
plt.plot(degrees, train_scores.mean(axis=1), "o--", label="학습성능 평균")
plt.ylabel('성능')
plt.xlabel('다항 차수')
plt.legend()
plt.title("최적 정규화")
plt.show()
```


<img width="406" alt="output_18_0" src="https://user-images.githubusercontent.com/59719711/89611875-3cdeb880-d8b9-11ea-9c6c-a0931eedee44.png">


```python

```
