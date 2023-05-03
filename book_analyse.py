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


st.markdown("<h3 id='part-1-age-analysis'>Part 1. 도서 분석</h3>", unsafe_allow_html=True)

books =  train[["Book-ID","Book-Title", "Book-Author", "Year-Of-Publication"]].drop_duplicates().merge(number_of_book_ratings, on="Book-ID")
books = books.join(average_book_rating, on="Book-ID")
books


popbooks = books.sort_values(by="N_ratings", ascending=False).nlargest(10, 'N_ratings')
popbooks


from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 10, 9

# seaborn 패키지로 barplot 그리기
sns.barplot(x='N_ratings', y='Book-Title', data=popbooks,palette='Set1')

# x축 레이블 90도 회전
plt.xticks(rotation=50)

# 그래프 제목 추가
plt.title('Top10 Books most read by users', fontsize=16)

# 그래프 출력
plt.show()



dashboard_url = "https://public.tableau.com/views/top30_16830926966980/1?:showVizHome=no&embed=true/language=ko-KR&:display_count=n&:origin=viz_share_link"
st.components.v1.html(f'<iframe src="{dashboard_url}" width="2000" height="2000"></iframe>')
