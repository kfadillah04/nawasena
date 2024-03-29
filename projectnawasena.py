#Khusnul mengerjakan impor data frame, membuat judul dan histogram gender

import streamlit as st
import pandas as pd
import plotly.express as px


st.title(":candlestick_chart: Mini Dashbord World Happiness")

st.write("### by Nawasena")

st.write("""
### Nama Anggota:
#### Viviana Ayu Lestari (021002101005)
#### Khusnul Fadillah (021002101006)
#### Putri Hindira Krisnha (021002101008)
#### Lutfiah Farah Azura (021002101009)""")

st.write("Dosen Pengampu: Sri Yani K dan Anung Ariwibowo")

df2015 = pd.read_csv('DataHappiness/2015.csv', sep =',')
#df = pd.read_csv('DataHappiness/2015.csv')
df2016 = pd.read_csv('DataHappiness/2016.csv', sep =',')
df2017 = pd.read_csv('DataHappiness/2017.csv', sep =',')
df2018 = pd.read_csv('DataHappiness/2018.csv', sep =',')
df2019 = pd.read_csv('DataHappiness/2019.csv', sep =',')

df = pd.read_csv('DataHappiness/2016.csv', sep =',')


df = pd.read_csv('DataHappiness/2017.csv', sep =',')

df = pd.read_csv('DataHappiness/2018.csv', sep =',')

df = pd.read_csv('DataHappiness/2019.csv', sep =',')

st.write("# Happiness Rank")

tahun = st.selectbox(
    "Pilih Tahun",
    options = df2015["year"].unique() )

df3 = df.query(
     'year' == tahun )

attributes = st.multiselect(
    "Pilih country:",
    options = ['Country']
)

plot_bar = px.bar(df3,
                    x = df["country"]. unique(),
                    y = attributes,
                    tittle = "Grafik Bar")

                
