

1. 파이썬 내장라이브러리 iplot

 - Plotly는 퀘벡 몬트리올에 본사가 있는 온라인 데이터 분석과 시각화 툴을 개발하는 테크 회사의 이름
 - import 방법 : import chart_studio.plotly as py
 - matplotlib 이나 seaborn 보다 그래프 시각화가 더 아름답고 웹상으로도 표현하는데 있어서 매우 훌륭함
 - 코드자체도 매우 쉬움
 - !pip install plotly
 - !pip install plotly --upgrade
 - 잦은 버전 업그레이드를 하므로 계속해서 업그레이드 해주는 것이 중요하다.
 - 웹상에서의 데이터 시각화와 오프라인상에서의 표현 코드가 다름
  - 즉 오프라인에서 데이터시각화 시, 코드를 명시해줘야함


'''
from plotly.offline import iplot
cf.go_offline()
'''
