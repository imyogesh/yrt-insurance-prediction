# coding: utf-8

import pickle
import numpy as np
import streamlit as st
import pandas as pd

# load the model from disk
model = pickle.load(open('model.pkl', 'rb'))

# Creating the Titles and Image
st.title("Predict Insurance Bill")

def load_data():
    df = pd.DataFrame({'sex': ['Male','Female'],
                       'smoker': ['Yes', 'No']}) 
    return df
df = load_data()


def load_data():
    df1 = pd.DataFrame({'region' : ['southeast' ,'northwest' ,'southwest' ,'northeast']}) 
    return df1
df1 = load_data()

# Take the users input
name = st.text_input("What is Firstname?")
sex = st.radio("Select Gender",("male", "female"))
smoker = st.selectbox("Are you a Smoker", df['smoker'].unique())
region = st.selectbox("Select your Region?", df1['region'].unique())
age = st.slider("What is your Age?", 18, 100)
bmi = st.slider("What is your BMI?", 10, 60)
children = st.slider("Number of children", 0, 10)

# converting text input to numeric to get back predictions from backend model.
if sex == 'male':
    gender = 1
else:
    gender = 0
    
if smoker == 'yes':
    smoke = 1
else:
    smoke = 0
    
if region == 'southeast':
    reg = 2
elif region == 'northwest':
    reg = 3
elif region == 'southwest':
    reg = 1
else:
    reg = 0
    

# store the inputs
features = [gender, smoke, reg, age, bmi, children]
# convert user inputs into an array fr the model

int_features = [int(x) for x in features]
final_features = [np.array(int_features)]


if st.button('Predict'):           # when the submit button is pressed
    prediction =  model.predict(final_features)
#     st.success(f'Your insurance bill would be: ${round(prediction[0],0)}')
    st.success('{}, Your insurance bill would be ${}'.format(name, {round(prediction[0],0)} ))

