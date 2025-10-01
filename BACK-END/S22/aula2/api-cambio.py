import requests
import json

CHAVE_API ='f5ed3fd81ef74aee073da4e951bf9c54e1cef6d1dae04ab9e3cc89acc367c51b'
URL = f'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL?token={CHAVE_API}'

resposta = requests.get(URL)

if resposta.status_code == 200:
    try:
        cotacoes = resposta.json()
        print("Cotações obtidas com sucesso")
        