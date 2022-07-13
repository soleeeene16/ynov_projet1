import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')


# fonction test que le prix est > 0 
def test_prixpositif():
    input1 = [[100,2,0]]#caractéristique maison
    model = load_model() #charge le modèle
    actual_result = model.predict(input1) #prédit le prix

    #vérification actual_result > 0
    assert actual_result[0]>0, " Le prix de la maison ne peut être négatif"


# fonction teste que le prix minimum est > à 10000 et prix maxamum < 1000000
def test_prixmin():
    input1 = [[100,2,0]]#caractéristique maison
    prix_min = 20000
    prix_max = 1000000
    model = load_model() #charge le modèle
    actual_result = model.predict(input1) #prédit le prix

    #vérification actual_result > 0
    assert actual_result[0]>prix_min and actual_result[0]<prix_max, " Le prix de la maison semble incorrect"

# fonction test que le nombre de chambre ne soit pas négatif ou égal à 0
def test_nbchambre():
    input1 = [[100,2,0]]#caractéristique maison

    #vérification nb de chambre supérieur à 0 
    assert input1[0][1]>0, " Le nombre de chambre doit être supérieur 0"

    # fonction test que le jardin est = 0 ou à 1
def test_jardin():
    input1 = [[100,2,1]]#caractéristique maison

    #vérification jardin = 0 ou jardin = 1
    assert (input1[0][2]==0 or input1[0][2]==1), " 0 ou 1 doit être insérer pour le jardin"
