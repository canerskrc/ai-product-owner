import streamlit as st
from utils.api import post

def task_breakdown_ui():
    st.header("🧠 Generate Technical Tasks from a Feature Idea")

    feature = st.text_area("Describe a feature or product need:",
                           placeholder="e.g., Add login functionality using JWT")

    if st.button("Generate Tasks"):
        with st.spinner("Thinking like a Product Owner Agent..."):
            response = post("/jira/tasks/generate", {"feature_description": feature})
            if response and "tasks" in response:
                st.success("Tasks Generated:")
                for task in response["tasks"]:
                    st.markdown(f"- {task}")
            else:
                st.error("Could not generate tasks. Please try again.")
