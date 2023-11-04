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
