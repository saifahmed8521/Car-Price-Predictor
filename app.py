import streamlit as st
import pickle
from datetime import datetime
import pandas as pd



model = pickle.load(open('LRModel.pkl','rb'))
df = pd.read_csv('CleanData.csv')
companies = sorted(df['company'].unique())
car_model = sorted(df['name'].unique())
year = sorted(df['year'].unique(),reverse=True)
fuel_type = df['fuel_type'].unique()

st.title('Welcome to Car Price Predictor')

select_company = st.selectbox('Select the Company',companies)
select_model= st.selectbox('Select the Model',car_model)
select_fueltype = st.selectbox('Select the fuel type',fuel_type)
select_year = st.selectbox('Select Year of Purchase',year)
KmCoveres = int(st.number_input('Kilometer Covers'))
st.write('Kilometer Covers ', KmCoveres)

def predict():
    prediction = model.predict(pd.DataFrame([[select_model,select_company,select_year,KmCoveres,select_fueltype]],columns=['name','company','year','kms_driven','fuel_type']))
    st.header(int(prediction))

if st.button('Predict'):
    predict()

# if car_model.find(companies):
#     return car_models

# def ShowModel():
#     for model in car_model:
#         model.find(select_company)
#         return model