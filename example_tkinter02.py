from tkinter import Tk, Entry, Label, Button

def press():
    print("poulstar")


main = Tk()

main.geometry('320x240')

Label(main, text="Name : ").grid(row=0, column=0)
Entry(main).grid(row=0 , column=1)
Button(main, text="Click", command=press).grid(row=1, column=0)



main.mainloop()





