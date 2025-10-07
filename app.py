import streamlit as st
from PIL import Image
import numpy as np
import random # Used to simulate AI detection

# --- Helper Functions (Simulated AI/Text Analysis) ---

def analyze_image(image):
    """
    Simulates AI image detection.
    In a real project, this would be a deep learning model.
    Here, we'll use a simple, random logic for demonstration.
    """
    # Convert image to numpy array to simulate processing
    img_array = np.array(image)

    # SIMULATION: A real model would analyze artifacts, pixels, etc.
    # We'll pretend images with an average pixel value over 128 are AI-generated.
    if img_array.mean() > 128:
        return "Likely AI-Generated", 0.2
    else:
        # Let's add some randomness to make it seem more realistic
        if random.random() > 0.5:
            return "Likely Authentic", 0.9
        else:
            return "Analysis Inconclusive", 0.6


def analyze_headline(url):
    """
    Simulates clickbait headline detection.
    In a real project, this would use Natural Language Processing (NLP).
    """
    # SIMULATION: Check for common clickbait words.
    clickbait_words = ["shocking", "secret", "unbelievable", "revealed", "what happens next"]
    # For the demo, we'll just use a placeholder title.
    # A real app would fetch the title from the URL.
    placeholder_title = "Shocking Secret of AI Revealed by Scientists!"

    if any(word in placeholder_title.lower() for word in clickbait_words):
        return "High Sensationalism Detected", 0.3
    else:
        return "Low Sensationalism", 0.8


# --- Streamlit Web App Interface ---

st.set_page_config(page_title="Media Credibility Hub", layout="wide", page_icon="🛡️")

# --- Hero Section / Title ---
st.markdown(
    """
    <style>
    .title-container {
        padding: 2rem;
        background: linear-gradient(135deg, #003366 0%, #006699 100%);
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .title-container h1 {
        font-size: 3rem;
        font-weight: bold;
    }
    .title-container p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    </style>
    <div class="title-container">
        <h1>🛡️ Media Credibility Hub</h1>
        <p>Analyze images and news links to uncover the truth in a world of AI.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# --- Main Application Logic ---
col1, col2 = st.columns(2, gap="large")

# --- Column 1: Image Uploader ---
with col1:
    st.header("1. Analyze an Image")
    st.markdown("Upload a photo to check if it's authentic or AI-generated.")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        st.write("") # Spacer
        with st.spinner('Analyzing image forensics...'):
            result, score = analyze_image(image)
            if score < 0.5:
                st.error(f"**Result:** {result} (Credibility Score: {score:.2f})")
            elif score < 0.7:
                st.warning(f"**Result:** {result} (Credibility Score: {score:.2f})")
            else:
                st.success(f"**Result:** {result} (Credibility Score: {score:.2f})")


# --- Column 2: URL Analyzer ---
with col2:
    st.header("2. Analyze a News URL")
    st.markdown("Paste a link to a news article to check its headline for sensationalism.")
    url_input = st.text_input("Enter URL here...")

    if url_input:
        # In a real app, you'd fetch the image from the URL here.
        st.info("URL analysis in this demo uses a placeholder image and title.")
        st.image("https://www.industrialempathy.com/img/remote/ZiClJf-1920w.jpg", caption="Image from URL (Placeholder)", use_column_width=True)

        st.write("") # Spacer
        with st.spinner('Analyzing URL content...'):
            # Image Analysis
            img_result, img_score = "Likely Authentic", 0.9 # Placeholder result

            # Headline Analysis
            headline_result, headline_score = analyze_headline(url_input)

            # Combined Score
            final_score = (img_score + headline_score) / 2

            st.write("---")
            st.subheader("Combined Analysis:")

            if final_score < 0.5:
                st.error(f"**Overall Credibility: LOW** (Score: {final_score:.2f})")
            elif final_score < 0.7:
                st.warning(f"**Overall Credibility: MEDIUM** (Score: {final_score:.2f})")
            else:
                st.success(f"**Overall Credibility: HIGH** (Score: {final_score:.2f})")

            st.write(f"
- **Image:** {img_result}
- **Headline:** {headline_result}
")
