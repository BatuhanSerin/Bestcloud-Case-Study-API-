from flask import Flask
from flask import request
import json


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/temperature', methods=['GET'])  #  http://127.0.0.1:7776/temperature
def home_page():

    data_set = {'Name': 'Batuhan', 'Lastname': 'Serin'}
    
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/temperature/city/', methods=['GET'])    #  /temperature/city/?city=ankara
def request_page():

    user_query = str(request.args.get('city'))



    data_set = {'City': f'temp {user_query}'}
    json_dump = json.dumps(data_set)
    
    return json_dump



if __name__ == '__main__':
    app.run(host="127.0.0.1" , port=7776)