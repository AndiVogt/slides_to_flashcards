import pyperclip

def copy_to_clipboard(text):
    if not isinstance(text, str):
        text = str(text)
    pyperclip.copy(text)
