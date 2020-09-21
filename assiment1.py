 from tkinter import * 
import webbrowser

# defining the fucntion to open and create a new tab with the users input
def new_Tab():
    f = open('index.html', 'w')
    userEntry = T.get()
    Html =  "<html><head></head><body><h1>"+ userEntry+"</h1></body</html>"
    f.write(Html)
    f.close()
    webbrowser.open_new_tab('index.html')

win = Tk()
text = StringVar()

win.geometry('220x220')
# label and inpout box for user 
L = Label(win,text="Enter you heading bellow")
L.pack()
T = Entry(win,textvariable=text)
T.pack() 
# define our button and configure it to open our function new_Tab
b1 = Button(win, text="open broswer")
b1.pack()
b1.configure(command=new_Tab)




