import pandas as pd
import plotly.express as px
import streamlit as st

# DataFrame laden:
movies = pd.read_csv(r'../data/imdb_clean.csv')

# Tab-Titel und -Icon festlegen:
st.set_page_config(page_title='Finde Deine Filme', page_icon=':film_frames:', layout="wide")

# Initialisiere Session State für gespeicherte Werte
if 'director_plot' not in st.session_state:
    st.session_state.director_plot = None
if 'actor_plot' not in st.session_state:
    st.session_state.actor_plot = None

# Überschrift der Seite:
st.markdown("<h1 style='text-align: center;'><u>Bewertungsentwicklung</u></h1>", unsafe_allow_html=True)
st.markdown("")  # Abstand

# Zwei Spalten für Regisseur & Schauspieler
col1, col2 = st.columns(2)

### REGISSEUR ###
with col1:
    with st.container():  # Container für Formular + Diagramm
        st.header('Analyse nach Regisseur 🎬')

        with st.form('Auswahl_Regisseur'):
            name_director = st.text_input('**Gib einen Namen ein:**', value="")
            rating_type_director = st.radio('**Wähle die Bewertungsart:**', ['Rating', 'Metascore'], key='director')
            submit_director = st.form_submit_button('Diagramm erstellen', type='primary')

        # Falls Button gedrückt wurde:
        if submit_director and name_director:
            movies_director = movies[movies['Director'].str.contains(name_director, case=False, na=False)]
            if not movies_director.empty:
                movies_director = movies_director.sort_values(by='Year')

                fig = px.line(
                    movies_director,
                    x='Year',
                    y=rating_type_director,
                    markers=True,
                    hover_data={'Title': True}
                )

                fig.update_layout(
                    title=f'{rating_type_director}-Entwicklung für {name_director}',
                    title_font={'size': 20, 'weight': 'bold'},
                    title_x=0.27,
                    xaxis_title='Year',
                    yaxis_title=rating_type_director,
                    hovermode='closest'
                )

                fig.update_traces(line_color='#FF4B4B')
                st.session_state.director_plot = fig  # Speichern des Diagramms

            else:
                st.warning('Keine Filme für diese/n Regisseur/in gefunden.')

        # Zeige gespeicherten Plot an, falls vorhanden
        if st.session_state.director_plot:
            st.plotly_chart(st.session_state.director_plot, use_container_width=True)

### SCHAUSPIELER ###
with col2:
    with st.container():  # Container für Formular + Diagramm
        st.header('Analyse nach Schauspieler 🎭')

        with st.form('Auswahl_Schauspieler'):
            name_actor = st.text_input('**Gib einen Namen ein:**', value="")
            rating_type_actor = st.radio('**Wähle die Bewertungsart:**', ['Rating', 'Metascore'], key='actor')
            submit_actor = st.form_submit_button('Diagramm erstellen', type='primary')

        # Falls Button gedrückt wurde:
        if submit_actor and name_actor:
            movies_actor = movies[movies['Cast'].str.contains(name_actor, case=False, na=False)]
            if not movies_actor.empty:
                movies_actor = movies_actor.sort_values(by='Year')

                fig = px.line(
                    movies_actor,
                    x='Year',
                    y=rating_type_actor,
                    markers=True,
                    hover_data={'Title': True}
                )

                fig.update_layout(
                    title=f'{rating_type_actor}-Entwicklung für {name_actor}',
                    title_font={'size': 20, 'weight': 'bold'},
                    title_x=0.27,
                    xaxis_title='Year',
                    yaxis_title=rating_type_actor,
                    hovermode='closest'
                )

                fig.update_traces(line_color='#FF4B4B')
                st.session_state.actor_plot = fig  # Speichern des Diagramms

            else:
                st.warning('Keine Filme für diese/n Schauspieler/in gefunden.')

        # Zeige gespeicherten Plot an, falls vorhanden
        if st.session_state.actor_plot:
            st.plotly_chart(st.session_state.actor_plot, use_container_width=True)
