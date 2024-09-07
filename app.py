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
fontname = st.selectbox("폰트 선택", unique(fontNames))

# 선택을 해서 fontname이 바뀌면 폰트가 바뀝니다.
plt.rc('font', family=fontname)

# DataFrame 생성
df = pd.DataFrame({
    '이름': ['영수', '철수', '민수'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 65.1]
})

st.dataframe(df, use_container_width=True)
# subplots를 실행하면 두 가지 값이 나옵니다. 
fig, ax = plt.subplots()
ax.bar(df['이름'], df['나이'])
st.pyplot(fig)