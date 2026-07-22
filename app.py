import streamlit as st

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Medical Cost Analysis",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# Title
# -------------------------
st.title("🏥 Medical Cost Analysis & Visualization System")

st.markdown(
    """
### Python Data Analytics Internship Project

This project analyzes a medical insurance dataset using Python to discover the key factors affecting medical charges.

**Developed by:** Qusai  
**University:** Lovely Professional University
"""
)

st.divider()

# -------------------------
# Dataset Information
# -------------------------
st.header("📁 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Records", "1,338")
    st.metric("Features", "7")

with col2:
    st.metric("Missing Values", "0")
    st.metric("Dataset", "Insurance.csv")

st.divider()

# -------------------------
# Business Findings
# -------------------------
st.header("📌 Key Business Findings")

st.success("Smoking is the strongest predictor of medical charges.")

st.info("Medical expenses generally increase with age.")

st.warning("Higher BMI is associated with higher insurance costs.")

st.success("Regional differences exist in medical insurance charges.")

st.divider()

# -------------------------
# Charts
# -------------------------
st.header("📊 Project Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.image("images/histogram.png", use_container_width=True, caption="Age Distribution")
    st.image("images/box_plot.png", use_container_width=True, caption="Medical Charges Distribution")
    st.image("images/heatmap.png", use_container_width=True, caption="Correlation Heatmap")

with col2:
    st.image("images/scatter_plot.png", use_container_width=True, caption="Age vs Medical Charges")
    st.image("images/pie_chart.png", use_container_width=True, caption="Smoker Distribution")
    st.image("images/bar_chart.png", use_container_width=True, caption="Average Charges by Smoking Status")

st.divider()

# -------------------------
# Conclusion
# -------------------------
st.header("✅ Conclusion")

st.write("""
This project demonstrates how Python, Pandas, Matplotlib, and Seaborn can transform raw healthcare data into meaningful business insights that support better insurance decision-making.
""")

st.divider()

st.caption("Developed by Qusai | Python Data Analytics Internship Project")