# Tracking Auto Slide Hands Presentasi

Aplikasi inovatif berbasis Kecerdasan Buatan (AI) yang memungkinkan mengontrol slide presentasi hanya dengan menggunakan gerakan tangan (gestur) di depan webcam. Tinggalkan *mouse* atau *clicker* 

Proyek ini dibangun menggunakan **Python** dengan memanfaatkan teknologi *Computer Vision* terkini.

## Fitur Utama
* **Deteksi Tangan Real-Time:** Menggunakan Google MediaPipe untuk melacak titik sendi jari secara instan dan akurat.
* **Kontrol "Next" (Geser Kanan):** Gerakkan telunjuk menyeberangi area kanan layar untuk berpindah ke slide selanjutnya.
* **Kontrol "Previous" (Geser Kiri):** Gerakkan telunjuk menyeberangi area kiri layar untuk kembali ke slide sebelumnya.
* **Anti-Spam (Cooldown System):** Terdapat jeda cerdas (1 detik) setelah setiap gerakan agar slide tidak bergeser berkali-kali secara tidak sengaja.
* **Kompatibilitas Universal:** Karena program ini menyimulasikan tombol *keyboard* (Panah Kiri/Kanan), aplikasi ini bisa digunakan untuk software apapun: PowerPoint, Google Slides, Keynote, Canva, PDF, hingga Galeri Foto.

## Teknologi yang Digunakan
* **[Python 3.11](https://www.python.org/)** - Bahasa Pemrograman utama.
* **[OpenCV](https://opencv.org/)** - Untuk mengakses webcam dan memproses *frame* video.
* **[MediaPipe](https://developers.google.com/mediapipe)** - Model AI (Machine Learning) yang mendeteksi dan melacak *landmark* tangan.
* **[PyAutoGUI](https://pyautogui.readthedocs.io/)** - Untuk melakukan otomatisasi penekanan tombol *keyboard*.
