from flask import * 
import json
from time import *
from pytz import *
from datetime import datetime
#Criar o aplicativo Flask - Para a construção dessa API foi utilizado o Flask, que é um micro framework para Python utilizado para criar aplicativos Web.
app = Flask(__name__)

#Criando o endpoint e a função para a home page
@app.route('/', methods=['GET'])

def home_page():
    IST = timezone('America/Sao_Paulo') 
    data_atual = datetime.now(IST)
    data_local = data_atual.astimezone(IST) 
    data = data_local.strftime('%a, %d %b %Y %H:%M:%S')
    data_set = {'Page': 'Home', 'Message': 'Welcome to the Pagar.me API', 'Timestamp':data} # Conjunto de dados que é um dicionário com todas as infos que a API deve retornar
    json_dump = json.dumps(data_set) #Converte as informações em um json

    return json_dump

#Criando endpoint e função para uma request
@app.route('/user/', methods=['GET'])

def request_page():
    IST = timezone('America/Sao_Paulo') 
    data_atual = datetime.now(IST)
    data_local = data_atual.astimezone(IST) 
    data = data_local.strftime('%a, %d %b %Y %H:%M:%S')
    user_query = str(request.args.get('user')) #O endpoint passa a ser /user/?user=usuario_de_sua_escolha
    data_set = {'Page': 'Request', 'Message': f'Welcome to the Pagar.me API. Successfully got the request for {user_query}', 'Timestamp':data} # Conjunto de dados que é um dicionário com todas as infos que a API deve retornar
    json_dump = json.dumps(data_set) #Converte as informações em um json

    return json_dump

