import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load data
num_words = 20000
(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=num_words)

# Pad sequences
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=256)
x_test = keras.preprocessing.sequence.pad_sequences(x_test, maxlen=256)

# Build model
model = keras.Sequential([
    keras.layers.Embedding(num_words, 2, input_length=256),
    keras.layers.Flatten(),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(5),
    keras.layers.Dense(1, activation='sigmoid')
])

# Summary
model.summary()

# Compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
history = model.fit(x_train, y_train, epochs=5, batch_size=100,
                    validation_data=(x_test, y_test), verbose=1)

# Plot accuracy
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.title("Accuracy")
plt.xlabel("Epoch")
plt.legend()
plt.show()
