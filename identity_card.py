from tkinter import*
root = Tk()

root.title("driving licence")
root.geometry("300x400")

root.configure(bg="white")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="driving licence")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Name :")
label_pin_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="pin :")
label_date of birth _tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="date of birth :")

#add label for name
label1_name = Label(root)
#add label for grade
label1_pin = Label(root)
#add label for Subjects
label1_date of birth  = Label(root)

#add function
def myCardDetails():
    name = "Krishna"
    print(type(name))
    pin = 451478
    print(type(grade))
    date of birth = 21 agust 1921
    print(type(subjects))

    label1_name["text"] = name
    label1_grade["text"] = pin
    label1_subjects["text"] = date of birth 


#add button
button1 = Button(root,text="show my ID card",command=myCardDetails)

button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label1_name)
label_pin_window = canvas.create_window(90, 205, anchor=CENTER, window=label1_pin)
label_date of birth _window = canvas.create_window(155, 252, anchor=CENTER, window=label1_date of birth )
canvas.pack()

root.mainloop()

