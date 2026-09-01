import streamlit as st
from google import genai
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Instrument Analyzer",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 InstruVision")
st.write("Upload an image and get insights using Gemini 3.6 Flash.")

# -----------------------------
# Gemini API Configuration
# -----------------------------
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# -----------------------------
# Image Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Analyze Button
# -----------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

    with col2:

        if st.button("Analyze Image"):

            with st.spinner("Analyzing image..."):

                prompt = """
                  You are an AI music education assistant.

                  Analyze the uploaded image of a musical instrument carefully.

                  Perform the following analysis:

                  1. INSTRUMENT IDENTIFICATION
                  - Identify the instrument.
                  - State your confidence level.

                  2. INSTRUMENT FAMILY
                  - Classify it as String, Wind, Percussion, Keyboard, or Electronic.

                  3. HOW IT'S PLAYED
                  - Briefly explain how the instrument is typically played.

                  4. VISIBLE PARTS & FUNCTIONS
                  - Identify visible parts and explain what each does.

                  5. LEARNING DIFFICULTY
                  - Give a general sense of how beginner-friendly this instrument is.

                  6. RELATED INSTRUMENTS
                  - Name 2-3 similar or related instruments.

                  7. INTERESTING FACTS
                  - Share 2-3 interesting facts.

                  OUTPUT FORMAT:

                  ## 🎵 Instrument Identification
                  Name:
                  Confidence:

                  ## 🎼 Family
                  ...

                  ## 🖐️ How It's Played
                  ...

                  ## 🔧 Visible Parts

                  | Part | Function |
                  |---|---|

                  ## 📈 Learning Difficulty
                  ...

                  ## 🔗 Related Instruments
                  - ...

                  ## 💡 Interesting Facts
                  - ...

                  IMPORTANT:
                  Do not claim a specific brand or model unless it is clearly visible.
"""

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=[prompt, image]
                )

                st.subheader("Analysis Result")
                st.write(response.text)