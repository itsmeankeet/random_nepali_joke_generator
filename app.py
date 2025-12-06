import streamlit as st
from src.random_nepali_joke_generator.utils import generate_joke, generate_prompt
import time  # optional, if you want to simulate loading

# Set page config
st.set_page_config(
    page_title="Nepali Joke Generator 🤣",
    page_icon="😂",
    layout="centered"
)

# Title
st.markdown("<h1 style='text-align: center; color: green;'>Random Nepali Joke Generator 🤣</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input section
with st.container():
    st.markdown("### Enter a topic below and get a funny Nepali joke!")
    topic = st.text_input("Topic:", placeholder="e.g., school, football, office...")

# Button
if st.button("Generate Joke 😆") and topic:
    # Show spinner while generating
    with st.spinner('Generating a funny joke for you... 🤹‍♂️ Please wait!'):
        time.sleep(1)  # Optional: simulate delay
        prompt = generate_prompt(topic)
        joke = generate_joke(prompt)

    # Display joke in a styled box
    st.markdown(
        f"""
        <div style="
            background-color:#e0f7fa;
            padding:20px;
            border-radius:10px;
            border:2px solid #00acc1;
            margin-top:20px;
            text-align:center;
            font-size:18px;
        ">
            {joke}
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color: gray;'>Made with ❤️ in Streamlit</p>", unsafe_allow_html=True)
