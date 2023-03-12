import requests
url='https://api.coincap.io/v2/assets/bitcoin/history?interval=d1'
response = requests.get(url) # Отправляем запрос

from pprint import pprint 
json_file = response.json() #биткойн

import pandas as pd
from datetime import datetime
data = pd.DataFrame(json_file['data'])
data['id'] = 'BTC'

def func(x):
    date = datetime.fromtimestamp(x/1000)
    return date.strftime('%Y-%m-%d %H:%M:%S')
data['time'] = data['time'].apply(func)

data['date'] = pd.to_datetime(data['date']).dt.date
data['time'] = pd.to_datetime(data['time']).dt.time


# pip install streamlit
import streamlit as st
import numpy as np
import altair

# Столбчатая диаграмма
st.bar_chart(data, x='date', y='priceUsd')


# Боковая панель
st.sidebar.selectbox('Select an assetd', data['id'])
st.sidebar.date_input(
    "When do you start?",
    value=(datetime(2022, 1, 1), datetime(2023, 1, 1)))



