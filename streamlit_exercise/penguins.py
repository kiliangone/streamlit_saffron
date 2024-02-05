### Import libraries
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title("🐧 Pingu")
st.image('penguins.png',caption='lovely penguins')

# st.sidebar.slider(label='user inüput for nothing',min_value=1,max_value=2)


st.header("Some Data About Pingu") #this results into a section 

df = pd.read_csv('./data/penguins_pimped.csv')
df_sample = df.sample(n=5)

st.dataframe(df_sample)


st.subheader('Pick an Island')

islands = df['island'].unique()

selected_island = st.selectbox(label='islands', options=islands)

if st.checkbox(label="do you really want to see the dataframe my dear user?"):
    st.dataframe(df[df['island'] == selected_island])
    #st.write(df[df['island'] == selected_island])


st.subheader("📈 Visualizations")
st.markdown("**Enjoy this beautiful scatter plot**")

fig, ax = plt.subplots()
ax = sns.scatterplot(
    data=df,
    x='bill_depth_mm',
    y='bill_length_mm',
    hue='species' # set to species
    )

st.pyplot(fig)

st.markdown('**This one is more interactive**')

fig_plotly = px.scatter(
    data_frame=df,
    x='bill_depth_mm',
    y='bill_length_mm',
    color='species',
    animation_frame='island')

st.plotly_chart(fig_plotly)

st.subheader("Where the Pingu come from?")

st.map(df)