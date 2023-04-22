import tensorflow as tf
from tensorflow import keras
from keras import layers

# Creating Model
model = keras.models.Sequential()
model.add(layers.Embedding(num_unique_words, 16, input_length=max_length))
"""
The layer will take as input an integer matrix of size (batch, input_length),
and the largest integer (i.e. word index) in the input should be no larger than num_words (vocabulary size).
Now model.output_shape is (None, input_length, 16), where `None` is the batch dimension.
"""
model.add(layers.SimpleRNN(32, dropout=0.9))
model.add(layers.Dense(1, activation="sigmoid"))

# Compiling the model
loss = keras.losses.BinaryCrossentropy(from_logits=False)
optim = keras.optimizers.Adam(lr=0.001)
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optim, metrics=metrics)

# Training
history = model.fit(train_padded, train_labels, epochs=5, validation_data=(val_padded, val_labels), verbose=2)
model.save("model.h5")
