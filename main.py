import cv2
import mediapipe as mp
import pyautogui  
import time       


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


waktu_jeda = 1.5  
waktu_terakhir_aksi = 0


cap = cv2.VideoCapture(0)
print("Sistem Auto Slide Aktif! Buka PowerPoint Anda. Tekan 'q' di layar kamera untuk keluar.")

while True:
    success, img = cap.read()
    if not success:
        break
        
    img = cv2.flip(img, 1) 
    tinggi_layar, lebar_layar, _ = img.shape 

    
    cv2.line(img, (int(lebar_layar * 0.3), 0), (int(lebar_layar * 0.3), tinggi_layar), (255, 0, 0), 2) # Garis Kiri Biru
    cv2.line(img, (int(lebar_layar * 0.7), 0), (int(lebar_layar * 0.7), tinggi_layar), (0, 255, 0), 2) # Garis Kanan Hijau
    
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
        
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
            x_telunjuk = hand_landmarks.landmark[8].x 
            
            
            waktu_sekarang = time.time()
            
            
            if (waktu_sekarang - waktu_terakhir_aksi) > waktu_jeda:
                
                
                if x_telunjuk > 0.7:
                    pyautogui.press('right') 
                    waktu_terakhir_aksi = waktu_sekarang 
                    cv2.putText(img, "NEXT ->", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    print("Geser Kanan (Next)")

                
                elif x_telunjuk < 0.3:
                    pyautogui.press('left') 
                    waktu_terakhir_aksi = waktu_sekarang 
                    cv2.putText(img, "<- PREV", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                    print("Geser Kiri (Prev)")

    
    cv2.imshow("Auto Slide Presentasi", img)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
