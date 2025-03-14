import streamlit as st

st.title("Startseite")


st.header("Gruppe 3 - Die Filmempfehlungs-App")
st.write("Willkommen auf unserer Filmempfehlungs-App.")
st.write("Hier kannst du dir anhand eines Genres die Top 3, 5 oder 10 "
         "Filme eines bestimmten Jahres anzeigen lassen.\n Oder du möchtest mehr Infos über einen bestimmten Film haben?"
         " Auch damit können wir dir helfen.\n Außerdem kannst du nach einem bestimmten Regisseur oder Schauspieler "
         "suchen und dir seine besten Filme anzeigen lassen.")

if st.button('Seite 1 - Filmübersicht'):
    st.switch_page("pages/1_Filmübersicht.py")
if st.button('Seite 2 - Detailierte Filmangaben'):
    st.switch_page("pages/2_Detailierte_Filmangaben.py")
if st.button('Seite 3 - Filmstatistiken'):
    st.switch_page("pages/3_Filmstatistiken.py")


