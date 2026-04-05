import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open("model.pkl","rb"))

st.title("🏏 T20 World Cup Score Predictor")

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'
]

cities = [
    'Mumbai','Delhi','Chennai','Kolkata','Bangalore',
    'Hyderabad','Lahore','Dubai','London','Sydney'
]

st.header("Match Situation")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Batting Team", teams)
with col2:
    bowling_team = st.selectbox("Bowling Team", teams)

city = st.selectbox("City", cities)

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input("Current Score")

with col4:
    overs = st.number_input("Overs Completed")

with col5:
    wickets = st.number_input("Wickets Fallen")

last_five = st.number_input("Runs in Last 5 Overs")

if st.button("Predict Score"):

    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets

    crr = current_score / overs if overs > 0 else 0

    input_df = pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[city],
        'current_score':[current_score],
        'balls_left':[balls_left],
        'wickets_left':[wickets_left],
        'crr':[crr],
        'last_five':[last_five]
    })

    result = pipe.predict(input_df)

    st.header(f"Predicted Final Score: {int(result[0])}")