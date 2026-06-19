# 🌿 Plant Disease Detection using Deep Learning

A full-stack AI-powered web application that detects plant diseases from leaf images using Deep Learning. The project leverages a custom CNN architecture, transfer learning with pretrained models, and hyperparameter optimization using Optuna to achieve high classification accuracy.

---

# 🚀 Live Demo

https://plant-frontend-latest.onrender.com/

### Frontend

https://plant-frontend-latest.onrender.com/

### Backend API

https://plant-backend-production-f0be.up.railway.app

### API Documentation

https://plant-backend-production-f0be.up.railway.app/docs

---

# 📖 Project Overview

Plant diseases can significantly impact crop yield and agricultural productivity. This project provides an automated disease detection system that allows users to upload a plant leaf image and instantly receive a disease prediction.

The application consists of:

* Streamlit Frontend for user interaction
* FastAPI Backend for model inference
* PyTorch Deep Learning Model
* Dockerized deployment
* Railway cloud hosting

---

# 🧠 Deep Learning Approach

This project explores and compares multiple deep learning architectures for plant disease classification using the PlantVillage dataset.

## Dataset

PlantVillage Dataset

### Classes (15)

* Pepper__bell___Bacterial_spot
* Pepper__bell___healthy
* Potato___Early_blight
* Potato___Late_blight
* Potato___healthy
* Tomato_Bacterial_spot
* Tomato_Early_blight
* Tomato_Late_blight
* Tomato_Leaf_Mold
* Tomato_Septoria_leaf_spot
* Tomato_Spider_mites_Two_spotted_spider_mite
* Tomato__Target_Spot
* Tomato__Tomato_YellowLeaf__Curl_Virus
* Tomato__Tomato_mosaic_virus
* Tomato_healthy

---

## Models Evaluated

### 1. Custom CNN

A Convolutional Neural Network was built from scratch using:

* Convolutional Layers
* Batch Normalization
* ReLU Activation
* Dropout Regularization
* Adaptive Average Pooling
* Fully Connected Classification Head

The custom model served as a strong baseline and achieved excellent performance.

---

### 2. Transfer Learning

To improve performance further, pretrained ImageNet models were evaluated.

#### VGG16

* ImageNet pretrained weights
* Fine-tuning selected layers
* Custom classifier head

#### ResNet18

* ImageNet pretrained weights
* Transfer learning approach
* Fully connected layer replaced for 15-class classification

---

## Hyperparameter Optimization

Hyperparameter tuning was performed using **Optuna**.

Parameters optimized:

* Learning Rate
* Batch Size
* Number of Hidden Layers
* Neurons per Layer
* Dropout Rate
* Weight Decay
* Optimizer Selection
* Number of Unfrozen Layers

This automated search process helped identify the best-performing model configuration.

---

## Final Performance

| Metric              | Score  |
| ------------------- | ------ |
| Training Accuracy   | 98.00% |
| Validation Accuracy | 97.77% |
| Test Accuracy       | 97.72% |

---

# 🛠️ Tech Stack

## Frontend

* Streamlit

## Backend

* FastAPI
* Uvicorn

## Deep Learning

* PyTorch
* Torchvision
* Optuna
* NumPy
* Pandas
* Matplotlib

## Deployment

* Docker
* Docker Hub
* Railway

---

# 🐳 Docker Images

## Backend Image

```
ankitroy01/plant-backend:latest
```

## Frontend Image

```
ankitroy01/plant-frontend:latest
```

---

# 📂 Project Structure

```
Plant-Disease-Detection-CNN
│
├── backend
│   ├── main.py
│   ├── predict.py
│   ├── model.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── notebooks
│   └── Plant_Disease_Training.ipynb
│
├── docker-compose.yml
├── README.md
└── .dockerignore
```

---

# ⚙️ Local Installation

## Clone Repository

```bash
git clone https://github.com/Ankit0974/Plant-Disease-Detection-CNN-.git
cd Plant-Disease-Detection-CNN-
```

---

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

Frontend runs at:

```
http://localhost:8501
```

---

# 🐳 Docker Setup

## Backend

```bash
docker build -t ankitroy01/plant-backend .
docker run -p 8001:8000 ankitroy01/plant-backend
```

## Frontend

```bash
docker build -t ankitroy01/plant-frontend .
docker run -p 8502:8501 ankitroy01/plant-frontend
```

---

## Docker Compose

```bash
docker compose up
```

---

# 🔗 API Endpoint

Prediction Endpoint

```
POST /predict
```

Send an image file and receive the predicted disease class.

---

# 👨‍💻 Author

### Ankit Roy

B.Tech CSE (AI & DS)

GitHub:
https://github.com/Ankit0974

---

# ⭐ Future Improvements

* Disease treatment recommendations
* Confidence score visualization
* Mobile responsive UI
* Additional crop support
* Model explainability using Grad-CAM
* Multi-language support

---

If you found this project useful, consider giving it a ⭐ on GitHub.
