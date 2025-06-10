import streamlit as st
import requests
from datetime import datetime, timedelta
import json

def ai_product_owner_ui():
    st.title("🤖 AI Product Owner Dashboard")
    
    # Sidebar navigation
    menu = st.sidebar.radio(
        "Navigation",
        ["📋 Backlog Management", "📊 Sprint Planning", "📈 Analytics", "📝 Reports"]
    )
    
    if menu == "📋 Backlog Management":
        backlog_management()
    elif menu == "📊 Sprint Planning":
        sprint_planning()
    elif menu == "📈 Analytics":
        analytics()
    elif menu == "📝 Reports":
        reports()

def backlog_management():
    st.header("Backlog Management")
    
    # Create new user story
    with st.expander("Create New User Story"):
        title = st.text_input("Story Title")
        description = st.text_area("Description")
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        
        if st.button("Generate with AI"):
            with st.spinner("AI is analyzing your story..."):
                # AI analizi ve öneriler
                st.success("AI Analysis Complete!")
                st.info("Suggested improvements and story points will appear here")
    
    # Backlog view
    st.subheader("Product Backlog")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.dataframe(
            data=[
                {"Title": "Sample Story 1", "Priority": "High", "Points": 5},
                {"Title": "Sample Story 2", "Priority": "Medium", "Points": 3},
            ],
            use_container_width=True
        )
    
    with col2:
        st.metric("Total Stories", "15")
        st.metric("Total Points", "45")

def sprint_planning():
    st.header("Sprint Planning")
    
    # Sprint creation
    with st.expander("Create New Sprint"):
        sprint_name = st.text_input("Sprint Name")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        
        if st.button("Plan Sprint with AI"):
            with st.spinner("AI is planning your sprint..."):
                # AI sprint planlama
                st.success("Sprint Planning Complete!")
    
    # Current sprint
    st.subheader("Current Sprint")
    st.info("Sprint 1 - In Progress")
    
    # Sprint metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Velocity", "15")
    with col2:
        st.metric("Completion Rate", "75%")
    with col3:
        st.metric("Quality Score", "8.5/10")

def analytics():
    st.header("Analytics Dashboard")
    
    # Velocity chart
    st.subheader("Team Velocity")
    # Burada gerçek bir grafik olacak
    st.line_chart({"Velocity": [10, 12, 15, 13, 17]})
    
    # Performance metrics
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Story Point Distribution")
        # Burada gerçek bir pasta grafik olacak
        st.bar_chart({"Points": [5, 3, 8, 2]})
    
    with col2:
        st.subheader("Priority Distribution")
        # Burada gerçek bir pasta grafik olacak
        st.bar_chart({"Priority": [8, 5, 3]})

def reports():
    st.header("Reports")
    
    # Report generation
    with st.expander("Generate New Report"):
        report_type = st.selectbox(
            "Report Type",
            ["Sprint Report", "Velocity Report", "Backlog Health Report"]
        )
        date_range = st.date_input(
            "Date Range",
            value=(datetime.now() - timedelta(days=30), datetime.now())
        )
        
        if st.button("Generate Report with AI"):
            with st.spinner("AI is generating your report..."):
                # AI rapor oluşturma
                st.success("Report Generation Complete!")
    
    # Recent reports
    st.subheader("Recent Reports")
    for i in range(3):
        with st.expander(f"Report {i+1} - {datetime.now().strftime('%Y-%m-%d')}"):
            st.write("Report content will appear here")
            st.download_button(
                "Download Report",
                data="Report content",
                file_name=f"report_{i+1}.pdf"
            ) 