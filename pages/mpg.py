from nturl2path import url2pathname
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("# 🚗 🚕 🚙 💨")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

# 페이지를 읽을 때마다 캐시 적용시 부담이 덜간다
@st.cache
def load_data():
    data = pd.read_csv(url)
    return data

data_load_state = st.text('Loading data...')
mpg = load_data()
data_load_state.text("Done! (using st.cache)")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(mpg.model_year.min(),mpg.model_year.max()))))

# Sidebar - origin
sorted_unique_origin = sorted(mpg.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)

st.text(selected_origin)

if selected_year > 0 :
    mpg = mpg[mpg.model_year == selected_year]

if len(selected_origin) > 0:
    mpg = mpg[mpg.origin.isin(selected_origin)]

st.dataframe(mpg)

st.line_chart(mpg["mpg"])

st.bar_chart(mpg["mpg"])

fig, ax = plt.subplots()
sns.barplot(data=mpg, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)

# fig = sns.countplot(data=mpg, x="origin")
# st.pyplot(fig) # AttributeError ==> 지원 안됨

fig, ax = plt.subplots(figsize=(10, 3))
sns.countplot(data=mpg, x="origin").set_title("지역별 자동차 연비 데이터 수")
st.pyplot(fig)

pxh = px.histogram(mpg, x="origin", title="지역별 자동차 연비 데이터 수")
st.plotly_chart(pxh)

fig, ax = plt.subplots()
sns.heatmap(data=mpg.corr(), annot=True, fmt='.2f').set_title("변수간 상관 관계")
st.pyplot(fig)

