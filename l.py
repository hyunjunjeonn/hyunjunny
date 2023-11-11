import streamlit as st
import pandas as pd
import numpy as np

st.title('hello')

dataframe = pd.DataFrame({
  'first column': [3, 2, 3, 4],
  'second column': [30, 20, 30, 40]
})

st.dataframe(dataframe, use_container_width=False)


st.table(dataframe)

st.metric(label="온도", value="10'C", delta="1.2C")
st.metric(label="삼성전자", value="61000 원", delta="-3200 원")

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1200 원", delta="-200 원")
col2.metric(label="일본JPY(100엔)", value="958.62 원", delta="-2.44 원")
col3.metric(label="유럽연합EUR", value="1,335.85 원", delta="1.24 원")


tab1, tab2 = st.tab("Cat","Dog")

with tab1:
  st.header("A cat")
  st.image("R68eywp-W.jpg",width=200)

with tab2:
  st.header("A dog")
  st.image("R68eywp-W.jpg",width=200)
