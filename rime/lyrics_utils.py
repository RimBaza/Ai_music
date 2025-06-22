import streamlit as st
import lyricsgenius

genius = lyricsgenius.Genius("CCBghOfV8Oo3VDIZAK0ILVSwJc7BftY5bLi_pjVUl4YK0Dwil0O2eQ6_kY52Zuz_")

def get_lyrics(title, artist):
    try:
        song = genius.search_song(title, artist)
        return song.lyrics if song else "Chanson introuvable."
    except Exception as e:
        return f"Erreur lors de la récupération des paroles : {e}"
    

