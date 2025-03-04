import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0, format="%.2f")

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0, format="%.2f")

    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0, format="%.2f")

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0, format="%.2f")

    with col3:
        BMI = st.number_input('BMI value', min_value=0.0, format="%.2f")

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.2f")

    with col2:
        Age = st.number_input('Age of the Person', min_value=0, step=1)

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
