# 🧠 MNIST Handwritten Digit Classifier

This project implements a Convolutional Neural Network (CNN) using TensorFlow and Keras to classify handwritten digits from the MNIST dataset. It also includes a simple Streamlit web interface for interactive prediction.

---

## 📂 Project Structure

📁 MNIST-Classifier
├── app.py # Streamlit web app
├── model.h5 # Saved trained CNN model
├── mnist_model.ipynb # Jupyter notebook for training and evaluation
├── requirements.txt # Project dependencies
└── runtime.txt # Python version specification for Streamlit Cloud


---

## 📊 Model Summary

- **Dataset:** MNIST (handwritten digits)
- **Model:** Convolutional Neural Network (CNN)
- **Accuracy:** ~98% on test set

---

## 📦 Setup Instructions

1. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
Install dependencies

pip install -r requirements.txt

requirements.txt

tensorflow
streamlit
pillow

runtime.txt (for Streamlit Cloud deployment)

python-3.10

🚀 Run the App Locally
streamlit run app.py
