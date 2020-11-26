from http import HTTPStatus
import json

import requests
import pedulum


resp = requests.get("https://balneabilidade.ima.sc.gov.br/relatorio/mapa")
if resp.status_code == HTTPStatus.OK:
    with open("latest.json", "w+") as f:
        f.write(json.dumps(resp.json), indent=4))

