#### 2019시즌 K리그1 득점,실점 과 승점의 상관정도 구하기

#1.파일 불러오기
kleague_df = pd.read_csv('/Users/wglee/Desktop/2019k리그순위.csv')
kleague_df

#2. 득점, 실점, 승점 데이터변수 만들기
gf = kleague_df['득점']
ga = kleague_df['실점']
points = kleague_df['승점']
gf, ga, points

#3. 상관관계계수 구하기
gf_points = round(np.corrcoef(gf, points)[0,1],2)
ga_points = round(np.corrcoef(ga, points)[0,1],2)
gf_points, ga_points

#4. 결정계수 구하기
gf_points = round((gf_points)**2,2)*100
ga_points = round((ga_points)**2,2)*100
gf_points, ga_points
