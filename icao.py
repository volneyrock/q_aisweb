import requests
from bs4 import BeautifulSoup
from collections import namedtuple


class AisWebRequestException(Exception):
    pass


class AisHtmlParseException(Exception):
    pass


class AisDataNotFoundException(Exception):
    pass


class AisWeb:
    def __init__(self, icao):
        self.url = "https://aisweb.decea.mil.br/"
        self.codigo_icao = icao
        self.soup = self._request_e_parse()

    def _request_e_parse(self):
        url = f"{self.url}?i=aerodromos&codigo={self.codigo_icao}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except requests.exceptions.RequestException as e:
            raise AisWebRequestException(f"Erro na requisição: {e}")
        except Exception as e:
            raise AisHtmlParseException(f"Erro no parsing do HTML: {e}")

    def metar(self):
        metar = self.soup.find("h5", string="METAR")
        if metar:
            return metar.find_next_sibling("p").text
        else:
            raise AisDataNotFoundException("Dados METAR não encontrados")

    def taf(self):
        taf = self.soup.find("h5", string="TAF")
        if taf:
            return taf.find_next_sibling("p").text
        else:
            raise AisDataNotFoundException("Dados TAF não encontrados")

    def nascer_do_sol(self):
        nascer_do_sol = self.soup.find("sunrise")
        if nascer_do_sol:
            return nascer_do_sol.text
        else:
            raise AisDataNotFoundException(
                "Dados de nascer do sol não encontrados"
            )

    def por_do_sol(self):
        por_do_sol = self.soup.find("sunset")
        if por_do_sol:
            return por_do_sol.text
        else:
            raise AisDataNotFoundException(
                "Dados de pôr do sol não encontrados"
            )

    def cartas(self):
        Carta = namedtuple('Carta', ['nome', 'link'])
        cartas = []
        cartas_ul = self.soup.find_all(
            "ul",
            class_="list list-icons list-primary list-icons-style-2"
        )
        for ul in cartas_ul:
            cartas_li = ul.find_all("li")
            for li in cartas_li:
                carta_a = li.find("a")
                if carta_a:
                    nome_carta = carta_a.get_text()
                    link_carta = carta_a.get("href")
                    carta = Carta(nome=nome_carta, link=link_carta)
                    cartas.append(carta)
        return cartas
