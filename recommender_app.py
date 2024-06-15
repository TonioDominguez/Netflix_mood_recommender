# Basic Libraries
import streamlit as st
import pandas as pd

# Load DataFrame

df_moods = pd.read_csv("df_moods.csv")

# Function to select movie or tv show
def type_selection(df_moods):
    choice = st.selectbox("Wanna watch a Movie or a TV Show?", ["Movie","Tv Show"])
    type_mood = df_moods[df_moods["type"] == choice]
    return type_mood

# Function for mood selection
def mood_selection():
    moods = ["anger", "disgust", "fear", "joy", "sadness", "surprise"]
    mood1 = st.selectbox(f"Select a mood according to what you want to see", moods)
    mood2 = st.selectbox(f"Select a second mood (optional)", ["None"] + moods)
    mood2 = mood2 if mood2 != "None" else None
    return mood1, mood2

# Function for mood recommendation
def mood_recommendation(type_mood, mood1, mood2):
    mood1_column = f"mood_{mood1}"
    if mood2:
        mood2_column = f"mood_{mood2}"
        recommended = type_mood[(type_mood[mood1_column] == 1) & (type_mood[mood2_column] == 1)]
    else:
        recommended = type_mood[type_mood[mood1_column] == 1]
    return recommended

# Principal Funtion
def netflix_recommender():
    st.title("Netflix Mood Recommender") 
    
    type_mood = type_selection(df_moods)
    mood1, mood2 = mood_selection()
    recommended = mood_recommendation(type_mood, mood1, mood2)
    
    if recommended.empty:
        st.write("No recommendations found for the selected moods. Please try different moods.")
    else:
        item_suggested = recommended.sample(1).iloc[0]
        st.write(f"### Title: {item_suggested['title']}")
        st.write(f"**Sentiment Mood:** {mood1}{' and ' + mood2 if mood2 else ''}")
        st.write(f"**Category:** {item_suggested['listed_in']}")
        st.write(f"**Director:** {item_suggested['director']}")
        st.write(f"**Cast:** {item_suggested['cast']}")
        st.write(f"**Country:** {item_suggested['country']}")
        st.write(f"**Rating:** {item_suggested['rating']}")
        
        if item_suggested["type"] == "Movie":
            st.write(f"**Movie Length:** {int(item_suggested['movie_length'])} min")
        elif item_suggested["type"] == "TV Show":
            st.write(f"**Number of Seasons:** {item_suggested['n_seasons']}")
        
        st.write(f"**Description:** {item_suggested['description']}")
    
# App exe
if __name__ == "__main__":
    netflix_recommender()