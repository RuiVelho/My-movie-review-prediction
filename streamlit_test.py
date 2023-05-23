import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

titles=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/movies_noexplode.csv') #Sentiment analysis
tiltes1=titles.drop(['titleType','originalTitle','isAdult','endYear','runtimeMinutes','numVotes','Titles'], axis=1)#['tconst', 'primaryTitle', 'genres', 'compound']
#tiltes=titles[titles['tconst', 'primaryTitle', 'genre', 'compound')]]
#getting dir names
dir_names_df = pd.read_csv("https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/pivot_dir.csv")
#getting the dir list
dir_names = dir_names_df.columns.drop('tconst').tolist()
#dir dataframes
directors=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/imbdir_rating.csv')
directors1=directors.sort_values(by="dir_rating", ascending=False)
directors1=directors1.reset_index()
directors1=directors1.drop(['index'], axis=1)
directors1= directors1[directors1["dir_rating"] > directors["dir_rating"].mean()]

directorslow = directors.sort_values(by="dir_rating", ascending=True)
directorslow=directorslow.reset_index()
directorslow=directorslow.drop(['index'], axis=1)
directorslow= directorslow[directorslow["dir_rating"] < directors["dir_rating"].mean()]
actors=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/actors_top10.csv')
table_actor_10_top = pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/table_actor_10.csv')
table_actor_10_tail = pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/table_actor_10_tail.csv')

genres_analysis=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/genres_analysis.csv')

words=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/genres_2205.csv')

action=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Action.csv')
adult=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Adult.csv')
adventure=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Adventure.csv')
animation=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Animation.csv')
biog=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Biography.csv')
comedy=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Comedy.csv')
crime=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Crime.csv')
documentary=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Documentary.csv')
drama=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Drama.csv')
family=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Family.csv')
fantasy=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Fantasy.csv')
filmnoir=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Film-Noir.csv')
game=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Game-Show.csv')
history=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/History.csv')
horror=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Horror.csv')
music=pd.read_csv('https://github.com/RuiVelho/My-movie-review-prediction/blob/main/Music.csv')
musical=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Musical.csv')
mystery=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Mystery.csv')
news=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/News.csv')
reality=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Reality-TV.csv')
romance=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Romance.csv')
scifi=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Sci-Fi.csv')
short=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Short.csv')
sports=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Sport.csv')
talk=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Talk-Show.csv')
thriller=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Thriller.csv')
war=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/War.csv')
western=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Western.csv')



st.set_page_config(page_title='Prediction of Futeture Movies',
                   page_icon=":movie_camera:")

dash = st.sidebar.radio(
    "Prediction of review for the future Movies",
    ('Titles Sentiment Analysis', 'Movies Statistics', 'Actors', 'Most common words in the Titles in each Category'))

if dash == 'Titles Sentiment Analysis':
    st.title('Titles Sentiment Analysis')
    tiltes1
    

if dash == 'Movies Statistics':
    col1, col2 = st.columns(2)
    with col1:
        st.title('Top Directors')
        directors1
    st.write("Average Director Rating: ", directors["dir_rating"].mean())
    with col2:
        st.title('Worst Directors')
        directorslow
    st.title('Genres Ratings')
    genres_analysis = genres_analysis.sort_values(by="count", ascending=False)
    genres_analysis
    st.write("Average Genre Rating", genres_analysis["Count_Rating"].mean())

if dash == "Actors":
    st.title('Top Actors')
    counts = table_actor_10_top.primaryName.value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=counts.index, autopct='%1.1f%%')
    ax1.axis('equal')
    st.pyplot(fig1)
    
    st.title('Worst Actors')
    counts2 = table_actor_10_tail.primaryName.value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(counts2, labels=counts2.index, autopct='%1.1f%%')
    ax2.axis('equal')
    st.pyplot(fig2)
    
if dash == 'Most common words in the Titles in each Category':
    category = st.sidebar.radio("Select the Category:", 
    options=words['genre'])
    if category == words['genre'].iloc[0]:
        st.subheader('Most Common Words in Titles of Drama Movies')
        col1, col2 = st.columns(2)
        with col1:
            drama_counts = dict(zip(drama['words'], drama['count']))
            wordcloud = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud.generate_from_frequencies(drama_counts)
            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud.png")
            st.image("wordcloud.png")
        
        with col2:
            drama
            
    
     if category == words['genre'].iloc[1]:
        st.subheader('Most Common Words in Titles of Comedy Movies')
        col1, col2 = st.columns(2)
        with col1:
            comedy_counts = dict(zip(comedy['words'], comedy['count']))
            wordcloud1 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud1.generate_from_frequencies(comedy_counts)
            plt.figure()
            plt.imshow(wordcloud1, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud1.png")
            st.image("wordcloud1.png")
        
        with col2:
            comedy
            
    if category == words['genre'].iloc[2]:
        st.subheader('Most Common Words in Titles of Action Movies')
        col1, col2 = st.columns(2)
        with col1:
            action_counts = dict(zip(action['words'], action['count']))
            wordcloud2 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud2.generate_from_frequencies(action_counts)
            plt.figure()
            plt.imshow(wordcloud2, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud2.png")
            st.image("wordcloud2.png")
        
        with col2:
            action
    
    if category == words['genre'].iloc[3]:
        st.subheader('Most Common Words in Titles of Crime Movies')
        col1, col2 = st.columns(2)
        with col1:
            crime_counts = dict(zip(crime['words'], crime['count']))
            wordcloud3 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud3.generate_from_frequencies(crime_counts)
            plt.figure()
            plt.imshow(wordcloud3, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud3.png")
            st.image("wordcloud3.png")
        
        with col2:
            crime
            
    if category == words['genre'].iloc[4]:
        st.subheader('Most Common Words in Titles of Adventure Movies')
        col1, col2 = st.columns(2)
        with col1:
            adventure_counts = dict(zip(adventure['words'], adventure['count']))
            wordcloud4 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud4.generate_from_frequencies(adventure_counts)
            plt.figure()
            plt.imshow(wordcloud4, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud4.png")
            st.image("wordcloud4.png")
        
        with col2:
            adventure
            
    if category == words['genre'].iloc[5]:
        st.subheader('Most Common Words in Titles of Thriller Movies')
        col1, col2 = st.columns(2)
        with col1:
            thriller_counts = dict(zip(thriller['words'], thriller['count']))
            wordcloud5 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud5.generate_from_frequencies(thriller_counts)
            plt.figure()
            plt.imshow(wordcloud5, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud5.png")
            st.image("wordcloud5.png")
        
        with col2:
            thriller
            
    if category == words['genre'].iloc[6]:
        st.subheader('Most Common Words in Titles of Romance Movies')
        col1, col2 = st.columns(2)
        with col1:
            romance_counts = dict(zip(romance['words'], romance['count']))
            wordcloud6 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud6.generate_from_frequencies(romance_counts)
            plt.figure()
            plt.imshow(wordcloud6, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud6.png")
            st.image("wordcloud6.png")
        
        with col2:
            romance
            
    if category == words['genre'].iloc[7]:
        st.subheader('Most Common Words in Titles of Horror Movies')
        col1, col2 = st.columns(2)
        with col1:
            horror_counts = dict(zip(horror['words'], horror['count']))
            wordcloud7 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud7.generate_from_frequencies(horror_counts)
            plt.figure()
            plt.imshow(wordcloud7, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud7.png")
            st.image("wordcloud7.png")
        
        with col2:
            horror
           
    if category == words['genre'].iloc[8]:
        st.subheader('Most Common Words in Titles of Mystery Movies')
        col1, col2 = st.columns(2)
        with col1:
            mystery_counts = dict(zip(mystery['words'], mystery['count']))
            wordcloud8 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud8.generate_from_frequencies(mystery_counts)
            plt.figure()
            plt.imshow(wordcloud8, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud8.png")
            st.image("wordcloud8.png")
        
        with col2:
            mystery
            
    if category == words['genre'].iloc[9]:
        st.subheader('Most Common Words in Titles of Animation Movies')
        col1, col2 = st.columns(2)
        with col1:
            animation_counts = dict(zip(animation['words'], animation['count']))
            wordcloud9 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud9.generate_from_frequencies(animation_counts)
            plt.figure()
            plt.imshow(wordcloud9, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud9.png")
            st.image("wordcloud9.png")
        
        with col2:
            animation
            
    if category == words['genre'].iloc[10]:
        st.subheader('Most Common Words in Titles of Fantasy Movies')
        col1, col2 = st.columns(2)
        with col1:
            fantasy_counts = dict(zip(fantasy['words'], fantasy['count']))
            wordcloud10 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud10.generate_from_frequencies(fantasy_counts)
            plt.figure()
            plt.imshow(wordcloud10, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud10.png")
            st.image("wordcloud10.png")
        
        with col2:
            fantasy
            
   
    #st.write(words[words['genre']==category]['count words'][0])
    #text=words[words['genre']==category]['count words'][0]
   
    #
        #word_counts = dict(zip(data['palavras'], data['contagem']))

        #words_filt= words[words['genre']==category]['count words'][0]
        #words_filt=dict(words_filt)
 
    #wordcloud = WordCloud(width=480, height=480, max_font_size=200, min_font_size=10, background_color = 'white')
    
    #viz1=wordcloud.generate_from_frequencies(dict(words[words['genre']==category]['count words'][0]))
    #plt.figure()
    #plt.imshow(wordcloud, interpolation="bilinear")
    #plt.axis("off")
    #plt.margins(x=0, y=0)
    #plt.show(viz1.figure)

#if dash == 'How good will your movie be?':

    #st.title('Prediction of review for the future Movies')

    #st.sidebar.header('Predict Your next Movies Selection')

    #director = st.sidebar.selectbox('Select the Director: ', options=dir_names + ["others"])

    #actors = st.sidebar.multiselect('Select the Actors: ', options=[1,2,3,4,5,6])
    
    #year= ('Select year: ', options=[2002,2023])

    #category = st.sidebar.selectbox('Select the category of movie: ', options=genres_analysis['genre'])
