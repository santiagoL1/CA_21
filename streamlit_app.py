import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Interactive sales dashboard')
st.write('this dashboard allows you to view sales data as user')

data = {
  'Year':[2010,2011,2012,2013,2014,2015],
  'Region': ['North','South', 'East' , 'West'  , 'Central' , 'North'],
  'Sales Amount' : [200,210,220,230,240,250]
}
df = pd.DataFrame(data)

selected_year = st.slider('Select a year', min_value=2010, max_value=2015, value = 2013)

st.write(f"Data for the year {selected_year}:")
filtered_df = df[df['Year'] == selected_year]
st.write(filtered_df)

fig, ax = plt.subplots()
ax.bar(filtered_df['Region']
