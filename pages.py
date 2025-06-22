import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load data
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# User input
st.title("Iris Flower Predictor")
sepal_length = st.slider("Sepal length", 4.0, 8.0)
sepal_width = st.slider("Sepal width", 2.0, 4.5)
petal_length = st.slider("Petal length", 1.0, 7.0)
petal_width = st.slider("Petal width", 0.1, 2.5)

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)

st.write("Prediction:", iris.target_names[prediction][0])
