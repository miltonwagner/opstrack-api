from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World 1"


@app.route("/status")
def status():
    return {
        "status": "online"
    }


@app.route("/tickets")
def tickets():
    return [
        {
            "id": 1,
            "titulo": "Computador não liga",
            "status": "aberto"
        },
        {
            "id": 2,
            "titulo": "Erro no sistema",
            "status": "em andamento"
        },
        {
            "id": 3,
            "titulo": "Solicitação de acesso",
            "status": "fechado"
        }
    ]


@app.route("/sobre")
def sobre():
    return {
        "nome": "OpsTrack API",
        "versao": "1.0.0"
    }
