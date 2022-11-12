import requests


class TreasuryBonds:
    """Tesouro Direto"""

    url_api = "https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json"

    def get_api(self):
        return requests.get(self.url_api, verify=False)



