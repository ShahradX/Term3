from tkinter import StringVar, Tk, Entry, Label, Button

def press():
    var_name = sv_name.get()
    sv_out.set(var_name)


main = Tk()

main.geometry('320x240')

sv_out = StringVar()
Label(main, textvariable=sv_out).pack()

sv_name = StringVar()
Entry(main, bg="#0288D1", textvariable=sv_name).pack()
Button(main, text="Click", command=press, bg="#689F38").pack()



main.mainloop()