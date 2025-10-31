# sleep-detection-system-for-drivers-

A Python-based real-time **Driver Drowsiness Detection System** using **OpenCV** and **MediaPipe FaceMesh**.  
It monitors the user’s eye openness from a webcam feed and determines whether the driver’s eyes are **open** or **closed**, which can be used to alert in case of drowsiness.

---

## 🧠 Features

- Real-time face and eye detection using MediaPipe
- Calculates eye openness (EAR-like method)
- Displays live webcam feed with eye landmarks
- Highlights eyes in **green** (open) or **red** (closed)
- Works efficiently on most standard webcams

---

## 🛠️ Requirements

Install the required libraries before running:

```bash
pip install opencv-python mediapipe numpy

▶️ How to Run

Clone the repository:

git clone https://github.com/<your-username>/driver-eye-monitoring.git
cd driver-eye-monitoring


Run the Python script:

python hryhtrh.py


A window will open showing your webcam feed:

Green text / circles → Eyes are open

Red text / circles → Eyes are closed

Press ESC to quit the program.

⚙️ How It Works

The program uses MediaPipe’s FaceMesh model to detect 468 facial landmarks.

Eye landmarks (specific index points) are extracted for both eyes.

The vertical and horizontal distances between key eye landmarks are used to estimate the Eye Aspect Ratio (EAR).

If the average eye openness falls below a threshold (0.2 by default), it is considered closed.

📸 Example Output
Status	Visualization
Eyes Open	🟢 Green outline and “EYES OPEN” text
Eyes Closed	🔴 Red outline and “EYES CLOSED” text
🚀 Future Improvements

Add an audio alert for prolonged eye closure

Integrate with Raspberry Pi or IoT systems

Use Blink frequency or PERCLOS (Percentage of Eye Closure) for advanced fatigue detection

Log drowsiness data for analytics

🧩 Tech Stack

Language: Python

Libraries: OpenCV, MediaPipe, NumPy

Model: FaceMesh from Google MediaPipe

👨‍💻 Author

Vishanth R
B.Tech CSE, SRM University – Kattankulathur
Passionate about AI, Computer Vision, and Automation.

🪪 License

This project is open-source and available under the MIT License
.
