import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# DataFrame laden:
movies = pd.read_csv(r'../data/imdb_clean.csv')

# Tab-Titel und -Icon festlegen:
st.set_page_config(page_title='Finde Deine Filme', page_icon=':film_frames:')

# Überschrift der Seite:
st.title('Bewertungsentwicklung von Filmen nach Regisseur & Schauspieler')

### REGISSEUR ###
# Zentrierte Überschrift für die Regisseur-Analyse:
st.header('Analyse nach Regisseur')

# Eingabefeld und Auswahl der Bewertungsart:
with st.form('Auswahl_Regisseur'):
    col1, col2 = st.columns(2)

    # User-Input für den Namen des Regisseurs:
    with col1:
        name_director = st.text_input('Gib einen Regisseur-Namen ein:')
        genres = st.checkbox('Wähle Deine Genres:', )

    with col2:
        rating_type_director = st.radio('Wähle den Bewertungstyp:',
                                        ['Rating', 'Metascore'],
                                        key='director')

# Falls eine Eingabe durch den User getätigt wurde / vorhanden ist:
if name_director:
    # DataFrame nach Namen filtern und ggf. auf Variable speichern
    movies_director = (movies[
                       movies['Director']
                       .str.contains(name_director, case=False, na=False)
                       ])
    # Prüfen, ob überhaupt Filme gefunden wurden
    if not movies_director.empty:
        movies_director = movies_director.sort_values(by='Year')