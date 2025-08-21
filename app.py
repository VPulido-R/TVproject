from flask import Flask, render_template, redirect, url_for
from picamera2 import Picamera2
from datetime import datetime
import os

app = Flask(__name__)

FOTOS_FOLDER = "static/fotos"
os.makedirs(FOTOS_FOLDER, exist_ok=True)

# Variable para guardar la última foto tomada
ultima_foto = None
ultima_fecha = None


@app.route("/")
def index():
    return render_template("index.html", foto=ultima_foto, fecha=ultima_fecha)


@app.route("/tomar_foto")
def tomar_foto():
    global ultima_foto, ultima_fecha

    picam2 = Picamera2()
    picam2.start()
    # Espera para ajustar exposición
    import time
    time.sleep(2)

    ahora = datetime.now()
    nombre_archivo = f"foto_{ahora.strftime('%Y%m%d_%H%M%S')}.jpg"
    archivo = os.path.join(FOTOS_FOLDER, nombre_archivo)

    picam2.capture_file(archivo)
    picam2.stop()

    # Guardamos para mostrar en la web
    ultima_foto = archivo
    ultima_fecha = ahora.strftime("%d/%m/%Y %H:%M:%S")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
