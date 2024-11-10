import dearpygui.dearpygui as dpg
from backend import *
import warnings
warnings.filterwarnings("ignore")

# globals
#worksheet_steps = ["How are you feeling today?", "Step 2 Question", "Step 3 Question"] # need to add in these questions
curr_step = 0
emotion = "no_emote"
emote = "no_emote"
curr_worksheet = []

dpg.create_context()
#dpg.show_style_editor()


'''Other Helper Functions'''
#the following function is from thiis github discussion page: https://github.com/hoffstadt/DearPyGui/discussions/1072
def add_and_load_image(image_path, parent=None):
    width, height, channels, data = dpg.load_image(image_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    if parent is None:
        return dpg.add_image(texture_id, pos=[100, 320])
    else:
        return dpg.add_image(texture_id, pos=[100, 320], parent=parent)


def update_prompt(optional_text):
    if curr_step < len(worksheets[emote]):
        dpg.set_value("__prompt_text", value= optional_text + "\n" + worksheets[emote][curr_step])
    else:
        dpg.set_value("__prompt_text", value="Journal entry and worksheet complete for today. \nAll input is logged if you ever want to go back and check your progress")
        
        #display trend
        data = load_session_data()
        emotion_counts = count_emotions(data)
        plot_emotion_frequency(emotion_counts)
        add_and_load_image("emotion_frequency_plot.png", parent="journal")
       




'''The callback functions'''
def retrieve_text_callback():
    global curr_step
    global emote
    response_text = ""
    if curr_step == 0:
        input_text = dpg.get_value("__input_text") # may need to do processing of this input
        emot = predict_emotions(input_text)
        emote = emot
        response_text = respond_to_user(emot)
        #log_session_data(emot, response_text)
    else:
        curr_worksheet.append(dpg.get_value("__input_text"))

    if curr_step == len(worksheets[emote]) - 1:
        log_session_data(emote, response_text, curr_worksheet)
    #else: 
        #in the else scenario, its gonna be saving input to json file


    #print(input_text) # for debugging
    dpg.set_value("__input_text", value="")
    curr_step = curr_step + 1 # increment the step
    update_prompt(response_text)

def show_form_callback():
    #global emotion
    #response_text = ""
    global emotion
    input_text = dpg.get_value("__input_text") # may need to do processing of this input
    emotion = predict_emotions(input_text)
    dpg.delete_item("journal")
    if emotion == "surprise":
        create_surprise_window()
        dpg.show_item("surprise_form_window")
    else:
        create_form_window(emotion)
        dpg.show_item("form_window")

def submit_form(sender, app_data):
    responses = {}
    for question in worksheets[emotion]:
        if len(question) == 2:
            responses[question[1]] = dpg.get_value(question[1])
        else:
            completed = []
            for item in question[2]:
                if dpg.get_value(item):
                    completed.append(item)
            responses[question[1]] = completed
    log_session_data(emote, "", responses)

    dpg.delete_item("form_window")
    create_final_window()
    dpg.show_item("final_window")


def surprise_submit_callback(sender, app_data):
    emotion = dpg.get_value("response-emotion")
    dpg.delete_item("surprise_form_window")
    create_form_window(emotion)
    dpg.show_item("form_window")

'''The window and all the elements it contains'''
with dpg.window(label="journal.ai", tag = "journal"):
    dpg.add_text("Hi! Welcome to your wellness journal", pos = [175, 10])
    dpg.add_text("Hello, how are you feeling today?", pos = [100, 80], tag="__prompt_text")
    dpg.add_input_text(width = 400, pos = [100, 180], tag = "__input_text", multiline = True)
    dpg.add_button(label="Submit", pos = [275, 300], callback=show_form_callback)

def create_surprise_window():
    with dpg.window(label="Form", tag="surprise_form_window", width=1000, height=400, show=False, autosize=True):
        dpg.add_text("Our model has detected, you're surprised.", tag="model_pred") 
        dpg.add_text("How do you feel in response to this surprise?", tag="prompt_text1")
        dpg.add_radio_button(items=["joy", "anger", "fear", "neutral"], tag="response-emotion")
        dpg.add_button(label="Submit", callback=surprise_submit_callback) 

def create_form_window(emotion):
    with dpg.window(label="Form", tag="form_window", width=1000, height=400, show=False, autosize=True):
        print(emotion)
        dpg.add_text("Our model has detected the emotion you are feeling is " + emotion + ".", tag="model_pred") 
        dpg.add_text(responses[emotion] + "\n\n", tag = "response_text")
        
        for question in worksheets[emotion]:
            print(question)
            if len(question) == 2:
                dpg.add_text(question[0], tag = question[1] + "_prompt_text") 
                dpg.add_input_text(tag=question[1], default_value="", width=300, multiline = True)
            else:
                dpg.add_text(question[0], tag = question[1] + "_prompt_text")
                for item in question[2]:
                    dpg.add_checkbox(label=item, tag=item, default_value=False)

        dpg.add_button(label="Submit", callback=submit_form)

def create_final_window():
    with dpg.window(label="Form", tag="final_window", width=1000, height=400, show=False, autosize=True):
        dpg.add_text("Journal entry and worksheet complete for today. \nAll input is logged if you ever want to go back and check your progress", tag="end")

dpg.create_viewport(title='journal.ai', width=1000, height=720)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("journal", True)
dpg.start_dearpygui()
dpg.destroy_context()




