
import joblib
import json
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

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
    "anger":"We can feel uncomfortable expressing strong emotions, such as anger. This can be especially true when how we express anger is disproportionate to the situation, or we have trouble maintaining control. Answering the following questions will help you find a safe way to explore your anger so that you can express it more appropriately when necessary.",
    "disgust":"Disgust often comes up when we encounter something that deeply conflicts with our values or sense of self. Let’s explore where this feeling is coming from and how it’s impacting you. Together, we can work to understand it better and find ways to process it so that it feels less overwhelming.",
    "fear":"Let's take some time to explore where this fear might be coming from and how it's affecting you. Sometimes breaking down what feels so big and intimidating can help it feel more manageable",
    "joy":"That's wonderful to hear! It sounds like you've worked hard to reach this place, and you deserve this way.",
    "neutral":"It sounds like you’re feeling pretty neutral right now—not particularly happy, sad, or anything in between. That’s completely okay; feeling neutral is a normal state to be in, and it can actually offer a lot of clarity and calm.",
    "sadness":"It's okay to feel this way, and you're not alone in it.",
    "shame":"Let's talk about what happened and how you're feeling. Maybe we can look at it together with compassion, and explore how to start working toward self-forgiveness.",
    "surprise":"Sometimes surprises can bring up a mix of other feelings, too, like excitement, confusion, or even anxiety. Let’s talk through what happened"
}

def respond_to_user(emotion):
    print("The model has detected that you are feeling " + emotion)
    print(responses[emotion])
    if (emotion == 'anger')
        worksheet = anger_worksheet()
    if (emotion == 'disgust')
        worksheet = disgust_worksheet()
    if (emotion == 'fear')
        worksheet = fear_worksheet()
    if (emotion == 'joy')
        worksheet = joy_worksheet()
    if (emotion == 'neutral')
        worksheet = neutral_worksheet()
    if (emotion == 'sadness')
        worksheet = sadness_worksheet()
    if (emotion == 'shame')
        worksheet = shame_worksheet()
    if (emotion == 'surprise')
        worksheet = surprise_worksheet()

    #alter session to save worksheet as well maybe?
    log_session_data(emotion, response_text, output_file="session_log.json")

def question_answer(question) {
    input(question)

}

#https://www.therapistaid.com/therapy-worksheet/building-happiness-exercises
def joy_worksheet() {
    responses = {}
    responses['reason'] = input("Is there anything particular you are happy about?")
    print("Have you done any of the following? (Y/N)")
    activites = ['Donated to charity', 'Spent time with loved ones', 'Exercised', 'Meditated', 'Journaled', 'Helped someone out', 'Went to work', 'Started a new hobby', 'Performed an old hobby']
    act_done = []
    for act in activites:
        resp = input(act)
        if resp == 'Y':
            act_done.append(act)

    responses['activites'] = act_done   
    return responses         
}


#https://soniamcdonald.com.au/wp-content/uploads/2020/03/Fear_Mastery-1.pdf
#https://www.webmd.com/mental-health/signs-of-fear
def fear_worksheet() {
    responses = {}
    responses['reason'] = input("Why are you afraid/anxious?")
    responses['feelings'] = input("How does this make you feel?")
    feelings = ['helpless', 'alone', 'despair', 'insecure', 'overwhelmed']
   
    responses['best'] = input("What's the best-case scenario in this situation")
    responses['fear'] = input("What's the worst that could happen in this situation?")
    responses['prevent'] = input("How can I prevent the worst to happen?")
    responses['action'] = input("If the worst does happen, what can I do to fix it?")
    
    symptoms = ["Increased heart rate", "Faster breathing or shortness of breath", "Butterflies or digestive changes"
                "Sweating and chills", "Trembling muscles"]

    responses['symptoms'] = []
    return responses
}


def surprise_worksheet() {
    output = input("How do you feel in response to this surprise? Anger, anxiety, joy, or nothing?")
    if output == 'anger':
        worksheet = anger_worksheet()
    elif output == 'anxiety':
        worksheet = fear_worksheet()
    elif output == 'joy'
        worksheet = joy_worksheet()
    else
        worksheet = {}

    worksheet['response_emotion'] = output
    return worksheet
    
}

#https://www.therapistaid.com/therapy-worksheet/core-beliefs
def shame_worksheet() {
    responses = {}
    print("Shame occurs when we fail to meet our own personal standards or others' expectations")
    responses['situation'] = input("What situation made you feel shame?")
    responses['thoughts'] = input("What negative thoughts about yourself did this situation cause?")
    print("What self-belief did this situation cause?")
    print(["I am unloveable", "I am not good enough", "I am a bad person", "I am stupid", "I am ugly", "I am abnormal",
            "I am boring, I am worthless", "I'm undeserving"])
    responses['belief'] = input("Enter one belief you experienced:")
    responses['evidence'] = input("Name three pieces of evidence contrary to this belief:")
    return responses
}

#https://www.therapistaid.com/therapy-worksheet/gratitude-journal-three-good-things
#https://www.betterup.com/blog/what-to-do-when-you-are-sad
def sadness_worksheet() {
    responses = {}
    responses['reason'] = input("Is there anything particular you are sad about?")
    print("It's ok to feel sad when faced with a negative situation. However, it's also important to take a step back and focus on the positive things in life.")
    responses['good thing'] = input("One good thing that happened today was...")
    responses['fun'] = input("I had fun today when...")
    responses['accomplishment'] = input("Something I accomplished today was...")
    responses['gratitude'] = input("Something I am grateful for today is...")

    print("Remember to reach out for help if you are feeling particularly sad. Some other things you can do to feel better are"\
    "listen to music, exercise, spend time with loved ones or spend time on a hobby")
    return responses
}

#https://eymtherapy.com/wp-content/uploads/2018/03/figuring-out-opposites.pdf
def disgust_worksheet() {
    responses = {}
    responses["target"] = input("What person do you feel disgust at")
    responses["situation"] = input("What did that person do to make you feel disgust?")
    responses["context"] = input("Is there a reason why that person might have acted that way")
    responses["reason"] = input("Why do you think that person thought acting that way was okay? Did they act that way on purpose?")
    valid = input("Do you think that reason makes it valid for that person to do that? (Y/N)")
    if valid == 'Y':
        print("Remember to be kind to the person you feel contempt for as the action was not entirely their fault")
    else:
        print("If you really feel that way, it is best for you to have a conversation with that person and explain how you are feeling to them.")
}

#
#https://www.therapistaid.com/therapy-worksheet/anger-warning-signs
def anger_worksheet() {
    responses = {}
    responses['situation'] = input('What situation or event are you angry about?')
    responses['context'] = input('Do you thing there is something deeper causing your anger?')
    responses['excuse'] = input('Why do you think the other people in this scenario acted the way they did?')
    responses['appropriate'] = input("Do you think your level of anger is appropriate to what is happening?")
    print('Which of the following ways have you reacted to your anger? (Enter y/n)')
    signs = ['Mind went blank', 'Insulted the other person', 'Face turned red', 'Body or hands shook', 'Sweating',
        'Threw things', 'Heavy/fast breathing', 'Scowling', 'Screaming/yelling', 'Clenching fists', 'Felt hot/sick',
        'Punched walls', 'Went quiet', 'Cried', 'Paced around the room', 'Headaches']
    signs_exp = []
    for sign in signs:
        resp = input(sign)
        if resp == 'y':
            signs_exp.append(sign)
    
    responses['signs'] = signs

    if sign in ['Insulted the other person', 'Threw things', 'Screaming/yelling', 'Punched walls']:
        print("Woah! Your actions may feel the other person feel unsafe or really hurt their feelings. In the future, walk away and try to calm down when you feel the urge to do these things.")
        responses['type'] = 'red'
    elif sign in ['Scowling', 'Went quiet', 'Cried', 'Paced around the room'] or signs == []:
        print("It looks like you are managing your anger in healthy ways!")
        responses['type'] = 'green'
    else
        print("Woah! It seems that your body is having an adverse physical reaction to anger. In the future, try to practice some deep breathing or muscle relaxing to calm your body")
        responses['type'] = 'yellow'

    return responses
}

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