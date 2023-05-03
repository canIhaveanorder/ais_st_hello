import streamlit as st
import pandas as pd
import numpy as np

st.header('도서분석')
st.sidebar.title('도서분석')

st.sidebar.markdown("""
    ## 도서관련 분석
    - [part 1. 도서 분석](#part-1-book-analysis)
    - [part 2. 작가 분석](#part-2-author-analysis)
    - [part 3. 출판년도 분석](#part-3-publisher-analysis)
""")


st.write("""
### Dataset
""")
df_train = pd.read_csv('data/AGE.csv')
st.dataframe(df_train)




js = "window.scrollTo(0, document.getElementById('part-1-age-analysis').offsetTop);"
