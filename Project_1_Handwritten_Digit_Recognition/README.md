### Handwritten-Digit-Recognition

This guide explains how to create a Handwritten Digit Recognition application using a Convolutional Neural Network (CNN) model and a graphical user interface (GUI) built with the Tkinter library. The application allows users to draw digits on a canvas and predicts the drawn digits in real-time.

## Prerequisites
  - Basic understanding of Python programming
  -	Familiarity with deep learning concepts and the Keras library
  -	Basic knowledge of GUI development with Tkinter
  -	Python 3.x installed on your machine]

## **•	Installation**

  1.	Clone or download the repository to your local machine.
  2.	Install the necessary Python libraries using the following command:
     
    pip install numpy tensorflow keras pillow opencv-python-headless
  
  4.	Run the gui_digit_recognizer.py script:
     
    python gui_digit_recognizer.py
  
  6.	The GUI window will appear, allowing you to draw digits on the canvas using your mouse.
  7.	After drawing a digit, click the "Recognise" button to predict the drawn digit.
  8.	The predicted digit and the associated confidence level will be displayed on the GUI.
  9.	To clear the canvas and draw a new digit, click the "Clear" button.

## Workflow

  **1.	Import Libraries and Load the Dataset:**
  - Import the necessary modules, including Keras, for training the model.
  -	Load the MNIST dataset, which provides training and testing data along with labels.
  
  **2.	Data Preprocessing:**
  
  - Reshape and preprocess the training and testing image data for CNN input.
  - Normalize pixel values to a range between 0 and 1.
  - Convert class labels to binary class matrices using one-hot encoding.
  
 **3.	Create the CNN Model:**
   - Build a CNN model architecture using Keras' Sequential API.
   - Add convolutional, pooling, and dropout layers for feature extraction and regularization.
   - Compile the model using a suitable loss function, optimizer, and evaluation metric.
  
  **4.	Model Training:**
  
  - Train the model using the training data and specified parameters.
  - Save the trained model's weights and definition to a file for later use.
  
  **5.	Model Evaluation:**
  
  - Evaluate the model's performance on the testing data to assess accuracy.
  
  **6.	Build GUI for Digit Recognition:**
  
  - Create a GUI using Tkinter, a Python standard library for creating graphical interfaces.
  - Implement canvas drawing capabilities and buttons for recognition and clearing.
  
  **7.	Digit Recognition with GUI:**
  - Load the trained model for digit recognition.
  - Capture drawn digits from the GUI canvas.
  - Preprocess the captured image and predict the digit using the model.
  - Display the predicted digit and confidence level on the GUI.

## Customization
  - Customize the GUI appearance, layout, and interaction logic by modifying the App class within the gui_digit_recognizer.py script.
  - To use your own trained model, update 'mnist.h5' with the path to your trained model file in the predict_digit function.

