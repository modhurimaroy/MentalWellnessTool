
import joblib
import warnings
warnings.filterwarnings("ignore")
import json
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

worksheets = {"anger": [("What situation or event are you angry about?", "reason"), 
                        ("Do you thing there is something deeper causing your anger?", "self-reflection"), 
                        ("Why do you think the other people in this scenario acted the way they did?", "peer-reflection"),
                        ("Do you think your level of anger is appropriate to what is happening?", "self-evaluation"),
                        ("Which of the following ways have you reacted to your anger?", "signs",
                        ['Mind went blank', 'Insulted the other person', 'Face turned red', 'Body or hands shook', 'Sweating',
                        'Threw things', 'Heavy/fast breathing', 'Scowling', 'Screaming/yelling', 'Clenching fists', 'Felt hot/sick',
                        'Punched walls', 'Went quiet', 'Cried', 'Paced around the room', 'Headaches'])], 
              "disgust": [("What person do you feel disgust at?", "target"), 
                          ("What did that person do to make you feel disgust?", "reason"), 
                          ("Is there a reason why that person might have acted that way?", "peer-reflection"), 
                          ("Why do you think that person thought acting that way was okay? Did they act that way on purpose?", "self-evaluation"),
                          ("Do you think that reason makes it valid for that person to do that?", "evaluation", ["Yes"])],
              "fear": [("Why are you afraid/anxious?", "reason"),
                       ("How does this make you feel?", "feelings", ['helpless', 'alone', 'despair', 'insecure', 'overwhelmed']), 
                       ("What's the best-case scenario in this situation?", "best-case-scenario"),
                       ("What's the worst that could happen in this situation?", "worst-case-scenario"),
                       ("How can I prevent the worst to happen?", "prevention"),
                       ("If the worst does happen, what can I do to fix it?", "mitigation"),
                       ("Have you experienced any physical symptoms?", "symptoms", 
                       ["Increased heart rate", "Faster breathing or shortness of breath", "Butterflies or digestive changes"
                            "Sweating and chills", "Trembling muscles"])],
              "joy": [("Is there anything particular you are happy about?", "joy_reason"), 
                      ("Have you done any of the following?", "activites", ['Donated to charity', 'Spent time with loved ones', 'Exercised', 'Meditated', 'Journaled', 'Helped someone out', 'Went to work', 'Started a new hobby', 'Performed an old hobby'])], 
              "neutral": [("It can be good to reflect on this too. Maybe think about your day a little more and type how you feel", "reflection")],
              "sadness": [ ("Is there anything particular you are sad about?", "reason"), 
                          ("It's ok to feel sad when faced with a negative situation.\nHowever, it's also important to take a step back and focus on the positive things in life. \nTry writing one good thing that happened today", "good-thing"), 
                          ("What about something fun you did?", "fun-thing"), 
                          ("What is something that you accomplished today, no matter how small?", "accomplishment"), 
                          ("What can you be grateful for?", "gratitude")],
              "shame": [("Shame occurs when we fail to meet our own personal standards or others' expectations, what situation made you feel shame?", "reason"), 
                        ("What negative thoughts about yourself did this situation cause?", "negative-thoughts"),
                        ("What self-belief did this situation cause: feeling unloveable, or worthless, or not good enough, or bad\n, or stupid, or ugly, or abnormal, or boring, or worthless?" "self-beliefs"), 
                        ("Now that you've identified a feeling, name three pieces of evidence contrary to this belief", "contary-evidence")]} 

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


def log_session_data(emotion, response_text, curr_worksheet, output_file="session_log.json"):
    session_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "emotion": emotion,
        "response": response_text,
        "worksheet":curr_worksheet
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


# Load session data from JSON
def load_session_data(filename="session_log.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Trend analysis functions
def count_emotions(data):
    emotions = [entry["emotion"] for entry in data]
    return Counter(emotions)

def emotions_over_time(data):
    dates = [entry["date"] for entry in data]
    datewise_emotions = {}
    for date, emotion in zip(dates, [entry["emotion"] for entry in data]):
        if date not in datewise_emotions:
            datewise_emotions[date] = Counter()
        datewise_emotions[date][emotion] += 1
    return datewise_emotions

# Visualization functions
def plot_emotion_frequency(emotion_counts):
    plt.bar(emotion_counts.keys(), emotion_counts.values())
    plt.xlabel("Emotion")
    plt.ylabel("Frequency")
    plt.title("Frequency of Emotions")
    # plt.show()
    plt.savefig("emotion_frequency_plot.png") 


def plot_emotions_over_time(datewise_emotions):
    for emotion in datewise_emotions[next(iter(datewise_emotions))].keys():
        plt.plot(datewise_emotions.keys(), 
                 [datewise_emotions[date].get(emotion, 0) for date in datewise_emotions], label=emotion)
    plt.xlabel("Date")
    plt.ylabel("Frequency")
    plt.title("Emotion Trends Over Time")
    plt.legend()
    # plt.show()
    plt.savefig("emotion_over-time_plot.png") 


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
    data = load_session_data()

   
    emotion_counts = count_emotions(data)
    print("Emotion frequency:", emotion_counts)
    plot_emotion_frequency(emotion_counts)

    
    datewise_emotions = emotions_over_time(data)
    plot_emotions_over_time(datewise_emotions)