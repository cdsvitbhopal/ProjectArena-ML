from flask import Flask, render_template, request
import numpy as np
import pickle 
import tensorflow as tf
from PIL import Image
import io
import base64
import markdown

model = tf.keras.models.load_model('check.h5')

def preprocess_image(img):
    img = img.resize((150, 150))  # Resize the image to match the input size of your model
    img = tf.keras.preprocessing.image.img_to_array(img)  # Convert image to numpy array# Normalize the pixel values
    img = np.expand_dims(img, axis=0)  # Add an extra dimension (batch dimension)
    return img

def image_to_base64(img):
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the uploaded image from the form data
        image = request.files['image']

        img = Image.open(image.stream)
    
    # Preprocess the image
        img = preprocess_image(img)
    
        # Perform the prediction
        predictions = model.predict(img)

        # Get the predicted class label
        predicted_class = np.argmax(predictions)
        print(predicted_class)
        class_labels = ['Glioma', 'Meningioma','No tumor', 'Pituitary']  # Define your class labels
        predicted_label = class_labels[predicted_class]
        
        img_base64 = image_to_base64(Image.open(image.stream))
    
    return render_template('result.html', description=predicted_label, image_data=img_base64)



if __name__ == '__main__':
    app.run(debug=True)