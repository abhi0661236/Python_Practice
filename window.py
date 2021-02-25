from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("TODO")
# We can set the default window size using geometry function like this.
window.geometry('500x400') # sets the width to 500px and the height to 400px.

# Note that the font parameter can be passed to any widget to change its font not labels only.
lbl = Label(window, text="Make a list of your Works", font = ("Arial Bold", 12))
lbl.grid(column=0, row=0)

# Now lets write the click event for the button.
# First, we will write the function that we need to execute when the button is clicked.
def clicked():
    res = txt.get()
    finalRes = combo.get() + " " + res
    lbl.configure(text=finalRes)

# We can add buttons with Button module
# Now we will wire it with the button by specifying the function like this:


btn = Button(window, text="Click Me", command=clicked)
# You can change background with bg and foreground with fg
btn.grid(column=2, row=1)




"""
    let's try getting the user input using the Tkinter Entry class (Tkinter textbox).
"""
# you can set the entry box disabled using state="disabled"
txt = Entry(window, width=10)
txt.grid(column=2, row=1)

# you can get entered text in entry textbox using get function.
# please scroll up to the clicked() function

# set focus to entry widget.
txt.focus()

"""
    To add a combobox widget, you can use the Combobox class from ttk library like this:
    from tkinter.ttk import *
"""

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"Text") # we add values in combobox using a tuple.
combo.current(1) # set the selected item

combo.grid(column=2, row=2) # Never forget to use grid function to display a widget.




window.mainloop()