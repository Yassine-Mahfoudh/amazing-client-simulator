import streamlit as st
import pickle
import numpy as np

# Chargement du modèle KMeans (entraine sur df_clean)
# with open("kmeans_model.pkl", "rb") as f:
#     model = pickle.load(f)

st.set_page_config(page_title="Simulateur Client Amazing", layout="centered")

st.title(" Simulateur de Client - Amazing Marketplace")
st.markdown("""
Ce formulaire permet de simuler un **nouveau client** en fonction de ses habitudes d'achat.
À partir de ces données, notre modèle IA prédit à **quelle catégorie** il appartient.
""")

# Formulaire d'entrée utilisateur
st.header(" Habitudes d'achat du client")

views = st.number_input("Nombre de pages vues", min_value=0, step=1)
carts = st.number_input("Nombre d'ajouts au panier", min_value=0, step=1)
purchases = st.number_input("Nombre d'achats", min_value=0, step=1)
avg_price = st.number_input("Prix moyen des produits consultés (€)", min_value=0.0, step=0.1)

# Bouton de prédiction
if st.button("Prédire la catégorie du client"):
    try:
        # Préparer l'entrée pour le modèle
        input_data = np.array([[views, carts, purchases, avg_price]])

        # Prédiction du modèle
        # cluster = model.predict(input_data)[0]

        # Affichage du résultat
        # st.success(f" Ce client est classé dans le groupe : **{cluster}**")
        st.success(f" Ce client est classé dans le groupe : XX")

    except Exception as e:
        st.error(f"Une erreur est survenue lors de la prédiction : {e}")

st.markdown("""
---
 **Projet IA & Big Data - 5e Année**  
Équipe Amazing 2025 \n
Yassine Mahfoudh \n
Faikoth Achake Monrenike SALAMI \n
NGANTOU YAMTCHEU Brice Igor \n

""")