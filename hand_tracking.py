import cv2
import mediapipe as mp 


mp_hands = mp.solutions.hands

mp_drawing = mp.solutions.drawing_utils 


webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    success, img = webcam.read()
    
    # Hand tracking model
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = mp_hands.Hands(max_num_hands =2, min_detection_confidence = 0.7, min_tracking_confidence = 0.6).process(img)
    
    # Draw annotations on the image
    
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, connections = mp_hands.HAND_CONNECTIONS)  
              
    
    cv2.imshow('Antoine',img)
    if cv2.waitKey(6) & 0xFF == ord("q"):
        break
    
webcam.release()
cv2.destroyAllWindows()