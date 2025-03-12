import pandas as pd
import plotly.express as px
import streamlit as st
import time

# Tab-Titel und -Icon festlegen
st.set_page_config(page_title='Finde Deine Filme', page_icon=':film_frames:')

# Überschrift der Seite
st.title('Beliebtheit von Filmen nach Regisseur / Schauspieler')

# Caching für das Laden der Daten
@st.cache_data
def load_movies():
    # Künstliche Verzögerung für den Ladeeffekt
    time.sleep(5)
    return pd.read_csv(r'../data/imdb_clean.csv')

# DataFrame auf Variable speichern
movies = load_movies

