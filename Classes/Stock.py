import requests
import json


class Stock:
    """Ações e BRDs"""

    url_api = "https://api.infomoney.com.br/ativos/top-alta-baixa-por-ativo/acao?sector=Todos&orderAtributte=Volume&pageIndex=1"

    def top_stocks(self, num_stocks: int):
        url = self.url_api + "&pageSize=" + str(num_stocks)
        return self._get_api(url)

    def search_stock(self, code):
        url = self.url_api + "&search=" + code
        return self._get_api(url)

    @staticmethod
    def _get_api(url):
        output = {}
        try:
            response = requests.get(url)
            if response.status_code == 200:
                output = {
                    "data": json.loads(response.content),
                    "error": None
                }
            else:
                output = {
                    "data": None,
                    "error": f"Não foi possível retornar os dados (status_code: {response.status_code})"
                }
        except:
            output = {
                "data": None,
                "error": "Não foi possível se conectar a API"
            }
        return output

    @staticmethod
    def format_stock(stock_data):
        output = ""
        if stock_data["error"]:
            output = stock_data["error"]
        elif len(stock_data["data"]["Data"]) == 0:
            output = "Nenhum resultado encontrado"
        else:
            output = "Dados de: " + stock_data["data"]["ReferenceDate"] + "\n\n"
            stocks = stock_data["data"]["Data"]
            for s in stocks:
                output += s["StockName"] + " (" + s["StockCode"] + ")\n"
                output += "Valor: " + s["ValueFormatted"] + "\n"
                output += "Variação dia: " + s["ChangeDayFormatted"] + "%\n"
                output += "Variação 12 meses: " + s["Change12MFormatted"] + "%\n"
                output += "Volume: " + s["VolumeFormatted"] + "\n"
                output += "\n"

        return output

