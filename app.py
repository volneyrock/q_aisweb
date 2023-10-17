from flask import Flask, render_template, request
from flask.views import View
from icao import AisWeb, AisDataNotFoundException


app = Flask(__name__)


def obter_dados_ais(icao):
    try:
        ais = AisWeb(icao)
        metar = ais.metar()
        taf = ais.taf()
        nascer_do_sol = ais.nascer_do_sol()
        por_do_sol = ais.por_do_sol()
        cartas = ais.cartas()
        return {
            "icao": icao,
            "metar": metar,
            "taf": taf,
            "nascer_do_sol": nascer_do_sol,
            "por_do_sol": por_do_sol,
            "cartas": cartas,
        }
    except AisDataNotFoundException:
        return None


class IcaoView(View):
    methods = ["GET", "POST"]

    def dispatch_request(self):
        dados_ais = None
        if request.method == "POST":
            icao = request.form["icao"]
            dados_ais = obter_dados_ais(icao)
        return render_template("icao_form.html", dados_ais=dados_ais)


app.add_url_rule("/", view_func=IcaoView.as_view("icao"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
