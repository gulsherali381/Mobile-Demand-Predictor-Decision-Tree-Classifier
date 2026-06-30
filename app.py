import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.set_page_config(page_title="Mobile Demand Predictor", page_icon="📱")

st.title("📱 Mobile Phone Demand Predictor")
st.markdown("### By Gulsher Ali | IIU AI Student")
st.markdown("---")

st.subheader("📝 Enter Phone Specifications")

col1, col2 = st.columns(2)

with col1:
    ram = st.slider("💾 RAM (GB)", 1, 16, 8)
    price = st.number_input("💰 Price (PKR)", min_value=5000, max_value=500000, value=75000, step=1000)
    camera = st.slider("📷 Camera (MP)", 2, 200, 50)

with col2:
    battery = st.slider("🔋 Battery (mAh)", 1000, 10000, 5000, step=100)
    storage = st.slider("💿 Storage (GB)", 16, 1024, 128)

st.markdown("---")

if st.button("🔍 Predict Demand!", use_container_width=True):
    input_data = np.array([[ram, price, camera, battery, storage]])
    prediction = model.predict(input_data)[0]

    st.markdown("---")
    st.subheader("📊 Result:")

    if prediction == 1:
        st.success("🔥 **High Demand!** This phone will sell well in the market!")
        st.balloons()
    else:
        st.error("📉 **Low Demand.** This phone will not sell well in the market.")

st.markdown("---")
st.caption("Decision Tree Classifier | Mobile Phone Demand Predictor")
