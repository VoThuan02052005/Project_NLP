import streamlit as st
import numpy as np

def play_scale(rate):
    sample_rate = rate
    duration = 0.5  # Each note duration of 0.5 seconds

    # Frequencies for the notes do, re, mi, fa, so, la, ti, do
    frequencies = [523.25, 493.88, 440.00, 392.00, 349.23, 329.63, 293.66, 261.63]

    # Generate and concatenate the sine waves for each note
    scale = np.concatenate([
        np.sin(np.pi * freq * np.linspace(0, duration, int(sample_rate * duration), False))
        for freq in frequencies
    ])
    return scale

st.header("Media elements")

cols = st.columns(3)
cols[0].image("C:/Users/vothu/PycharmProjects\ProjectNLP/ChatGPT Image Nov 12, 2025, 02_44_42 PM.png", use_container_width=True, caption="sentiment analysis logo")
st.write("Play a scale")
st.audio(play_scale(44100), sample_rate=44100)
st.container(border=True).video("https://www.youtube.com/watch?v=cnHHCR7EW10&list=RDMMNrSkiem0t8I&index=4", autoplay=True)