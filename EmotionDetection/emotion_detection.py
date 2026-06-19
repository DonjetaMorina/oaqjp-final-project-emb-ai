import requests
import json

def emotion_detector(text_to_analyze):
    # Define URL, headers, and payload
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Post request to Watson NLP
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convert response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion block from the nested structure
    # Based on the Watson response structure observed in Task 2
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract individual scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Logic to find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Format the desired output dictionary
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output