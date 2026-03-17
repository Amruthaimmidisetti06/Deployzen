import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import load_img
from google.colab import files
import matplotlib.pyplot as plt

# Load pretrained VGG16 (without top layer)
base = VGG16(weights='imagenet', include_top=False, input_shape=(224,224,3))

# Freeze layers
for l in base.layers:
    l.trainable = False

# Add custom layers
x = Flatten()(base.output)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
out = Dense(3, activation='softmax')(x)

# Final model
model = Model(base.input, out)

# Compile
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary (same as your output)
model.summary()

# Upload image
files.upload()

# Show image
img = load_img('dog1.jpg', target_size=(224,224))
plt.imshow(img)
plt.axis('off')
plt.show()
