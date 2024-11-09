
import joblib
import json
from datetime import datetime

# Load Model
pipe_lr = joblib.load(open("./emotion_classifier_pipe_lr.pkl", "rb"))

# Function
def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]

def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results[0]

responses = {
    "anger":"Find yourself a safe place, away from others, where you will not be disturbed; a place where you have time to calm down if you are feeling highly emotional. Writing down your feelings can help you understand them and become more comfortable with them— identifying what is reasonable and unreasonable",
    "disgust":"Disgust often comes up when we encounter something that deeply conflicts with our values or sense of self. Let’s explore where this feeling is coming from and how it’s impacting you. Together, we can work to understand it better and find ways to process it so that it feels less overwhelming.",
    "fear":"Let's take some time to explore where this fear might be coming from and how it's affecting you. Sometimes breaking down what feels so big and intimidating can help it feel more manageable",
    "joy":"That's wonderful to hear! It sounds like you've worked hard to reach this place, and you deserve this way.",
    "neutral":"It sounds like you’re feeling pretty neutral right now—not particularly happy, sad, or anything in between. That’s completely okay; feeling neutral is a normal state to be in, and it can actually offer a lot of clarity and calm.",
    "sadness":"It's okay to feel this way, and you're not alone in it. What do you think might be underneath this sadness?",
    "shame":"Let's talk about what happened and how you're feeling. Maybe we can look at it together with compassion, and explore how to start working toward self-forgiveness.",
    "surprise":"Sometimes surprises can bring up a mix of other feelings, too, like excitement, confusion, or even anxiety. Let’s talk through what happened"
}

def respond_to_user(emotion):
    print("The model has detected that you are feeling " + emotion)
    print(responses[emotion])
    return responses[emotion]


def log_session_data(emotion, response_text, output_file="session_log.json"):
    session_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "emotion": emotion,
        "response": response_text
    }
    
    try:
        with open(output_file, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data.append(session_entry)
    
    # Write updated data back to JSON file
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    
    print(f"Session data saved to {output_file}.")

if __name__=="__main__":
    emotion_cats = pipe_lr.classes_
    input = "I feel anxious"
    output = get_prediction_proba(input)
    results = dict(zip(emotion_cats, output))
    #print(results)
    emot = predict_emotions(input)
    #print(emot)
    #print(emotion_cats)
    response_text = respond_to_user(emot)
    log_session_data(emot, response_text)