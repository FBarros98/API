from flask import * 
import json, time

#Criar o aplicativo Flask - Para a construção dessa API foi utilizado o Flask, que é um micro framework para Python utilizado para criar aplicativos Web.
app = Flask(__name__)

#Criando o endpoint e a função para a home page
@app.route('/', methods=['GET'])

def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page', 'Timestamp':time.time()} # Conjunto de dados que é um dicionário com todas as infos que a API deve retornar
    json_dump = json.dumps(data_set) #Converte as informações em um json

    return json_dump

#Criando endpoint e função para uma request
@app.route('/user/', methods=['GET'])

def request_page():
    user_query = str(request.args.get('user')) #O endpoint passa a ser /user/?user=asdfaddsaf
    data_set = {'Page': 'Request', 'Message': f'Successfully got the request for {user_query}', 'Timestamp':time.time()} # Conjunto de dados que é um dicionário com todas as infos que a API deve retornar
    json_dump = json.dumps(data_set) #Converte as informações em um json

    return json_dump

