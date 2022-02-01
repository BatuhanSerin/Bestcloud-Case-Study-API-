from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Name': 'Batuhan', 'Lastname': 'Serin'}
    
    json_dump = json.dumps(data_set)

    
    return json_dump

@app.route('/city/', methods=['GET'])
def request_page():

    user_query = str(request.args.get('city'))



    data_set = {'City': f'temp {user_query}'}
    json_dump = json.dumps(data_set)
    
    return json_dump



if __name__ == '__main__':
    app.run(port=7776)