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





dashboard_url = "https://public.tableau.com/views/top30_16830926966980/1?:showVizHome=no&embed=true/language=ko-KR&:display_count=n&:origin=viz_share_link"
components.html(
  """
  <iframe src="https://prod-apnortheast-a.online.tableau.com/t/informationvisualization/views/AccountTracking/AccountTracking?::embed=yes&:tabs=yes&:toolbar=yes&:origin=viz_share_link"
    width="1600" height="2000">
  </iframe>
  ""
