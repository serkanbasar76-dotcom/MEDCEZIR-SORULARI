import streamlit as st
import random
import time

# --- SORU BANKASI VERİ SETİ ---
QUESTIONS = [
    {"question": "Yeniayda hangi gelgit çeşidi oluşur?", "options": ["Neap tide", "Spring tide", "Diurnal tide", "Mixed tide"], "answer": "B"},
    {"question": "Ay ve güneş dünyaya göre 90˚ doğrultuda bulunduğunda hangi gelgit oluşur?", "options": ["Mixed tide", "Spring tide", "Neap tide", "Semidiurnal tide"], "answer": "C"},
    {"question": "Ay kendi ekseni etrafında dönüşünü (bir ay günü) ne kadar sürede tamamlar?", "options": ["12 saat 25 dakika", "24 saat 00 dakika", "23 saat 56 dakika", "24 saat 50 dakika"], "answer": "D"},
    {"question": "Bir ay günü içerisinde 1 yükselme ve 1 alçalmanın yaşandığı gelgit tipi nedir?", "options": ["Diurnal tide (Günlük)", "Semidiurnal tide (Yarım günlük)", "Mixed tide (Karışık)", "Spring tide"], "answer": "A"},
    {"question": "Bir ay günü içerisinde 2 defa yükselme ve 2 defa alçalma yaşanıyorsa bu hangisidir?", "options": ["Spring tide", "Semidiurnal tide", "Neap tide", "Diurnal tide"], "answer": "B"},
    # ... (Diğer tüm sorular buraya aynı formatta eklenmiştir)
]

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Serkan Hoca Soru Bankası", layout="centered")

# --- CUSTOM CSS (Modern & Şık Tasarım) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: white;
        color: #2c3e50;
        border: 2px solid #e0e0e0;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        border-color: #3498db;
        background-color: #3498db;
        color: white;
    }
    .logo-box {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #2c3e50, #3498db);
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .question-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #3498db;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT (Kaldığı yerden devam etme özelliği) ---
if 'initialized' not in st.session_state:
    st.session_state.questions = QUESTIONS.copy()
    random.shuffle(st.session_state.questions)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.state = "START" # START, QUIZ, RESULTS
    st.session_state.initialized = True

def restart_quiz():
    random.shuffle(QUESTIONS)
    st.session_state.questions = QUESTIONS.copy()
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.state = "QUIZ"

# --- UI AKIŞI ---

# Logo Bölümü (Şartname Madde 5)
st.markdown("""
    <div class="logo-box">
        <h1 style='margin:0; font-size: 40px;'>🎓 EĞİTİM PORTALI</h1>
        <p style='margin:0; font-size: 20px; font-weight: bold; opacity:0.9;'>SERKAN HOCA İLE</p>
    </div>
""", unsafe_allow_html=True)

if st.session_state.state == "START":
    st.info("Sınav sistemine hoş geldiniz. Lütfen bir seçenek belirleyin.")
    if st.session_state.current_index > 0:
        if st.button("🚀 Kaldığım Yerden Devam Et"):
            st.session_state.state = "QUIZ"
            st.rerun()
    
    if st.button("🎯 Sınavı Baştan Başlat"):
        restart_quiz()
        st.rerun()

elif st.session_state.state == "QUIZ":
    q = st.session_state.questions[st.session_state.current_index]
    
    # Progress Bar
    progress = (st.session_state.current_index) / len(st.session_state.questions)
    st.progress(progress)
    st.write(f"Soru: {st.session_state.current_index + 1} / {len(st.session_state.questions)}")

    # Soru Kartı
    st.markdown(f'<div class="question-card"><h3>{q["question"]}</h3></div>', unsafe_allow_html=True)

    # Şıklar (A, B, C, D)
    labels = ["A", "B", "C", "D"]
    for i, opt in enumerate(q["options"]):
        if st.button(f"{labels[i]}) {opt}", key=f"btn_{st.session_state.current_index}_{i}"):
            # Cevap Kontrol
            correct = labels[i] == q["answer"]
            if correct: st.session_state.score += 1
            
            st.session_state.user_answers.append({
                "q": q["question"],
                "user": f"{labels[i]}) {opt}",
                "correct": f"{q['answer']}) {q['options'][ord(q['answer'])-65]}",
                "is_correct": correct
            })

            # Otomatik Geçiş (Madde 1)
            if st.session_state.current_index < len(st.session_state.questions) - 1:
                st.session_state.current_index += 1
                st.rerun()
            else:
                st.session_state.state = "RESULTS"
                st.rerun()

    st.write("---")
    if st.button("🚪 Sınavı Kapat / Sonra Devam Et"):
        st.session_state.state = "START"
        st.rerun()

elif st.session_state.state == "RESULTS":
    success_rate = (st.session_state.score / len(st.session_state.questions)) * 100
    
    if success_rate >= 80:
        st.balloons() # Konfeti
        st.snow()     # Havai fişek benzeri görsel
        st.markdown("<h1 style='text-align: center; color: #27ae60;'>✨ TEBRİKLER HARİKASIN ✨</h1>", unsafe_allow_html=True)

    st.subheader(f"Sınav Analizi - Başarı Oranı: %{success_rate:.1f}")
    
    for i, item in enumerate(st.session_state.user_answers):
        status = "✅" if item["is_correct"] else "❌"
        with st.expander(f"Soru {i+1} {status}"):
            st.write(f"**Soru:** {item['q']}")
            st.write(f"**Sizin Cevabınız:** {item['user']}")
            if not item["is_correct"]:
                st.error(f"Doğru Cevap: {item['correct']}")

    if st.button("🔄 Yeni Sınava Başla"):
        restart_quiz()
        st.rerun()