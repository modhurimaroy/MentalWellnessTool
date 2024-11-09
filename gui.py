import dearpygui.dearpygui as dpg

# globals
worksheet_steps = ["How are you feeling today?", "Step 2 Question", "Step 3 Question"]
curr_step = 0



dpg.create_context()
#dpg.show_style_editor()


'''Other Helper Functions'''
def update_prompt():
    if curr_step < len(worksheet_steps):
        dpg.set_value("__prompt_text", value=worksheet_steps[curr_step])
    else:
        dpg.set_value("__prompt_text", value="Journal entry and worksheet complete for today. \nAll input is logged if you ever want to go back and check your progress")



'''The callback functions'''
def retrieve_text_callback():
    global curr_step
    input_text = dpg.get_value("__input_text") # may need to do processing of this input
    #print(input_text) # for debugging
    dpg.set_value("__input_text", value="")
    curr_step = curr_step + 1 # increment the step
    update_prompt()





'''The window and all the elements it contains'''
with dpg.window(label="journal.ai", tag = "journal"):
    dpg.add_text("Hi! Welcome to your wellness journal", pos = [175, 10])
    dpg.add_text(worksheet_steps[0], pos = [100, 140], tag="__prompt_text")
    dpg.add_input_text(width = 400, pos = [100, 180], tag = "__input_text", multiline = True)
    dpg.add_button(label="Submit", pos = [275, 300], callback=retrieve_text_callback)




dpg.create_viewport(title='journal.ai', width=640, height=480)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("journal", True)
dpg.start_dearpygui()
dpg.destroy_context()




