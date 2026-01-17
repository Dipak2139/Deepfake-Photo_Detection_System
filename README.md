# 🧠 Deepfake Photo Detection System

A deep learning–based web application that detects whether an uploaded face image is **REAL** or **FAKE (Deepfake)** using a Convolutional Neural Network (CNN) and a Flask web interface.

This project is developed as both:
- 🎓 **MCA Final Year Project**
- 💻 **Personal AI / ML Portfolio Project**

---

## 🚀 Features

- 📷 Upload an image and detect if it is REAL or FAKE
- 🤖 Deep learning model trained using **MobileNetV2 (Transfer Learning)**
- 📊 Displays **confidence percentage**
- 🎨 Color-coded results:
  - 🟢 Green → REAL image
  - 🔴 Red → FAKE image
- 🖼️ Uploaded image shown with the result
- 🗑️ **Delete Image button** to remove uploaded images (privacy-friendly)
- ⚡ Loading animation for better user experience
- 🌐 Flask-based web application
- 🔐 No permanent image storage

---

## 🧪 How Deepfake Detection Works

1. User uploads a face image
2. Image is preprocessed (resized to 224×224, normalized)
3. Image is passed to a trained CNN model
4. Model outputs a probability score
5. Based on a threshold (0.55), image is classified as:
   - **REAL**
   - **FAKE**
6. Result and confidence score are displayed on the UI

---

## 🏗️ Tech Stack

### 🔹 Backend
- Python
- Flask
- TensorFlow / Keras

### 🔹 Deep Learning
- MobileNetV2 (Transfer Learning)
- CNN (Binary Classification)

### 🔹 Frontend
- HTML
- CSS
- JavaScript

### 🔹 Tools
- OpenCV
- Git & GitHub


