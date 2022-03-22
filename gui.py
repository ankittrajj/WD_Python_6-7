# tkinter

from tkinter import *
window = Tk()
window.title("myfirstApp")

#function
def click():
    enter_text = textbox.get()
    output.delete(0.0,END)

#     exceptional handling
    try:
        define = my_dict[enter_text]
    except:
        define = 'not available'
    output.insert(END,define)


Label(window,text='Hello i am new to GUI',bg='red').grid(row=0,column=0,sticky=W)

# textbox
textbox = Entry(window,width=10,bg='white').grid(row=1,column=0,sticky=W)

#submit button
Button(window,text='Submit',command = click,bg='blue',fg='white').grid(row=2,column=0,sticky=W)

# Label
Label(window,text='Defination',bg='red').grid(row=3,column=0,sticky=W)

# text box
output = Text(window,width=30,height=40,bg='white').grid(row=4,column=0,sticky=W)

# dict
my_dict={
    'animal':'dog',
    'bug':'error in code'
}


window.mainloop()

