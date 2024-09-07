import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import pandas as pd

# 한글폰트를 적용하겠습니다.
# 현재 경로를 알기 위해서 os 모듈을 import 합니다.
import os
# 폰트 관련 설정을 해줍니다.
import matplotlib.font_manager as fm  

# 중복되지 않고 유일한 값을 반환합니다.
def unique(list):
    x = np.array(list)
    return np.unique(x)

# 폰트를 등록합니다.
# os.getcwd()는 현재 경로입니다.
font_dirs = [os.getcwd() + '/fonts']

# 현재 경로에 있는 fonts 폴더에서 폰트를 찾습니다.
font_files = fm.findSystemFonts(fontpaths=font_dirs)

# 폰트 매니저에 찾은 폰트를 추가합니다.
for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
fontNames = [f.name for f in fm.fontManager.ttflist]

# 폰트 이름으로 선태 박스를 만듭니다.
#fontname = st.selectbox("폰트 선택", unique(fontNames))

# 선택을 해서 fontname이 바뀌면 폰트가 바뀝니다.
plt.rc('font', family='NanumGothicOTF')

# CSV 파일 읽기
df = pd.read_csv('recycle data1.csv', encoding='cp949')


st.dataframe(df, use_container_width=True)
# subplots를 실행하면 두 가지 값이 나옵니다. 
fig, ax = plt.subplots()
bars = ax.barh(df['구분'], df['수도권'])
ax.set_title("수도권 재활용 가격 원/kg", fontsize=16)
# 레이블 값 추가 (막대 끝에 값 표시)
for bar in bars:
    width = bar.get_width()  # 막대의 길이 (값)
    ax.text(width, bar.get_y() + bar.get_height()/2,  # 텍스트 위치 설정
            f'{width:,.0f}',  # 소수점 없이 표시
            va='center',  # 세로 정렬: 중앙
            ha='left')  # 가로 정렬: 막대 오른쪽에 배치

st.pyplot(fig)