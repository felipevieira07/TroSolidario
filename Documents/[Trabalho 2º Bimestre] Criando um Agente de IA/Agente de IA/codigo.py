from flask import Flask, render_template, request
from nl import nl_to_logic
from logica import logic_to_nl, substituir_proposicoes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    tipo = ""
    proposicoes = {"P": "", "Q": "", "R": "", "S": ""}

    if request.method == "POST":
        tipo = request.form.get("tipo")
        entrada = request.form.get("entrada")

        # proposições definidas pelo usuário
        proposicoes = {
            "P": request.form.get("P"),
            "Q": request.form.get("Q"),
            "R": request.form.get("R"),
            "S": request.form.get("S")
        }

        if tipo == "nl":
            resultado = nl_to_logic(entrada)

        elif tipo == "logica":
            resultado = logic_to_nl(entrada)
            resultado = substituir_proposicoes(resultado, proposicoes)

    return render_template(
        "index.html",
        resultado=resultado,
        tipo=tipo,
        proposicoes=proposicoes
    )


if __name__ == "__main__":
    app.run(debug=True)
