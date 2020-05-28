
1. 분류모형의 종류, 분류 성능평가

- 크게 2가지로 나뉘는데,
	- 첫째 확률적 모형
	- 둘째 판별함수 모형
	이다.


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

###### 분류모형의 종류

    1. 확률적 모형(방법론)
        (1) 직접 조건부확률 함수의 모양을 추정하는 확률적 판별모형
        (2) *베이즈 정리를 사용한* 간접적으로 추정하는 확률적 생성모형
    2. 판별함수 모형(방법론)
    
    * 모형	       *  방법론
    LDA/QDA	확률적 생성모형
    나이브 베이지안	확률적 생성모형
    로지스틱 회귀	확률적 판별모형
    의사결정나무	확률적 판별모형
    퍼셉트론	판별함수 모형
    서포트벡터머신	판별함수 모형
    인공신경망	판별함수 모형
  

### 확률적 모형

    사이킷런 패키지에서 조건부확률  𝑃(𝑦=𝑘|𝑥) 을 사용하는 분류모형들은 모두 predict_proba 메서드와 predict_log_proba 메서드를 지원한다. 이 메서드들은 독립변수  𝑥 가 주어지면 종속변수  𝑦 의 모든 카테고리 값에 대해 조건부확률 또는 조건부확률의 로그값을 계산한다.
    
    log 확률값을 쓰는 이유는 값이 아주 작은 경우 부동소수점의 구별이 어렵고 오차가 발생할 우려가 있어서 그것을 더 정확하게 나타내기 위해 사용

##### 확률적 생성 모형

###### QDA
    QDA(Quadratic Discriminant Analysis)는 조건부확률 기반 생성(generative) 모형의 하나이다.


```python
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([0, 0, 0, 1, 1, 1])

plt.scatter(X[:3, 0], X[:3, 1], c="k", s=100, edgecolor='k', linewidth=2, label="y=0")
plt.scatter(X[3:, 0], X[3:, 1], c="w", s=100, edgecolor='k', linewidth=2, label="y=1")
plt.title("학습용 데이터")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.show()
```


<img width="399" alt="output_5_0" src="https://user-images.githubusercontent.com/59719711/82555383-9da40200-9ba2-11ea-96a3-5a0374106dee.png">



```python
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

model = QuadraticDiscriminantAnalysis().fit(X,y)
model
```




    QuadraticDiscriminantAnalysis(priors=None, reg_param=0.0,
                                  store_covariance=False, tol=0.0001)




```python
x = [[0, 0]]
p = model.predict_proba(x)[0]

plt.subplot(211)
plt.scatter(X[:3, 0], X[:3, 1], c="k", s=100, edgecolor='k', linewidth=2, label="y=0")
plt.scatter(X[3:, 0], X[3:, 1], c="w", s=100, edgecolor='k', linewidth=2, label="y=1")
plt.scatter(x[0][0], x[0][1], c='r', s=100, edgecolor='k', marker='x', linewidth=5)
plt.title("테스트 데이터")
plt.xlabel("x1")
plt.ylabel("x2")
plt.subplot(212)
plt.bar(model.classes_, p)
plt.title("조건부 확률분포")
plt.gca().xaxis.grid(False)
plt.xticks(model.classes_, ["$P(y=0|x_{test})$", "$P(y=1|x_{test})$"])
plt.ylabel("확률값")
plt.tight_layout()
plt.show()
```


<img width="420" alt="output_7_0" src="https://user-images.githubusercontent.com/59719711/82555399-a7c60080-9ba2-11ea-9270-425eac2f118a.png">


###### 나이브 베이지안 모형
    조건부확률 기반 생성 모형의 장점 중 하나는 클래스가 3개 이상인 경우에도 바로 적용할 수 있다는 점이며, 나이브 베이지안(Naive Bayesian) 모형도 조건부확률 모형의 일종이다.


```python
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

news = fetch_20newsgroups(subset="all")
model = Pipeline([
    ('vect', TfidfVectorizer(stop_words="english")),
    ('nb', MultinomialNB()),
])
model.fit(news.data, news.target)

n = 1
x = news.data[n:n + 1]
y = model.predict(x)[0]
print(x[0])
print("=" * 80)
print("실제 클래스:", news.target_names[news.target[n]])
print("예측 클래스:", news.target_names[y])
```

    From: mblawson@midway.ecn.uoknor.edu (Matthew B Lawson)
    Subject: Which high-performance VLB video card?
    Summary: Seek recommendations for VLB video card
    Nntp-Posting-Host: midway.ecn.uoknor.edu
    Organization: Engineering Computer Network, University of Oklahoma, Norman, OK, USA
    Keywords: orchid, stealth, vlb
    Lines: 21
    
      My brother is in the market for a high-performance video card that supports
    VESA local bus with 1-2MB RAM.  Does anyone have suggestions/ideas on:
    
      - Diamond Stealth Pro Local Bus
    
      - Orchid Farenheit 1280
    
      - ATI Graphics Ultra Pro
    
      - Any other high-performance VLB card
    
    
    Please post or email.  Thank you!
    
      - Matt
    
    -- 
        |  Matthew B. Lawson <------------> (mblawson@essex.ecn.uoknor.edu)  |   
      --+-- "Now I, Nebuchadnezzar, praise and exalt and glorify the King  --+-- 
        |   of heaven, because everything he does is right and all his ways  |   
        |   are just." - Nebuchadnezzar, king of Babylon, 562 B.C.           |   
    
    ================================================================================
    실제 클래스: comp.sys.ibm.pc.hardware
    예측 클래스: comp.sys.ibm.pc.hardware



```python
plt.subplot(211)
plt.bar(model.classes_, model.predict_proba(x)[0])
plt.xlim(-1, 20)
plt.gca().xaxis.grid(False)
plt.xticks(model.classes_)
plt.xlabel("카테고리(클래스)")
plt.ylabel("확률값")

plt.subplot(212)
plt.bar(model.classes_, model.predict_log_proba(x)[0])
plt.xlim(-1, 20)
plt.gca().xaxis.grid(False)
plt.xticks(model.classes_)
plt.xlabel("카테고리(클래스)")
plt.ylabel("확률의 로그값")
plt.suptitle("조건부 확률분포")

plt.show()
```


<img width="393" alt="output_10_0" src="https://user-images.githubusercontent.com/59719711/82555427-b57b8600-9ba2-11ea-8fee-5837cc30f419.png">



##### 확률적 판별 모형
    확률적 생성 모형의 경우 베이즈 정리를 통해 구한 반면 판별 모형은 직접 찾아내는 방법
    
        p(y = k | x = f(x)
        
    단, 이 함수  𝑓(𝑥) 는 0보다 같거나 크고 1보다 같거나 작다는 조건을 만족해야 한다.

###### 로지스틱 회귀 모형
    로지스틱 회귀 모형은 확률론적 판별 모형에 속한다.


```python
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

X0, y = make_classification(n_features=1, n_redundant=0,
                            n_informative=1, n_clusters_per_class=1, random_state=4)

model = LogisticRegression().fit(X0, y)

xx = np.linspace(-3, 3, 100)
XX = xx[:, np.newaxis]

prob = model.predict_proba(XX)[:, 1]
# prob = 1.0/(1 + np.exp(-model.coef_[0][0]*xx - model.intercept_[0]))

x_test = [[-0.2]]

plt.subplot(211)
plt.plot(xx, prob)
plt.scatter(X0, y, marker='o', c=y, s=100, edgecolor='k', linewidth=2)
plt.scatter(x_test[0], model.predict_proba(x_test)[0][1:], marker='x', s=500, c='r', lw=5)
plt.xlim(-3, 3)
plt.ylim(-.2, 1.2)
plt.xlabel("x")
plt.ylabel("y=0 또는 y=1일 확률")
plt.legend(["$P(y=1|x_{test})$"])
plt.subplot(212)
plt.bar(model.classes_, model.predict_proba(x_test)[0])
plt.xlim(-1, 2)
plt.gca().xaxis.grid(False)
plt.xticks(model.classes_, ["$P(y=0|x_{test})$", "$P(y=1|x_{test})$"])
plt.title("조건부 확률분포")
plt.xlabel("카테고리(클래스)")
plt.ylabel("확률값")
plt.tight_layout()
plt.show()
```


<img width="427" alt="output_13_0" src="https://user-images.githubusercontent.com/59719711/82555457-c1ffde80-9ba2-11ea-92e0-071969022a1d.png">




```python

```

### 판별함수 모형
    또 다른 분류 방법은 동일한 클래스가 모여 있는 영역과 그 영역을 나누는 경계면(boundary plane)을 정의하는 것.
    
            판별 경계선:𝑓(𝑥)=0
            클래스 1:𝑓(𝑥)>0
            클래스 0:𝑓(𝑥)<0

    사이킷런에서 판별함수 모형은 판별함수값을 출력하는 decision_function 메서드를 제공한다.
        * model.decision_function(x) > 나오는 값에 따라 클래스 판별

###### 퍼셉트론
    퍼셉트론(Perceptron)은 가장 단순한 판별함수 모형이다. 다음 그림과 같이 직선이 경계선(boundary line)으로 데이터 영역을 나눈다.


```python
from sklearn.linear_model import Perceptron
from sklearn.datasets import load_iris
iris = load_iris()
idx = np.in1d(iris.target, [0, 2])
X = iris.data[idx, 0:2]
y = iris.target[idx]

model = Perceptron(max_iter=100, eta0=0.1, random_state=1).fit(X, y)
XX_min, XX_max = X[:, 0].min() - 1, X[:, 0].max() + 1
YY_min, YY_max = X[:, 1].min() - 1, X[:, 1].max() + 1
XX, YY = np.meshgrid(np.linspace(XX_min, XX_max, 1000),
                     np.linspace(YY_min, YY_max, 1000))
ZZ = model.predict(np.c_[XX.ravel(), YY.ravel()]).reshape(XX.shape)
plt.contour(XX, YY, ZZ, colors='k')
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, edgecolor='k', linewidth=1)

idx = [22, 36, 70, 80]
plt.scatter(X[idx, 0], X[idx, 1], c='r', s=100, alpha=0.5)
for i in idx:
    plt.annotate(i, xy=(X[i, 0], X[i, 1] + 0.1))
plt.grid(False)
plt.title("퍼셉트론의 판별영역")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()
```


<img width="393" alt="output_17_0" src="https://user-images.githubusercontent.com/59719711/82555480-cf1ccd80-9ba2-11ea-8cee-6c5ff498af44.png">



```python
plt.bar(range(len(idx)), model.decision_function(X[idx]))
plt.xticks(range(len(idx)), idx)
plt.gca().xaxis.grid(False)
plt.title("각 데이터의 판별함수 값")
plt.xlabel("표본 번호")
plt.ylabel("판별함수값 f(x)")
plt.show()
```


<img width="387" alt="output_18_0" src="https://user-images.githubusercontent.com/59719711/82555500-dc39bc80-9ba2-11ea-8ecd-cb54055bbec2.png">



```python
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data[:, :2]
y = iris.target
idx = np.logical_or(iris.target == 0, iris.target == 1)
X = iris.data[idx, :3]
y = iris.target[idx]

fig = plt.figure()
ax = Axes3D(fig, elev=20, azim=10)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, marker='o', s=100, cmap=mpl.cm.jet)
ax.plot_surface(np.array([[4, 4], [7, 7]]), np.array([[2, 4.5], [2, 4.5]]),
                np.array([[2, 4], [2, 4]]), color='g', alpha=.3)
plt.title("3차원 특징데이터의 판별경계")
plt.xlabel("x")
plt.ylabel("y")
ax.set_zlabel("z")
plt.show()
# 하이퍼 플레인(decision hyperplane)
```


<img width="446" alt="output_19_0" src="https://user-images.githubusercontent.com/59719711/82555527-e6f45180-9ba2-11ea-9144-c572400b3d8e.png">


###### 커널 SVM(Kernel Support Vector Machine)


```python
from sklearn import svm

xx, yy = np.meshgrid(np.linspace(-3, 3, 500),
                     np.linspace(-3, 3, 500))
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)

model = svm.NuSVC().fit(X, Y)
Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
           origin='lower', cmap=plt.cm.PuOr_r)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=3)
plt.scatter(X[:, 0], X[:, 1], s=30, c=Y, cmap=plt.cm.Paired)
idx = [0, 20, 40, 60]
plt.scatter(X[idx, 0], X[idx, 1], c=Y[idx], s=200, alpha=0.5)
for i in idx:
    plt.annotate(i, xy=(X[i, 0], X[i, 1]+0.15), color='white')
plt.grid(False)
plt.axis([-3, 3, -3, 3])
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("커널 SVM의 판별영역")
plt.show()
```


<img width="391" alt="output_21_0" src="https://user-images.githubusercontent.com/59719711/82555553-f378aa00-9ba2-11ea-83e7-cf75713eaa74.png">



```python
plt.bar(range(len(idx)), model.decision_function(X[idx]))
plt.xticks(range(len(idx)), idx)
plt.gca().xaxis.grid(False)
plt.xlabel("표본 번호")
plt.ylabel("판별함수값 f(x)")
plt.title("각 데이터의 판별함수 값")
plt.show()
```


<img width="387" alt="output_22_0" src="https://user-images.githubusercontent.com/59719711/82555597-ff646c00-9ba2-11ea-9719-e4569ce5f62a.png">


### 다중 클래스 분류
    확률적 모형은 클래스가 3개 이상인 경우를 다중 클래스(Multi-Class) 분류문제도 풀 수 있지만 판별함수 모형은 종속변수의 클래스가 2개인 경우를 이진(Binary Class) 분류문제밖에는 풀지 못한다.

    이때는 OvO (One-Vs-One) 방법이나 OvR (One-vs-the-Rest) 방법 등을 이용하여 여러개의 이진 클래스 분류문제로 변환하여 푼다.

##### OvO 방법
    OvO (One-Vs-One) 방법은  𝐾 개의 클래스가 존재하는 경우, 이 중 2개의 클래스 조합을 선택하여  𝐾(𝐾−1)/2 개의 이진 클래스 분류문제를 풀고 이진 분류문제를 풀어 가장 많은 결과가 나온 클래스를 선택하는 방법이다. 선택받은 횟수로 선택하면 횟수가 같은 경우도 나올 수 있기 때문에 각 클래스가 얻은 조건부 확률값을 모두 더한 값을 비교하여 가장 큰 조건부 확률 총합을 가진 클래스를 선택한다.

##### OvR 방법
    OvO 방법은 클래스의 수가 많아지면 실행해야 할 이진 분류문제의 수가 너무 많아진다.
    OvR(One-vs-the-Rest) 방법은  𝐾 개의 클래스가 존재하는 경우, 각각의 클래스에 대해 표본이 속하는지(y=1) 속하지 않는지(y=0)의 이진 분류문제를 푼다. OvO와 달리 클래스 수만큼의 이진 분류문제를 풀면 된다.
    OvR에서도 판별 결과의 수가 같은 동점 문제가 발생할 수가 있기 때문에 각 클래스가 얻은 조건부 확률값을 더해서 이 값이 가장 큰 클래스를 선택한다.


```python

```


```python

```

# 분류 성능평가

    confusion_matrix(y_true, y_pred)
    accuracy_score(y_true, y_pred)
    precision_score(y_true, y_pred)
    recall_score(y_true, y_pred)
    fbeta_score(y_true, y_pred, beta)
    f1_score(y_true, y_pred)
    classfication_report(y_true, y_pred)
    roc_curve
    auc


```python
from sklearn.metrics import confusion_matrix

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
```


```python
confusion_matrix(y_true, y_pred)
```




    array([[2, 0, 0],
           [0, 0, 1],
           [1, 0, 2]])



     실제/예측    P     N
       P(양성)    TP    FN
       N(음성)    FP    TN


```python
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [0, 0, 1, 1, 0, 1]
confusion_matrix(y_true, y_pred)
```




    array([[2, 0],
           [1, 3]])




```python
# 순서가 양성, 음성 순으로 고정 시키려면
confusion_matrix(y_true, y_pred, labels=[1,0])
```




    array([[3, 1],
           [0, 2]])



###### 평가점수
이진 분류평가표로부터 하나의 평가점수(score)를 계산하여 그 값을 최종적인 기준으로 사용하는 경우가 많다. 이 때도 관점에 따라 다양한 평가점수가 쓰인다.
    
    정확도¶
    정확도(accuracy)는 전체 샘플 중 맞게 예측한 샘플 수의 비율을 뜻한다. 높을수록 좋은 모형이다. 일반적으로 학습에서 최적화 목적함수로 사용된다.

    accuracy=𝑇𝑃+𝑇𝑁 / 𝑇𝑃+𝑇𝑁+𝐹𝑃+𝐹𝑁

    정밀도¶
    정밀도(precision)은 양성 클래스에 속한다고 출력한 샘플 중 실제로 양성 클래스에 속하는 샘플 수의 비율을 말한다. 높을수록 좋은 모형이다. FDS의 경우, 사기 거래라고 판단한 거래 중 실제 사기 거래의 비율이 된다.

    precision=𝑇𝑃 / 𝑇𝑃+𝐹𝑃

    재현율¶
    재현율(recall)은 실제 양성 클래스에 속한 표본 중에 양성 클래스에 속한다고 출력한 표본의 수의 비율을 뜻한다. 높을수록 좋은 모형이다. FDS의 경우 실제 사기 거래 중에서 실제 사기 거래라고 예측한 거래의 비율이 된다. TPR(true positive rate) 또는 민감도(sensitivity)라고도 한다.

    recall=𝑇𝑃 / 𝑇𝑃+𝐹𝑁

    위양성율¶
    위양성율(fall-out)은 실제 양성 클래스에 속하지 않는 표본 중에 양성 클래스에 속한다고 출력한 표본의 비율을 말한다. 다른 평가점수와 달리 낮을수록 좋은 모형이다. FDS의 경우에는 실제로는 정상 거래인데 FDS가 사기 거래라고 예측한 거래의 비율이 된다. FPR(false positive rate)또는 1에서 위양성률의 값을 뺀 값을 특이도(specificity)라고도 한다.

    fallout=𝐹𝑃 / 𝐹𝑃+𝑇𝑁

    F점수¶
    정밀도와 재현율의 가중조화평균(weight harmonic average)을 F점수(F-score)라고 한다. 정밀도에 주어지는 가중치를 베타(beta)라고 한다.

    𝐹𝛽=(1+𝛽2)(precision×recall) / (𝛽2precision+recall)

    베타가 1인 경우를 특별히 F1점수라고 한다.

    𝐹1=2⋅precision⋅recall/(precision+recall)


```python
from sklearn.metrics import classification_report

y_true = [0, 0, 0, 1, 1, 0, 0]
y_pred = [0, 0, 0, 0, 1, 1, 1]

print(classification_report(y_true, y_pred, target_names=['class 0', 'class 1']))
```

                  precision    recall  f1-score   support
    
         class 0       0.75      0.60      0.67         5
         class 1       0.33      0.50      0.40         2
    
        accuracy                           0.57         7
       macro avg       0.54      0.55      0.53         7
    weighted avg       0.63      0.57      0.59         7
    



```python
y_true = [0, 0, 1, 1, 2, 2, 2]
y_pred = [0, 0, 1, 2, 2, 2, 1]
target_names = ['class 0', 'class 1', 'class 2']
print(classification_report(y_true, y_pred, target_names=target_names))
```

                  precision    recall  f1-score   support
    
         class 0       1.00      1.00      1.00         2
         class 1       0.50      0.50      0.50         2
         class 2       0.67      0.67      0.67         3
    
        accuracy                           0.71         7
       macro avg       0.72      0.72      0.72         7
    weighted avg       0.71      0.71      0.71         7
    


##### ROC 커브¶
    위에서 설명한 각종 평가 점수 중 재현율(recall)과 위양성률(fall-out)은 일반적으로 양의 상관 관계가 있다.
    ROC(Receiver Operator Characteristic) 커브는 클래스 판별 기준값의 변화에 따른 위양성률(fall-out)과 재현율(recall)의 변화를 시각화


```python
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

X, y = make_classification(n_samples=16, n_features=2,
                           n_informative=2, n_redundant=0,
                           random_state=0)

model = LogisticRegression().fit(X, y)
y_hat = model.predict(X)
f_value = model.decision_function(X)

df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=["f", "y_hat", "y"])
df.sort_values("f", ascending=False).reset_index(drop=True)
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
      <th>f</th>
      <th>y_hat</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.363163</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.065047</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.633657</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.626171</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.624967</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.219678</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.378296</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.094285</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-0.438666</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-0.765888</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>-0.926932</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>-1.046770</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-1.214700</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-1.429382</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-2.081586</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>-4.118969</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
confusion_matrix(y, y_hat, labels=[1, 0])
```




    array([[7, 1],
           [1, 7]])




```python
recall = 7 / (6 + 2)
fallout = 1 / (1 + 7)
print("recall =", recall)
print("fallout =", fallout)
```

    recall = 0.875
    fallout = 0.125



```python
from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y, model.decision_function(X))
fpr, tpr, thresholds
```




    (array([0.   , 0.   , 0.   , 0.125, 0.125, 0.375, 0.375, 1.   ]),
     array([0.   , 0.125, 0.75 , 0.75 , 0.875, 0.875, 1.   , 1.   ]),
     array([ 3.36316277,  2.36316277,  1.21967832,  0.37829565,  0.09428499,
            -0.76588836, -0.92693183, -4.11896895]))




```python
fpr, tpr, thresholds = roc_curve(y, model.predict_proba(X)[:, 1])
fpr, tpr, thresholds
```




    (array([0.   , 0.   , 0.   , 0.125, 0.125, 0.375, 0.375, 1.   ]),
     array([0.   , 0.125, 0.75 , 0.75 , 0.875, 0.875, 1.   , 1.   ]),
     array([1.9139748 , 0.9139748 , 0.77200693, 0.59346197, 0.5235538 ,
            0.31736921, 0.28354759, 0.01600107]))




```python
plt.plot(fpr, tpr, 'o-', label="Logistic Regression")
plt.plot([0, 1], [0, 1], 'k--', label="random guess")
plt.plot([fallout], [recall], 'ro', ms=10)
plt.xlabel('위양성률(Fall-Out)')
plt.ylabel('재현률(Recall)')
plt.title('Receiver operating characteristic example')
plt.show()
```


<img width="393" alt="output_43_0" src="https://user-images.githubusercontent.com/59719711/82555629-1014e200-9ba3-11ea-9fcf-25fe1c5c9d38.png">



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
