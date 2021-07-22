from tkinter import Button, Label, Tk, IntVar

number = 0

def press(oprator):
    if oprator == "+":
        number = sv_number.get()
        number += 1
        sv_number.set(number)

    elif oprator == "-":
        number = sv_number.get()
        number -= 1
        sv_number.set(number)
        

main = Tk()
main.geometry('329x240')

Button(main, text="+", command=lambda :press("+")).pack()
sv_number = IntVar()
Label(main, textvariable=sv_number).pack()
Button(main, text="-", command=lambda :press("-")).pack()

main.mainloop()