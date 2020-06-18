###### SQLAlchemy
    - 파이썬에서 사용한 ORM
        - ORM : Object Relational Mapping
            - 데이터베이스를 객체화 시켜서 데이터베이스에 있는 데이터를 CRUD 할 수 있다. / CRUD 는 crate, read, update, delete
            - 쿼리 대신 함수 형태로 CRUD를 할 수 있다.
            - 사용하는 데이터베이스를 변경하는 경우 엔진만 바꿔주면 됨
    - 설치 : pip install sqlalchemy


```python
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
```


```python
# 데이터베이스 연결
engine = create_engine('mysql://root:Lwglwk5120!@54.180.4.238/world')
engine

# ?charset=utf-8
```




    Engine(mysql://root:***@54.180.4.238/world)




```python
# 테이블 객체 생성을 위한 클래스 작성
Base = declarative_base()

class User(Base):
    __tablename__ = 'user1' # 테이블 이름
    
    # 컬럼 데이터 작성
    user_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    email = Column(String(30))
    age = Column(Integer)
    rdate = Column(DateTime)
    
    # 생성자 함수
    def __init__(self, name, email, age, rdate):
        self.name = name
        self.email = email
        self.age = age
        self.rdate = rdate
        
    # repr 함수
    def __repr__(self):
        return '<User {}, {}, {}, {}>'.format(
        self.name, self.email, self.age, self.rdate)
```


```python
# engine에 연결된 데이터베이스(world)에 테이블 생성
Base.metadata.create_all(engine)
```


```python
# 데이터베이스에 session 연결
Session = sessionmaker(engine)
session = Session()
session
```




    <sqlalchemy.orm.session.Session at 0x7fc006df0c50>




```python
# insert
user = User('jin', 'jin@gmail.com', 27, '2020-06-18')
user
```




    <User jin, jin@gmail.com, 27, 2020-06-18>




```python
session.add(user)
```


```python
# run transaction
session.commit()
```


```python
# many insert
users = [
    User('alice', 'alice@daum.net',34, '2020-06-17'),
    User('John', 'john@naver.com',31, '2020-06-16'),
    
]
```


```python
session.add_all(users)
```


```python
session.commit()
```


```python
# rollback : session에 있는 객체를 초기화
session.rollback()
```

###### 2. select


```python
# all
results = session.query(User).all()
list(results)
```




    [<User jin, jin@gmail.com, 27, 2020-06-18 00:00:00>,
     <User alice, alice@daum.net, 34, 2020-06-17 00:00:00>,
     <User John, john@naver.com, 31, 2020-06-16 00:00:00>]




```python
# filter : ==, !=, >, <, <=, >=, like, in_
results = session.query(User).filter(User.name == 'jin')
list(results)
```




    [<User jin, jin@gmail.com, 27, 2020-06-18 00:00:00>]




```python
# filter : like
results = session.query(User).filter(User.email.like('%gmail%'))
list(results)
```




    [<User jin, jin@gmail.com, 27, 2020-06-18 00:00:00>]




```python
# filter : in_
results = session.query(User).filter(User.name.in_(['alice', 'john']))
list(results)
```




    [<User alice, alice@daum.net, 34, 2020-06-17 00:00:00>,
     <User John, john@naver.com, 31, 2020-06-16 00:00:00>]




```python
# filter : or_
results = session.query(User).filter(
    or_(User.name == 'jin', User.age == 34)
)
list(results)
```




    [<User jin, jin@gmail.com, 27, 2020-06-18 00:00:00>,
     <User alice, alice@daum.net, 34, 2020-06-17 00:00:00>]




```python
# order by
results = session.query(User).order_by(User.age.asc())
list(results)
```




    [<User jin, jin@gmail.com, 27, 2020-06-18 00:00:00>,
     <User John, john@naver.com, 31, 2020-06-16 00:00:00>,
     <User alice, alice@daum.net, 34, 2020-06-17 00:00:00>]




```python
# count
session.query(User).count()
```




    3



###### 3. update


```python
data = session.query(User).filter(User.name == 'jin').one()
data
```




    <User jin, jin@gmail.com, 27, 2020-06-18 00:00:00>




```python
data.age = 30
```


```python
session.add(data)
session.commit()
```

###### 4. delete


```python
# delete
session.query(User).filter(User.name == 'john').delete()
```




    1




```python
session.commit()
```


```python
# delete table
User.__table__.drop(engine)
```

###### 5. with pandas


```python
import pandas as pd
import seaborn as sns
COLORS = sns.color_palette()
```

* 데이터 저장하기


```python
iris_df = sns.load_dataset('iris')
iris_df.tail(3)
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>virginica</td>
    </tr>
  </tbody>
</table>
</div>




```python
engine
```




    Engine(mysql://root:***@54.180.4.238/world)




```python
iris_df.to_sql(name='iris', con=engine, if_exists='replace')
```

* 데이터 가져오기


```python
engine = create_engine('mysql://root:Lwglwk5120!@54.180.4.238/world')
```


```python
QUERY = '''
    select *
    from city
'''

city_df = pd.read_sql(QUERY, engine)
city_df.tail(3) 
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
      <th>ID</th>
      <th>Name</th>
      <th>CountryCode</th>
      <th>District</th>
      <th>Population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4076</th>
      <td>4077</td>
      <td>Jabaliya</td>
      <td>PSE</td>
      <td>North Gaza</td>
      <td>113901</td>
    </tr>
    <tr>
      <th>4077</th>
      <td>4078</td>
      <td>Nablus</td>
      <td>PSE</td>
      <td>Nablus</td>
      <td>100231</td>
    </tr>
    <tr>
      <th>4078</th>
      <td>4079</td>
      <td>Rafah</td>
      <td>PSE</td>
      <td>Rafah</td>
      <td>92020</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
