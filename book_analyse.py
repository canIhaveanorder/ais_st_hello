import streamlit as st
import pandas as pd
import numpy as np

st.header('고객분석')
st.sidebar.title('고객분석')

### Dataset
""")
df_train = pd.read_csv('data/AGE.csv')
st.dataframe(df_train)




js = "window.scrollTo(0, document.getElementById('part-1-age-analysis').offsetTop);"
