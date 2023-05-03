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

    html_temp = """
    <div class='tableauPlaceholder' id='viz1608299294117' style='position: relative'><noscript><a href='#'><img alt=' '
                src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;Top1YoutubeInfluencerinallCountries&#47;Dashboard1&#47;1_rss.png'
                style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='Top1YoutubeInfluencerinallCountries&#47;Dashboard1' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image'
            value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;Top1YoutubeInfluencerinallCountries&#47;Dashboard1&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en' /></object></div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1608299294117');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) {
        vizElement.style.width = '1130px';
        vizElement.style.height = '727px';
    } else if (divElement.offsetWidth > 500) {
        vizElement.style.width = '1130px';
        vizElement.style.height = '727px';
    } else {
        vizElement.style.width = '100%';
        vizElement.style.height = '1527px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
    """
    components.html(html_temp, width=1130, height=700)
    st.markdown(f'Link to the public dashboard [here](https://public.tableau.com/views/Top1YoutubeInfluencerinallCountries/Dashboard1?:language=en&:display_count=y&:origin=viz_share_link)')
    st.markdown(f"**Data source and information about data collect can be found on [AccreditedDebtRelief website](https://www.accrediteddebtrelief.com/blog/every-countrys-most-popular-youtuber/)**")

    max_width_str = f"max-width: 1030px;"
    st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)
