from tkinter import Tk, Button

#create window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

#Event Handler for Keypress
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
    