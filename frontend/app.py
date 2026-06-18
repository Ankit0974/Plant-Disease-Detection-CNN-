import streamlit as st
import requests
from PIL import Image

API_URL = API_URL = "https://plant-backend-production-f0be.up.railway.app/predict"

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Plant Disease Detection")
st.write("Upload a leaf image to identify the disease.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Predict Disease"):

        with st.spinner("Analyzing image..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            try:

                response = requests.post(
                    API_URL,
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Prediction Complete!")

                    st.subheader("Result")

                    st.write(
                        f"**Disease:** {result['prediction']}"
                    )

                    st.write(
                        f"**Confidence:** {result['confidence']}%"
                    )

                else:
                    st.error(
                        f"Server Error: {response.status_code}"
                    )

            except Exception as e:
                st.error(
                    f"Could not connect to API\n\n{e}"
                )