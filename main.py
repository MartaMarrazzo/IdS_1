from tkinter import *

from PIL import ImageTk, Image

root = Tk()
my_frame = LabelFrame(root, text="Have a look & book your holiday!", padx= 60, pady= 15 )
login_frame = LabelFrame(root, text="Log-in", padx=60, pady=100)
root.iconbitmap('C:/Users/marra/Desktop/pythonProject/firstexercise')


#indico una per una le immagini da mostrare sulla home
my_Image1 = ImageTk.PhotoImage(Image.open("im1.jpg"))
my_Image2 = ImageTk.PhotoImage(Image.open("im4.jpg"))
my_Image3 = ImageTk.PhotoImage(Image.open("im2.jpg"))
my_Image4 = ImageTk.PhotoImage(Image.open("im5.jpg"))
my_Image5 = ImageTk.PhotoImage(Image.open("im3.jpg"))


#riempio una lista con le immagini scelte
list_Images = [my_Image1, my_Image2, my_Image3, my_Image4, my_Image5]

status = Label(my_frame, text="Image 1 of " + str(len(list_Images)), bd=1, relief=SUNKEN)
status.grid(row=2, column=0 , columnspan=3, sticky=W + E)

my_label = Label(image=my_Image1)
my_label.grid(row=0, column=0, columnspan=3)

variable = StringVar(login_frame)
variable.set("Select")

w=OptionMenu(login_frame, variable, "Owner","Client","Worker")
w.grid(row=0, column=1)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = Label(image=list_Images[image_number-1])
    button_forward = Button(my_frame, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(my_frame, text="<<", command=lambda: back(image_number-1))

    if image_number==5:
        button_forward=Button(my_frame, text=">>", state=DISABLED)

    status = Label(my_frame, text="Image " +str(image_number) + " of " + str(len(list_Images)))
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)



    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = Label(image=list_Images[image_number - 1])
    button_forward = Button(my_frame, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(my_frame, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(my_frame, text="<<", state=DISABLED)


    status = Label(my_frame, text="Image " +str(image_number) + " of " + str(len(list_Images)))
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(my_frame, text="<<", command=back, state=DISABLED)
button_exit = Button(my_frame, text="exit", command=root.quit)
button_forward = Button(my_frame, text=">>", command=lambda: forward(2))


label_name = Label(login_frame, text="Enter your name:" )
label_password= Label(login_frame, text= "Enter your password: ")
label_iam= Label(login_frame, text=" I am...")
name = Entry(login_frame, width=50)
name.grid(row=1, column=1)
password = Entry(login_frame, width=50)
password.grid(row=2, column=1)
label_iam.grid(row=0, column=0)

def check():
    L_name = Label(login_frame, name.get(), password.get())
    L_name.grid(row=1, column=2)




button_name = Button(login_frame, text = "Log-in", command = check)
button_name.grid(row=3, column=1)


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
my_frame.grid(row=2, column=0, columnspan=1, sticky=W+E)
login_frame.grid(row=0, column=3, columnspan=1)
label_name.grid(row=1, column=0)
label_password.grid(row=2, column=0)

root.mainloop()
