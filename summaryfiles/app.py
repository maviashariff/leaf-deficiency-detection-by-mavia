from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import os
import cv2
import uuid
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# =========================
# Configuration
# =========================
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = (".png", ".jpg", ".jpeg")

# =========================
# Load Model
# =========================
model = tf.keras.models.load_model("leaf_nutrient_model.h5")

CLASS_NAMES = ["Healthy", "Nitrogen", "Phosphorus", "Potassium"]

SUGGESTIONS = {
    "Nitrogen": "Possible nitrogen deficiency detected. Consider balanced nitrogen-rich nutrients.",
    "Phosphorus": "Possible phosphorus deficiency detected. Monitor plant growth and root development.",
    "Potassium": "Possible potassium deficiency detected. Check leaf edges and overall plant strength.",
    "Healthy": "Leaf appears healthy. No major nutrient deficiency detected."
}

# =========================
# Image Validation Helpers
# =========================
def is_dark_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return np.mean(gray) < 40

def is_blurry_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    return variance < 100

def looks_like_leaf(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    _, s, v = cv2.split(hsv)
    return np.mean(s) > 40 and np.mean(v) > 50

# =========================
# Routes
# =========================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "leaf_image" not in request.files:
        return "No file uploaded"

    file = request.files["leaf_image"]

    if file.filename == "":
        return "No selected file"

    if not file.filename.lower().endswith(ALLOWED_EXTENSIONS):
        return "Invalid file format"

    # Secure + unique filename
    filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    # =========================
    # Validation Layer
    # =========================
    raw_img = cv2.imread(file_path)

    if raw_img is None:
        return "Invalid image file"

    if is_dark_image(raw_img):
        return render_template(
            "result.html",
            prediction="Invalid Image",
            confidence=0,
            suggestion="Image is too dark. Please capture the leaf in proper lighting.",
            image_path=file_path
        )

    if is_blurry_image(raw_img):
        return render_template(
            "result.html",
            prediction="Invalid Image",
            confidence=0,
            suggestion="Image is too blurry. Please hold the camera steady.",
            image_path=file_path
        )

    if not looks_like_leaf(raw_img):
        return render_template(
            "result.html",
            prediction="Leaf Not Found",
            confidence=0,
            suggestion="No leaf detected. Please upload a clear leaf image.",
            image_path=file_path
        )

    # =========================
    # Nutrient Prediction
    # =========================
    img = image.load_img(file_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)[0]
    predicted_index = np.argmax(predictions)
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = round(float(predictions[predicted_index]) * 100, 2)

    return render_template(
        "result.html",
        prediction=predicted_class,
        confidence=confidence,
        suggestion=SUGGESTIONS[predicted_class],
        image_path=file_path
    )

# =========================
# Run App
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

