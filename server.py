"""
This file is the one you need to execute to run the flask server locally
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def home():
    '''
    The home page of the website
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def run_emotional_analysis():
    '''
    The function that runs emotional analysis
    '''

    text_to_analyze = request.args.get('textToAnalyze')

    emotions_response = emotion_detector(text_to_analyze)


    if emotions_response['dominant_emotion'] is not None:
        return (
            f"For the given statement, the system response is \n"
            f"anger: {emotions_response['anger']} \n"
            f"disgust: {emotions_response['disgust']} \n"
            f"fear: {emotions_response['fear']} \n"
            f"joy: {emotions_response['joy']} \n"
            f"sadness: {emotions_response['sadness']}"
            f" The dominant emotion is {emotions_response['dominant_emotion']}"
        )

    return "Invalid text! Please try again!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
