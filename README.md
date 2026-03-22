# 🪄 Auto Slide Presentasi dengan AI (Hand Gesture Control)

Aplikasi Kecerdasan Buatan (AI) sederhana yang memungkinkan Anda mengontrol perpindahan slide presentasi (PowerPoint, Google Slides, dll) hanya dengan menggunakan **gerakan tangan (gestur)** di depan webcam. Tinggalkan *clicker* atau *mouse* Anda, dan presentasilah layaknya seorang penyihir! ✨

## 🚀 Fitur Utama
* **Deteksi Tangan Real-time:** Menggunakan teknologi Google MediaPipe untuk melacak pergerakan jari secara instan.
* **Kontrol Geser Kanan (Next):** Gerakkan jari telunjuk ke arah kanan layar untuk berpindah ke slide selanjutnya.
* **Kontrol Geser Kiri (Previous):** Gerakkan jari telunjuk ke arah kiri layar untuk kembali ke slide sebelumnya.
* **Sistem Cooldown Anti-Spam:** Dilengkapi jeda waktu otomatis (1,5 detik) agar slide tidak melompat berkali-kali dalam satu gerakan.
* **Kompatibel Universal:** Karena meniru ketukan *keyboard* fisik, aplikasi ini bekerja di **semua software presentasi** (PowerPoint, Keynote, Canva, Google Slides, hingga PDF Viewer).

## 🛠️ Teknologi yang Digunakan (Tech Stack)
* **Python 3.11** (Bahasa Pemrograman)
* **OpenCV** (Untuk akses Webcam dan pemrosesan video)
* **MediaPipe** (Otak AI untuk pelacakan *landmark* tangan)
* **PyAutoGUI** (Untuk simulasi penekanan tombol *keyboard*)

---

## 💻 Cara Instalasi (Untuk Developer)

Jika Anda ingin menjalankan atau memodifikasi *source code* proyek ini di komputer Anda, ikuti langkah-langkah berikut:

### 1. Persiapan Kelengkapan
Pastikan Anda sudah menginstal [Python 3.11](https://www.python.org/downloads/) di komputer Anda.

### 2. Download Proyek
*Clone* repository ini atau download sebagai ZIP, lalu ekstrak ke dalam sebuah folder:
```bash
git clone [https://github.com/USERNAME_GITHUB_ANDA/NAMA_REPOSITORY_ANDA.git](https://github.com/USERNAME_GITHUB_ANDA/NAMA_REPOSITORY_ANDA.git)
