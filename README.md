# 🤖 AI Penganalisis Sentimen & Topik Kebijakan Publik

Sebuah aplikasi Python yang secara otomatis memanen data dari berbagai artikel berita online untuk menganalisis sentimen media dan topik perdebatan utama mengenai sebuah kebijakan publik.

---

## 🏛️ Studi Kasus

Di tengah dinamika politik yang cepat, lembaga pemerintah, firma humas, dan korporasi perlu memahami reaksi publik terhadap sebuah kebijakan baru secara akurat dan efisien. Proyek ini lahir untuk mengotomatiskan proses tersebut, mengubah ratusan artikel berita menjadi sebuah laporan analisis yang ringkas dan padat.

Studi kasus yang digunakan adalah analisis pemberitaan media mengenai program "Makan Bergizi Gratis".

---

## ⚙️ Arsitektur Solusi

Aplikasi ini menggunakan pendekatan "Orkestrasi Manual" yang andal untuk memastikan alur kerja yang logis dan hasil yang berkualitas.

1.  **Pengumpulan Data (Web Scraping):** Skrip menggunakan **Selenium** untuk membuka browser secara otomatis, mengunjungi daftar URL berita, dan mengekstrak judul serta isi artikel. Metode ini terbukti andal dalam melewati pertahanan anti-scraping sederhana.
2.  **Analisis per Artikel:** Setiap artikel yang berhasil dipanen kemudian dianalisis satu per satu oleh sebuah *chain* **LangChain**. Menggunakan "otak" dari model **Llama 3 via Groq API**, AI menentukan sentimen (Positif, Negatif, Netral) dan mengekstrak poin-poin utama dari setiap berita.
3.  **Sintesis & Rangkuman Akhir:** Semua hasil analisis individu dikumpulkan dan diserahkan ke *chain* LangChain final. AI kemudian bertindak sebagai "Kepala Analis" yang membuat sebuah kesimpulan gabungan, merangkum sentimen umum dan tema-tema yang paling sering muncul dari semua sumber.

---

## 💻 Tumpukan Teknologi (Tech Stack)

* **Python**
* **LangChain**: Framework utama untuk orkestrasi dan interaksi dengan LLM.
* **Groq API (Llama 3 8B)**: Sebagai "otak" atau LLM yang melakukan analisis.
* **Selenium**: Untuk web scraping tingkat lanjut yang mampu mengotomatisasi browser asli.
* **BeautifulSoup4**: Untuk mem-parsing dan membersihkan data HTML.
* **Pandas**: (Digunakan dalam salah satu versi pengembangan) untuk analisis data terstruktur.

---

## 🚀 Instalasi & Setup

1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/Anxten/ai-sentiment-analyst.git](https://github.com/Anxten/ai-sentiment-analyst.git)
    cd ai-sentiment-analyst
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install semua library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Buat file `.env` dan masukkan kunci API Groq Anda:**
    ```
    GROQ_API_KEY='gsk_xxxxxxxxxxxxxxxxxx'
    ```

---

## ▶️ Cara Penggunaan

Cukup jalankan file aplikasi utama dari terminal. Skrip akan secara otomatis memproses daftar URL yang ada di dalamnya.

```bash
python app.py