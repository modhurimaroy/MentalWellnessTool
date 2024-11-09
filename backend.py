
import joblib
import json
from datetime import datetime

worksheets = {"no_emote": ["How are you feeling today"],
              "anger": ["What situation or event are you angry about?", 
                        "Do you thing there is something deeper causing your anger?", 
                        "Why do you think the other people in this scenario acted the way they did?",
                        "Do you think your level of anger is appropriate to what is happening?"], 
              "disgust": ["What person do you feel disgust at?", 
                          "What did that person do to make you feel disgust?", 
                          "Is there a reason why that person might have acted that way?", 
                          "Why do you think that person thought acting that way was okay? Did they act that way on purpose?"],
              "fear": ["Why are you afraid/anxious?", 
                       "How does this make you feel: helpless, alone, depair, insecure, or overwhelmed? \n It can be useful to narrow down your feelings.", 
                       "What's the best-case scenario in this situation?", 
                       "What's the worst that could happen in this situation?",
                       "How can I prevent the worst to happen?",
                       "If the worst does happen, what can I do to fix it? Maybe the worst case scenario is not as bad as you think"],
              "joy": ["Is there anything particular you are happy about?", 
                      "Have you done any of the following: donated to charity, spent time with loved ones, \nexcercised, meditated, journaled, helped someone out, \nwent to work, started a new hobby, did an old hobby? \n It can be good to reflect on the days you feel good as well."], 
              "neutral": ["It can be good to reflect on this too. Maybe think about your day a little more and type how you feel"],
              "sadness": ["Is there anything particular you are sad about?", 
                          "It's ok to feel sad when faced with a negative situation.\nHowever, it's also important to take a step back and focus on the positive things in life. \nTry writing one good thing that happened today", 
                          "What about something fun you did?", 
                          "What is something that you accomplished today, no matter how small?", 
                          "What can you be grateful for?", "Remember to reach out for help if you are feeling particularly sad. \nSome other things you can do to feel better are"\
                          "listen to music, exercise, \nspend time with loved ones or spend time on a hobby"],
              "shame": ["Shame occurs when we fail to meet our own personal standards or others' expectations, what situation made you feel shame?", 
                        "What negative thoughts about yourself did this situation cause?", 
                        "What self-belief did this situation cause: feeling unloveable, or worthless, or not good enough, or bad\n, or stupid, or ugly, or abnormal, or boring, or worthless?", 
                        "Now that you've identified a feeling, name Name three pieces of evidence contrary to this belief"], 
              "surprise": ["How do you feel in response to this surprise? Anger, anxiety, joy, or nothing?",
                           "once you think you've identified a more accurate emotion, restart the program"]}

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
    "anger":"Find yourself a safe place, away from others, where you will not be disturbed; \na place where you have time to calm down if you are feeling highly emotional. \nWriting down your feelings can help you understand them and become more comfortable with them: \nidentifying what is reasonable and unreasonable",
    "disgust":"Disgust often comes up when we encounter something that deeply conflicts with our values \nor sense of self. Let’s explore where this feeling is coming from \nand how it’s impacting you. Together, we can work to understand it better and find ways to process \nit so that it feels less overwhelming.",
    "fear":"Let's take some time to explore where this fear might be coming from and how it's affecting you. \nSometimes breaking down what feels so big and intimidating \ncan help it feel more manageable",
    "joy":"That's wonderful to hear! It sounds like you've worked hard to reach this place, and you deserve this way.",
    "neutral":"It sounds like you’re feeling pretty neutral right now—not particularly happy, sad, or anything in between. \nThat’s completely okay; feeling neutral is a \nnormal state to be in, and it can actually offer a lot of clarity and calm.",
    "sadness":"It's okay to feel this way, and you're not alone in it. What do you think might be underneath this sadness?",
    "shame":"Let's talk about what happened and how you're feeling. Maybe we can look at it together with compassion, \nand explore how to start working toward self-forgiveness.",
    "surprise":"Sometimes surprises can bring up a mix of other feelings, too, like excitement, confusion, or even anxiety. \nLet’s talk through what happened"
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

# if __name__=="__main__":
#     emotion_cats = pipe_lr.classes_
#     input = "I feel anxious"
#     output = get_prediction_proba(input)
#     results = dict(zip(emotion_cats, output))
#     #print(results)
#     emot = predict_emotions(input)
#     #print(emot)
#     #print(emotion_cats)
#     response_text = respond_to_user(emot)
#     log_session_data(emot, response_text)