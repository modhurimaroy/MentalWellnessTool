import dearpygui.dearpygui as dpg
from backend import *
import warnings
warnings.filterwarnings("ignore")

# globals
#worksheet_steps = ["How are you feeling today?", "Step 2 Question", "Step 3 Question"] # need to add in these questions
curr_step = 0
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





'''The window and all the elements it contains'''
with dpg.window(label="journal.ai", tag = "journal"):
    dpg.add_text("Hi! Welcome to your wellness journal", pos = [175, 10])
    dpg.add_text(worksheets[emote][0], pos = [100, 80], tag="__prompt_text")
    dpg.add_input_text(width = 400, pos = [100, 180], tag = "__input_text", multiline = True)
    dpg.add_button(label="Submit", pos = [275, 300], callback=retrieve_text_callback)




dpg.create_viewport(title='journal.ai', width=1000, height=720)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("journal", True)
dpg.start_dearpygui()
dpg.destroy_context()




