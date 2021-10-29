import pandas as pd
import streamlit as st
import numpy as np


st.write("""
         # Alles alles gute zum Geburtstag Niklas!!      
         
         """)
#ohne sidebar in der Mitte
x = st.slider('wie viel Spaß werden wir heute haben?')  
st.write(x, 'In Koffenheiten:', x * x)
st.image('Niklas.jpg', width= 250)

st.write('Deine Freunde Andre, Annie, Nina, Marco, Max, Lenni, Sarah und Clemens :)')
