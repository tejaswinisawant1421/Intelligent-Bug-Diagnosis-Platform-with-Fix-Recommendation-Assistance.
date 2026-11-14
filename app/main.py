
import streamlit as st

st.set_page_config(
    page_title="Intelligent Bug Diagnosis Platform",
    page_icon="🐞",
    layout="wide"
)

st.title("🐞 Intelligent Bug Diagnosis Platform")

st.subheader(
    "AI-Powered Bug Analysis and Fix Recommendations"
)

st.markdown("---")

st.success("Welcome! Your application is running successfully.")

st.write(
    """
    This platform helps developers analyze software bugs,
    identify possible root causes, detect duplicate defects,
    and recommend potential solutions using AI and RAG.
    """
)

st.header("Project Modules")

col1, col2 = st.columns(2)

with col1:
    st.info("**1. Bug Submission Module**")
    st.write("Submit bug descriptions, error logs and stack traces.")

    st.info("**2. Log Analysis Module**")
    st.write("Analyze error messages and technical logs.")

with col2:
    st.info("**3. Duplicate Detection Module**")
    st.write("Find similar historical bug reports.")

    st.info("**4. Fix Recommendation Module**")
    st.write("Generate possible solutions for reported bugs.")

st.markdown("---")
st.caption("Milestone 1 | Foundation and Bug Understanding")
