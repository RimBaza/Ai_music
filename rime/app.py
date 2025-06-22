import streamlit as st
from lyrics_utils import get_lyrics
from transformers import pipeline, set_seed

st.markdown(
    """
    <style>
    /* Fond de toute la page */
    html, body, .stApp {
        background-color: #FBFBF9 !important;
        color: black !important;
    }

    /* Texte de tous les éléments Streamlit */
    [class^="css"] {
        color: black !important;
    }

    /* Fond de certains conteneurs spécifiques */
    .stApp > header, .block-container {
        background-color: #FBFBF9 !important;
    }

    /* Saisie texte et labels */
    label, .stTextInput {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

generator = pipeline("text-generation", model="gpt2")

# Optional: define a dummy lyrics fetcher (you can replace with Genius later)
def get_lyrics(artist, word):
    return f"These are some dummy lyrics by {artist} using the word '{word}'..."

# Streamlit interface
st.title("🎵 Rythme With AI")

word = st.text_input("Enter a word to rhyme with:", "Love")

if word:
    # Get lyrics (or use placeholder)
    #lyrics = get_lyrics("adele", word)
    #st.text_area("Lyrics or sample text:", lyrics, height=200)

    # Generate AI lyrics
    st.subheader("AI-generated lines:")
    results = generator(f"Write a lyric with the word '{word}':", max_length=30, num_return_sequences=3)
    for i, result in enumerate(results):
        st.write(f"→ {result['generated_text']}")
else:
    st.write("Please enter a word to generate rhymes.")