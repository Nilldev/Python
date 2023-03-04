from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
    'id': 1,
    'título': 'Uma breve história da humanidade',
    'autor': 'Stephen Hawking'
    },
    {
    'id': 2,
    'título': 'A vida de Isaac Newton',
    'autor' :'JJ. kingsman'
    },
    {
    'id': 3,
    'título': '100 dias entre céu e mar',
    'autor': 'Amir Klink'
    },
          ]

@app.route('/livros')
def obter_livros():
    return jsonify(livros)

app.run(port=5000,host='localhost',debug= True)