import streamlit as st
import torch
from audiocraft.models import MusicGen

# Set page configuration for a sleek, professional design with an orange theme
st.set_page_config(
    page_title="Text-to-Audio Generator",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS for sharp lines and orange-themed UI
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            color: #333333;
        }
        .stApp {
            background-color: #ffffff;
        }
        .stTextInput > div > div > input {
            border: 1px solid #ff6600;
            border-radius: 0;
        }
        .stButton > button {
            background-color: #ff6600;
            color: #ffffff;
            border-radius: 0;
        }
    </style>
    ", unsafe_allow_html=True)

# Title and description
st.title("🎵 Text-to-Audio Generator")
st.markdown("Transform your text descriptions into **custom 30-second instrumental tracks**.")

# Input field for the text description
description = st.text_input("Enter a description of the music you want to generate:")

# Generate button
if st.button("Generate Music"):
    if not description:
        st.warning("Please enter a music description to proceed.")
    else:
        with st.spinner("Generating your custom track..."):
            # Load the pre-trained MusicGen model
            model = MusicGen.get_pretrained('melody')
            model.set_generation_params(duration=30)

            # Generate the music based on the description
            audio_output = model.generate([description])

            # Convert the output to a playable format
            output_path = "generated_music.wav"
            model.save_wav(audio_output[0], output_path)

        # Display the audio player
        st.audio(output_path, format='audio/wav')
        st.success("Your custom instrumental track is ready!")