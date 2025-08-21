from flask import Flask, render_template, redirect, url_for
from picamera2 import Picamera2
import time
import os

app = Flask(__name__)

# Carpeta donde se guardarán las fotos
FOTOS_FOLDER = "static/fotos"
os.makedirs(FOTOS_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tomar_foto")
def tomar_foto():
    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)  # espera para ajustar exposición
    archivo = os.path.join(FOTOS_FOLDER, "foto_web.jpg")
    picam2.capture_file(archivo)
    picam2.stop()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
