import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

# DataFrame laden:
movies = pd.read_csv(r'C:\Users\Admin\Documents\DataCraft\11_Datenvisualisierung_mit_Python\Streamlit_Project_1\data\imdb_clean.csv')

# Tab-Titel und -Icon festlegen:
st.set_page_config(page_title='Finde Deine Filme', page_icon=':film_frames:')

# Überschrift der Seite:
st.markdown("<h1 style='text-align: center;'><u>Bewertungsentwicklung</u></h1>",
            unsafe_allow_html=True)

# Leerzeile für größeren Abstand zur Hauptüberschrift einfügen:
st.markdown('')
st.markdown('')

### REGISSEUR ###
# Zentrierte Überschrift für die Regisseur-Analyse:
st.header('Analyse nach Regisseur:clapper:')

# Eingabefeld und Auswahl der Bewertungsart:
with st.form('Auswahl_Regisseur'):
    col1, col2 = st.columns(2)

    # User-Input für den Namen des Regisseurs:
    with col1:
        name_director = st.text_input('**Gib einen Namen ein:**')

    # Auswahl der Bewertungsart
    with col2:
        rating_type_director = st.radio('**Wähle die Bewertungsart:**',
                                        ['Rating', 'Metascore'],
                                        key='director')

        # Kurze Erläuterung der Bewertungsarten
        st.markdown(
            "<p style='font-size:12px; font-style:italic;'><b>Rating:</b> "
            "IMDb-Bewertung, <b>Metascore:</b> Kritiker-Bewertung</p>",
            unsafe_allow_html=True)

    # Submit-Button einfügen
    st.form_submit_button('Diagramm erstellen', type='primary')

# Falls eine Eingabe durch den User getätigt wurde / vorhanden ist:
if name_director:

    # DataFrame nach Namen filtern und ggf. auf Variable speichern:
    movies_director = (movies[
        movies['Director']
        .str.contains(name_director, case=False, na=False)
    ])

    # Prüfen, ob überhaupt Filme gefunden wurden:
    if not movies_director.empty:

        # Ist das DataFrame nicht leer, wird nun nach Jahren sortiert:
        movies_director = movies_director.sort_values(by='Year')

        # Plot erstellen:
        fig = px.line(
            movies_director,
            x='Year',
            y=rating_type_director,
            markers=True,
            hover_data={'Title': True}
        )
        # Layout anpassen:
        fig.update_layout(
            title=f'{rating_type_director}-Entwicklung für {name_director}',
            title_font={'size': 20, 'weight': 'bold'},
            title_x=0.27,
            xaxis_title='Year',
            yaxis_title=rating_type_director,
            hovermode='closest'
        )

        # Linienfarbe ändern
        fig.update_traces(line_color='#FF4B4B')

        # Plot ausgeben
        st.plotly_chart(fig)

    # Falls keine Filme gefunden werden:
    else:
        st.write('Keine Filme für diese/n Regisseur/in gefunden.')

# Trennlinie hinzufügen
st.divider()

### SCHAUSPIELER ###
# Zentrierte Überschrift für die Schauspieler-Analyse:
st.header('Analyse nach Schauspieler:performing_arts:')

# Eingabefeld und Auswahl der Bewertungsart:
with st.form('Auswahl_Schauspieler'):
    col1, col2 = st.columns(2)

    # User-Input für den Namen des Schauspielers:
    with col1:
        name_actor = st.text_input('**Gib einen Namen ein:**')

    # Auswahl der Bewertungsart
    with col2:
        rating_type_actor = st.radio('**Wähle die Bewertungsart:**',
                                     ['Rating', 'Metascore'],
                                     key='actor')

        # Kurze Erläuterung der Bewertungsarten
        st.markdown(
            "<p style='font-size:12px; font-style:italic;'><b>Rating:</b> "
            "IMDb-Bewertung, <b>Metascore:</b> Kritiker-Bewertung</p>",
            unsafe_allow_html=True)

    # Submit-Button einfügen
    st.form_submit_button('Diagramm erstellen', type='primary')

# Falls eine Eingabe durch den User getätigt wurde / vorhanden ist:
if name_actor:

    # DataFrame nach Namen filtern und ggf. auf Variable speichern:
    movies_actor = (movies[
        movies['Cast']
        .str.contains(name_actor, case=False, na=False)
    ])

    # Ist das DataFrame nicht leer, wird nun nach Jahren sortiert:
    if not movies_actor.empty:
        movies_actor = movies_actor.sort_values(by='Year')

        # Plot erstellen
        fig = px.line(
            movies_actor,
            x='Year',
            y=rating_type_actor,
            markers=True,
            hover_data={'Title': True}
        )
        # Layout anpassen:
        fig.update_layout(
            title=f'{rating_type_actor}-Entwicklung für {name_actor}',
            title_font={'size': 20, 'weight': 'bold'},
            title_x=0.27,
            xaxis_title='Year',
            yaxis_title=rating_type_actor,
            hovermode='closest'
        )

        # Linienfarbe ändern
        fig.update_traces(line_color='#FF4B4B')

        # Plot ausgeben
        st.plotly_chart(fig)

    # Falls keine Filme gefunden werden:
    else:
        st.write('Keine Filme für diese/n Schauspieler/in gefunden')
