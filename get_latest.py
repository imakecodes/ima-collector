from http import HTTPStatus
import json
import os

import requests
import pendulum


resp = requests.get("https://balneabilidade.ima.sc.gov.br/relatorio/mapa")
if resp.status_code == HTTPStatus.OK:
    with open("latest.json", "w+") as f:
        f.write(json.dumps(resp.json(), indent=4))

        filename = "{}.json".format(pendulum.now().strftime("%Y-%m-%d"))
        os.system(f"cp latest.json ./data/{filename}") 




