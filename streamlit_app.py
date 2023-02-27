import pandas as pd
import streamlit as st
import squarify
import matplotlib.pyplot as plt

url = 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/state/totals/nst-est2019-alldata.csv'
df = pd.read_csv(url, encoding='latin-1')

df = df[df['SUMLEV']==40] # Filter out summary level rows
df = df[['NAME', 'POPESTIMATE2019']] # Keep only the columns we need
df = df.rename(columns={'NAME': 'State', 'POPESTIMATE2019': 'Population'}) # Rename the columns

st.title('US States by Population')
st.write('This treemap shows the population of each US state in 2019.')
st.write('Hover over a square to see the state name and population.')

fig, ax = plt.subplots()
squarify.plot(sizes=df['Population'], label=df['State'], alpha=.8 )
plt.axis('off')
st.pyplot()
