import streamlit as st
import requests
import joblib
import json

import pandas as pd
import numpy as np
import plotly.figure_factory as ff

MLFLOW_URI = 'http://127.0.0.1:5000/invocations'

st.write("""

# Projet 7

""")

st.markdown("<b>Implémentez un modèle de scoring</b>", unsafe_allow_html=True)

st.sidebar.header('User Input Values')

st.subheader('User Entered parameters for xxx :')


# Les données exemplaires ------------------------------------------------------
@st.cache
def load_data ():
    data = pd.read_csv('data/data_sampled.csv')
    data.fillna(0, inplace=True)
    return data

data = load_data()

st.write(data.head(5))


# Chargement du modèle ---------------------------------------------------------
model = joblib.load('gb_modele.joblib')

# Affichage du titre et des données relatives au client sélectionné ------------
st.sidebar.header('Sélectionnez le numéro client')
id_client = st.sidebar.selectbox('Identifiant client', data['SK_ID_CURR'])

st.subheader('Les données relatives au client sélectionné')

data_client = data.loc[data['SK_ID_CURR'] == int(id_client)].transpose()
data_client.columns = ['Informations clients']
st.write(data_client)

# Préparation des graphiques comparatifs
st.subheader('Graphique 1')
amt_inc_total = np.log(data.loc[data['SK_ID_CURR'] == int(id_client), 'AMT_INCOME_TOTAL'].values[0])
x_a = [np.log(data['AMT_INCOME_TOTAL'])]
fig_a = ff.create_distplot(x_a,['AMT_INCOME_TOTAL'], bin_size=0.3)
fig_a.add_vline(x=amt_inc_total, annotation_text=' Vous êtes ici')

st.plotly_chart(fig_a, use_container_width=True)

st.header('''Résultat de la demande de crédit''')
per_pos = model.predict_proba(data.loc[data['SK_ID_CURR'] == int(id_client)])[0][1]
if per_pos == 1 :
    st.markdown("<p style=color:Green;font-weight:bold> Génial ! Votre crédit est accepté</p>" , unsafe_allow_html=True)
else :
    st.markdown("<p style=color:Red;font-weight:bold> Votre crédit est refusé</p>" , unsafe_allow_html=True)
    st.write('Votre crédit est refusé si ce score est supérieur à 0.59 : {}'.format(round(per_pos,3)))
