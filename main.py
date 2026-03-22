import cv2
import mediapipe as mp
import pyautogui  # Tangan robot penekan keyboard
import time       # Pengatur waktu (cooldown)

# 1. Persiapan AI
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# 2. Pengaturan Jeda (Cooldown) agar slide tidak melompat berkali-kali
waktu_jeda = 1.5  # Jeda 1.5 detik setelah ganti slide
waktu_terakhir_aksi = 0

# Menyalakan Kamera
cap = cv2.VideoCapture(0)
print("Sistem Auto Slide Aktif! Buka PowerPoint Anda. Tekan 'q' di layar kamera untuk keluar.")

while True:
    success, img = cap.read()
    if not success:
        break
        
    img = cv2.flip(img, 1) # Efek cermin
    tinggi_layar, lebar_layar, _ = img.shape # Mengambil ukuran layar kamera

    # Menggambar garis batas Zona Kiri, Tengah, dan Kanan di layar
    cv2.line(img, (int(lebar_layar * 0.3), 0), (int(lebar_layar * 0.3), tinggi_layar), (255, 0, 0), 2) # Garis Kiri Biru
    cv2.line(img, (int(lebar_layar * 0.7), 0), (int(lebar_layar * 0.7), tinggi_layar), (0, 255, 0), 2) # Garis Kanan Hijau
    
    # Terjemahkan warna dan proses dengan AI
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Menggambar kerangka tangan
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # 3. MENGAMBIL KOORDINAT JARI TELUNJUK (Titik ke-8)
            # MediaPipe memberikan nilai x dari 0.0 (paling kiri) sampai 1.0 (paling kanan)
            x_telunjuk = hand_landmarks.landmark[8].x 
            
            # 4. LOGIKA PENGGESER SLIDE & COOLDOWN
            waktu_sekarang = time.time()
            
            # Cek apakah waktu jeda sudah berlalu
            if (waktu_sekarang - waktu_terakhir_aksi) > waktu_jeda:
                
                # Jika telunjuk melewati garis hijau (Zona Kanan) -> NEXT SLIDE
                if x_telunjuk > 0.7:
                    pyautogui.press('right') # Pencet panah kanan
                    waktu_terakhir_aksi = waktu_sekarang # Reset timer
                    cv2.putText(img, "NEXT ->", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    print("Geser Kanan (Next)")

                # Jika telunjuk melewati garis biru (Zona Kiri) -> PREV SLIDE
                elif x_telunjuk < 0.3:
                    pyautogui.press('left') # Pencet panah kiri
                    waktu_terakhir_aksi = waktu_sekarang # Reset timer
                    cv2.putText(img, "<- PREV", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                    print("Geser Kiri (Prev)")

    # Tampilkan layar video
    cv2.imshow("Auto Slide Presentasi", img)

    # Tombol keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()