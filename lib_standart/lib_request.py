from requests.auth import HTTPBasicAuth
from json import loads, dumps
import requests

class BajarDatos():
    def json(self):
        r = requests.get('http://35.185.220.144:9200/vpro/_search',
                         auth=HTTPBasicAuth('elastic', 'cyttek')
                         )
        # id_list = [each.get('_source') for each in Json['hits']['hits']]
        Json = r.json()
        for y in Json['hits']['hits']:
            for x in y['_source']:
                print(x)

Object = BajarDatos()
# Object.html()
Object.json()
