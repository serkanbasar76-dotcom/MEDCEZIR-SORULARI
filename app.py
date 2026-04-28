import streamlit as st
import random

# --- TÜM 35 SORU ---
QUESTIONS = [
    {"question": "Yeniayda hangi gelgit çeşidi oluşur?", "options": ["Neap tide", "Spring tide", "Diurnal tide", "Mixed tide"], "answer": "B"},
    {"question": "Ay ve güneş dünyaya göre 90˚ doğrultuda bulunduğunda hangi gelgit oluşur?", "options": ["Mixed tide", "Spring tide", "Neap tide", "Semidiurnal tide"], "answer": "C"},
    {"question": "Ay kendi ekseni etrafında dönüşünü (bir ay günü) ne kadar sürede tamamlar?", "options": ["12 saat 25 dakika", "24 saat 00 dakika", "23 saat 56 dakika", "24 saat 50 dakika"], "answer": "D"},
    {"question": "Bir ay günü içerisinde 1 yükselme ve 1 alçalmanın yaşandığı gelgit tipi nedir?", "options": ["Diurnal tide (Günlük)", "Semidiurnal tide (Yarım günlük)", "Mixed tide (Karışık)", "Spring tide"], "answer": "A"},
    {"question": "Bir ay günü içerisinde 2 defa yükselme ve 2 defa alçalma yaşanıyorsa bu hangisidir?", "options": ["Spring tide", "Semidiurnal tide", "Neap tide", "Diurnal tide"], "answer": "B"},
    {"question": "Bir ay günü içerisinde düzensizliklerin yaşandığı gelgitler hangi adla anılır?", "options": ["Slack water", "Semidiurnal tide", "Mixed tide", "Neap tide"], "answer": "C"},
    {"question": "Spring tide için aşağıdakilerden hangisi doğrudur?", "options": ["Zayıf gelgitler olur.", "Kuvvetli gelgitler olur.", "Sadece kutuplarda görülür.", "Ay ve güneş 90 derece açıdadır."], "answer": "B"},
    {"question": "Ay, Güneş ve Dünya’nın aynı doğrultuda bulunduğu gelgit evresi hangisidir?", "options": ["Spring tide", "Neap tide", "Mixed tide", "Diurnal tide"], "answer": "A"},
    {"question": "Ayın Dolunay ve Yeniay evrelerinde hangi tip gelgit oluşur?", "options": ["Neap tide", "Semidiurnal tide", "Spring tide", "Slack water"], "answer": "C"},
    {"question": "Neap tide (ölü gelgit) için aşağıdakilerden hangisi söylenebilir?", "options": ["Kuvvetli gelgitler olur.", "Zayıf gelgitler olur.", "Ay ve dünya aynı hizadadır.", "En yüksek su seviyesidir."], "answer": "B"},
    {"question": "Ay ve Güneş'in Dünya'ya göre 90˚ doğrultuda bulunduğu durum hangi terimle ifade edilir?", "options": ["Spring tide", "Diurnal tide", "Neap tide", "Mixed tide"], "answer": "C"},
    {"question": "Kutuplarda yükselmenin belirgin görüldüğü gelgit tipi hangisidir?", "options": ["Neap tide", "Spring tide", "Mixed tide", "Semidiurnal tide"], "answer": "A"},
    {"question": "Ayın ilkdördün ve sondördün evrelerinde hangi gelgit oluşur?", "options": ["Spring tide", "Neap tide", "Diurnal tide", "Slack water"], "answer": "B"},
    {"question": "Ay ve güneşin dünyaya göre 90˚ doğrultuda bulunduğu gelgit tipi hangisidir?", "options": ["Mixed tide", "Spring tide", "Diurnal tide", "Neap tide"], "answer": "D"},
    {"question": "Ay, güneş ve dünyanın aynı doğrultuda bulunduğu gelgit tipi hangisidir?", "options": ["Spring tide", "Neap tide", "Semidiurnal tide", "Mixed tide"], "answer": "A"},
    {"question": "Bütün yüksek suların ortalaması (Mean High Water) kısaltması hangisidir?", "options": ["MLW", "MSL", "MHW", "HAT"], "answer": "C"},
    {"question": "Bütün alçak suların ortalaması (Mean Low Water) kısaltması hangisidir?", "options": ["MHW", "MLW", "LAT", "MSL"], "answer": "B"},
    {"question": "HW ve LW zamanlarında yaşanan gelgit akıntısının durgunlaştığı zamana ne denir?", "options": ["Spring tide", "Neap tide", "Slack water (Stand)", "Diurnal tide"], "answer": "C"},
    {"question": "Aşağıdakilerden hangisi dünya genelinde kullanılan bir gelgit cetveli değildir?", "options": ["Admiralty Tide Tables (ATT)", "Beaufort Wind Scale", "Amerikan gelgit cetvelleri (NOAA)", "Brown’s Almanac"], "answer": "B"},
    {"question": "ATT (Admiralty Tide Tables) kaç ciltten (volume) oluşur?", "options": ["4", "6", "10", "8"], "answer": "D"},
    {"question": "ATT Vol-1 (NP 201) hangi bölgeye aittir?", "options": ["Avrupa", "Birleşik krallık ve İrlanda", "Hint okyanusu", "Güney Pasifik"], "answer": "B"},
    {"question": "ATT Vol-2 (NP 202) hangi bölgenin verilerini kapsar?", "options": ["Hint Okyanusu", "Güney Çin Denizi", "Avrupa", "Batı Afrika"], "answer": "C"},
    {"question": "Hint Okyanusu gelgit verileri için hangi ATT cildine bakılmalıdır?", "options": ["Vol-1", "Vol-2", "Vol-3", "Vol-4"], "answer": "C"},
    {"question": "ATT Vol-4 (NP 204) hangi bölgeye aittir?", "options": ["Güney Pasifik Okyanusu", "Kuzey Pasifik Okyanusu", "Akdeniz", "Güney Amerika"], "answer": "A"},
    {"question": "Güney Çin Denizi ve Endonezya hangi ATT cildinde yer alır?", "options": ["Vol-5 (NP 205)", "Vol-8 (NP 208)", "Vol-2 (NP 202)", "Vol-1 (NP 201)"], "answer": "A"},
    {"question": "ATT Vol-6 (NP 206) hangi bölgeye aittir?", "options": ["Güney Amerika", "Hint Okyanusu", "Kuzey Pasifik Okyanusu", "Avrupa"], "answer": "C"},
    {"question": "Güneybatı Atlantik Okyanusu ve Güney Amerika verileri hangi cilttedir?", "options": ["Vol-3", "Vol-7 (NP 207)", "Vol-5", "Vol-1"], "answer": "B"},
    {"question": "Güneydoğu Atlantik Okyanusu, Batı Afrika ve Akdeniz hangi cilttedir?", "options": ["Vol-8 (NP 208)", "Vol-4 (NP 204)", "Vol-6 (NP 206)", "Vol-2 (NP 202)"], "answer": "A"},
    {"question": "Amerikan Tides Cetvellerinde (NOAA) hangi zaman referansı kullanılır?", "options": ["GMT", "UTC", "LMT (Local Mean Time)", "ZT"], "answer": "C"},
    {"question": "ATT cetvellerinde (British Admiralty) hangi zaman kullanılır?", "options": ["LMT", "GMT", "SMT", "LZT"], "answer": "B"},
    {"question": "ATT Part-I’de hangi limanlara ait listeler bulunur?", "options": ["Tali Limanlar", "Sadece nehir limanları", "Askeri limanlar", "Ana Limanlar (Standard Ports)"], "answer": "D"},
    {"question": "ATT Part-II’de hangi limanlara ait listeler bulunur?", "options": ["Tali Limanlar (Secondary Ports)", "Ana Limanlar", "Balıkçı limanları", "Sadece Avrupa limanları"], "answer": "A"},
    {"question": "Sadece ana limanlar için verilmiş olan cetvel tipi hangisidir?", "options": ["Diurnal curve", "Spring-neap eğrisi cetvelleri", "Tidal stream atlas", "Current tables"], "answer": "B"},
    {"question": "Java Denizi ve Vietnam gibi tropik bölgelerde hangi gelgit çeşidi görülür?", "options": ["Semidiurnal tide", "Mixed tide", "Spring tide", "Diurnal Tide (Günlük)"], "answer": "D"},
    {"question": "Avustralya kıyıları ve Doğu Asya'da yaygın görülen gelgit tipi hangisidir?", "options": ["Diurnal tide", "Mixed Tide (Karışık)", "Neap tide", "Spring tide"], "answer": "B"}
]

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Serkan Hoca Eğitim Portalı", layout="centered")

# --- CSS: EKRANA SIĞDIRMA VE RENK DÜZENLEMESİ ---
st.markdown("""
    <style>
    /* Üst ve alt boşlukları azaltarak ekrana sığdıralım */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    html, body, [class*="st-"] {
        color: #1a1a1a !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #ffffff;
        color: #2c3e50 !important;
        border: 1.5px solid #3498db;
        font-size: 15px;
        margin-bottom: 2px;
        text-align: left;
        padding-left: 15px;
    }
    .stButton>button:hover {
        background-color: #3498db;
        color: white !important;
    }
    .logo-box {
        text-align: center;
        padding: 15px;
        background: linear-gradient(135deg, #2c3e50, #3498db);
        border-radius: 12px;
        margin-bottom: 15px;
    }
    .logo-box h2, .logo-box p { color: white !important; margin: 0; }
    .question-card {
        background-color: #fcfcfc;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #3498db;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'initialized' not in st.session_state:
    st.session_state.questions = QUESTIONS.copy()
    random.shuffle(st.session_state.questions)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.app_state = "START"
    st.session_state.initialized = True

def start_fresh():
    random.shuffle(QUESTIONS)
    st.session_state.questions = QUESTIONS.copy()
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.app_state = "QUIZ"

# --- LOGO ---
st.markdown(f"""
    <div class="logo-box">
        <h2>🌊 GELGİT SINAVI</h2>
        <p>SERKAN HOCA İLE</p>
    </div>
""", unsafe_allow_html=True)

# --- AKIŞ ---
if st.session_state.app_state == "START":
    if st.session_state.current_index > 0:
        if st.button("🚀 Kaldığım Yerden Devam Et"):
            st.session_state.app_state = "QUIZ"
            st.rerun()
    
    if st.button("🎯 Sınavı Baştan Başlat"):
        start_fresh()
        st.rerun()

elif st.session_state.app_state == "QUIZ":
    q = st.session_state.questions[st.session_state.current_index]
    total_q = len(st.session_state.questions)
    curr_q = st.session_state.current_index + 1

    # Soru Sayacı (1/35 gibi) - Madde 11
    st.write(f"**Soru: {curr_q} / {total_q}**")
    
    # Soru Kartı
    st.markdown(f'<div class="question-card"><b>{q["question"]}</b></div>', unsafe_allow_html=True)

    # Şıklar
    labels = ["A", "B", "C", "D"]
    for i, opt in enumerate(q["options"]):
        if st.button(f"{labels[i]}) {opt}", key=f"opt_{st.session_state.current_index}_{i}"):
            is_correct = labels[i] == q["answer"]
            if is_correct: st.session_state.score += 1
            
            st.session_state.user_answers.append({
                "q": q["question"],
                "u_ans": f"{labels[i]}) {opt}",
                "c_ans": f"{q['answer']}) {q['options'][ord(q['answer'])-65]}",
                "res": is_correct
            })

            if st.session_state.current_index < total_q - 1:
                st.session_state.current_index += 1
                st.rerun()
            else:
                st.session_state.app_state = "RESULTS"
                st.rerun()

    if st.button("🚪 Kapat ve Sakla"):
        st.session_state.app_state = "START"
        st.rerun()

elif st.session_state.app_state == "RESULTS":
    perc = (st.session_state.score / len(st.session_state.questions)) * 100
    
    if perc >= 80:
        st.balloons()
        st.snow()
        st.markdown("<h2 style='text-align: center; color: #2ecc71;'>🎉 TEBRİKLER HARİKASIN 🎉</h2>", unsafe_allow_html=True)
    
    st.info(f"Başarı Oranı: %{perc:.1f} | Doğru: {st.session_state.score} | Yanlış: {len(st.session_state.questions)-st.session_state.score}")
    
    for i, item in enumerate(st.session_state.user_answers):
        icon = "✅" if item["res"] else "❌"
        with st.expander(f"Soru {i+1}: {icon}"):
            st.write(f"**Soru:** {item['q']}")
            st.write(f"Cevabın: {item['u_ans']}")
            if not item["res"]:
                st.write(f"Doğru: :green[{item['c_ans']}]")

    if st.button("🔄 Yeniden Başla"):
        start_fresh()
        st.rerun()
