import cv2
from datetime import datetime

def draw_greeting(frame, top, right, bottom, left, name):
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    hour = datetime.now().hour

    #  Correct conditional expression
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    cv2.putText(frame, f"{greeting}, {name}!", (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def draw_dashboard(frame, date, time, weather):
    cv2.putText(frame, date, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    cv2.putText(frame, time, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    cv2.putText(frame, weather, (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
