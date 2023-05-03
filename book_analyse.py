import streamlit as st
import pandas as pd
import numpy as np

st.header('도서분석')
st.sidebar.title('도서분석')

st.write("""
### Dataset
""")
df_train = pd.read_csv('data/TRAIN.csv')
st.dataframe(df_train)

