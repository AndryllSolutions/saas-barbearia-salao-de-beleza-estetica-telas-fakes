from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")

# MOCKS
fake_clientes = [
    {"id": 1, "nome": "Amanda Pellin", "email": "amanda@email.com", "nascimento": "09/10/1995"},
    {"id": 2, "nome": "Anna Tavares", "email": "anna@email.com", "nascimento": "13/07/1994"},
]

@app.route("/") # RENDERIZA A PAGINA INICIAL
def painel():
    return render_template("painel.html")


@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/comandas")
def comandas():
    return render_template("comandas.html")

@app.route("/profissionais")
def profissionais():
    return render_template("profissionais.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")
#########################comentario
@app.route("/relatorios")
def relatorios():
    return render_template("relatorios.html")


@app.route("/configuracoes")
def configuracoes():
    return render_template("configuracoes.html")



if __name__ == "__main__":
    app.run(debug=True)