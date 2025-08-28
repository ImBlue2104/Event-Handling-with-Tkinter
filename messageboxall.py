from tkinter import Tk, Button, messagebox

root = Tk()
root.title("Message box testing")
root.geometry("500x500")

def popup():
    messagebox.showinfo("New Info" , "New Tv Show Releases Soon!")
    messagebox.showerror("Error!", "Check Code and Fix!")
    messagebox.askquestion("Question!!", "What is your age?")

Button(text="Click Me to see popups!", fg="white", bg="black", cmd = popup).pack()

root.mainloop()
