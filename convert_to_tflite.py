import tensorflow as tf

# Path to your trained model
MODEL_PATH = "model/deepfake_model"

# Load SavedModel
model = tf.keras.models.load_model(MODEL_PATH)

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

# Save TFLite model
with open("model/deepfake_model.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ TFLite model saved successfully")
