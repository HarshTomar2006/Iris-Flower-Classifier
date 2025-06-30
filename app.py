import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🌸 Iris Flower Classifier")
st.write("Enter values to predict the Iris species:")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0)
sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0)
petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0)

# Predict
if st.button("Predict"):
    values = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    result = model.predict(values)[0]
    names = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"🌼 Predicted: {names[result]}")
