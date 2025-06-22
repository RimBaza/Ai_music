import streamlit as st
import pandas as pd


def load_data(url):
    
    st.write("Loading data...")
    df=pd.read_csv(url)
    return df



df=load_data("train.csv")
st.write("Data loaded successfully!")
st.dataframe(df)
st.button("Rerun")



x = st.slider('x') 

st.write(x,'seauare', x*x)


add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)