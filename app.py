from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# Initialisation de l'application Flask
app = Flask(__name__)

# Charger le modèle
MODEL_PATH = "modele.h5"
model = load_model(MODEL_PATH)

# Charger les noms des classes (par exemple)
CLASS_NAMES = ["Classe1", "Classe2", "Classe3"]  # Remplacez par vos classes réelles

@app.route("/")
def home():
    # Charger la page principale
    return render_template("cookify.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Vérification de l'image reçue
    if "image" not in request.files:
        return jsonify({"error": "Aucune image reçue"}), 400

    file = request.files["image"]
    if file:
        # Prétraiter l'image pour qu'elle soit compatible avec le modèle
        try:
            image = load_img(file, target_size=(224, 224))  # Adapter à votre modèle
            image_array = img_to_array(image) / 255.0
            image_array = np.expand_dims(image_array, axis=0)

            # Prédire la classe
            predictions = model.predict(image_array)
            predicted_class = np.argmax(predictions, axis=1)[0]
            predicted_class_name = CLASS_NAMES[predicted_class]

            return jsonify({"predicted_class": predicted_class, "predicted_class_name": predicted_class_name})

        except Exception as e:
            return jsonify({"error": f"Erreur lors du traitement de l'image : {str(e)}"}), 500

    return jsonify({"error": "Erreur lors de l'envoi du fichier"}), 500

if __name__ == "__main__":
    app.run(debug=True)
