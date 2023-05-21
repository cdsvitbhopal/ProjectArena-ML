# heartclassification
Implemented a Heart Audio Classifier using Methods of CNN and RNN in Deep Learning

### Dataset used:
For the Heart Sound Challenge, the most ideal dataset to use was the PhysioNet/PASCAL database because the dataset's audio file has been taken via both clinical methods (i.e. a Digital Stethoscope) and also general methods (i.e. an iPhone Stethoscope app). <br>
Note: The Repo does not contain the audio files for Heart Sounds, this repo only showcases the code for the algorithms used.
<br>
### Main code is shown in Classification.ipynb
## CNN Approach
In the CNN approach, a spectrogram was made using a Short Term Fourier Transform of all the Audio Files using the tf.signal module. All the spectrograms were then all spaced out to a consistent length for the CNNs input size.
<br>
![Screenshot_20230215_134958](https://user-images.githubusercontent.com/63441604/231683532-c4281921-72a0-4385-9ca8-2f62bf06a15c.png)

The Convolutional Neural Network was used for a multiclass Image Classification using the tensorflow keras library. It has 2 Conv2D layers which gets flattened into a Fully Connected Layer which classifies audio data.

![download (1)](https://user-images.githubusercontent.com/63441604/231684155-610d9d91-fd79-4dfc-8f7e-c65ed4ee46ab.png)

## RNN Approach
For The RNN Approach, we first built a dataloading function loading audio file and extracting the features using Mel Frequency Cepstrum Coefficients (MFCCs)

![download (6)](https://user-images.githubusercontent.com/63441604/231684568-7a6d3df8-a82b-4a96-afbc-91402e25fefa.jpeg)

We then built a Bidirectional LSTM Model with the extracted Features. Bidirectional LSTM (BiLSTM) is a recurrent neural network. Unlike standard LSTM, the input flows in both directions, and it’s capable of utilizing information from both sides. It’s also a powerful tool for modeling the sequential dependencies between audio signals in both directions of the sequence.

![lstm](https://user-images.githubusercontent.com/63441604/231684861-fcebb24d-d8db-4489-8a99-743c3d3fe6e5.png)

## Test-set accuracies
The outcome after running both the models: -

CNN Model - It achieved an Accuracy of 80%.
RNN Model - It achieved an Accuracy of 75%
