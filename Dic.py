from tkinter import Tk, PhotoImage, Label, Entry, Button, Text, END
from difflib import get_close_matches
from tkinter import messagebox

import json
import pyttsx3

engine = pyttsx3.init()  # creating instance of engine class

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# functionality Part

def search():
    data = json.load(open('data.json'))
    word = enterWorldEntry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        textArea.delete(1.0, END)
        for item in meaning:
            textArea.insert(END, u'\u2022' + item + '\n\n')

    elif len(get_close_matches(word, data.keys())) > 0:
        closeMatch = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno(f'confirm', f'Did you mean {closeMatch} instead?')
        if res:
            enterWorldEntry.delete(0, END)
            enterWorldEntry.insert(END, str(closeMatch))
            meaning = data[closeMatch]
            textArea.delete(1.0, END)
            for item in meaning:
                textArea.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error', 'The word doesnt exist, please double '
                                          'check it')
            enterWorldEntry.delete(0, END)
            textArea.delete(1.0, END)

        # GUI


def clear():
    enterWorldEntry.delete(0, END)
    textArea.delete(1.0, END)


def exit():
    res = messagebox.askyesno('Confirm', 'Do you want exit')
    if res:
        window.destroy()
    else:
        pass


def wordaudio():
    engine.say(enterWorldEntry.get())
    engine.runAndWait()


def meaningaudio():
    engine.say(textArea.get(1.0, END))
    engine.runAndWait()


window = Tk()

window.geometry('1000x624+100+30')
window.title('Talking dictionary made by Nasir')
window.resizable(False, False)
BackgroundImage = PhotoImage(file='talkauido.png')
backgroundLabel = Label(window, image=BackgroundImage)
backgroundLabel.place(x=0, y=0)

enterWorldLabel = Label(window, background='whitesmoke', text='Enter Word', font=('casteller', 15, 'bold',
                                                                                  ), foreground='red3')
enterWorldLabel.place(x=530, y=30)

enterWorldEntry = Entry(window, font=('arial', 23, 'bold'), justify='center', bd=8, relief='raised')
enterWorldEntry.place(x=510, y=80)

searchImage = PhotoImage(file='searchicon.png')
# resizedImage = searchImage.subsample(2, 2)

searchButton = Button(window, image=searchImage, bd=0, background='whitesmoke', cursor='hand2',
                      activebackground='whitesmoke', command=search)

searchButton.place(x=620, y=150)

microphoneImage = PhotoImage(file='mic.png')
# resizedMicrophone = microphoneImage.subsample(2, 2)
microphoneButton = Button(window, image=microphoneImage, bd=0, background='whitesmoke',
                          cursor='hand2', command=wordaudio)
microphoneButton.place(x=720, y=153)

meaningLabel = Label(window, text='MEANING', font=('casteller', 29, 'bold',
                                                   ), fg='red3')
meaningLabel.place(x=580, y=240)

textArea = Text(window, width=34, height=8, font=('arial', 16, 'bold'))
textArea.place(x=460, y=300)

# audio image Button

audioImage = PhotoImage(file='microphone.png')
audioImageButton = Button(window, image=audioImage, bd=0,
                          highlightbackground='whitesmoke', activebackground='whitesmoke',
                          cursor='hand2', command=meaningaudio)
audioImageButton.place(x=550, y=510)

# clear audio Button
clearImage = PhotoImage(file='clear.png')
clearImageButton = Button(window, image=clearImage, bd=0,
                          highlightbackground='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                          command=clear)
clearImageButton.place(x=650, y=510)

# exit button
exitImage = PhotoImage(file='exitbottom.png')
exitButton = Button(window, image=exitImage, bd=0,
                    highlightbackground='whitesmoke', activebackground='whitesmoke',
                    cursor='hand2', command=exit)
exitButton.place(x=750, y=510)


def enter_function(event):
    searchButton.invoke()


window.bind('<Return>', enter_function)

window.mainloop()
