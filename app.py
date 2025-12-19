import streamlit as st
from classifier import classify_message
from agents import (
    positive_feedback_agent,
    negative_feedback_agent,
    query_handler_agent
)
from database import init_db
from logger import add_log, get_logs
from database import get_ticket_count

init_db()

st.set_page_config(page_title="Banking Support AI", layout="wide")
st.title("🏦 Banking Customer Support AI Agent (LLM-Powered)")

user_input = st.text_input("Enter your message")

if st.button("Submit") and user_input:
    classification = classify_message(user_input)

    if classification == "Positive Feedback":
        response = positive_feedback_agent()
        agent_used = "Positive Feedback Agent"

    elif classification == "Negative Feedback":
        response = negative_feedback_agent(user_input)
        agent_used = "Negative Feedback Agent"

    else:
        response = query_handler_agent(user_input)
        agent_used = "Query Handler Agent"

    add_log(user_input, classification, agent_used, response)

    st.subheader("🧠 Classification")
    st.write(classification)

    st.subheader("💬 Response")
    st.success(response)

st.divider()
st.subheader("📜 Logs & Debug View")

for log in get_logs()[::-1]:
    st.json(log)


st.divider()
st.subheader("Support Ticket Statistics")
st.write(f"Total Support Tickets: {get_ticket_count()}")
