import streamlit as st
from engine import StoryEngine

st.set_page_config(page_title="AI Story Weaver (OpenAI Engine)", layout="wide")

if "engine" not in st.session_state:
    st.session_state.engine = StoryEngine()

if "started" not in st.session_state:
    st.session_state.started = False

if "choices" not in st.session_state:
    st.session_state.choices = None

st.title("📖 AI Story Weaver (OpenAI Engine)")

# Sidebar — Story Setup
with st.sidebar:
    st.header("Story Setup")
    title = st.text_input("Title")
    genre = st.selectbox(
        "Genre",
        ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror", "Comedy"]
    )
    hook = st.text_area("Initial Hook")
    temperature = st.slider("Creativity", 0.1, 1.5, 0.7)

    if st.button("Start Story"):
        result = st.session_state.engine.continue_story(genre, hook, temperature)
        st.session_state.started = True

# Main Story UI
if st.session_state.started:

    st.subheader("📜 Story So Far")
    for paragraph in st.session_state.engine.story:
        st.markdown(paragraph)

    user_input = st.text_area("Add your part")

    col1, col2, col3 = st.columns(3)

    # Continue AI
    if col1.button("Continue with AI"):
        st.session_state.engine.continue_story(genre, user_input, temperature)

    # Branching choices
    if col2.button("Give Me Choices"):
        st.session_state.choices = st.session_state.engine.give_choices(genre, temperature)

    # Undo last
    if col3.button("Undo Last"):
        if st.session_state.engine.story:
            st.session_state.engine.story.pop()

    # Show choices
    if st.session_state.choices:
        st.subheader("Choose a direction")
        for choice in st.session_state.choices:
            if st.button(choice):
                st.session_state.engine.story.append(choice)
                st.session_state.choices = None
