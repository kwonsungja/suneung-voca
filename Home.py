# home.py

import streamlit as st
import pandas as pd
import random
from gtts import gTTS
import base64
from io import BytesIO, StringIO

# 데이터 직접 정의 (CSV 파일 없이 사용 가능)
@st.cache_data
def load_data():
    csv_data = """
word,meaning,part_of_speech,example
abandon,버리다,verb,He decided to abandon the plan.
acquire,얻다,verb,She acquired knowledge from books.
adapt,적응하다,verb,You must adapt to new environments.
adjust,조정하다,verb,He adjusted the mirror.
analyze,분석하다,verb,Scientists analyze the data carefully.
annual,매년의,adjective,The annual event is held in May.
approach,접근하다,verb,She approached the teacher.
appropriate,적절한,adjective,Wear appropriate clothes.
assume,가정하다,verb,Don’t assume too much.
attitude,태도,noun,His attitude is always positive.
available,이용 가능한,adjective,The service is available now.
benefit,이익,noun,Exercise has many benefits.
capable,능력 있는,adjective,She is capable of doing it.
cause,원인,noun,What is the cause of the problem?
claim,주장하다,verb,He claimed that he was innocent.
"""
    return pd.read_csv(StringIO(csv_data.strip()))

# 발음 오디오 생성
def tts_audio(word):
    tts = gTTS(text=word, lang='en')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    audio_bytes = mp3_fp.read()
    b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio autoplay="true" controls>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# 앱 UI
st.set_page_config(page_title="수능 보카", layout="centered")
st.title("📘 수능 영어 보카")
st.caption("예문과 함께 단어, 품사, 뜻을 확인하고 발음도 들어보세요!")

df = load_data()

# 무작위 단어 뽑기
if st.button("🎲 단어 뽑기"):
    word_info = df.sample(1).iloc[0]
    st.markdown(f"### 🔤 단어: **{word_info['word']}**")
    st.markdown(f"**품사**: *{word_info['part_of_speech']}*")
    st.markdown(f"**뜻**: {word_info['meaning']}")
    st.markdown(f"**예문**: _{word_info['example']}_")

    if st.button("🔊 발음 듣기"):
        tts_audio(word_info["word"])
else:
    st.markdown("👉 위 버튼을 눌러 단어를 시작해보세요.")


    if st.button("🔊 발음 듣기"):
        tts_audio(word)
else:
    st.markdown("👆 위 버튼을 눌러 단어를 시작해보세요.")

