
# Import required libraries
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    
    """

    text_to_analyse = request.args.get("textToAnalyze")
    print(text_to_analyse)
    emotion_data = emotion_detector(text_to_analyse)
    return f"For the given statement, the system response is 'anger': {emotion_data['anger']}, 'disgust': {emotion_data['disgust']}, 'fear': {emotion_data['fear']}, 'joy': {emotion_data['joy']}, and 'sadness': {emotion_data['sadness']}. The dominant emotion is {emotion_data['dominant_emotion']}."


@app.route("/")
def render_index_page():
    """
    
    """

    return render_template("index.html")

if __name__ == "__main__":  
    app.run(port = 5000) 