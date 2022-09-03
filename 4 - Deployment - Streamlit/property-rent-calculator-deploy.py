# -*- coding: utf-8 -*-
"""
Created on Sat, Sep 03 10:15:00 2022
@author: antunes-lima
"""

# importing libraries
import pandas as pd
import numpy as np
from joblib import load
import streamlit as st

# model import
f = open('property-rent-calc.joblib', 'rb')
model = load(f)

# scaler import
s = open('property-rent-scaler.joblib', 'rb')
scaler = load(s)

# funcions
def predict_property(property_type, neighborhood, size_m2, bedrooms, suite, parking):
    df_predict = pd.DataFrame({
        'size_m2': [size_m2],
        'bedrooms': [bedrooms],
        'suite': [suite],
        'parking': [parking],
        'bedrooms_per_size': [int(bedrooms)/int(size_m2)],
        'suite_per_size': [int(suite)/int(size_m2)],
        'parking_per_size': [int(parking)/int(size_m2)],
        'property_type_Apartamento': [0],
        'property_type_Kitnet': [0],
        'neighborhood_ AGUAS CLARAS': [0],
        'neighborhood_ ASA NORTE': [0],
        'neighborhood_ ASA SUL': [0],
        'neighborhood_ JARDINS MANGUEIRAL': [0],
        'neighborhood_ LAGO NORTE': [0],
        'neighborhood_ NOROESTE': [0],
        'neighborhood_ OCTOGONAL': [0],
        'neighborhood_ PARK SUL': [0],
        'neighborhood_ SAMAMBAIA': [0],
        'neighborhood_ SOBRADINHO': [0],
        'neighborhood_ SUDOESTE': [0],
        'neighborhood_ TAGUATINGA': [0],
        'neighborhood_ TIER_1': [0],
        'neighborhood_ TIER_2': [0],
        'neighborhood_ TIER_3': [0],
        'neighborhood_ TIER_4': [0],
        'neighborhood_ TIER_5': [0],
        'neighborhood_ TIER_6': [0],
        'neighborhood_ VICENTE PIRES': [0]
        })
     
    if property_type == 'Apartment':
        df_predict.property_type_Apartamento.replace(0, 1, inplace=True)
    if property_type == 'Kitnet':
        df_predict.property_type_Kitnet.replace(0, 1, inplace=True)
    
    if neighborhood == 'NOROESTE':
        df_predict['neighborhood_ NOROESTE'].replace(0, 1, inplace=True)
    if neighborhood == 'PARK SUL':
        df_predict['neighborhood_ PARK SUL'].replace(0, 1, inplace=True)
    if neighborhood == 'SETOR INDUSTRIAL':
        df_predict['neighborhood_ TIER_6'].replace(0, 1, inplace=True)
    if neighborhood == 'PARK WAY':
        df_predict['neighborhood_ TIER_6'].replace(0, 1, inplace=True)
    if neighborhood == 'SUDOESTE':
        df_predict['neighborhood_ SUDOESTE'].replace(0, 1, inplace=True)
    if neighborhood == 'LAGO SUL':
        df_predict['neighborhood_ TIER_6'].replace(0, 1, inplace=True)
    if neighborhood == 'ASA SUL':
        df_predict['neighborhood_ ASA SUL'].replace(0, 1, inplace=True)
    if neighborhood == 'OCTOGONAL':
        df_predict['neighborhood_ OCTOGONAL'].replace(0, 1, inplace=True)
    if neighborhood == 'LAGO NORTE':
        df_predict['neighborhood_ LAGO NORTE'].replace(0, 1, inplace=True)
    if neighborhood == 'ASA NORTE':
        df_predict['neighborhood_ ASA NORTE'].replace(0, 1, inplace=True)
    if neighborhood == 'AGUAS CLARAS':
        df_predict['neighborhood_ AGUAS CLARAS'].replace(0, 1, inplace=True)
    if neighborhood == 'JARDINS MANGUEIRAL':
        df_predict['neighborhood_ JARDINS MANGUEIRAL'].replace(0, 1, inplace=True)
    if neighborhood == 'CRUZEIRO':
        df_predict['neighborhood_ TIER_5'].replace(0, 1, inplace=True)
    if neighborhood == 'JARDIM BOTANICO':
        df_predict['neighborhood_ TIER_5'].replace(0, 1, inplace=True)
    if neighborhood == 'VILA PLANALTO':
        df_predict['neighborhood_ TIER_4'].replace(0, 1, inplace=True)
    if neighborhood == 'GUARA':
        df_predict['neighborhood_ TIER_4'].replace(0, 1, inplace=True)
    if neighborhood == 'VARJAO':
        df_predict['neighborhood_ TIER_2'].replace(0, 1, inplace=True)
    if neighborhood == 'SIG':
        df_predict['neighborhood_ TIER_2'].replace(0, 1, inplace=True)
    if neighborhood == 'VILA DA TELEBRASILIA':
        df_predict['neighborhood_ TIER_2'].replace(0, 1, inplace=True)
    if neighborhood == 'SOBRADINHO':
        df_predict['neighborhood_ SOBRADINHO'].replace(0, 1, inplace=True)
    if neighborhood == 'VICENTE PIRES':
        df_predict['neighborhood_ VICENTE PIRES'].replace(0, 1, inplace=True)
    if neighborhood == 'VILA ESTRUTURAL':
        df_predict['neighborhood_ TIER_2'].replace(0, 1, inplace=True)
    if neighborhood == 'SAMAMBAIA':
        df_predict['neighborhood_ SAMAMBAIA'].replace(0, 1, inplace=True)
    if neighborhood == 'TAGUATINGA':
        df_predict['neighborhood_ TAGUATINGA'].replace(0, 1, inplace=True)
    if neighborhood == 'CANDANGOLANDIA':
        df_predict['neighborhood_ TIER_2'].replace(0, 1, inplace=True)
    if neighborhood == 'RECANTO DAS EMAS':
        df_predict['neighborhood_ TIER_2'].replace(0, 1, inplace=True)
    if neighborhood == 'RIACHO FUNDO':
        df_predict['neighborhood_ TIER_2'].replace(0, 1, inplace=True)
    if neighborhood == 'SAO SEBASTIAO':
        df_predict['neighborhood_ TIER_2'].replace(0, 1, inplace=True)
    if neighborhood == 'CEILANDIA':
        df_predict['neighborhood_ TIER_3'].replace(0, 1, inplace=True)
    if neighborhood == 'FORMOSA':
        df_predict['neighborhood_ TIER_1'].replace(0, 1, inplace=True)
    if neighborhood == 'BRAZLANDIA':
        df_predict['neighborhood_ TIER_1'].replace(0, 1, inplace=True)
    if neighborhood == 'NUCLEO BANDEIRANTE':
        df_predict['neighborhood_ TIER_3'].replace(0, 1, inplace=True)
    if neighborhood == 'GAMA':
        df_predict['neighborhood_ TIER_3'].replace(0, 1, inplace=True)
    if neighborhood == 'PLANALTINA':
        df_predict['neighborhood_ TIER_1'].replace(0, 1, inplace=True)
    if neighborhood == 'SANTA MARIA':
        df_predict['neighborhood_ TIER_1'].replace(0, 1, inplace=True)
    if neighborhood == 'LUZIANIA':
        df_predict['neighborhood_ TIER_1'].replace(0, 1, inplace=True)
    if neighborhood == 'PARANOA':
        df_predict['neighborhood_ TIER_1'].replace(0, 1, inplace=True)
    if neighborhood == 'VALPARAISO DE GOIAS':
        df_predict['neighborhood_ TIER_1'].replace(0, 1, inplace=True)
    
    num_attributes = df_predict.columns[:7]
    df_predict[num_attributes] = scaler.transform(df_predict[num_attributes])
    
    prediction = model.predict(df_predict)
    print(prediction[0])
    return int(prediction[0])

def main():
    st.title('Property Rent Calculator')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Property Rent Calculator </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    property_type = st.selectbox("Property type", (
        'Apartment',
        'Kitnet'
        ))
    neighborhood = st.selectbox("Neighborhood", (
        'NOROESTE',
        'PARK SUL',
        'SETOR INDUSTRIAL',
        'PARK WAY',
        'SUDOESTE',
        'LAGO SUL',
        'ASA SUL',
        'OCTOGONAL',
        'LAGO NORTE',
        'ASA NORTE',
        'AGUAS CLARAS',
        'JARDINS MANGUEIRAL',
        'CRUZEIRO',
        'JARDIM BOTANICO',
        'VILA PLANALTO',
        'GUARA',
        'VARJAO',
        'SIG',
        'VILA DA TELEBRASILIA',
        'SOBRADINHO',
        'VICENTE PIRES',
        'VILA ESTRUTURAL',
        'SAMAMBAIA',
        'TAGUATINGA',
        'CANDANGOLANDIA',
        'RECANTO DAS EMAS',
        'RIACHO FUNDO',
        'SAO SEBASTIAO',
        'CEILANDIA',
        'FORMOSA',
        'BRAZLANDIA',
        'NUCLEO BANDEIRANTE',
        'GAMA',
        'PLANALTINA',
        'SANTA MARIA',
        'LUZIANIA',
        'PARANOA',
        'VALPARAISO DE GOIAS'
        ))
    size_m2 = st.text_input("Size in m²","")
    bedrooms = st.text_input("Number of bedrooms","")
    suite = st.text_input("Number of suites","")
    parking = st.text_input("Parking spots","")
    result = ''
    if st.button('Predict'):
        result = predict_property(property_type, neighborhood, size_m2, bedrooms, suite, parking)
    st.success('The predicted rent value for this property is:  {}'.format(result))
    if st.button('About'):
        st.text('Model trained using Scikit-learn')
        st.text('App built with Streamlit')

# code
if __name__ == '__main__':
    main()