from tkinter import Tk, Entry, Label, Button

def press():
    print("code meli sahih ast")


main = Tk()

main.geometry('320x240')

Label(main, text="code meli : ").pack()
Entry(main, bg="#B8FF00").pack()
Button(main, text="barresi", command=press, bg="#000000").pack()



main.mainloop()