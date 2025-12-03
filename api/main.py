from flask import Flask, render_template, request, jsonify
import os
import resend
from mangum import Mangum  # Adaptador WSGI -> Lambda (serverless)

# Configura API Resend
resend.api_key = "re_c1tpEyD8_NKFusih9vKVQknRAQfmFcWCv"

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/enviar_email", methods=["POST"])
def enviar_email():
    data = request.form
    email_usuario = data.get("email")

    if not email_usuario:
        return jsonify({"error": "Email não fornecido"}), 400

    try:
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": email_usuario,
            "subject": "Bem-vindo ao EcoBottle 🌱",
            "html": """
            <p>Obrigado por se inscrever na nossa newsletter!</p>
            <p>Aqui está seu guia exclusivo para um futuro sustentável 🌍</p>
            <p>Equipe EcoBottle 💚</p>
            """
        })
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

handler = Mangum(app)

if __name__ == "__main__":
    app.run(debug=True)