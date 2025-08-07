# home.py

import streamlit as st
import pandas as pd
import random
from gtts import gTTS
import base64
from io import BytesIO

# CSV 파일 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("suneung_vocab.csv")
    return df

# 발음용 MP3 생성 및 재생
def tts_audio(word):
    tts = gTTS(text=word, lang='en')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    audio_bytes = mp3_fp.read()
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
        <audio autoplay="true" controls>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

# 앱 제목
st.title("📘 수능 보카 마스터")
st.subheader("고1을 위한 수능 필수 단어 암기 앱")

# 데이터 불러오기
df = load_data()

# 무작위 단어 선택
if st.button("🎲 단어 뽑기"):
    random_idx = random.randint(0, len(df) - 1)
    word = df.loc[random_idx, "word"]
    pos = df.loc[random_idx, "pos"]
    meaning = df.loc[random_idx, "meaning"]

    st.markdown(f"### 📝 단어: **{word}**")
    st.markdown(f"**품사**: {pos}")
    st.markdown(f"**뜻**: {meaning}")
    
    if st.button("🔊 발음 듣기"):
        tts_audio(word)
else:
    st.markdown("👉 위 버튼을 눌러 단어를 시작해보세요.")

