import streamlit as st
import random

# --- TÜM 35 SORU (HAM VERİ) ---
RAW_QUESTIONS = [
    {"question": "Yeniayda hangi gelgit çeşidi oluşur?", "options": ["Neap tide", "Spring tide", "Diurnal tide", "Mixed tide"], "answer_index": 1},
    {"question": "Ay ve güneş dünyaya göre 90˚ doğrultuda bulunduğunda hangi gelgit oluşur?", "options": ["Mixed tide", "Spring tide", "Neap tide", "Semidiurnal tide"], "answer_index": 2},
    {"question": "Ay kendi ekseni etrafında dönüşünü (bir ay günü) ne kadar sürede tamamlar?", "options": ["12 saat 25 dakika", "24 saat 00 dakika", "23 saat 56 dakika", "24 saat 50 dakika"], "answer_index": 3},
    {"question": "Bir ay günü içerisinde 1 yükselme ve 1 alçalmanın yaşandığı gelgit tipi nedir?", "options": ["Diurnal tide (Günlük)", "Semidiurnal tide (Yarım günlük)", "Mixed tide (Karışık)", "Spring tide"], "answer_index": 0},
    {"question": "Bir ay günü içerisinde 2 defa yükselme ve 2 defa alçalma yaşanıyorsa bu hangisidir?", "options": ["Spring tide", "Semidiurnal tide", "Neap tide", "Diurnal tide"], "answer_index": 1},
    {"question": "Bir ay günü içerisinde düzensizliklerin yaşandığı gelgitler hangi adla anılır?", "options": ["Slack water", "Semidiurnal tide", "Mixed tide", "Neap tide"], "answer_index": 2},
    {"question": "Spring tide için aşağıdakilerden hangisi doğrudur?", "options": ["Zayıf gelgitler olur.", "Kuvvetli gelgitler olur.", "Sadece kutuplarda görülür.", "Ay ve güneş 90 derece açıdadır."], "answer_index": 1},
    {"question": "Ay, Güneş ve Dünya’nın aynı doğrultuda bulunduğu gelgit evresi hangisidir?", "options": ["Spring tide", "Neap tide", "Mixed tide", "Diurnal tide"], "answer_index": 0},
    {"question": "Ayın Dolunay ve Yeniay evrelerinde hangi tip gelgit oluşur?", "options": ["Neap tide", "Semidiurnal tide", "Spring tide", "Slack water"], "answer_index": 2},
    {"question": "Neap tide (ölü gelgit) için aşağıdakilerden hangisi söylenebilir?", "options": ["Kuvvetli gelgitler olur.", "Zayıf gelgitler olur.", "Ay ve dünya aynı hizadadır.", "En yüksek su seviyesidir."], "answer_index": 1},
    {"question": "Ay ve Güneş'in Dünya'ya göre 90˚ doğrultuda bulunduğu durum hangi terimle ifade edilir?", "options": ["Spring tide", "Diurnal tide", "Neap tide", "Mixed tide"], "answer_index": 2},
    {"question": "Kutuplarda yükselmenin belirgin görüldüğü gelgit tipi hangisidir?", "options": ["Neap tide", "Spring tide", "Mixed tide", "Semidiurnal tide"], "answer_index": 0},
    {"question": "Ayın ilkdördün ve sondördün evrelerinde hangi gelgit oluşur?", "options": ["Spring tide", "Neap tide", "Diurnal tide", "Slack water"], "answer_index": 1},
    {"question": "Ay ve güneşin dünyaya göre 90˚ doğrultuda bulunduğu gelgit tipi hangisidir?", "options": ["Mixed tide", "Spring tide", "Diurnal tide", "Neap tide"], "answer_index": 3},
    {"question": "Ay, güneş ve dünyanın aynı doğrultuda bulunduğu gelgit tipi hangisidir?", "options": ["Spring tide", "Neap tide", "Semidiurnal tide", "Mixed tide"], "answer_index": 0},
    {"question": "Bütün yüksek suların ortalaması (Mean High Water) kısaltması hangisidir?", "options": ["MLW", "MSL", "MHW", "HAT"], "answer_index": 2},
    {"question": "Bütün alçak suların ortalaması (Mean Low Water) kısaltması hangisidir?", "options": ["MHW", "MLW", "LAT", "MSL"], "answer_index": 1},
    {"question": "HW ve LW zamanlarında yaşanan gelgit akıntısının durgunlaştığı zamana ne denir?", "options": ["Spring tide", "Neap tide", "Slack water (Stand)", "Diurnal tide"], "answer_index": 2},
    {"question": "Aşağıdakilerden hangisi dünya genelinde kullanılan bir gelgit cetveli değildir?", "options": ["Admiralty Tide Tables (ATT)", "Beaufort Wind Scale", "Amerikan gelgit cetvelleri (NOAA)", "Brown’s Almanac"], "answer_index": 1},
    {"question": "ATT (Admiralty Tide Tables) kaç ciltten (volume) oluşur?", "options": ["4", "6", "10", "8"], "answer_index": 3},
    {"question": "ATT Vol-1 (NP 201) hangi bölgeye aittir?", "options": ["Avrupa", "Birleşik krallık ve İrlanda", "Hint okyanusu", "Güney Pasifik"], "answer_index": 1},
    {"question": "ATT Vol-2 (NP 202) hangi bölgenin verilerini kapsar?", "options": ["Hint Okyanusu", "Güney Çin Denizi", "Avrupa", "Batı Afrika"], "answer_index": 2},
    {"question": "Hint Okyanusu gelgit verileri için hangi ATT cildine bakılmalıdır?", "options": ["Vol-1", "Vol-2", "Vol-3", "Vol-4"], "answer_index": 2},
    {"question": "ATT Vol-4 (NP 204) hangi bölgeye aittir?", "options": ["Güney Pasifik Okyanusu", "Kuzey Pasifik Okyanusu", "Akdeniz", "Güney Amerika"], "answer_index": 0},
    {"question": "Güney Çin Denizi ve Endonezya hangi ATT cildinde yer alır?", "options": ["Vol-5 (NP 205)", "Vol-8 (NP 208)", "Vol-2 (NP 202)", "Vol-1 (NP 201)"], "answer_index": 0},
    {"question": "ATT Vol-6 (NP 206) hangi bölgeye aittir?", "options": ["Güney Amerika", "Hint Okyanusu", "Kuzey Pasifik Okyanusu", "Avrupa"], "answer_index": 2},
    {"question": "Güneybatı Atlantik Okyanusu ve Güney Amerika verileri hangi cilttedir?", "options": ["Vol-3", "Vol-7 (NP 207)", "Vol-5", "Vol-1"], "answer_index": 1},
    {"question": "Güneydoğu Atlantik Okyanusu, Batı Afrika ve Akdeniz hangi cilttedir?", "options": ["Vol-8 (NP 208)", "Vol-4 (NP 204)", "Vol-6 (NP 206)", "Vol-2 (NP 202)"], "answer_index": 0},
    {"question": "Amerikan Tides Cetvellerinde (NOAA) hangi zaman referansı kullanılır?", "options": ["GMT", "UTC", "LMT (Local Mean Time)", "ZT"], "answer_index": 2},
    {"question": "ATT cetvellerinde (British Admiralty) hangi zaman kullanılır?", "options": ["LMT", "GMT", "SMT", "LZT"], "answer_index": 1},
    {"question": "ATT Part-I’de hangi limanlara ait listeler bulunur?", "options": ["Tali Limanlar", "Sadece nehir limanları", "Askeri limanlar", "Ana Limanlar (Standard Ports)"], "answer_index": 3},
    {"question": "ATT Part-II’de hangi limanlara ait listeler bulunur?", "options": ["Tali Limanlar (Secondary Ports)", "Ana Limanlar", "Balıkçı limanları", "Sadece Avrupa limanları"], "answer_index": 0},
    {"question": "Sadece ana limanlar için verilmiş olan cetvel tipi hangisidir?", "options": ["Diurnal curve", "Spring-neap eğrisi cetvelleri", "Tidal stream atlas", "Current tables"], "answer_index": 1},
    {"question": "Java Denizi ve Vietnam gibi tropik bölgelerde hangi gelgit çeşidi görülür?", "options": ["Semidiurnal tide", "Mixed tide", "Spring tide", "Diurnal Tide (Günlük)"], "answer_index": 3},
    {"question": "Avustralya kıyıları ve Doğu Asya'da yaygın görülen gelgit tipi hangisidir?", "options": ["Diurnal tide", "Mixed Tide (Karışık)", "Neap tide", "Spring tide"], "answer_index": 1}
]

# --- SESSION STATE ---
if 'initialized' not in st.session_state:
    st.session_state.questions = []
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.app_state = "START"
    st.session_state.initialized = True

def prepare_quiz():
    """Soruları ve şıkları dengeli şekilde karıştıran ana algoritma."""
    shuffled_qs = []
    temp_qs = RAW_QUESTIONS.copy()
    random.shuffle(temp_qs) # Soruları karıştır (Madde 4)
    
    for item in temp_qs:
        opts = item["options"].copy()
        correct_text = opts[item["answer_index"]] # Doğru cevabı metin olarak sakla
        random.shuffle(opts) # Şıkları kendi içinde karıştır
        new_correct_index = opts.index(correct_text) # Yeni doğru şıkkın harf karşılığını bul
        
        shuffled_qs.append({
            "question": item["question"],
            "options": opts,
            "answer_index": new_correct_index
        })
    
    st.session_state.questions = shuffled_qs
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.app_state = "QUIZ"

# --- SAYFA AYARLARI VE CSS ---
st.set_page_config(page_title="Serkan Hoca Eğitim Portalı", layout="centered")

st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; }
    .q-badge { background-color: #34495e; color: white !important; padding: 4px 12px; border-radius: 20px; font-weight: bold; margin-bottom: 10px; }
    html, body, [class*="st-"] { color: #2c3e50 !important; }
    .stExpander div { color: #ffffff !important; }
    .stExpander { background-color: #2c3e50 !important; border-radius: 8px; margin-bottom: 8px; }
    .stExpander summary p { color: #ffffff !important; font-weight: bold; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ffffff; color: #2c3e50 !important; border: 1.5px solid #3498db; text-align: left; padding-left: 15px; }
    .stButton>button:hover { background-color: #3498db; color: white !important; }
    .logo-box { text-align: center; padding: 15px; background: linear-gradient(135deg, #2c3e50, #3498db); border-radius: 12px; margin-bottom: 15px; }
    .logo-box h2, .logo-box p { color: white !important; margin: 0; }
    .question-card { background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 5px solid #2c3e50; margin-bottom: 10px; }
    .result-panel { color: white !important; background-color: #1a1a1a; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 20px;}
    .result-panel h3, .result-panel p { color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
st.markdown(f'<div class="logo-box"><h2>🌊 GELGİT SINAVI</h2><p>SERKAN HOCA İLE</p></div>', unsafe_allow_html=True)

# --- AKIŞ ---
if st.session_state.app_state == "START":
    if st.session_state.questions and st.session_state.current_index > 0:
        if st.button("🚀 Kaldığım Yerden Devam Et"):
            st.session_state.app_state = "QUIZ"
            st.rerun()
    
    if st.button("🎯 Sınavı Baştan Başlat"):
        prepare_quiz()
        st.rerun()

elif st.session_state.app_state == "QUIZ":
    q = st.session_state.questions[st.session_state.current_index]
    labels = ["A", "B", "C", "D"]
    
    st.markdown(f'<div class="q-badge">SORU: {st.session_state.current_index + 1} / {len(st.session_state.questions)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="question-card"><b>{q["question"]}</b></div>', unsafe_allow_html=True)

    for i, opt in enumerate(q["options"]):
        if st.button(f"{labels[i]}) {opt}", key=f"q_{st.session_state.current_index}_opt_{i}"):
            is_correct = i == q["answer_index"]
            if is_correct: st.session_state.score += 1
            
            st.session_state.user_answers.append({
                "q": q["question"],
                "u_ans": f"{labels[i]}) {opt}",
                "c_ans": f"{labels[q['answer_index']]}) {q['options'][q['answer_index']]}",
                "res": is_correct
            })

            if st.session_state.current_index < len(st.session_state.questions) - 1:
                st.session_state.current_index += 1
                st.rerun()
            else:
                st.session_state.app_state = "RESULTS"
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚪 Kapat ve Sakla"):
        st.session_state.app_state = "START"
        st.rerun()

elif st.session_state.app_state == "RESULTS":
    perc = (st.session_state.score / len(st.session_state.questions)) * 100
    if perc >= 80:
        st.balloons(); st.snow()
        st.markdown("<h2 style='text-align: center; color: #2ecc71;'>🎉 TEBRİKLER HARİKASIN 🎉</h2>", unsafe_allow_html=True)
    
    st.markdown(f'<div class="result-panel"><h3>Sonuç: %{perc:.1f}</h3><p>Doğru: {st.session_state.score} | Yanlış: {len(st.session_state.questions)-st.session_state.score}</p></div>', unsafe_allow_html=True)
    
    wrongs = [item for item in st.session_state.user_answers if not item["res"]]
    if not wrongs:
        st.success("Tebrikler! Hiç yanlışınız yok.")
    else:
        for i, item in enumerate(wrongs):
            with st.expander(f"❌ Yanlış Yapılan Soru {i+1}"):
                st.markdown(f"<p style='color: white;'><b>Soru:</b> {item['q']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #ff7675;'><b>Senin Cevabın:</b> {item['u_ans']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #55efc4;'><b>Doğru Cevap:</b> {item['c_ans']}</p>", unsafe_allow_html=True)

    if st.button("🔄 Yeniden Başla"):
        prepare_quiz()
        st.rerun()
