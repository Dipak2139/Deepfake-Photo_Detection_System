from flask import flash
from flask import redirect, url_for
from flask import send_from_directory
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
from utils.preprocess import preprocess_image



app = Flask(__name__)
app.secret_key = "deepfake-secret-key"


# Configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
MODEL_PATH = "model/deepfake_model.h5"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model once
model = tf.keras.models.load_model(MODEL_PATH)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_url = None

    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", result="No file uploaded")

        file = request.files["image"]

        if file.filename == "":
            return render_template("index.html", result="No file selected")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            image_url = f"/uploads/{filename}"  # for displaying image

            try:
                image = preprocess_image(filepath)
                prediction = model.predict(image)[0][0]
                confidence = prediction * 100

                # ✅ Balanced threshold
                if prediction >= 0.55:
                    result = f"FAKE IMAGE DETECTED (Confidence: {confidence:.2f}%)"
                else:
                    result = f"REAL IMAGE DETECTED (Confidence: {100 - confidence:.2f}%)"

            except Exception as e:
                result = str(e)

        else:
            result = "Invalid file type"

    return render_template("index.html", result=result, image_url=image_url)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/delete/<filename>", methods=["POST"])
def delete_image(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash("Image deleted from database successfully")
    return redirect(url_for("index"))






if __name__ == "__main__":
    app.run(debug=True)
