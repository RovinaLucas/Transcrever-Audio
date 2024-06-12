import streamlit as st
import speech_recognition as sr

def principal():
  st.title("Transcrição de voz")
  upload = st.file_uploader("Faça o upload do arquivo de audio", type=["wav"])
  if upload is not None:
    transcrever(upload)

def transcrever(upload):
  recognizer = sr.Recognizer()
  with sr.AudioFile(upload) as source:
    st.write("Transcrevendo...")
    audio = recognizer.record(source)
    texto = recognizer.recognize_google(audio, language="pt-BR")
    st.write(texto)
principal()
