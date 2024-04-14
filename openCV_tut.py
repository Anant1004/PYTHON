import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam, change to the appropriate index if you have multiple cameras

# Read the first frame
ret, frame1 = cap.read()

# Loop to continuously capture frames
while True:
    # Read the next frame
    ret, frame2 = cap.read()

    # Compute the absolute difference between the current and previous frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Apply a blur to reduce noise and improve motion detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold the image to identify regions with significant changes
    _, thresh = cv2.threshold(blurred, 20, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the detected motion
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Adjust this threshold based on your scene
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the original frame with motion rectangles
    cv2.imshow('Motion Detection', frame2)

    # Update the previous frame
    frame1 = frame2

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
