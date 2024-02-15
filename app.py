from flask import Flask, render_template

app = Flask(__name__)

""" Rotas para ponto de acesso para estabelecer uma comunicacao entre outros PROGRAMAS que podem estar 
acessando essa informacao, ou usuarios que queiram acessar essa informacao
esa informacao sera devolvida por eles
"""
class Tarefas():
    pass

@app.route("/")
def index():
    return "Hello, world"

@app.route("/about")
def about():
    return f"Pagina sobre"

if __name__ == "__main__":
    app.run(debug=True)