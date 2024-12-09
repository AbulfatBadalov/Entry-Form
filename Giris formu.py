import tkinter as tk
view=tk.Tk()

view.geometry("400x200")

view.title("Giris Formu")

ad="Abulfat"
kod=12345

x=tk.StringVar()

user=tk.Label(text="Username girin: ")
user.place(x=20,y=30)

password=tk.Label(text="Password girin: ")
password.place(x=20,y=50)

user_entry=tk.Entry()
user_entry.place(x=106,y=30)

password_entry=tk.Entry()
password_entry.place(x=106,y=50)

answer=tk.Label(text="",font="Vardana,5")
answer.place(x=70,y=120)

def submitbut():
    adi=x.get()
    kodu=x.get()
    if adi!="" or kodu!="":
        if adi==ad and kod==kodu:
            answer.config(text="Dogrudur",fg="green")
        else:
            answer.config(text="Yanlisdir",fg="Red")
    else:
        answer.config(text="Zehmet olmasa boslugu doldurun.")

submit=tk.Button(text="Submit",command=submitbut)
submit.place(x=181,y=70)






view.mainloop()