import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')


st.title('Prédiction de prix de maison')

taille = st.number_input("Insérer la taille de la maison")
nb_rooms = st.number_input("Insérer le nombre de chambre", step=1)
garden = st.number_input("Avez-vous un jardin ? Insérer 1 pour 'Oui' et 0 pour 'Non'", step=1)

model = load_model()

if taille <= 0:
    st.write('mettre taille correcte')
if nb_rooms <= 0:
    st.write("mettre nombre de chambre correct")
if garden < 0 or garden > 1:
    st.write("mettre numéro jardin correct.")

if taille > 0 and nb_rooms > 0:
    
    X = [[taille, nb_rooms, garden]]
    prediction = model.predict(X)

    ## afficher la prediction
    st.write("Le prix de la maison est : {}".format(int(prediction[0])),"€")
