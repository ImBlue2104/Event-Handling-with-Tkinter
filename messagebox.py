from tkinter import Tk, Button, messagebox

#Setup Window
root = Tk()
root.title("Virus Checker")
root.geometry("200x200")

#Function for Displaying Warning Message
#Called once button clicked
def msg():
    messagebox.showwarning("Virus Alert", "Virus Found")

#Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=50)

#Entering main evet loop
root.mainloop()