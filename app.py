# ============================================================
#   SIVA MedBot - Servidor Flask
#   Version 3.0 - Produccion
# ============================================================

import os
from flask import Flask, render_template, request, jsonify
from siva_medbot import analizar_sintomas, aplicar_heuristicas, obtener_todos_sintomas

app = Flask(__name__)

@app.route("/")
def index():
    sintomas = obtener_todos_sintomas()
    return render_template("index.html", sintomas=sintomas)

@app.route("/analizar", methods=["POST"])
def analizar():
    data = request.get_json()
    sintomas_usuario = data.get("sintomas", {})

    if not sintomas_usuario:
        return jsonify({"error": "Por favor selecciona al menos un sintoma."})

    resultados = analizar_sintomas(sintomas_usuario)
    resultados = aplicar_heuristicas(sintomas_usuario, resultados)

    return jsonify({
        "resultados": resultados,
        "total_sintomas": len(sintomas_usuario)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)