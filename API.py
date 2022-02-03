from random import random
from flask import Flask
from flask import request
import requests
import json



app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])  #  http://127.0.0.1:7776
def home_page():

    data_set = {'Name': 'Batuhan', 'Lastname': 'Serin'}
    
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/temperature', methods=['GET'])    #  http://127.0.0.1:7776/temperature?city=ankara
def request_page():

    city = str(request.args.get('city'))
    
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=95edf34d0dd7709f36b7ac7f67cf2399')

    data = response.json()
    # getting the main dict block
    main = data['main']
    # getting temperature
    temperature = main['temp']

    print(temperature-273.15,data)

    data_set = {'City': f'{city.capitalize()}' , 'Temperature': f'{"{:.2f}".format(temperature-273.15)}C'}
    json_dump = json.dumps(data_set)
    
    return json_dump



if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=7776)
