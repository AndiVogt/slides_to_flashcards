from localconfig import paths, prompt_templates
from pdf_reader import get_file_paths, get_slide_content
from utils.formatting import split_text_content, convert_to_gpt_prompts, group_slide_content
from excel_writer import generate_output
from utils.data_processing import copy_to_clipboard
from gui import MyGUI
import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title("Slides to Flashcards")
root.geometry("400x300")



# get all slide_paths in folder
file_paths = get_file_paths(paths["slides"])
print("file paths created")
# returns content of slides in text form 
slide_contents = get_slide_content(file_paths)
print("slide groups created") 
# groups slides in single list elements
slide_groups = group_slide_content(slide_contents)

# # creates gpt prompts
gpt_prompts = convert_to_gpt_prompts(slide_groups, prompt_templates)
print("created prompts")
# print(gpt_prompts)

app = MyGUI(master=root, callback=lambda text: copy_to_clipboard(text), nested_list=gpt_prompts)
# Add the GUI to the window
app.pack()
app.mainloop()

# processes the gpt response and writes everything to excel
generate_output(app.new_text_list)
