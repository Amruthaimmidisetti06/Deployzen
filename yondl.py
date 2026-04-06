import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import boston_housing
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

mean, std = x_train.mean(axis=0), x_train.std(axis=0)
x_train = (x_train - mean) / std
x_test = (x_test - mean) / std

model = keras.Sequential([
    keras.Input(shape=(x_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

history = model.fit(x_train, y_train, epochs=100, batch_size=16,
                    validation_split=0.2, verbose=1)

loss, mae = model.evaluate(x_test, y_test)
print("\nTest MAE:", mae)

pred = model.predict(x_test)
print("\nFirst 5 predictions:\n", pred[:5])
print("\nActual values:\n", y_test[:5])

plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Validation')
plt.legend()
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()
