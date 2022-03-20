import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(
   page_title='Boilerplate App',
   page_icon='chart_with_upwards_trend',
   layout='wide',
   initial_sidebar_state='expanded'
 )

with st.sidebar:
   selected = option_menu(
         menu_title="Main Menu",  # required
         options=["Home", "Projects", "Contact"],  # required
         icons=["house", "book", "envelope"],  # optional
         menu_icon="cast",  # optional
         default_index=0,  # optional
   )


st.title('Sample Title')

