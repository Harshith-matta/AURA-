import streamlit as st

from agents.decision_agent import decision_agent
from agents.planning_agent import planning_agent
from agents.monitoring_agent import monitoring_agent
from agents.adaptation_agent import adaptation_agent
from agents.exam_agent import exam_agent
from agents.tool_agent import tool_agent

from utils.pdf_processor import extract_text_from_pdf

st.title("AURA - Agentic AI Student Assistant")

# Inputs
year = st.selectbox("Select Year", ["1st", "2nd", "3rd", "4th"])
goal = st.text_input("Your Goal (e.g., Data Science, Web Dev)")
days_left = st.number_input("Days left for exam", 0, 100)

# PDF Upload
pdf_file = st.file_uploader("Upload Study Material / Question Papers", type=["pdf"])

if st.button("Run AURA"):

    decision = decision_agent(year, goal, days_left)
    plan = planning_agent(decision)
    tools = tool_agent(goal)

    st.subheader("🧠 Decision Agent")
    st.write(decision)

    st.subheader("📅 Planning Agent")
    for p in plan:
        st.write("- " + p)

    st.subheader("🛠️ Tool Agent")
    for t in tools:
        st.write("- " + t)

    # Exam Agent
    if pdf_file:
        text = extract_text_from_pdf(pdf_file)
        exam_result = exam_agent(text)

        st.subheader("⚡ Exam Survival Agent")
        st.write("Important Topics:")
        st.write(exam_result["important_topics"])

    # Monitoring & Adaptation (demo values)
    progress = 40  # simulate
    monitor = monitoring_agent(2, 5)
    adapt = adaptation_agent(days_left, progress)

    st.subheader("📊 Monitoring Agent")
    st.write(monitor)

    st.subheader("🔁 Adaptation Agent")
    st.write(adapt)