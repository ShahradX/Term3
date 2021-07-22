from tkinter import Tk, Entry, Label, Button

def press():
    print("poulstar")


main = Tk()

main.geometry('320x240')

Label(main, text="Name : ").pack()
Entry(main, bg="#0288D1").pack()
Button(main, text="Click", command=press, bg="#689F38").pack()



main.mainloop()