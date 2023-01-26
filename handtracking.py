import cv2
import mediapipe as mp

# Initialize the MediaPipe Hands module
mpHands = mp.solutions.hands
Hands = mpHands.Hands()

# Initialize the MediaPipe drawing utilities
mpDraw = mp.solutions.drawing_utils

# Open the default camera for video capture
cap = cv2.VideoCapture(0)

# Check if camera is opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")
    exit()

while True:
    # Read a frame from the video stream
    success, img = cap.read()

    # Check if a frame was read successfully
    if not success:
        print("Error reading video stream")
        break

    # Convert the frame from BGR to RGB color space
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect hands in the image
    results = Hands.process(converted_image)

    # Check if any hands were detected
    if results.multi_hand_landmarks:
        for hand_in_frame in results.multi_hand_landmarks:
            # Draw the hand landmarks on the image
            mpDraw.draw_landmarks(img, hand_in_frame, mpHands.HAND_CONNECTIONS)

    # Display the image with the hand landmarks
    cv2.imshow(" Hand Tracking ", img)

    # Wait for a key press before proceeding to the next frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
