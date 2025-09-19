"""
Module containing function for emotion analysis of input text using the "Emotion Predict" 
function in the Watson NLP library
"""

# Import required libraries
import requests
import json

def emotion_detector(text_to_analyse):
    """
    Function that takes text to perform emotional analysis on as input and outputs analysis data
    """
    # URL to emotion analysis service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    # Define required headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Store text to be analysed in JSON format
    input_json = {"raw_document": {"text": text_to_analyse}}
    # Send POST request with json and headers and get response
    response = requests.post(url, json = input_json, headers = headers)

    # Check for status code 400 and return all values as None if present
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    # Convert response text into a dictionary
    response_data = json.loads(response.text)
    # Extract emotions dictionary from data
    emotion_data = response_data["emotionPredictions"][0]["emotion"]
    
    # Iterate over the emotion data, extracting scores for each emotion and comparing to the current 
    # highest seen score (starting at 0) find the emotion with the highest score
    highest_score = 0
    for emotion in emotion_data:   
        if emotion_data[emotion] > highest_score:
            highest_score = emotion_data[emotion]
            dominant_emotion = emotion
    
    # Add dominant emotion to emotion_data dictionary and return it
    emotion_data['dominant_emotion'] = dominant_emotion
    return emotion_data
