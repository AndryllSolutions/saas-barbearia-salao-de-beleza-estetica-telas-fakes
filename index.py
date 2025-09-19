from flask import Flask, render_template

# templates está dentro da pasta api
app = Flask(__name__, template_folder="templates")

# MOCKS
fake_clientes = [
    {"id": 1, "nome": "Amanda Pellin", "email": "amanda@email.com", "nascimento": "09/10/1995"},
    {"id": 2, "nome": "Anna Tavares", "email": "anna@email.com", "nascimento": "13/07/1994"},
]
fake_comandas = [
    {"id": 101, "cliente": "Amanda Pellin", "status": "Aberta", "valor": "R$ 120,00"},
    {"id": 102, "cliente": "Carlos Silva", "status": "Fechada", "valor": "R$ 80,00"}
]

fake_profissionais = [
    {"id": 1, "nome": "João Barbosa", "funcao": "Barbeiro", "comissao": "30%"},
    {"id": 2, "nome": "Maria Costa", "funcao": "Manicure", "comissao": "25%"}
]

fake_servicos = [
    {"id": 1, "nome": "Corte Masculino", "preco": "R$ 40,00", "categoria": "Cabelo"},
    {"id": 2, "nome": "Pintura Unha", "preco": "R$ 25,00", "categoria": "Unhas"}
]

@app.route("/")
def painel():
    return render_template("painel.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html", fake_clientes=fake_clientes)


@app.route("/comandas")
def comandas():
    return render_template("comandas.html", fake_comandas=fake_comandas)

@app.route("/profissionais")
def profissionais():
    return render_template("profissionais.html", fake_profissionais=fake_profissionais)

@app.route("/servicos")
def servicos():
    return render_template("servicos.html", fake_servicos=fake_servicos)


@app.route("/relatorios")
def relatorios():
    return render_template("relatorios.html")

@app.route("/configuracoes")
def configuracoes():
    return render_template("configuracoes.html")


@app.route("/marcas")
def marcas():
    return render_template("marcas.html")

@app.route("/pacotes")
def pacotes():
    return render_template("pacotes.html")

@app.route("/pacotes_predefinidos")
def pacotes_predefinidos():
    return render_template("pacotes_predefinidos.html")

@app.route("/ajuda")
def ajuda():
    return render_template("ajuda.html")

@app.route("/whatsapp_marketing")
def whatsapp_marketing():
    return render_template("whatsapp_marketing.html")












if __name__ == "__main__":
    app.run(debug=True)
