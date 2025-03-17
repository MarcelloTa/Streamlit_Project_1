import streamlit as st

# Tab-Titel und -Icon festlegen:
st.set_page_config(page_title='FDF | Finde Deine Filme',
                   page_icon=':film_frames:')

# Überschrift setzen
st.title("Finde Deine Filme :film_frames:")

# Grußzeile
st.write('Willkommen bei "Finde Deine Filme" - der App mit der Du '
         'Deine Lieblingsfilme findest.')

# Infotext zur App
st.write("Hier kannst Du Dir anhand eines Genres die Top 3, 5 oder 10 "
         "Filme eines bestimmten Jahres anzeigen lassen (Filmübersicht). "
         "Oder Du möchtest mehr Infos über einen bestimmten Film haben? "
         "Auch damit können wir Dir helfen (Detaillierte Filmangaben). "
         "Außerdem kannst Du nach einem bestimmten Regisseur oder Schauspieler "
         "suchen und Dir die Bewertungen der entsprechenden Filme anzeigen "
         "lassen (Filmstatistiken).")

# Trennstreifen mit extra Abstand darunter zum Ausgleich
st.divider()
st.markdown('')

# Link-Button zu den anderen Seiten
if st.button('Seite 1 - Filmübersicht :star:'):
    st.switch_page("pages/1_Filmübersicht.py")

if st.button('Seite 2 - Detaillierte Filmangaben :mag_right:'):
    st.switch_page("pages/2_Detaillierte_Filmangaben.py")

if st.button('Seite 3 - Filmstatistiken :clapper:'):
    st.switch_page("pages/3_Filmstatistiken.py")
