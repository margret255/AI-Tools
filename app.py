import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Load the saved model
model = tf.keras.models.load_model("mnist_model.h5")

st.title("MNIST Digit Classifier 🧠")
st.write("Upload a 28x28 handwritten digit image (black & white), and we'll predict the digit!")

uploaded_file = st.file_uploader("Choose a digit image...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    image = ImageOps.invert(image)  # Invert for white digit on black background
    image = image.resize((28, 28))  # Resize to 28x28
    img_array = np.array(image).astype("float32") / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    st.image(image, caption="Uploaded Image", width=150)
    st.markdown(f"### Predicted Digit: {predicted_class}")
    st.markdown(f"Confidence: {confidence * 100:.2f}%")
