from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# CONFIG DO EMAIL
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# COLOQUE SEU E-MAIL E SENHA APP DO GMAIL
app.config['MAIL_USERNAME'] = 'vnnzsala1@gmail.com'
app.config['MAIL_PASSWORD'] = 'vinicouter'

mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/enviar_email', methods=['POST'])
def enviar_email():
    email_usuario = request.form['email']

    msg = Message(
        subject="Bem-vindo ao EcoBottle 🌱",
        sender=app.config['MAIL_USERNAME'],
        recipients=[email_usuario]
    )

    msg.body = """Obrigado por se inscrever na nossa newsletter!
Aqui está seu guia exclusivo para um futuro sustentável 🌍

Equipe EcoBottle 💚
"""

    mail.send(msg)

    return redirect('/')  # depois podemos voltar com modal via JS

if __name__ == '__main__':
    app.run(debug=True)
