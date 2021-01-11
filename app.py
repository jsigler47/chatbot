from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_sentiment(msg):
    msg = msg.lower()
    msg.replace('sentiment', '')
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(msg)
    print(sentiment_dict)

    if sentiment_dict['compound'] >= 0.05:
        return('That has a positive sentiment')
    elif sentiment_dict['compound'] <= -0.05:
        return('That has a negative sentiment.')
    else:
        return('That has a neutral sentiment.')


def print_help():
    return "I can do many things. Include the word of what you want me to do in your message. Current functions include, 'sentiment', and 'help'"


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if "sentiment" in userText.lower():
        return str(get_sentiment(userText))
    elif "help" in userText.lower():
        return print_help()
    else:
        return "I'm not sure what you're looking for"


if __name__ == "__main__":
    app.run(debug=True)
