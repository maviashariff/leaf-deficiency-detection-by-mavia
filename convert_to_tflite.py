import tensorflow as tf

# Load existing model
model = tf.keras.models.load_model("leaf_nutrient_model.h5")

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Optional: Optimize (recommended)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

# Save model
with open("leaf_nutrient_model.tflite", "wb") as f:
    f.write(tflite_model)

print("TFLite model created successfully.")
