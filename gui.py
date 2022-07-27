import os
import tkinter as tk

root = tk.Tk()
root.geometry('1280x720')
root.configure(bg='#856ff8')
root.title('FACIAL DETECTION IN A MULTIMODAL BACKGROUND FOR REAL-TIME IMAGES')
svalue = tk.StringVar()  # defines the widget state as string

message = tk.Label(root, text="FACIAL DETECTION IN A MULTIMODAL BACKGROUND FOR REAL-TIME IMAGES", bg="#80BFFF", fg="black", width=100,
                   height=5, font=('times', 20, 'italic bold '))
message.pack(padx=10, pady=10)

l = tk.Label(root, text="Add new person", bg="#CDF0EA")
l.config(font=("Courier", 30))
l.pack(padx=10, pady=10)

w = tk.Entry(root, textvariable=svalue, width=20, fg="red",
             font=('times', 20))  # adds a textarea widget
w.pack(padx=10, pady=10)


def train_fisher_btn_load():
    name = svalue.get()
    os.system('python train_fisher.py %s' % name)


def recog_fisher_btn_load():
    os.system('python recog_fisher.py')


def add_person():
    name = svalue.get()
    os.system('python add_person.py %s' % name)


add_btn = tk.Button(root, text="Add Person", command=add_person, fg="black", bg="#BDF2D5",
                    width=10, height=1, borderwidth=20, activebackground="Red", font=('times', 20, 'italic bold '))
add_btn.pack(padx=10, pady=10)

f = tk.Frame(root, height=2, width=400, bg="black")
f.pack(padx=10, pady=10)


l = tk.Label(root, text="Train", bg="#CDF0EA")
l.config(font=("Courier", 30))
l.pack(padx=10, pady=10)

trainF_btn = tk.Button(root, text="Train Model", command=train_fisher_btn_load, fg="black", bg="#BDF2D5",
                       width=10, height=1, borderwidth=20, activebackground="Red", font=('times', 20, 'italic bold '))
trainF_btn.pack(padx=10, pady=10)

f = tk.Frame(root, height=1, width=400, bg="black")
f.pack(padx=10, pady=10)

l = tk.Label(root, text="Recognize", bg="#CDF0EA")
l.config(font=("Courier", 30))
l.pack(padx=10, pady=10)

recogF_btn = tk.Button(root, text="Recognize", command=recog_fisher_btn_load, fg="black", bg="#BDF2D5",
                       width=10, height=1, borderwidth=20, activebackground="Red", font=('times', 20, 'italic bold '))
recogF_btn.pack(padx=10, pady=10)


root.mainloop()
