from tkinter import * 
from PIL import ImageTk, Image # This is used to get the picture
from playsound import playsound

root = Tk()

# Change tkinter icon
icon = 'med.ico'
root.iconbitmap(icon)
root.title("Random Buttons")
counter = 0

def count():
    global counter
    counter +=1
    l['text'] = f'Surprise! You have clicked the button {counter} times'
    return counter

def close():
    exit()
    # Will exit the program

def saySomething():
    print("Hey look at me!")

def makeNoise():
    playsound("livin.mp3") # this plays bon jovi
    
def makePicture():
    c = Canvas(root, width = 10, height=20)
    picture = ImageTK.PhotoImage(Image.open())


b4Image = ImageTk.PhotoImage(Image.open('C:/Users/eatin/OneDrive/Documents/Python/Personal Studies/GUI/Cow.jpg'))
b1 = Button(text = 'I bet you will not click me!', command = count)
b2 = Button(text = 'Exit Program', command = exit)
b3 = Button(text = 'I will say something', command = saySomething)
b4 = Button(text = 'I make noise', command = makeNoise, image = b4Image)
b5 = Button(text = 'I make a picture!', command = makePicture)
b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 1, column = 0)
b4.grid(row = 1, column = 1)

l = Label(text = 'Just a label')
l.grid(row = 2, column = 1)

################### Adding an image to the app ############################
# We put the image on a canvas first
can = Canvas(root, width = 200, height = 200)
img = ImageTk.PhotoImage(Image.open("puppy.png"))

can.create_image(20,20,anchor = NW, image = img)

root.mainloop()