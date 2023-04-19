from utils.data_processing import copy_to_clipboard
import tkinter as tk
import tkinter.ttk as ttk

class MyGUI(tk.Frame):
    def __init__(self, master=None, nested_list=None, callback=None):
        super().__init__(master)

        if nested_list is None:
            raise ValueError("nested_list cannot be None")
        self.nested_list = nested_list
        self.current_list = 0
        self.new_text_list = list()
        self.current_element = 0
        self.callback = callback

        #style
        style = ttk.Style()
        style.theme_use("alt")

        
        # create widgets using grid layout
        self.list_label = tk.Label(self, text=f"List {self.current_list+1}/{len(self.nested_list)}", 
                                   background="grey", 
                                   foreground="white")
        self.element_label = tk.Label(self, text=f"Element {self.current_element+1}/{len(self.nested_list[self.current_list])}")
        self.copy_button = tk.Button(self, text="Kopieren", command=self.copy_element)
        
        # place widgets in the window using grid layout
        self.list_label.grid(row=0, column=0, padx=10, pady=10)
        self.element_label.grid(row=1, column=0, padx=10, pady=10)
        self.copy_button.grid(row=2, column=0, padx=10, pady=10)

        
    def copy_element(self):
        current_element = self.nested_list[self.current_list][self.current_element]
        copy_to_clipboard(current_element)
        self.next_element()

    def next_element(self):
        if self.current_element == len(self.nested_list[self.current_list]) - 1:
            input_label = tk.Label(self, text="Enter text:")
            self.input_field = tk.Entry(self)
            save_button = tk.Button(self, text="Okay", command=self.save_text)
            input_label.grid(row=3, column=0, padx=10, pady=10)
            self.input_field.grid(row=4, column=0, padx=10, pady=10)
            save_button.grid(row=5, column=0, padx=10, pady=10)
            self.copy_button.config(state="disabled")
        else:
            self.current_element += 1
            self.update_labels()
        if self.current_element == 0 and self.current_list < len(self.nested_list) - 1:
            self.current_list += 1
            self.update_labels()
            self.current_element = 0


    def update_labels(self):
        self.list_label.config(text=f"List {self.current_list+1}/{len(self.nested_list)}")
        self.element_label.config(text=f"Element {self.current_element+1}/{len(self.nested_list[self.current_list])}")

    def save_text(self):
        new_text = self.input_field.get() # retrieve text from Entry widget
        self.new_text_list.append(new_text+"\n") # add text to new_text_list
        self.copy_button.config(state="normal") # enable the copy button

        # check if the main window still exists before accessing or destroying any widgets
        if self.master and self.master.winfo_exists():

            # check if we have reached the end of the current list
            if self.current_element == len(self.nested_list[self.current_list]) - 1:
                print("end of list")
                # check if we have reached the end of the nested list
                if self.current_list == len(self.nested_list) - 1:
                    # we have reached the end of the nested list, so call the callback function with the new text list
                    if self.callback:
                        self.callback(self.new_text_list)
                    # close the GUI
                    self.master.destroy()
                else:
                    # move to the next list
                    self.current_list += 1
                    self.current_element = 0
                    self.update_labels()
            else:
                # move to the next element in the current list
                self.current_element += 1
                self.update_labels()

            try:
                # remove the input field and okay button
                if hasattr(self, 'input_field') and self.input_field.winfo_exists():
                    self.input_field.destroy()
                if hasattr(self, 'okay_button') and self.okay_button.winfo_exists():
                    self.okay_button.destroy()
                self.master.focus_set()
            except:
                print("Program finished")
                return self.new_text_list