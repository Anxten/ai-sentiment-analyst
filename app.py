# app.py (Versi Final yang Benar untuk Proyek Analis Sentimen)

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Impor fungsi scraper yang sudah kita buat
from scraper import scrape_kompas_article

# Memuat kunci dari .env
load_dotenv()

# --- LANGKAH 1: SIAPKAN DAFTAR TARGET URL ---
list_url_target = [
    'https://nasional.kompas.com/read/2024/05/23/10135061/prabowo-koreksi-istilah-makan-siang-gratis-yang-tepat-makan-bergizi-gratis',
    'https://nasional.kompas.com/read/2024/07/18/05185291/utak-atik-janji-makan-siang-gratis-prabowo-anggaran-dipertimbangkan-turun-ke?page=all',
    'https://nasional.kompas.com/read/2025/01/04/07305791/prabowo-minta-bahan-baku-makan-bergizi-gratis-murni-dari-dalam-negeri'
]

# --- LANGKAH 2: SETUP LLM ---
print("--- [SETUP] Mempersiapkan 'Mesin' AI Groq... ---")
# Inisialisasi LLM dengan menyertakan API Key secara eksplisit
llm = ChatGroq(
    model_name="llama3-8b-8192", 
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# --- LANGKAH 3: PROSES SETIAP ARTIKEL DALAM LOOP ---
print("--- [PROSES DIMULAI] Menganalisis beberapa artikel berita... ---")
semua_hasil_analisis = [] 

prompt_individu = ChatPromptTemplate.from_template(
    "Anda adalah seorang analis politik yang objektif. Berdasarkan judul dan isi artikel berita berikut, tentukan sentimennya (Positif, Negatif, Netral) dan sebutkan 1-2 poin utamanya.\n\n"
    "JUDUL: {judul}\nISI:\n{isi_artikel}\n\n"
    "HASIL ANALISIS SINGKAT DALAM BAHASA INDONESIA:"
)
rantai_analisis_individu = prompt_individu | llm | StrOutputParser()

for url in list_url_target:
    try:
        print(f"\nMemanen data dari: {url}...")
        judul, isi_artikel = scrape_kompas_article(url)
        print(f"-> Judul '{judul}' berhasil dipanen.")
        
        print("--> Mengirim ke AI untuk analisis individu...")
        hasil_analisis = rantai_analisis_individu.invoke({
            "judul": judul,
            "isi_artikel": isi_artikel
        })
        semua_hasil_analisis.append(hasil_analisis)
        print("--> Analisis individu selesai.")
    except Exception as e:
        print(f"--> Gagal memproses URL: {url}. Error: {e}")

# --- LANGKAH 4: BUAT SINTESIS AKHIR ---
print("\n\n--- [LANGKAH FINAL] Membuat rangkuman dari semua analisis... ---")
laporan_gabungan = "\n\n".join(semua_hasil_analisis)

prompt_sintesis = ChatPromptTemplate.from_template(
    "Anda adalah seorang kepala analis riset. Anda telah menerima beberapa laporan analisis dari tim Anda.\n\n"
    "Berikut adalah kumpulan laporan tersebut:\n{kumpulan_laporan}\n\n"
    "Tugas Anda: Berdasarkan semua laporan di atas, buatlah sebuah kesimpulan akhir dalam 2-3 paragraf. "
    "Rangkum sentimen umum dari media terhadap topik ini dan apa saja tema-tema yang paling sering muncul secara keseluruhan. "
    "PASTIKAN SELURUH JAWABAN ANDA DISAJIKAN DALAM BAHASA INDONESIA."
)
rantai_sintesis = prompt_sintesis | llm | StrOutputParser()

kesimpulan_akhir = rantai_sintesis.invoke({"kumpulan_laporan": laporan_gabungan})

print("\n\n==================== KESIMPULAN AKHIR ====================")
print(kesimpulan_akhir)
print("==========================================================")
print("\nProses Analisis Massal Selesai dengan Sukses!")