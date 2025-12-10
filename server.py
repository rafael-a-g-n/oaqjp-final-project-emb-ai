"""
Flask server for emotion detection web application.

This module provides a web interface for analyzing emotions in text
using the Watson NLP emotion detection service.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main index page.

    Returns:
        str: Rendered HTML template for the index page
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Processes the text input from the user and returns emotion analysis
    results in a formatted string.

    Returns:
        str: Formatted string containing emotion scores and dominant emotion,
             or error message for invalid input
    """
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (indicating an error)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract the emotions and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format the response string
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
