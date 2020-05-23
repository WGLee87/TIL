
1. 시계열 데이터 다루기

    - pandas에서 시계열 자료를 생성하는 방법은 인덱스를 DatatimeIndex 자료형으로 만들어야함.
    - '''
    pd.to_datetime, pd.date_range 로 사용한다. '''
    - 이미 생성되어 있는 데이터에서 시간형으로 바꿔주고자 할땐,,
    ''' df = pd.to_DataFrame([변수명], infer_datetime_format=True) ''' 로 설정하지만 상황에 따라서는 format=%Y%m%d 등 으로 형식을 지정해줘야 하는 경우도 있음.
    - resample 함수는 시간 간격을 재조정하는 리샘플링(resampling)이 가능하다.



2. 주가데이터 불러오기(FinanceReader)

    - FinanceDataReader 설치 후 import 하기 (설치는 터미널 혹은 주피터노트북에서 pip install -U finance_datareader)
    - import FinanceDataReader as fdr 로 데이터 불러오기
    - NASDAQ, KOSPI 등 전 세계 주가정보 데이터가 있음
    - 주가데이터 불러오기
    ''' df = fdr.DataReader('AAPL', '2019-04-01', '2019-04-30') '''



3. matplotlib 의 기능
    - plt.legend()는 그래프의 label을 붙여주는 기능이다.