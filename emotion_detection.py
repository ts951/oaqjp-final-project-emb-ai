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
    # Return response data
    return response.text
    
    
    # Convert JSON data in response to a dictionary
    #response_data = json.loads(response.text)

    #print(response_data)

#emotion_detection("I'm so pissssssed!")