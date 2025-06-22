import streamlit as st
import matplotlib.pyplot as plt


main_pag = st.Page("pages.py", title="Page 2", icon="❄️")

page_3 = st.Page("page2.py", title="Page 3", icon="🎉")

pg = st .navigation([main_pag, page_3])

pg.run()

