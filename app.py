import streamlit as st
import joblib
import random

model = joblib.load("chatbot.pkl")
vector = joblib.load("vector.pkl")
res = joblib.load("res.pkl")

st.title("ChatBot")
st.write("Ask Something to the Chatbot")
user = st.text_input("You : ")

if st.button("Send"):
    if user:
        user_vector = vector.transform([user]).toarray()
        predict = model.predict(user_vector)[0]
        if predict in res :
            reply = random.choice(res[predict])
            st.success("Bot: " + reply)