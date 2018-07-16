"""
This is a calculate written by python tkinter
"""
from tkinter import *

# set the window
root = Tk()
root.title('calculator')
root.geometry('300x210+300+300')     # the size of the window is 200x210, the position is (300, 300)


# set the display
display = StringVar()
display.set('0')
label_result = Label(root, bg='grey', width=28, height=3, anchor=SE, textvariable=display)
label_result.grid(row=0, column=0, columnspan=4)

# set clear button


def clear_all():
    display.set('0')


clear_button = Button(root, text='C', width=3, command=clear_all)
clear_button.grid(row=1, column=0)

# set back button


def back():
    display.set(str(display.get())[:-1])


back_button = Button(root, text='del', width=3, command=back)
back_button.grid(row=1, column=1)

# set other buttons


def updateDisplay(button_str):
    content = display.get()
    if content == '0':
        content = ''
    display.set(content + button_str)


Button(root, text = '/', width = 3, command = lambda:updateDisplay('/')).grid(row = 1, column = 2)
Button(root, text = '*', width = 3, command = lambda:updateDisplay('*')).grid(row = 1, column = 3)
Button(root, text = '7', width = 3, command = lambda:updateDisplay('7')).grid(row = 2, column = 0)
Button(root, text = '8', width = 3, command = lambda:updateDisplay('8')).grid(row = 2, column = 1)
Button(root, text = '9', width = 3, command = lambda:updateDisplay('9')).grid(row = 2, column = 2)
Button(root, text = '-', width = 3, command = lambda:updateDisplay('-')).grid(row = 2, column = 3)
Button(root, text = '4', width = 3, command = lambda:updateDisplay('4')).grid(row = 3, column = 0)
Button(root, text = '5', width = 3, command = lambda:updateDisplay('5')).grid(row = 3, column = 1)
Button(root, text = '6', width = 3, command = lambda:updateDisplay('6')).grid(row = 3, column = 2)
Button(root, text = '+', width = 3, command = lambda:updateDisplay('+')).grid(row = 3, column = 3)
Button(root, text = '1', width = 3, command = lambda:updateDisplay('1')).grid(row = 4, column = 0)
Button(root, text = '2', width = 3, command = lambda:updateDisplay('2')).grid(row = 4, column = 1)
Button(root, text = '3', width = 3, command = lambda:updateDisplay('3')).grid(row = 4, column = 2)
Button(root, text = '0', width = 10, command = lambda:updateDisplay('0')).grid(row = 5, column = 0, columnspan = 2)
Button(root, text = '.', width = 3, command = lambda:updateDisplay('.')).grid(row = 5, column = 2)

# set equal button


def equal():
    result = eval(display.get())
    display.set(display.get() + '=\n' + str(result))


Button(root, text = '=', width = 3, bg = 'orange', height = 3,command = lambda:equal()).grid(row = 4, column = 3, rowspan = 2)


# run
root.mainloop()



