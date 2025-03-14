import pandas as pd
import plotly.express as px
import streamlit as st
import time
import datetime

st.set_page_config(page_title='Die besten Filme')


customers = pd.read_csv(r'C:\Users\Admin\Documents\DataCraft\11_Datenvisualisierung_mit_Python\Streamlit_Project_1\data\imdb_clean.csv')


genre_unique = customers["Genre"].unique()




#numerical_cols = customers['Year'].unique()
#values = st.slider("Year", min_value=1929, max_value=2025)


#year = customers[customers["Genre"].apply(lambda e:any(genre in e for genre in categorical_cols)) &
                 #customers["Year"].apply(lambda v:any(year in v for year in values))]

st.title("Die Top 3, 5 und 10 der Filme-App")

with st.form("Darstellungsform"):
    col1, col2, col3 = st.columns(3)

    with col1:
        # Selectbox erstellt einen Dropdown mit auswählbaren Werten:
        genre_selection = st.selectbox('Welche Kategorie interessiert dich?',
                                     genre_unique)
    with col2:
        #
        year_selection = st.slider('Aus welchem Jahr willst du den Film sehen?', min_value=1929, max_value=2025)
    with col3:
        top_selection = st.radio('Wie viele Filme?', options=[3, 5, 10])

    st.form_submit_button('Diagramm erstellen', type='primary')




if genre_selection and year_selection:

    movies_selection = customers[customers['Genre'].str.contains(genre_selection) & (customers['Year'] == year_selection)]

    st.write(movies_selection[['Title', 'Rating']])






    # Übermittlungsknopf hinzufügen (ohne Knopf nicht sinnvoll):


#scores_by_profession = (customers.groupby(categorical_cols)
 #                       [target_selection]
 #                       .mean()
  #                      .sort_values(ascending=False))