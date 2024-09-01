import pandas as pd
from io import StringIO
import streamlit as st

# Titre de l'application
st.title("Recherche d'adresses IP")

# Champ de texte pour que l'utilisateur puisse entrer les données
user_input = st.text_area("Entrez vos données ici:", height=300)

# Vérification que l'utilisateur a entré des données
if user_input:
    # Utilisation de StringIO pour lire les données saisies par l'utilisateur comme un fichier
    data_io = StringIO(user_input)
    
    # Charger les données dans un DataFrame Pandas
    try:
        df = pd.read_csv(data_io, delimiter=' ', header=None, names=[
            "37.65.33.52" "48596" "France" "Île-de-France" "Arpajon" "Societe Francaise Du Radiotelephone - SFR SA" "14390" "9038"
        ])
        
        # Afficher les données sous forme de tableau
        st.write("Données importées:")
        st.dataframe(df)

        # Champ de texte pour le filtre de l'utilisateur
        filter_input = st.text_input("Recherchez par FAI (exemple: Orange):")

        if filter_input:
            # Filtrer les données par FAI
            filtered_df = df[df['FAI'].str.contains(filter_input, case=False, na=False)]
            st.write(f"Résultats pour '{filter_input}':")
            st.dataframe(filtered_df)
        
    except Exception as e:
        st.error(f"Erreur lors de l'importation des données: {e}")
else:
    st.write("Veuillez entrer les données dans la zone de texte ci-dessus.")
