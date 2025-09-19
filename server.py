"""
Module for server deployment of Emotion Detector to port 5000 using Flask
"""

# Import required libraries
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create instance of Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Route for emotion detection. Gets the input text and calls emotion detector function to 
    perform analysis, displays output as text to user on web page
    """
    # Get text to analyse from html
    text_to_analyse = request.args.get("textToAnalyze")
    # Get emotion data
    emotion_data = emotion_detector(text_to_analyse)
    # Return formatted data to user 
    return f"For the given statement, the system response is 'anger': {emotion_data['anger']}, \
     'disgust': {emotion_data['disgust']}, 'fear': {emotion_data['fear']}, 'joy': {emotion_data['joy']}, \
     and 'sadness': {emotion_data['sadness']}. The dominant emotion is {emotion_data['dominant_emotion']}."


@app.route("/")
def render_index_page():
    """
    Index route. Render's index.html
    """
    # Render index.html
    return render_template("index.html")

if __name__ == "__main__":  
    app.run(port = 5000) 
