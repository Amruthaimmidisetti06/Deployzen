import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Train:", dict(zip(*np.unique(y_train, return_counts=True))))
print("\nTest:", dict(zip(*np.unique(y_test, return_counts=True))))

idx = np.random.randint(0, len(x_train), 25)

plt.figure(figsize=(5,5))
for i, j in enumerate(idx):
    plt.subplot(5,5,i+1)
    plt.imshow(x_train[j], cmap='gray')
    plt.axis('off')

plt.show()
