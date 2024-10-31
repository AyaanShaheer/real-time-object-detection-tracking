import cv2
import torch

# Load YOLOv5 model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).to(device)

# Open webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize frame to match YOLOv5 input size
    frame_resized = cv2.resize(frame, (640, 640))  # YOLOv5 default size is 640x640

    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

    # Perform detection
    results = model(frame_rgb)  # Forward pass through the model

    # Get detections
    detections = results.pred[0]  # Get the predictions for the first image in the batch

    # Process detections
    for *box, conf, cls in detections.tolist():  # Convert tensor to list
        x1, y1, x2, y2 = map(int, box)  # Convert bounding box coordinates to integers
        label = f"{model.names[int(cls)]} {conf:.2f}"  # Format label with confidence
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Draw bounding box
        cv2.putText(frame, label, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)  # Draw label

    # Show the frame with detections
    cv2.imshow('YOLOv5 Detection', frame)

    # Exit on pressing 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        print("Exiting...")
        break

# Clean up
cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
