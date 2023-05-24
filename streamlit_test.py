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
music=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Music.csv')
musical=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Musical.csv')
mystery=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Mystery.csv')
news=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/News.csv')
realitv=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/Reality-TV.csv')
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
    st.dataframe(tiltes1, 100, 400)
    
    st.write("With this table we intend to analyse the impact of titles when the people are looking for a movie to watch. These analysis is done in based of the words that are in the titles.")
    st.write("We have 3 columns representing the scores of different feelings that each title can provoke. The column 'Pos' represents the positive sentiment score, the 'Neg'column represents the negative sentiment score and the 'Neu' column represents the Neutral sentiment score. The last column ('Compound')  represents the final sentiment analysis score for each title. The range of this column goes from -1 to 1, where negative values represent that the title has a negative impact, and positive values represent that the title has positive impact.")
    

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
    category = st.selectbox("Select the Category:", 
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
            wordcloud4 = WordCloud(width=850, height=850, max_font_size=250, min_font_size=20, background_color = 'white')
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

    if category == words['genre'].iloc[11]:
        st.subheader('Most Common Words in Titles of Sci-Fi Movies')
        col1, col2 = st.columns(2)
        with col1:
            scifi_counts = dict(zip(scifi['words'], scifi['count']))
            wordcloud11 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud11.generate_from_frequencies(scifi_counts)
            plt.figure()
            plt.imshow(wordcloud11, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud11.png")
            st.image("wordcloud11.png")
            
        with col2:
            scifi
            
    if category == words['genre'].iloc[12]:
        st.subheader('Most Common Words in Titles of Biography Movies')
        col1, col2 = st.columns(2)
        with col1:
            biog_counts = dict(zip(biog['words'], biog['count']))
            wordcloud12 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud12.generate_from_frequencies(biog_counts)
            plt.figure()
            plt.imshow(wordcloud12, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud12.png")
            st.image("wordcloud12.png")
            
        with col2:
            biog
            
    if category == words['genre'].iloc[13]:
        st.subheader('Most Common Words in Titles of Family Movies')
        col1, col2 = st.columns(2)
        with col1:
            family_counts = dict(zip(family['words'], family['count']))
            wordcloud13 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud13.generate_from_frequencies(family_counts)
            plt.figure()
            plt.imshow(wordcloud13, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud13.png")
            st.image("wordcloud13.png")
            
        with col2:
            family
            
    if category == words['genre'].iloc[14]:
        st.subheader('Most Common Words in Titles of History Movies')
        col1, col2 = st.columns(2)
        with col1:
            history_counts = dict(zip(history['words'], history['count']))
            wordcloud14 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud14.generate_from_frequencies(history_counts)
            plt.figure()
            plt.imshow(wordcloud14, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud14.png")
            st.image("wordcloud14.png")
            
        with col2:
            history           
            
    if category == words['genre'].iloc[15]:
        st.subheader('Most Common Words in Titles of Music Movies')
        col1, col2 = st.columns(2)
        with col1:
            music_counts = dict(zip(music['words'], music['count']))
            wordcloud15 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud15.generate_from_frequencies(music_counts)
            plt.figure()
            plt.imshow(wordcloud15, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud15.png")
            st.image("wordcloud15.png")
            
        with col2:
            music

    if category == words['genre'].iloc[15]:
        st.subheader('Most Common Words in Titles of Music Movies')
        col1, col2 = st.columns(2)
        with col1:
            music_counts = dict(zip(music['words'], music['count']))
            wordcloud15 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud15.generate_from_frequencies(music_counts)
            plt.figure()
            plt.imshow(wordcloud15, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud15.png")
            st.image("wordcloud15.png")
            
        with col2:
            music
            
    if category == words['genre'].iloc[16]:
        st.subheader('Most Common Words in Titles of Documentary Movies')
        col1, col2 = st.columns(2)
        with col1:
            documentary_counts = dict(zip(documentary['words'], documentary['count']))
            wordcloud16 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud16.generate_from_frequencies(documentary_counts)
            plt.figure()
            plt.imshow(wordcloud16, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud16.png")
            st.image("wordcloud16.png")
            
        with col2:
            documentary
            
    if category == words['genre'].iloc[17]:
        st.subheader('Most Common Words in Titles of War Movies')
        col1, col2 = st.columns(2)
        with col1:
            war_counts = dict(zip(war['words'], war['count']))
            wordcloud17 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud17.generate_from_frequencies(war_counts)
            plt.figure()
            plt.imshow(wordcloud17, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud17.png")
            st.image("wordcloud17.png")
            
        with col2:
            war
            
    if category == words['genre'].iloc[18]:
        st.subheader('Most Common Words in Titles of Sport Movies')
        col1, col2 = st.columns(2)
        with col1:
            sports_counts = dict(zip(sports['words'], sports['count']))
            wordcloud18 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud18.generate_from_frequencies(sports_counts)
            plt.figure()
            plt.imshow(wordcloud18, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud18.png")
            st.image("wordcloud18.png")
            
        with col2:
            sports
            
    if category == words['genre'].iloc[19]:
        st.subheader('Most Common Words in Titles of Musical Movies')
        col1, col2 = st.columns(2)
        with col1:
            musical_counts = dict(zip(musical['words'], musical['count']))
            wordcloud19 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud19.generate_from_frequencies(musical_counts)
            plt.figure()
            plt.imshow(wordcloud19, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud19.png")
            st.image("wordcloud19.png")
            
        with col2:
            musical
            
    if category == words['genre'].iloc[20]:
        st.subheader('Most Common Words in Titles of Western Movies')
        col1, col2 = st.columns(2)
        with col1:
            western_counts = dict(zip(western['words'], western['count']))
            wordcloud20 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud20.generate_from_frequencies(western_counts)
            plt.figure()
            plt.imshow(wordcloud20, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud20.png")
            st.image("wordcloud20.png")
            
        with col2:
            western
            
    if category == words['genre'].iloc[21]:
        st.subheader('Most Common Words in Titles of Film-Noir Movies')
        col1, col2 = st.columns(2)
        with col1:
            filmnoir_counts = dict(zip(filmnoir['words'], filmnoir['count']))
            wordcloud21 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud21.generate_from_frequencies(filmnoir_counts)
            plt.figure()
            plt.imshow(wordcloud21, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud21.png")
            st.image("wordcloud21.png")
            
        with col2:
            filmnoir
            
    if category == words['genre'].iloc[22]:
        st.subheader('Most Common Words in Titles of Short Movies')
        col1, col2 = st.columns(2)
        with col1:
            short_counts = dict(zip(short['words'], short['count']))
            wordcloud22 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud22.generate_from_frequencies(short_counts)
            plt.figure()
            plt.imshow(wordcloud22, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud22.png")
            st.image("wordcloud22.png")
            
        with col2:
            short
            
    if category == words['genre'].iloc[23]:
        st.subheader('Most Common Words in Titles of Reality Tv')
        col1, col2 = st.columns(2)
        with col1:
            realitv_counts = dict(zip(realitv['words'], realitv['count']))
            wordcloud23 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud23.generate_from_frequencies(realitv_counts)
            plt.figure()
            plt.imshow(wordcloud23, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud23.png")
            st.image("wordcloud23.png")
            
        with col2:
            realitv
            
    if category == words['genre'].iloc[24]:
        st.subheader('Most Common Words in Titles of Talk Shows')
        col1, col2 = st.columns(2)
        with col1:
            talk_counts = dict(zip(talk['words'], talk['count']))
            wordcloud24 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud24.generate_from_frequencies(talk_counts)
            plt.figure()
            plt.imshow(wordcloud24, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud24.png")
            st.image("wordcloud24.png")
            
        with col2:
            talk
            
    if category == words['genre'].iloc[25]:
        st.subheader('Most Common Words in Titles of Games Shows')
        col1, col2 = st.columns(2)
        with col1:
            game_counts = dict(zip(game['words'], game['count']))
            wordcloud25 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud25.generate_from_frequencies(game_counts)
            plt.figure()
            plt.imshow(wordcloud25, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud25.png")
            st.image("wordcloud25.png")
            
        with col2:
            game
            
    if category == words['genre'].iloc[26]:
        st.subheader('Most Common Words in Titles of News')
        col1, col2 = st.columns(2)
        with col1:
            news_counts = dict(zip(news['words'], news['count']))
            wordcloud26 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud26.generate_from_frequencies(news_counts)
            plt.figure()
            plt.imshow(wordcloud26, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud26.png")
            st.image("wordcloud26.png")
            
        with col2:
            news
            
    if category == words['genre'].iloc[27]:
        st.subheader('Most Common Words in Titles of Adults Movies')
        col1, col2 = st.columns(2)
        with col1:
            adult_counts = dict(zip(adult['words'], adult['count']))
            wordcloud27 = WordCloud(width=700, height=700, max_font_size=300, min_font_size=20, background_color = 'white')
            wordcloud27.generate_from_frequencies(adult_counts)
            plt.figure()
            plt.imshow(wordcloud27, interpolation="bilinear")
            plt.axis("off")
            plt.margins(x=0, y=0)
            plt.savefig("wordcloud27.png")
            st.image("wordcloud27.png")
            
        with col2:
            adult
            
            
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
