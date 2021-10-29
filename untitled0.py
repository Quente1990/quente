import pandas as pd
import streamlit as st
import numpy as np

enableCORS = False

st.write("""
         # Alles alles gute zum Geburtstag Niklas!!      
         
         """)
#ohne sidebar in der Mitte
x = st.slider('wie viel Spaß werden wir heute haben?')  
st.write(x, 'In Koffenheiten:', x * x)



st.write('Deine Freunde Andre, Annie, Nina, Marco, Max, Sarah und Clemens :)')