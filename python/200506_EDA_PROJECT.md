
1. EDA PROJECT

	- 데이터프레임에 있는 0값(null값 아님) row 제거하기
		- '''  df = df[df.column명 != 0] '''
	- 2개의 다른 데이터 merge 하기
		- pd.merge(data1, data2, on=기준이 될 column, how='outer' / 'inner' (outer는 겹치는 부분이 없더라도 일단 출력, inner는 겹치는 부분만 출력)
	- null값 채우기
		- 결측값을 특정 값으로 채우기 (replace missing values with scalar value) : df.fillna(0) / string도 가능
		- 결측값을 앞 방향 혹은 뒷 방향으로 채우기 (fill gaps forward or backward) : fillna(method='ffill' or 'pad'), fillna(method='bfill' or 'backfill')
		- 앞/뒤 방향으로 결측값 채우는 회수를 제한하기 (limit the amount of filling)

     : fillna(method='ffill', limit=number), fillna(method='bfill', limit=number)
		- 결측값을 변수별 평균으로 대체하기(filling missing values with mean per columns)

      : df.fillna(df.mean()), df.where(pd.notnull(df), df.mean(), axis='columns')
	- matplotlib - 하나의 그래프에 여러 데이터 넣어 표현하기
		-''' plt.figure(figsize=(20,12))
		     plt.plot(x데이터, y데이터 등등등)
		     plt.plot(x데이터, y데이터 등등등)
			.
			.
			.		     
		     plt.show() '''
