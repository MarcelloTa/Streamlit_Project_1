import pandas as pd
import streamlit as st

st.set_page_config(page_title='Page 2 - Detailierte Filmangaben')
st.title("Detailierte Filmangaben")

# csv lesen
load_imdb = pd.read_csv(r'C:\Users\Admin\Documents\DataCraft\11_Datenvisualisierung_mit_Python\Streamlit_Project_1\data\imdb_clean.csv')

# eingabefeld film
filmtitel = st.text_input('Bitte Filmtitel eingeben:')

# suche nach filmtitel und ausgabe
if filmtitel:
    # eingegebener text mit tabelle vergleichen + groß- und kleinschreibung ignorieren
    filmdaten = load_imdb[load_imdb['Title'].str.lower() == filmtitel.lower()]

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

    # error anzeige, wenn das eingegebene nicht mit der tabelle übereinstimmt
    else:
        st.error('Bitte überprüfe die Schreibweise.')

else:
    st.info('Bitte gib einen Filmtitel ein.')


# random button
if st.button('Zufallsfilm'):
    zufallsfilm = load_imdb.sample(1).iloc[0]

    st.success(f'Dein Zufallsfilm ist: {zufallsfilm['Title']}')
    #st.write(zufallsfilm['Title'])



