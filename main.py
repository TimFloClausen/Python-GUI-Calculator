import tkinter as TK
import math


window = TK.Tk()
window.title("Python-GUI-Calculator")

window.geometry("400x550+660+340")
window.resizable(False, False)
window.iconbitmap("thehalaldesign-math-6683827.ico")

frame1 = TK.Frame(window)
frame1.pack(side='left', anchor='n')
frame2 = TK.Frame(window)
frame2.pack(side='left', anchor='n')
frame3 = TK.Frame(window)
frame3.pack(side='left', anchor='n')
frame4 = TK.Frame(window)
frame4.pack(side='left', anchor='n')
frame5 = TK.Frame(window)
frame5.pack(side='left', anchor='n')

pixel = TK.PhotoImage(width=55, height=55)


def buttons(text, frame):
    button = TK.Button(frame, text=text, font=("San Francisc", 20), image=pixel, bg="#202225255", fg="white", compound="center")
    return button
def buttons_ops(text, frame, bg, fg):
    button = TK.Button(frame, text=tetx,  font=("San Francisc", 20), image=pixel, bg=bg, fg=fg, activebackground="black",
                       compound="center")
    return button

btn1 = buttons('1',frame1).pack()
btn4 = buttons('4', frame1).pack()
btn7 = buttons('7', frame1).pack()


window.mainloop()