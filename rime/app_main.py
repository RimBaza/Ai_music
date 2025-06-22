import streamlit as st
from transformers import pipeline


generator = pipeline("text-generation", model="gpt2")

def get_lyrics(artist, word):
    return f"These are some dummy lyrics by {artist} using the word '{word}'..."


st.title("🎵 Rythme With AI")

word = st.text_input("Enter a word to rhyme with:", "Love")
artist = st.text_input("Enter an artist's name:", "John Doe")

if word and artist:
    lyrics = get_lyrics(artist, word)

    if word:
   
        st.text_area("Lyrics or sample text:", lyrics, height=200)

        st.subheader("AI-generated lines:")
        results = generator(f"Write a lyric with the word '{word}':", max_length=20, num_return_sequences=3)
       
        for i, result in enumerate(results):
            st.write(f"→ {result['generated_text']}")
    
    else :
        st.write("Please enter a word to generate rhymes.")
