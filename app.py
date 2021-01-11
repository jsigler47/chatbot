from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_sentiment(msg):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(msg)

    if sentiment_dict['compound'] >= 0.05 :
        return('That was pretty nice.')
    elif sentiment_dict['compound'] <= -0.05 :
        return('That was not very nice.')
    else:
        return('That was pretty neutral.')


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_sentiment(userText))


if __name__ == "__main__":
    app.run(debug=True)
