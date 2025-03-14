import pandas as pd
import plotly.express as px
import streamlit as st
import time

st.set_page_config(page_title='Page 2 - Detailierte Filmanalyse')

# csv lesen
@st.cache_data
def load_imdb():
    return pd.read_csv(r'C:\Users\Admin\Documents\DataCraft\11_Datenvisualisierung_mit_Python\Streamlit_Project_1\data\imdb_clean.csv')


# csv in funktion
imdb_seite_2 = load_imdb()

# eingabefeld film
filmtitel = st.text_input('Bitte Filmtitel eingeben:')

# suche nach filmtitel und ausgabe
if filmtitel:
    # eingegebener text mit tabelle vergleichen + groß- und kleinschreibung ignorieren
    filmdaten = imdb_seite_2[imdb_seite_2['Title'].str.lower() == filmtitel.lower()]

    # überprüfung, ob der film gefunden wurde
    if not filmdaten.empty:
        st.success(f'Hier sind die Informationen zu {filmtitel}:')

        ###st.write(filmdaten)
        # alle daten einzeln anzeigen
        filme = filmdaten.iloc[0]
        st.write(f'**Title**: {filme['Title']}')
        st.write(f'**Year**: {filme['Year']}')
        st.write(f'**Certificate**: {filme['Certificate']}')
        st.write(f'**Duration_(min)**: {filme['Duration_(min)']}')
        st.write(f'**Genre**: {filme['Genre']}')
        st.write(f'**Rating**: {filme['Rating']}')
        st.write(f'**Metascore**: {filme['Metascore']}')
        st.write(f'**Director**: {filme['Director']}')
        st.write(f'**Cast**: {filme['Cast']}')
        st.write(f'**Votes**: {filme['Votes']}')
        st.write(f'**Description**: {filme['Description']}')
        st.write(f'**Review_Count**: {filme['Review_Count']}')
        st.write(f'**Review_Title**: {filme['Review_Title']}')
        st.write(f'**Review**: {filme['Review']}')

    #
    else:
        st.error('Bitte überprüfe die Schreibweise.')

else:
    st.info('Bitte gib einen Filmtitel ein.')







if st.button('Zufallsfilm'):
    zufallsfilm = imdb_seite_2.sample(1).iloc[0]

    st.success(f'Dein Zufallsfilm ist: {zufallsfilm['Title']}')
    st.write(zufallsfilm)










## Spalten für x-Achse:
#categorical_cols = ['Gender', 'Profession', 'Work Experience', 'Family Size']
## Spalten für y-Achse:
#numerical_cols = ['Annual Income ($)', 'Spending Score (1-100)']
#
#st.title('Kundenanalyse-App!')
#
## Bündelt verschiedene grafische Elemente zu einem zusammenhängenden Formular
## Nutzerangaben können übergeben und dann per Knopfdruck alle verarbeitet werden
#with st.form('analysis_form'):
#    col1, col2 = st.columns(2)
#
#    # Leitet ein, was in Spalte 1 erscheint:
#    with col1:
#        # Selectbox erstellt einen Dropdown mit auswählbaren Werten:
#        cat_selection = st.selectbox('Welche Kategorie interessiert dich?',
#                                     categorical_cols)
#    with col2:
#        # Radio buttons mit anklickbaren Werten:
#        target_selection = st.radio('Von was willst du die Mittelwerte sehen?',
#                                    numerical_cols)
#
#    # Übermittlungsknopf hinzufügen (ohne Knopf nicht sinnvoll):
#    st.form_submit_button('Diagramm erstellen', type='primary')
#
## Säulendiagramm dynamisch generieren:
#scores_by_profession = (customers.groupby(cat_selection)
#                        [target_selection]
#                        .mean()
#                        .sort_values(ascending=False))
#
#scores_profession_barchart = px.bar(
#    scores_by_profession,
#    scores_by_profession.index,
#    target_selection,
#)
#
#st.plotly_chart(scores_profession_barchart)
#
## Expander, um Dataframe ein- und auszublenden:
#with st.expander('Daten anschauen', expanded=False):
#    st.dataframe(customers)
