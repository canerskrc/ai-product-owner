import streamlit as st
from components.task_breakdown import task_breakdown_ui
from components.sprint_report import sprint_report_ui

st.set_page_config(
    page_title="AI Product Owner Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.image("static/logo.png", use_column_width=True)
st.sidebar.title("AI Product Owner")
st.sidebar.caption("Your Autonomous Assistant")

menu = st.sidebar.radio("Navigation", ["🧠 Generate Tasks", "📊 Sprint Report"])

if menu == "🧠 Generate Tasks":
    task_breakdown_ui()
elif menu == "📊 Sprint Report":
    sprint_report_ui()
