
import streamlit as st
import pandas

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


content2 = "Below you can find some of the projects I have worked on. Feel free to contact me!"
st.write(content2)


col3, colempty, col4 = st.columns([1.7, 0.1, 1.7])
df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")
