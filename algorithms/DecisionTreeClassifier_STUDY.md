```python
from sklearn.datasets import load_iris
data = load_iris()
X = data.data
y = data.target

feature_names = data.feature_names[2:]

from sklearn.tree import DecisionTreeClassifier
tree1 = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=0).fit(X, y)
```


```python
from sklearn.metrics import classification_report
print(classification_report(y, tree1.predict(X)))
```

                  precision    recall  f1-score   support
    
               0       1.00      1.00      1.00        50
               1       0.98      1.00      0.99        50
               2       1.00      0.98      0.99        50
    
        accuracy                           0.99       150
       macro avg       0.99      0.99      0.99       150
    weighted avg       0.99      0.99      0.99       150
    



```python
from sklearn.model_selection import cross_val_score, KFold
cv = KFold(5, shuffle=True, random_state=0)
# cross_val_score(tree1, X, y, scoring='accuracy', cv=cv).mean()
cross_val_score(tree1, X, y, scoring='accuracy', cv=5).mean()
```




    0.9333333333333332




```python
mean_test_accuracy = []

for max_depth in np.arange(3,10):
    model = DecisionTreeClassifier(max_depth=max_depth)
    mean_test_accuracy.append(cross_val_score(model, X, y, scoring='accuracy', cv=5).mean())
    
# plt.plot(np.arange(3,10), train_accuracy)
plt.plot(np.arange(3,10), mean_test_accuracy)
plt.show()
```


<img width="386" alt="output_3_0" src="https://user-images.githubusercontent.com/59719711/83937926-b56abf80-a80b-11ea-8908-65cac9d1c7c0.png">




```python
from sklearn.tree import plot_tree

plot_tree(tree1)
plt.show() # 위의 tree1 모델 depth=4 를 따른 거임. 그래프 비율은 맞춰야할 필요 있음
```


<img width="357" alt="output_4_0" src="https://user-images.githubusercontent.com/59719711/83937931-c0255480-a80b-11ea-8073-0ca84ad9b0a0.png">


