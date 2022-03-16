import requests
from py_zipkin.zipkin import zipkin_span, zipkin_client_span
from py_zipkin.encoding import Encoding
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


def http_transport(encoded_span):
      apmurl = os.getenv('APM_URL')
      apmkey = os.getenv('APM_KEY')
      requests.post(
             apmurl + '/20200101/observations/public-span?dataFormat=zipkin&dataFormatVersion=2&dataKey=' + apmkey,
        data=encoded_span,
        headers={'Content-Type': 'application/json'},
    )

@app.route('/')
def init():
    cep = request.args.get('cep')
    with zipkin_span(
        service_name='getcep',
        span_name=cep,
        transport_handler=http_transport,
        sample_rate=100,
        encoding = Encoding.V2_JSON
    ):
        resposta = getcep(cep)
        
        if resposta.status_code != 200:
            return str(resposta.raise_for_status())
        else:
            resposta = jsonify(resposta.json())
            return resposta

@zipkin_client_span(service_name='viacep', span_name='call_api')
def getcep(cep):
    url = "https://viacep.com.br/ws/" + cep + "/json/"
    response = requests.request("GET", url)
    return response

if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', threaded=True)