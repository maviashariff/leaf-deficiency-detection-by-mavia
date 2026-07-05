import tensorflow as tf
import tf2onnx

# Load model safely
model = tf.keras.models.load_model("leaf_nutrient_model.h5", compile=False)

# Define input signature (fixed batch size)
spec = (tf.TensorSpec((1, 224, 224, 3), tf.float32, name="input"),)

# Convert and save
model_proto, _ = tf2onnx.convert.from_keras(
    model,
    input_signature=spec,
    opset=13,
    output_path="leaf_nutrient_model.onnx"
)

print("ONNX model saved successfully.")
