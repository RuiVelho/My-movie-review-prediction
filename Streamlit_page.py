import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

titles=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/movies_noexplode.csv') #Sentiment analysis
#tiltes=titles[titles['tconst', 'primaryTitle', 'genre', 'compound')]]

directors=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/imbdir_rating.csv')
directors=directors.sort_values(by="dir_rating", ascending=False).head(10)
directors=directors.reset_index()
directors=directors.drop(['index'], axis=1)

actors=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/actors_top10.csv')

genres_analysis=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/genres_analysis.csv')


st.set_page_config(page_title='Prediction of Futeture Movies',
                   page_icon=":movie_camera:")

dash = st.sidebar.radio(
    "Prediction of review for the future Movies",
    ('Titles Sentiment Analysis', 'Movies Statistics', 'How good will your movie be?'))

if dash == 'Titles Sentiment Analysis':
    st.title('Titles Sentiment Analysis')
    titles
    

if dash == 'Movies Statistics':
    col1, col2 = st.columns(2)
    with col1:
        st.title('Top 10 Directors')
        directors
    
    with col2:
        st.title('Top 10 Actors')
        actors
    
    st.title('Genres Analysis')
    genres_analysis

if dash == 'How good will your movie be?':

    st.title('Prediction of review for the future Movies')

    st.sidebar.header('Predict Your next Movies Selection')

    director = st.sidebar.selectbox('Select the Director: ', options=[1,2,3,4,5,6])

    actors = st.sidebar.multiselect('Select the Actors: ', options=[1,2,3,4,5,6])
    
    year= ('Select the Actors: ', options=[2002,2023])

    category = st.sidebar.selectbox('Select the category of movie: ', options=genres_analysis['genre'])
       # if category == "Drama":
             # genres_df
  


    #    pages = {
#        "Data Analysis": page_plot1,    #names will change, don't worry :)
#        "Algorithm": page_plot2     #names will change, don't worry :)
#        }
#    selected_page = st.selectbox(
 #       "Choose Page",
#        pages.keys()
        
        
