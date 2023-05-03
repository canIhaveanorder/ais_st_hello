import streamlit as st
import pandas as pd
import numpy as np

st.header('고객분석')
st.sidebar.title('고객분석')

st.write("""
### Dataset
""")
df_train = pd.read_csv('data/AGE.csv')
st.dataframe(df_train)

