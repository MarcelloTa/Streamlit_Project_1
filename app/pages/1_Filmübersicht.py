import pandas as pd
import streamlit as st

# Tab-Titel und -Icon festlegen:
st.set_page_config(page_title='FDF | Finde Deine Filme', page_icon=':film_frames:')

customers = pd.read_csv(r'../data/imdb_clean.csv')


categorical_cols = customers["Genre"].unique()


st.title("Die TOP 3, 5 oder 10 Filme :star:")

with st.form("Darstellungsform"):
    col1, col2, col3 = st.columns(3)

    with col1:
        # Selectbox erstellt einen Dropdown mit auswählbaren Werten:
        cat_selection = st.selectbox('Welches Genre interessiert Dich?',
                                     categorical_cols)
    with col2:
        target_selection = st.slider("Aus welchem Jahr?", min_value=1929, max_value=2025)
    with col3:
        top_n_movie = st.radio("Top 3, 5 oder 10 der Filme?", options=[3, 5, 10])
    # Übermittlungsknopf hinzufügen (ohne Knopf nicht sinnvoll):
    submit = st.form_submit_button('Filme anzeigen', type='primary')

if submit:
    if cat_selection and target_selection and top_n_movie:

        movie = customers[customers["Genre"].str.contains(cat_selection)& (customers["Year"]==target_selection)]

        rating_movie = movie.sort_values(by="Rating", ascending=False)

        top_movie = rating_movie.head(top_n_movie)

        st.write(top_movie[["Title", "Genre", "Year","Rating"]])

