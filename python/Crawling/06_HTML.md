##### 1. HTML (Hyper Text Markup Language)
    - 웹 문서를 작성하는 마크업 언어
    - 웹 페이지를 구성하는 언어
        - HTML : 화면의 레이아웃이나 텍스트
        - CSS : 화면의 색상, 크기 등의 스타일
        - Javasript : 화면의 클릭, 드래그 등등의 이벤트 

###### 1-1 HTML의 구성요소
    - Document
        - 페이지 전체
    - Element
        - 계층적 구조로 이루어져 있으며 모여서 Document를 이룸
        - 시작 태그와 끝 태그로 구성
    - Tag
        - 시작태그와 끝 태그로 구성된 엘리먼트 존재
        - 시작태그에는 여러가지 속성값이 존재
        - 태그와 태그 사이에는 문자열 데이터가 존재
        - 태그의 이름에 따라서 태그의 목적이 달라짐
    - Attribute
        - 시작태그 안에 포함되는 속성값
        - id, class
            - 엘리먼트를 선택하기 위한 목적으로 만들어진 속성값
        - 기타 등등


```python
%%html
<div class='wrapper'>
    <button id='btn-1', type='button'>HTML1</button>
    <button id='btn-2', type='button', style='color:red;'>HTML2</button>
</div>
```


<div class='wrapper'>
    <button id='btn-1', type='button'>HTML1</button>
    <button id='btn-2', type='button', style='color:red;'>HTML2</button>
</div>



###### 1-2 속성값
    - id : 웹페이지에서 유일한 값
    - class
        - 여러가지의 값 사용 가능
        - 하나의 엘리먼트에 여러가지 값 사용 가능


```python
%%html
<div class='wrapper'>
    <button id='btn-1', class='bt no1', type='button'>HTML1</button>
    <button id='btn-2', class='bt no2', type='button', style='color:grey;'>HTML2</button>
</div>
```


<div class='wrapper'>
    <button id='btn-1', class='bt no1', type='button'>HTML1</button>
    <button id='btn-2', class='bt no2', type='button', style='color:grey;'>HTML2</button>
</div>



###### 1-3 Tag의 종류
    - head : 제목을 나타낼때 사용
    - p : 한줄의 문자열을 출력하기 위한 태그
    - span : 한블럭의 문자열을 출력
    - div : 레이아웃을 나타내는 태그, 가장 많이 사용
    - table : row와 column이 있는 테이블 모양을 나타낼때 사용을 나타낼때 사용되는 태그


```python
%%html
<h1>FastCampus</h1>
<h2>FastCampus</h2>
<h3>FastCampus</h3>
<h4>FastCampus</h4>
<h5>FastCampus</h5>
<h6>FastCampus</h6>

<p>파이썬은 재미있습니다.</p>
<p>내일은 휴강입니다.</p>

<span>파이썬은 재미있습니다.</span>
<span>내일은 휴강입니다.</span>

#div
<div>
    <p>html1</p>
    <p>html2</p>
</div>
<div>
    <p>html3</p>
</div>

#테이블
<table>
    <caption>테이블 제목</caption>
    <thead>
        <tr>
            <th>코드</th>
            <th>회사명</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0001</td>
            <td>삼성전자</td>
        </tr>
         <tr>
            <td>0002</td>
            <td>GS</td>
        </tr>
    </tbody>
</table>
```


<h1>FastCampus</h1>
<h2>FastCampus</h2>
<h3>FastCampus</h3>
<h4>FastCampus</h4>
<h5>FastCampus</h5>
<h6>FastCampus</h6>

<p>파이썬은 재미있습니다.</p>
<p>내일은 휴강입니다.</p>

<span>파이썬은 재미있습니다.</span>
<span>내일은 휴강입니다.</span>

#div
<div>
    <p>html1</p>
    <p>html2</p>
</div>
<div>
    <p>html3</p>
</div>

#테이블
<table>
    <caption>테이블 제목</caption>
    <thead>
        <tr>
            <th>코드</th>
            <th>회사명</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0001</td>
            <td>삼성전자</td>
        </tr>
         <tr>
            <td>0002</td>
            <td>GS</td>
        </tr>
    </tbody>
</table>



ul, li : 리스트를 나타내는 태그


```python
%%html

<ul>
    <li>data1</li>
    <li>data2</li>
    <li>data3</li>
</ul>
```



<ul>
    <li>data1</li>
    <li>data2</li>
    <li>data3</li>
</ul>



a
 - 링크를 출력하는 태그
 - href 속성값에 이동할 URL 데이터를 넣음


```python
%%html

<a href='http://fastcampus.co.kr' target='_blank'>fast_campus</a>

<img style='width:300px;' src='http://image.dongascience.com/Photo/2019/11/18063021bb3d49392700c1eca527622b.jpg'>
```



<a href='http://fastcampus.co.kr' target='_blank'>fast_campus</a>

<img style='width:300px;' src='http://image.dongascience.com/Photo/2019/11/18063021bb3d49392700c1eca527622b.jpg'>



iframe : 외부 URL 링크의 페이지를 보여주기 위한 태그


```python
%%html

<iframe src='https://www.daum.co.kr/' width='100%' height='400px;'></iframe>
```



<iframe src='https://www.daum.co.kr/' width='100%' height='400px;'></iframe>



input
 - text
 - password
 - radio
 - checkbox


```python
%%html

<input type='text'></input>
<input type='password', placeholder='비밀번호'></input>
<input type='radio', name='data'>radio1</input>
<input type='radio', name='data'>radio2</input>
<input type='checkbox'>checkbox1</input>
```



<input type='text'></input>
<input type='password', placeholder='비밀번호'></input>
<input type='radio', name='data'>radio1</input>
<input type='radio', name='data'>radio2</input>
<input type='checkbox'>checkbox1</input>



select, option
 - 옵션을 선택할 수 있는 드랍다운 형태의 태그


```python
%%html
<select>
    <option>data1</option>
    <option>data2</option>
</select>
    
```


<select>
    <option>data1</option>
    <option>data2</option>
</select>





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


```python

```
