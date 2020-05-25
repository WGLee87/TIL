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
from sklearn.datasets import make_classification

X0, y = make_classification(n_features=1, n_redundant=0, n_informative=1,
                            n_clusters_per_class=1, random_state=4)

plt.scatter(X0, y, c=y, s=100, edgecolor="k", linewidth=2)
sns.distplot(X0[y == 0, :], label="y = 0", hist=False)
sns.distplot(X0[y == 1, :], label="y = 1", hist=False)
plt.ylim(-0.2, 1.2)
plt.show()
```


<img width="383" alt="output_1_0" src="https://user-images.githubusercontent.com/59719711/82790812-a862dd80-9ea7-11ea-81b8-90c124467ce7.png">


```python
import statsmodels.api as sm
X = sm.add_constant(X0)
logit_mod = sm.Logit(y, X)
logit_res = logit_mod.fit(disp=0)
print(logit_res.summary())
```

                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:                      y   No. Observations:                  100
    Model:                          Logit   Df Residuals:                       98
    Method:                           MLE   Df Model:                            1
    Date:                Mon, 25 May 2020   Pseudo R-squ.:                  0.7679
    Time:                        13:36:07   Log-Likelihood:                -16.084
    converged:                       True   LL-Null:                       -69.295
    Covariance Type:            nonrobust   LLR p-value:                 5.963e-25
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const          0.2515      0.477      0.527      0.598      -0.683       1.186
    x1             4.2382      0.902      4.699      0.000       2.470       6.006
    ==============================================================================



```python
xx = np.linspace(-3, 3, 100)
mu = logit_res.predict(sm.add_constant(xx))
plt.plot(xx, mu, lw=3)
plt.scatter(X0, y, c=y, s=100, edgecolor="k", lw=2)
plt.scatter(X0, logit_res.predict(X), label=r"$\hat{y}$", marker='s', c=y,
            s=100, edgecolor="k", lw=1)
plt.xlim(-3, 3)
plt.xlabel("x")
plt.ylabel(r"$\mu$")
plt.title(r"$\hat{y} = \mu(x)$")
plt.legend()
plt.show()
```


<img width="397" alt="output_3_0" src="https://user-images.githubusercontent.com/59719711/82790836-b4e73600-9ea7-11ea-9dfe-51a074836992.png">



```python
mu = logit_res.predict(sm.add_constant(X0))
mu
```




    array([1.04929299e-01, 9.99641612e-01, 4.44440023e-03, 9.99530677e-01,
           3.58110343e-01, 2.04918708e-02, 6.54541453e-01, 3.86195551e-02,
           9.89842887e-01, 2.07101181e-01, 7.86433474e-02, 9.92499043e-01,
           1.50630826e-02, 5.68083738e-04, 9.56058664e-01, 4.41027755e-03,
           9.90604578e-01, 9.90156041e-01, 9.98459875e-01, 9.95363005e-01,
           1.45449074e-03, 4.34440146e-01, 9.93387015e-01, 7.34044423e-03,
           9.46515676e-01, 9.98426391e-01, 9.99386145e-01, 8.58894203e-01,
           9.59747694e-01, 7.11851272e-01, 9.93911870e-01, 4.73894928e-01,
           9.97206781e-01, 1.03660581e-04, 9.44052986e-03, 2.03216369e-02,
           1.49668272e-03, 3.71173753e-02, 2.01286880e-02, 9.98724376e-01,
           9.02914042e-01, 9.83073242e-01, 4.23156909e-02, 9.66926538e-02,
           9.28741299e-04, 2.02100167e-02, 9.51345273e-01, 2.13053815e-03,
           1.90089061e-01, 1.04659429e-01, 9.92878272e-01, 9.72218645e-01,
           9.94725175e-01, 2.07097110e-03, 9.98911959e-01, 1.00072555e-02,
           6.47690522e-02, 9.96179414e-01, 9.82916974e-01, 3.71171306e-02,
           1.62773237e-03, 6.47103122e-01, 9.89883441e-01, 9.94681728e-01,
           9.93039412e-01, 9.77691232e-02, 8.52160896e-01, 2.57051948e-02,
           9.99927870e-01, 9.89411582e-01, 1.37305649e-02, 1.29709701e-03,
           9.99921811e-01, 1.21937000e-01, 9.98965004e-01, 9.56721626e-04,
           4.85993984e-03, 9.87302191e-01, 9.96968199e-01, 9.74066666e-01,
           7.02069223e-01, 8.35170668e-02, 1.18959765e-02, 1.60209549e-03,
           9.27319686e-01, 1.78566748e-02, 5.28035658e-02, 9.62755919e-01,
           9.94462469e-01, 9.96864882e-01, 9.34759860e-01, 8.94057437e-01,
           1.48463930e-03, 9.99976779e-01, 8.89871359e-01, 4.51461349e-02,
           5.39111979e-02, 5.76801178e-02, 6.74988539e-02, 4.04127948e-01])




```python
plt.scatter(X0, y, c=y, s=100, edgecolor="k", lw=2, label="데이터")
plt.plot(X0, logit_res.fittedvalues * 0.1, label="판별함수값")
plt.legend()
plt.show()
```


<img width="391" alt="output_5_0" src="https://user-images.githubusercontent.com/59719711/82790861-bdd80780-9ea7-11ea-9e46-76de86986cd4.png">


###### 연습문제
    붓꽃 분류문제에서 클래스가 세토사와 베르시칼라 데이터만 사용하고 (setosa=0, versicolor=1) 독립변수로는 꽃받침 길이(Sepal Length)와 상수항만 사용하여 StatsModels 패키지의 로지스틱 회귀모형으로 결과를 예측하고 보고서를 출력한다. 이 보고서에서 어떤 값이 세토사와 베르시칼라를 구분하는 기준값(threshold)으로 사용되고 있는가?
    
    위 결과를 분류결과표(confusion matrix)와 분류결과보고서(classification report)로 나타내라.
    
    이 모형에 대해 ROC커브를 그리고 AUC를 구한다. 이 때 Scikit-Learn의 LogisticRegression을 사용하지 않고 위에서 StatsModels로 구한 모형을 사용한다.


```python
from sklearn.datasets import load_iris
iris = load_iris()
idx = np.in1d(iris.target, [0,1])
x = iris.data[idx,:1]
x0 = sm.add_constant(x)
y = iris.target[idx]
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])




```python
logit_result = sm.Logit(y,x0).fit(disp=0)
print(logit_result.summary())
```

                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:                      y   No. Observations:                  100
    Model:                          Logit   Df Residuals:                       98
    Method:                           MLE   Df Model:                            1
    Date:                Mon, 25 May 2020   Pseudo R-squ.:                  0.5368
    Time:                        14:38:28   Log-Likelihood:                -32.106
    converged:                       True   LL-Null:                       -69.315
    Covariance Type:            nonrobust   LLR p-value:                 6.320e-18
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const        -27.8315      5.434     -5.122      0.000     -38.481     -17.182
    x1             5.1403      1.007      5.107      0.000       3.168       7.113
    ==============================================================================



```python
print(logit_result.params)
round(logit_result.params[0] / logit_result.params[1],3)
```

    [-27.83145099   5.14033614]





    -5.414




```python
from sklearn.metrics import roc_curve
fpr, tpr, threshholds = roc_curve(y,logit_result.fittedvalues)
fpr, tpr, threshholds
```




    (array([0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
            0.02, 0.06, 0.06, 0.1 , 0.2 , 0.22, 0.28, 0.44, 0.6 , 0.68, 0.78,
            0.82, 0.9 , 0.92, 0.98, 1.  ]),
     array([0.  , 0.02, 0.06, 0.12, 0.16, 0.18, 0.22, 0.28, 0.32, 0.48, 0.52,
            0.58, 0.68, 0.78, 0.88, 0.9 , 0.9 , 0.92, 0.94, 0.98, 1.  , 1.  ,
            1.  , 1.  , 1.  , 1.  , 1.  ]),
     array([ 9.15090198,  8.15090198,  7.12283475,  6.60880114,  6.09476752,
             5.58073391,  5.0667003 ,  4.55266668,  4.03863307,  3.01056584,
             2.49653223,  1.98249861,  1.468465  ,  0.95443139,  0.44039777,
            -0.07363584, -0.58766946, -1.10170307, -1.61573668, -2.1297703 ,
            -2.64380391, -3.15783753, -3.67187114, -4.18590475, -4.69993837,
            -5.21397198, -5.72800559]))




```python
plt.plot(fpr, tpr, 'o-', label='logistic regression')
plt.plot([0,1],[0,1], 'k--')
plt.legend()
plt.show()
```


<img width="378" alt="output_11_0" src="https://user-images.githubusercontent.com/59719711/82790895-ccbeba00-9ea7-11ea-9dea-0c19be09b0be.png">



```python

```

###### 로지스틱 회귀를 사용한 이진 분류의 예¶

    Acceptance: 0이면 불합격, 1이면 합격
    BCPM: Bio/Chem/Physics/Math 과목의 학점 평균
    GPA: 전체과목 학점 평균
    VR: MCAT Verbal reasoning 과목 점수
    PS: MCAT Physical sciences 과목 점수
    WS: MCAT Writing sample 과목 점수
    BS: MCAT Biological sciences 과목 점수
    MCAT: MCAT 촘점
    Apps: 의대 지원 횟수


```python
data_med = sm.datasets.get_rdataset("MedGPA", package="Stat2Data")
df_med = data_med.data
df_med.tail()
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
      <th>Accept</th>
      <th>Acceptance</th>
      <th>Sex</th>
      <th>BCPM</th>
      <th>GPA</th>
      <th>VR</th>
      <th>PS</th>
      <th>WS</th>
      <th>BS</th>
      <th>MCAT</th>
      <th>Apps</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>D</td>
      <td>0</td>
      <td>M</td>
      <td>2.41</td>
      <td>2.72</td>
      <td>8</td>
      <td>8</td>
      <td>8.0</td>
      <td>8</td>
      <td>32</td>
      <td>7</td>
    </tr>
    <tr>
      <th>51</th>
      <td>D</td>
      <td>0</td>
      <td>M</td>
      <td>3.51</td>
      <td>3.56</td>
      <td>11</td>
      <td>8</td>
      <td>6.0</td>
      <td>9</td>
      <td>34</td>
      <td>6</td>
    </tr>
    <tr>
      <th>52</th>
      <td>A</td>
      <td>1</td>
      <td>F</td>
      <td>3.43</td>
      <td>3.48</td>
      <td>7</td>
      <td>10</td>
      <td>7.0</td>
      <td>10</td>
      <td>34</td>
      <td>14</td>
    </tr>
    <tr>
      <th>53</th>
      <td>D</td>
      <td>0</td>
      <td>M</td>
      <td>2.61</td>
      <td>2.80</td>
      <td>7</td>
      <td>5</td>
      <td>NaN</td>
      <td>6</td>
      <td>18</td>
      <td>6</td>
    </tr>
    <tr>
      <th>54</th>
      <td>D</td>
      <td>0</td>
      <td>M</td>
      <td>3.36</td>
      <td>3.44</td>
      <td>11</td>
      <td>11</td>
      <td>8.0</td>
      <td>9</td>
      <td>39</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.stripplot(x="GPA", y="Acceptance", data=df_med,
              jitter=True, orient='h', order=[1, 0])
plt.grid(True)
plt.show()

sns.stripplot('GPA', 'Acceptance', data=df_med, orient='h')
plt.grid(True)
plt.show()
```


<img width="382" alt="output_15_0" src="https://user-images.githubusercontent.com/59719711/82790922-d7794f00-9ea7-11ea-92f9-51bcb02d2269.png">



<img width="382" alt="output_15_1" src="https://user-images.githubusercontent.com/59719711/82790945-df38f380-9ea7-11ea-9fd5-82d774308cd4.png">



```python
med_model = sm.Logit.from_formula('Acceptance ~ Sex + BCPM + GPA + VR + PS + WS + BS + Apps', data=df_med).fit(disp=0)
print(med_model.summary())
```

                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:             Acceptance   No. Observations:                   54
    Model:                          Logit   Df Residuals:                       45
    Method:                           MLE   Df Model:                            8
    Date:                Mon, 25 May 2020   Pseudo R-squ.:                  0.5913
    Time:                        15:14:23   Log-Likelihood:                -15.160
    converged:                       True   LL-Null:                       -37.096
    Covariance Type:            nonrobust   LLR p-value:                 6.014e-07
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept    -46.6414     15.600     -2.990      0.003     -77.216     -16.067
    Sex[T.M]      -2.2835      1.429     -1.597      0.110      -5.085       0.518
    BCPM          -6.1633      6.963     -0.885      0.376     -19.811       7.484
    GPA           12.3973      8.611      1.440      0.150      -4.479      29.274
    VR             0.0790      0.311      0.254      0.799      -0.530       0.688
    PS             1.1673      0.539      2.164      0.030       0.110       2.225
    WS            -0.7784      0.396     -1.968      0.049      -1.554      -0.003
    BS             1.9184      0.682      2.814      0.005       0.582       3.255
    Apps           0.0512      0.147      0.348      0.728      -0.237       0.340
    ==============================================================================



```python
# df_med["Prediction"] = result_med.predict(df_med)
# sns.boxplot(x="Acceptance", y="Prediction", data=df_med)
# plt.show()

df_med['prediction'] = med_model.predict(df_med)
sns.boxplot('Acceptance', 'prediction', data=df_med)
plt.show()
```


<img width="393" alt="output_17_0" src="https://user-images.githubusercontent.com/59719711/82790973-ea8c1f00-9ea7-11ea-82b3-2a17c4b04331.png">



```python
med_model = sm.Logit.from_formula('Acceptance ~ PS + BS', data=df_med).fit(disp=0)
print(med_model.summary())
```

                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:             Acceptance   No. Observations:                   55
    Model:                          Logit   Df Residuals:                       52
    Method:                           MLE   Df Model:                            2
    Date:                Mon, 25 May 2020   Pseudo R-squ.:                  0.3315
    Time:                        15:17:31   Log-Likelihood:                -25.333
    converged:                       True   LL-Null:                       -37.896
    Covariance Type:            nonrobust   LLR p-value:                 3.503e-06
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept    -15.5427      4.684     -3.318      0.001     -24.723      -6.362
    PS             0.4798      0.316      1.518      0.129      -0.140       1.099
    BS             1.1464      0.387      2.959      0.003       0.387       1.906
    ==============================================================================


    위 결과를 바탕으로 0.4798PS+1.1464BS - 15.5427 의 점수가 0보다 크면 합격, 작으면 불합격을 의미

    위 결과를 바탕으로 다음 점수가 15.5427보다 크면 합격이라고 예측할 수 있다.
    0.4798PS+1.1464BS


```python
ps = 9.0
bs = 9.8

0.4798*ps + 1.1464*bs
```




    15.55292




```python

```

###### 연습문제
    붓꽃 분류문제에서 클래스가 베르시칼라(versicolor)와 버지니카(virginica) 데이터만 사용하여(versicolor=0, virginica=1) 로지스틱 회귀모형으로 결과를 예측하고 보고서를 출력한다. 독립변수는 모두 사용한다. 이 보고서에서 버지니카와 베르시칼라를 구분하는 경계면의 방정식을 찾아라.
    위 결과를 분류결과표와 분류결과보고서로 나타내라.
    이 모형에 대해 ROC커브를 그리고 AUC를 구하라. 이 때 Scikit-Learn의 LogisticRegression을 사용하지 않고 위에서 StatsModels로 구한 모형을 사용한다.


```python
from sklearn.datasets import load_iris
iris = load_iris()
idx = np.in1d(iris.target, [1,2])
w = pd.DataFrame(iris.data[idx], columns=iris.feature_names)
w0 = sm.add_constant(w)
z = iris.target[idx] - 1
```


```python
iris_model = sm.Logit(z, w0).fit(disp=0)
print(iris_model.summary())
```

                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:                      y   No. Observations:                  100
    Model:                          Logit   Df Residuals:                       95
    Method:                           MLE   Df Model:                            4
    Date:                Mon, 25 May 2020   Pseudo R-squ.:                  0.9142
    Time:                        15:46:54   Log-Likelihood:                -5.9493
    converged:                       True   LL-Null:                       -69.315
    Covariance Type:            nonrobust   LLR p-value:                 1.947e-26
    =====================================================================================
                            coef    std err          z      P>|z|      [0.025      0.975]
    -------------------------------------------------------------------------------------
    const               -42.6378     25.708     -1.659      0.097     -93.024       7.748
    sepal length (cm)    -2.4652      2.394     -1.030      0.303      -7.158       2.228
    sepal width (cm)     -6.6809      4.480     -1.491      0.136     -15.461       2.099
    petal length (cm)     9.4294      4.737      1.990      0.047       0.145      18.714
    petal width (cm)     18.2861      9.743      1.877      0.061      -0.809      37.381
    =====================================================================================
    
    Possibly complete quasi-separation: A fraction 0.60 of observations can be
    perfectly predicted. This might indicate that there is complete
    quasi-separation. In this case some parameters will not be identified.



```python
z_pred = iris_model.predict(w0) >= 0.5
```

    분류결과표(confusion matrix)와 분류결과보고서(classification report)


```python
from sklearn.metrics import confusion_matrix
confusion_matrix(z, z_pred)
```




    array([[49,  1],
           [ 1, 49]])




```python
from sklearn.metrics import classification_report
print(classification_report(z,z_pred))
```

                  precision    recall  f1-score   support
    
               0       0.98      0.98      0.98        50
               1       0.98      0.98      0.98        50
    
        accuracy                           0.98       100
       macro avg       0.98      0.98      0.98       100
    weighted avg       0.98      0.98      0.98       100
    



```python
from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(z, iris_model.fittedvalues)
plt.plot(fpr, tpr, 'o-')
plt.show()
```


<img width="378" alt="output_29_0" src="https://user-images.githubusercontent.com/59719711/82790994-f4ae1d80-9ea7-11ea-8610-c0f3f1f6fb91.png">



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
data_wrole = sm.datasets.get_rdataset("womensrole", package="HSAUR")
df_wrole = data_wrole.data
df_wrole["ratio"] = df_wrole.agree / (df_wrole.agree + df_wrole.disagree)
df_wrole.tail()
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
      <th>education</th>
      <th>sex</th>
      <th>agree</th>
      <th>disagree</th>
      <th>ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>37</th>
      <td>16</td>
      <td>Female</td>
      <td>13</td>
      <td>115</td>
      <td>0.101562</td>
    </tr>
    <tr>
      <th>38</th>
      <td>17</td>
      <td>Female</td>
      <td>3</td>
      <td>28</td>
      <td>0.096774</td>
    </tr>
    <tr>
      <th>39</th>
      <td>18</td>
      <td>Female</td>
      <td>0</td>
      <td>21</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>40</th>
      <td>19</td>
      <td>Female</td>
      <td>1</td>
      <td>2</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>41</th>
      <td>20</td>
      <td>Female</td>
      <td>2</td>
      <td>4</td>
      <td>0.333333</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 수동으로 종속변수값을 0~1 사이값으로 만들어줘야함 10점까지인거면 /10 100점까지면 /100
```


```python
sns.scatterplot('education', 'ratio', style='sex', data=df_wrole)
plt.show()
```


<img width="393" alt="output_38_0" src="https://user-images.githubusercontent.com/59719711/82791047-07285700-9ea8-11ea-8b94-81ae50444d08.png">



```python
model_wrole = sm.Logit.from_formula('ratio ~ education+sex', data=df_wrole).fit()
print(model_wrole.summary())
```

    Optimization terminated successfully.
             Current function value: 0.448292
             Iterations 6
                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:                  ratio   No. Observations:                   41
    Model:                          Logit   Df Residuals:                       38
    Method:                           MLE   Df Model:                            2
    Date:                Mon, 25 May 2020   Pseudo R-squ.:                  0.3435
    Time:                        16:18:18   Log-Likelihood:                -18.380
    converged:                       True   LL-Null:                       -27.997
    Covariance Type:            nonrobust   LLR p-value:                 6.660e-05
    ===============================================================================
                      coef    std err          z      P>|z|      [0.025      0.975]
    -------------------------------------------------------------------------------
    Intercept       2.0442      0.889      2.299      0.022       0.302       3.787
    sex[T.Male]    -0.1968      0.736     -0.267      0.789      -1.640       1.247
    education      -0.2127      0.071     -2.987      0.003      -0.352      -0.073
    ===============================================================================



```python
model_wrole = sm.Logit.from_formula('ratio ~ education', data=df_wrole).fit()
print(model_wrole.summary())
```

    Optimization terminated successfully.
             Current function value: 0.449186
             Iterations 6
                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:                  ratio   No. Observations:                   41
    Model:                          Logit   Df Residuals:                       39
    Method:                           MLE   Df Model:                            1
    Date:                Mon, 25 May 2020   Pseudo R-squ.:                  0.3422
    Time:                        16:31:45   Log-Likelihood:                -18.417
    converged:                       True   LL-Null:                       -27.997
    Covariance Type:            nonrobust   LLR p-value:                 1.202e-05
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept      1.9345      0.781      2.478      0.013       0.405       3.464
    education     -0.2117      0.071     -2.983      0.003      -0.351      -0.073
    ==============================================================================



```python
edu_pred = model_wrole.predict(df_wrole)
```


```python
sns.scatterplot(x="education", y="ratio", data=df_wrole)
xx = np.linspace(0, 20, 100)
df_wrole_p = pd.DataFrame({"education": xx})
plt.plot(xx, model_wrole.predict(df_wrole_p), "r-", lw=4, label="예측")
plt.legend()
plt.show()
```


<img width="393" alt="output_42_0" src="https://user-images.githubusercontent.com/59719711/82791065-0ee7fb80-9ea8-11ea-8060-df9573c0cb58.png">



```python

```
