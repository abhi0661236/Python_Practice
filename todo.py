from tkinter import *

window = Tk()
# setting the title for the window
window.title("TO DO")
window.geometry("350x400") # sets the default size for window

greet = Label(text="Make the Goals for the day", font = ("Arial Bold", 12))
greet.grid(column=1,row=1)

window.mainloop()