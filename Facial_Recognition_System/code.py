# Facial Detection using Python


import cv2  # Import OpenCV library

# Load the cascade classifier for face detection
face_cap = cv2.CascadeClassifier("C:/Users/Yash/Downloads/haarcascade_frontalface_default.xml")  # Ensure correct path

# Verify that the cascade file was loaded successfully
if face_cap.empty():
    print("Error: Cascade file not loaded. Check file path.")
    exit()

# Initialize video capture
video_cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, video_data = video_cap.read()
    if not ret:
        print("Failed to grab video frame")
        break
    
    # Convert the frame to grayscale (for face detection)
    gray_frame = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cap.detectMultiScale(
        gray_frame,         # Input grayscale frame
        scaleFactor=1.1,    # Parameter to scale the image
        minNeighbors=7,     # Increase neighbors to reduce false positives
        minSize=(30, 30),   # Minimum face size
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        # You can filter overlapping faces here if needed
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the live video feed
    cv2.imshow("Live Video - Press 'a' to Exit", video_data)
    
    # Break the loop when 'a' key is pressed
    if cv2.waitKey(10) == ord("a"):
        break

# Release resources and close all OpenCV windows
video_cap.release()
# cv2.destroyAllWindows()