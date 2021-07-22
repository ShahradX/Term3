from tkinter import Tk, Button

def my_button(click):
    if click == "2":
        print("2")
    elif click == "3":
        print("3")
    elif click == "4":
        print("4")


main = Tk()
main.geometry("320x240")


Button(main, text="Click 1", command=lambda :my_button("2")).pack()
Button(main, text="Click 2", command=lambda :my_button("3")).pack()
Button(main, text="Click 3", command=lambda :my_button("4")).pack()

main.mainloop()