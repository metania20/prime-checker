import streamlit as st
import math
import random
import time
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Prime Lab: Interactive Studio",
    page_icon="🧬",
    layout="centered"
)

# 2. Inisialisasi Session State
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = [
        {"Nama Pemain": "Bot Einstein", "Skor": 60, "Mode": "30 Detik"}
    ]
if "game_aktif" not in st.session_state:
    st.session_state.game_aktif = False
if "waktu_mulai" not in st.session_state:
    st.session_state.waktu_mulai = 0
if "skor_time" not in st.session_state:
    st.session_state.skor_time = 0
if "soal_time" not in st.session_state:
    st.session_state.soal_time = random.randint(2, 99)
if "angka_lab" not in st.session_state:
    st.session_state.angka_lab = 31

# 3. Fungsi Logika Matematika & Teori Bilangan
def cek_prima_detail(n):
    if n <= 1:
        return False, []
    faktor = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            faktor.append(i)
            if i != n // i:
                faktor.append(n // i)
    faktor.sort()
    return (len(faktor) == 2), faktor

def cari_prima_berikutnya(n):
    kandidat = n + 1
    while not cek_prima_detail(kandidat)[0]:
        kandidat += 1
    return kandidat

# 4. CSS Dinamis & Styling Futuristik
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
        color: #0f172a;
    }
    p, label, span, div, h1, h2, h3, .stMarkdown {
        color: #0f172a;
    }
    .lab-title {
        font-size: 2.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #0284c7, #4f46e5, #db2777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
    }
    .lab-sub {
        text-align: center;
        color: #475569;
        font-size: 0.95rem;
        margin-bottom: 22px;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(12px);
        border-radius: 18px;
        padding: 22px;
        border: 1px solid #cbd5e1;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        margin-bottom: 16px;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(10, 1fr);
        gap: 6px;
        margin-top: 15px;
    }
    .cell-prime {
        background: linear-gradient(135deg, #10b981, #059669);
        color: #ffffff !important;
        font-weight: bold;
        text-align: center;
        padding: 8px 0;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.25);
        font-size: 0.85rem;
    }
    .cell-comp {
        background: #f1f5f9;
        color: #64748b !important;
        text-align: center;
        padding: 8px 0;
        border-radius: 8px;
        font-size: 0.85rem;
        text-decoration: line-through;
    }
    .cell-one {
        background: #fef3c7;
        color: #b45309 !important;
        text-align: center;
        padding: 8px 0;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .badge-spesial {
        display: inline-block;
        background: #f3e8ff;
        border: 1px solid #c084fc;
        color: #6b21a8 !important;
        font-weight: 600;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 0.82rem;
        margin: 4px 4px 4px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="lab-title">🧬 Prime Lab: Interactive Studio</div>', unsafe_allow_html=True)
st.markdown('<div class="lab-sub">Laboratorium Eksplorasi Teori Bilangan, Saringan Visual, Kriptografi RSA, & Arena Game</div>', unsafe_allow_html=True)

import streamlit.components.v1 as components

# 4b. Musik Latar Fun & Bouncy (Arpeggio + Bass Ringan)
components.html(
    """
    <script>
        let audioCtx = null;
        let isStarted = false;
        let step = 0;

        // Pola melodi ceria naik-turun (C major / G major / A minor / F major)
        const leadNotes = [
            523.25, 659.25, 783.99, 659.25,
            880.00, 783.99, 659.25, 587.33,
            587.33, 783.99, 987.77, 783.99,
            880.00, 783.99, 659.25, 523.25
        ];

        // Bass ringan pengiring agar lebih "fun"
        const bassNotes = [
            130.81, 0, 196.00, 0,
            220.00, 0, 164.81, 0,
            196.00, 0, 246.94, 0,
            174.61, 0, 196.00, 0
        ];

        function playTone(freq, duration, type, peakGain) {
            if (!audioCtx || freq === 0) return;
            const osc = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();

            osc.type = type;
            osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

            const now = audioCtx.currentTime;
            gainNode.gain.setValueAtTime(0.0008, now);
            gainNode.gain.exponentialRampToValueAtTime(peakGain, now + 0.02);
            gainNode.gain.exponentialRampToValueAtTime(0.0008, now + duration);

            osc.connect(gainNode);
            gainNode.connect(audioCtx.destination);

            osc.start(now);
            osc.stop(now + duration + 0.02);
        }

        function playBeat() {
            const idx = step % leadNotes.length;
            playTone(leadNotes[idx], 0.18, "triangle", 0.085);
            playTone(bassNotes[idx], 0.22, "sine", 0.07);
            step++;
        }

        function startFunMusic() {
            if (isStarted) return;
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!audioCtx) {
                audioCtx = new AudioContext();
            }
            if (audioCtx.state === "suspended") {
                audioCtx.resume();
            }
            if (audioCtx.state === "running") {
                isStarted = true;
                playBeat();
                setInterval(playBeat, 210); // Tempo upbeat & fun
            }
        }

        window.addEventListener("load", startFunMusic);
        startFunMusic();

        ["click", "touchstart", "keydown"].forEach(evt => {
            window.parent.document.addEventListener(evt, startFunMusic, { once: true });
            document.addEventListener(evt, startFunMusic, { once: true });
        });
    </script>
    """,
    height=0,
)
# 4 Tab Super Interaktif
t_cek, t_grid, t_game, t_rsa = st.tabs([
    "🔬 Lab Deteksi & Pola",
    "🟩 Papan Saringan Visual",
    "⏱️ Time-Attack & Leaderboard",
    "🔐 Simulasi Kriptografi RSA"
])

# ==========================================================
# TAB 1: LIVE REACTIVE DETECTOR & POLA SPESIAL
# ==========================================================
with t_cek:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    c_in, c_btn = st.columns([3, 1])
    with c_btn:
        st.write("")
        st.write("")
        if st.button("🎲 Angka Kejutan", use_container_width=True):
            st.session_state.angka_lab = random.choice([13, 17, 29, 31, 37, 42, 71, 97, 101, 121])

    with c_in:
        n_uji = st.number_input(
            "Ketik atau ubah angka (langsung teranalisis otomatis):",
            min_value=0,
            max_value=1000000000,
            value=st.session_state.angka_lab,
            step=1
        )
        st.session_state.angka_lab = n_uji

    is_p, faktor_n = cek_prima_detail(n_uji)
    prima_next = cari_prima_berikutnya(n_uji)
    jarak_prima = prima_next - n_uji

    if is_p:
        st.success(f"✨ **{n_uji:,}** adalah **BILANGAN PRIMA**!")
        
        # Deteksi Pola Unik Teori Bilangan
        badges = ['<span class="badge-spesial">✓ Tepat 2 Pembagi</span>']
        if cek_prima_detail(n_uji - 2)[0] or cek_prima_detail(n_uji + 2)[0]:
            badges.append('<span class="badge-spesial">👯 Twin Prime (Prima Kembar)</span>')
        
        dibalik = int(str(n_uji)[::-1])
        if dibalik != n_uji and cek_prima_detail(dibalik)[0]:
            badges.append(f'<span class="badge-spesial">🔄 Emirp (Dibalik jadi {dibalik}, tetap prima!)</span>')
            
        st.markdown("".join(badges), unsafe_allow_html=True)
    else:
        st.error(f"🔸 **{n_uji:,}** **BUKAN Bilangan Prima** ({'Bilangan Komposit' if n_uji > 1 else 'Batas Awal'}).")
        if n_uji > 1:
            st.write(f"**Pembagi ({len(faktor_n)} faktor):** `{', '.join(map(str, faktor_n))}`")

    st.divider()
    m1, m2, m3 = st.columns(3)
    m1.metric("Status Bilangan", "PRIMA" if is_p else "NON-PRIMA")
    m2.metric("Prima Berikutnya", f"{prima_next:,}")
    m3.metric("Prime Gap (Jarak)", f"+{jarak_prima} langkah")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================
# TAB 2: PAPAN GRID SARINGAN ERATOSTHENES INTERAKTIF
# ==========================================================
with t_grid:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🟩 Visualisasi Saringan Eratosthenes")
    st.write("Geser slider untuk menyaring bilangan komposit secara visual. Kotak **hijau menyala** adalah bilangan prima!")
    
    max_grid = st.slider("Tampilkan papan angka dari 1 sampai:", 20, 100, 50, step=10)
    filter_kelipatan = st.selectbox(
        "Sorot proses eliminasi kelipatan:",
        ["Tampilkan Hasil Akhir (Semua Prima)", "Tahap 1: Coret Kelipatan 2", "Tahap 2: Coret Kelipatan 2 & 3", "Tahap 3: Coret Kelipatan 2, 3, & 5"]
    )

    html_grid = '<div class="grid-container">'
    for num in range(1, max_grid + 1):
        if num == 1:
            html_grid += f'<div class="cell-one" title="1 bukan prima">1</div>'
        else:
            tercoret = False
            if filter_kelipatan == "Tahap 1: Coret Kelipatan 2":
                tercoret = (num > 2 and num % 2 == 0)
            elif filter_kelipatan == "Tahap 2: Coret Kelipatan 2 & 3":
                tercoret = (num > 2 and num % 2 == 0) or (num > 3 and num % 3 == 0)
            elif filter_kelipatan == "Tahap 3: Coret Kelipatan 2, 3, & 5":
                tercoret = (num > 2 and num % 2 == 0) or (num > 3 and num % 3 == 0) or (num > 5 and num % 5 == 0)
            else:
                tercoret = not cek_prima_detail(num)[0]

            if tercoret:
                html_grid += f'<div class="cell-comp">{num}</div>'
            else:
                html_grid += f'<div class="cell-prime">{num}</div>'
    html_grid += '</div>'
    st.markdown(html_grid, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================
# TAB 3: GAME TIME-ATTACK 30 DETIK + LEADERBOARD KELAS
# ==========================================================
with t_game:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("⏱️ Tantangan 30 Detik & Papan Skor Kelas")
    
    nama_pemain = st.text_input("Masukkan Nama Pemain / Kelompok:", value="Mahasiswa Untirta")
    
    if not st.session_state.game_aktif:
        if st.button("🔥 MULAI TANTANGAN 30 DETIK!", type="primary", use_container_width=True):
            st.session_state.game_aktif = True
            st.session_state.waktu_mulai = time.time()
            st.session_state.skor_time = 0
            st.session_state.soal_time = random.randint(2, 99)
            st.rerun()
    else:
        sisa_waktu = max(0, int(30 - (time.time() - st.session_state.waktu_mulai)))
        
        if sisa_waktu > 0:
            c_w, c_s = st.columns(2)
            c_w.metric("⏳ Sisa Waktu", f"{sisa_waktu} detik")
            c_s.metric("🏆 Skor Sementara", f"{st.session_state.skor_time} Poin")
            
            st.markdown(f"### Apakah **{st.session_state.soal_time}** Bilangan Prima?")
            b1, b2 = st.columns(2)
            status_soal = cek_prima_detail(st.session_state.soal_time)[0]
            
            if b1.button("✅ YA (PRIMA)", use_container_width=True):
                if status_soal:
                    st.session_state.skor_time += 10
                else:
                    st.session_state.skor_time = max(0, st.session_state.skor_time - 5)
                st.session_state.soal_time = random.randint(2, 99)
                st.rerun()
                
            if b2.button("❌ BUKAN", use_container_width=True):
                if not status_soal:
                    st.session_state.skor_time += 10
                else:
                    st.session_state.skor_time = max(0, st.session_state.skor_time - 5)
                st.session_state.soal_time = random.randint(2, 99)
                st.rerun()
        else:
            st.session_state.game_aktif = False
            st.balloons()
            st.success(f"⏰ **WAKTU HABIS!** Skor akhir **{nama_pemain}**: **{st.session_state.skor_time} Poin**")
            st.session_state.leaderboard.append({
                "Nama Pemain": nama_pemain,
                "Skor": st.session_state.skor_time,
                "Mode": "30 Detik"
            })
            st.session_state.leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x["Skor"], reverse=True)[:5]

    st.divider()
    st.write("🏅 **Top 5 Leaderboard Kelas:**")
    st.dataframe(pd.DataFrame(st.session_state.leaderboard), use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================
# TAB 4: SIMULASI KRIPTOGRAFI KUNCI PUBLIK (RSA)
# ==========================================================
with t_rsa:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🔐 Penerapan Nyata: Kunci Publik Kriptografi (RSA)")
    st.write("Tahukah kamu? Keamanan perbankan & pesan WhatsApp bergantung pada perkalian **dua bilangan prima** ($N = p \\times q$) yang sangat sulit difaktorkan kembali!")
    
    daftar_p_kecil = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    col_p, col_q = st.columns(2)
    p = col_p.selectbox("Pilih Bilangan Prima Pertama (p):", daftar_p_kecil, index=2)
    q = col_q.selectbox("Pilih Bilangan Prima Kedua (q):", daftar_p_kecil, index=4)
    
    kunci_publik = p * q
    phi_n = (p - 1) * (q - 1)
    
    st.info(f"🔑 **Kunci Publik ($N = p \\times q$):** `{p} × {q} = {kunci_publik}`")
    st.write(f"🧮 **Fungsi Totient Euler $\\phi(N) = (p-1)(q-1)$:** `{phi_n}`")
    st.caption("Komputer dengan mudah mengalikan p dan q menjadi N, tetapi memecah N kembali menjadi p dan q untuk angka ratusan digit membutuhkan waktu ribuan tahun!")
    st.markdown('</div>', unsafe_allow_html=True)
