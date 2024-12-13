from ultralytics import YOLO

# Load the model
model = YOLO("runs/detect/train4/weights/best.pt")

# Predict on the image
results = model.predict(source="BSPCoin-10-1.jpg", conf=0.3)

# For each result (in case of multiple images)
for result in results:
    # Print bounding boxes
    print("Bounding Boxes:")
    boxes = result.boxes
    for box in boxes:
        # Get class and confidence
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        
        # Get bounding box coordinates
        xyxy = box.xyxy[0]
        x1, y1, x2, y2 = xyxy
        
        # Print detailed information
        print(f"Class: {model.names[cls]}")
        print(f"Confidence: {conf:.2f}")
        print(f"Bounding Box (x1,y1,x2,y2): {x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f}")
    
    # Optionally, you can also save the annotated image
    result.save(filename="prediction_result.jpg")
print("Total number of images processed:", len(results))

# Method 2: Number of detected objects
print("Number of detected objects:", len(results[0].boxes))

# Alternative method
result = results[0]  # Assuming single image
num_detections = len(result.boxes)
print("Number of detections:", num_detections)