
import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/mee2.jpg')

with col2:
    st.title('Muntazir')
    content = """
              Hey, I'm Muntazir — a passionate programmer, a dedicated high school student, 
              and, of course, a teenager who's always curious and eager to learn new things. 
              I enjoy solving problems through code and constantly challenging myself to 
              grow both academically and creatively.
              """
    st.info(content)
