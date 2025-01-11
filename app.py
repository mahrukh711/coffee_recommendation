import pickle
import streamlit as st
import requests
import pandas as pd

# Helper function to load pickle files
def load_pickle(file_path):
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except AttributeError as e:
        st.error(f"Incompatible pickle file: {file_path}. Error: {e}")
        return None

# Fetch poster function
def fetch_poster(coffee_id):
    url = "https://api.sampleapis.com/coffee/hot"
    try:
        data = requests.get(url).json()
        for coffee in data:
            if coffee['id'] == coffee_id:
                return coffee.get('image', "https://via.placeholder.com/150")
    except Exception as e:
        st.error(f"Error fetching poster: {e}")
    return "https://via.placeholder.com/150"

# Recommendation function
def recommend(selected_name):
    try:
        index = coffee_name[coffee_name['name'] == selected_name].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_coffee_name = []
        recommended_coffee_poster = []
        for i in distances[1:6]:  # Top 5 recommendations
            coffee_id = coffee_name.iloc[i[0]].id
            recommended_coffee_poster.append(fetch_poster(coffee_id))
            recommended_coffee_name.append(coffee_name.iloc[i[0]].name)
        return recommended_coffee_name, recommended_coffee_poster
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        return [], []

# Streamlit app
st.header("Coffee Recommendation System Using Machine Learning")

# Load pickle files
coffee_name = load_pickle('artificates/coffeeAnalysis_list.pkl')
similarity = load_pickle('artificates/similarity.pkl')

if coffee_name is not None and similarity is not None:
    coffeeAnalysis_list = coffee_name['name'].values
    selected_coffee = st.selectbox(
        'Type or select a coffee to get a recommendation',
        coffeeAnalysis_list
    )

    if st.button('Show recommendation'):
        recommended_coffee_name, recommended_coffee_poster = recommend(selected_coffee)
        if recommended_coffee_name:
            for i in range(len(recommended_coffee_name)):
                with st.container():
                    st.text(recommended_coffee_name[i])
                    st.image(recommended_coffee_poster[i])
        else:
            st.warning("No recommendations available.")
