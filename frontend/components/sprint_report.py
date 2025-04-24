import streamlit as st
from utils.api import post

def sprint_report_ui():
    st.header("📊 Sprint Summary Report")

    team_json = st.text_area("Team Workload Data (JSON format):",
                             '{"alice": 5, "murat": 3}')

    issues_json = st.text_area("Sprint Issues List (JSON format):",
                               '[{"title": "Fix auth bug", "status": "done", "assignee": "alice"}]')

    velocity = st.number_input("Historical Velocity (Story Points):", value=6.0, step=0.5)

    if st.button("Generate Report"):
        with st.spinner("Analyzing Sprint with AI Agent..."):
            try:
                payload = {
                    "team_data": eval(team_json),
                    "issues": eval(issues_json),
                    "historical_velocity": velocity
                }
                result = post("/reports/sprint", payload)
                if result and "report" in result:
                    st.subheader("🧾 Sprint Report")
                    st.markdown(result["report"]["summary"])
                else:
                    st.error("Report generation failed.")
            except Exception as e:
                st.error(f"Invalid input: {e}")

