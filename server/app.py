from flask import Flask, jsonify, request
from flask_cors import CORS

#bring in the files that I wrote
from data import *


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
        data = Data()
        post_data = request.get_json()
        season = int(post_data['season'])
        season_data = data.seasonLineCountByCharacter(season)
        return jsonify(season_data)

#This route will get the data for the sentiment analysis
@app.route('/seasonSentimentData',methods=['GET', 'POST'])
def seasonSentimentData():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        season = int(post_data['season'])
        season_data = data.sentimentByCharacter(season)
        return jsonify(season_data)


if __name__ == '__main__':
    app.run()
