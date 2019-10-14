from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)
#CORS(app, resources={r'/*': {'origins': '*'}})


#This route will get the data for the number of times each character
#speaks per seasion.
@app.route('/seasonSpeachCount', methods=['GET', 'POST'])
def seasonSpeachCount():
    if request.method == 'POST':
        post_data = request.get_json()
        season = int(post_data['season'])
        print(season)
        return jsonify('pong!')


if __name__ == '__main__':
    app.run()
