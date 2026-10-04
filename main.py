import tkinter as TK
import math


window = TK.Tk()
window.title("Python-GUI-Calculator")


window.resizable(False, False)
window.iconbitmap("thehalaldesign-math-6683827.ico")

entry = TK.Entry(window, width=9, font=("San Francisco", 38, "bold"), state="readonly")
entry.pack(pady=(30, 10))

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


def command(text):
    entry.config(state='normal')
    entry.insert(TK.END, text) 
    entry.config(state='readonly')



def buttons(text, frame):
    button = TK.Button(frame, text=text, font=("San Francisco", 20), image=pixel, bg="#202225", fg="white", compound="center",
                        command=lambda :command(text))
    return button
def buttons_ops(text, frame, bg, fg):
    button = TK.Button(frame, text=text,  font=("San Francisco", 20), image=pixel, bg=bg, fg=fg, activebackground=bg,
                        compound="center", command=lambda:command(text))
    return button

pi = buttons_ops('π', frame1, "#616161", "white").pack()
btn1 = buttons('1', frame1).pack()
btn4 = buttons('4', frame1).pack()
btn7 = buttons('7', frame1).pack()

btnx2 = buttons_ops('x²', frame2, "#616161", "white").pack()
btn2 = buttons('2', frame2).pack()
btn5 = buttons('5', frame2).pack()
btn8 = buttons('8', frame2).pack()


btn0 = buttons_ops('0', frame2, '#202225255', 'white').pack()


btnx3 = buttons_ops('x³', frame3, "#616161", "white").pack()
btnsr= buttons_ops('√', frame4, "#616161", "white").pack()
plus = buttons_ops('+', frame4, "#ff9006", 'white').pack()
minus= buttons_ops('-', frame4,  "#ff9006", 'white').pack()
mul = buttons_ops('x', frame4, "#ff9006", 'white').pack()
div = buttons_ops('/', frame4, "#ff9006", 'white').pack()

btn3 = buttons('3', frame3).pack()
btn6 = buttons('6', frame3).pack()
btn9 = buttons('9', frame3).pack()



window.mainloop()