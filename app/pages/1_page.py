from cProfile import label

import pandas as pd
import plotly.express as px
import streamlit as st
import time
import datetime

st.set_page_config(page_title='Die besten Filme')


customers = pd.read_csv(r'C:\Users\Admin\Documents\GitHub\Streamlit_Project_1\data\imdb_clean.csv')
categorical_cols = customers["Genre"].unique()


st.title("Die Top 3, 5 und 10 der Filme-App")

with st.form("Darstellungsform"):
    col1, col2, col3 = st.columns(3)

    with col1:
        # Selectbox erstellt einen Dropdown mit auswählbaren Werten:
        cat_selection = st.selectbox('Welche Kategorie interessiert dich?',
                                     categorical_cols)
    with col2:
        target_selection = st.slider("Aus welchem Jahr möchtest du den Film ansehen?", min_value=1929, max_value=2025)
    with col3:
        top_n_movie = st.radio("Top 3, 5 und 10 der Filme.", options=[3,5,10])
    # Übermittlungsknopf hinzufügen (ohne Knopf nicht sinnvoll):
    st.form_submit_button('Diagramm erstellen', type='primary')

movie = customers[customers["Genre"].str.contains(cat_selection)& (customers["Year"]==target_selection)]

rating_movie = movie.sort_values(by="Rating", ascending=False)

top_movie = rating_movie.head(top_n_movie)

st.write(top_movie[["Title", "Genre", "Year","Rating"]])

