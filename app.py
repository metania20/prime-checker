import streamlit as st

# Konfigurasi halaman web
st.set_page_config(page_title="Prime Number Checker", page_icon="🔢", layout="centered")

# CSS kustom untuk tema ungu pastel
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F5FC;
    }
    h1 {
        color: #5E35B1;
    }
    div.stButton > button:first-child {
        background-color: #9575CD;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #7E57C2;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

def cek_bilangan_prima(n):
    """Fungsi untuk mengecek bilangan prima dan mencari faktor pembaginya."""
    if n <= 1:
        return False, []
    
    faktor = []
    for i in range(1, n + 1):
        if n % i == 0:
            faktor.append(i)
            
    # Bilangan prima hanya memiliki tepat 2 faktor: 1 dan bilangan itu sendiri
    is_prime = (len(faktor) == 2)
    return is_prime, faktor

# Bagian Judul dan Deskripsi Web
st.title("🔢 Prime Number Checker")
st.write("Aplikasi pengecekan bilangan prima berbasis web menggunakan Python.")
st.divider()

# 1. Input bilangan dari pengguna
angka = st.number_input(
    "Masukkan bilangan bulat positif:",
    min_value=0,
    value=7,
    step=1
)

# 2. Tombol pengecekan & 3. Penentuan hasil
if st.button("Cek Bilangan Prima", use_container_width=True):
    bilangan = int(angka)
    is_prime, daftar_faktor = cek_bilangan_prima(bilangan)
    
    if is_prime:
        st.success(f"✅ Angka **{bilangan}** adalah **BILANGAN PRIMA**.")
        st.info(f"**Alasan:** Hanya memiliki 2 faktor pembagi, yaitu **{daftar_faktor[0]}** dan **{daftar_faktor[1]}**.")
    else:
        st.error(f"❌ Angka **{bilangan}** **BUKAN** bilangan prima.")
        if bilangan <= 1:
            st.info("**Alasan:** Bilangan prima harus merupakan bilangan asli yang lebih besar dari 1.")
        else:
            st.info(f"**Alasan:** Memiliki {len(daftar_faktor)} faktor pembagi, yaitu: {daftar_faktor}")