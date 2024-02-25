from tkinter import *

def evaluate():
    exp=display.get(1.0, END)
    res=eval(exp)
    display.delete(1.0, END)
    display.insert(END,res)
def clear_all():
    display.delete(1.0, END)
def clear():
    display.delete("end-2c",END)
def enter_1():
    display.insert(END,"1")
def enter_2():
    display.insert(END,"2")
def enter_3():
    display.insert(END,"3")
def enter_4():
    display.insert(END,"4")
def enter_5():
    display.insert(END,"5")
def enter_6():
    display.insert(END,"6")
def enter_7():
    display.insert(END,"7")
def enter_8():
    display.insert(END,"8")
def enter_9():
    display.insert(END,"9")
def enter_0():
    display.insert(END,"0")
def enter_00():
    display.insert(END,"00")
def enter_plus():
    display.insert(END,"+")
def enter_minus():
    display.insert(END,"-")
def enter_div():
    display.insert(END,"/")
def enter_mul():
    display.insert(END,"*")
def enter_dec():
    display.insert(END,".")

calc = Tk()
calc.title("Calculator by CodSoft")
calc.configure(bg="white")

calc_frame = Frame(calc, width=300, height=600, bg="black")
calc_frame.pack(side=TOP)

display = Text(calc_frame, width=30, height=5, bg="white", fg="black",font=("Courier New", 18))
display.pack(side=TOP)

calc_frame1 = Frame(calc_frame, width=300, height=100, bg="black")
calc_frame1.pack(side=TOP)

btnc = Button(calc_frame1, text="AC", bg="black", fg='black', command=lambda:clear_all(), width=3)
btnc.pack(side=LEFT)
btnd = Button(calc_frame1, text="DEL", bg="black", fg='black', command=lambda:clear(),width=3)
btnd.pack(side=LEFT)
btndiv = Button(calc_frame1, text="/", bg="black", fg='black', command=lambda:enter_div(),width=3)
btndiv.pack(side=LEFT)
btndec = Button(calc_frame1, text=".", bg="black", fg='black', command=lambda:enter_dec(),width=3)
btndec.pack(side=LEFT)

calc_frame2 = Frame(calc_frame, width=300, height=100, bg="black")
calc_frame2.pack(side=TOP)

btn7 = Button(calc_frame2, text="7", bg="black", fg='black', command=lambda:enter_7(),width=3)
btn7.pack(side=LEFT)
btn8 = Button(calc_frame2, text="8", bg="black", fg='black', command=lambda:enter_8(),width=3)
btn8.pack(side=LEFT)
btn9 = Button(calc_frame2, text="9", bg="black", fg='black', command=lambda:enter_9(),width=3)
btn9.pack(side=LEFT)
btnmul = Button(calc_frame2, text="*", bg="black", fg='black', command=lambda:enter_mul(),width=3)
btnmul.pack(side=LEFT)

calc_frame3 = Frame(calc_frame, width=300, height=100, bg="black")
calc_frame3.pack(side=TOP)

btn4 = Button(calc_frame3, text="4", bg="black", fg='black', command=lambda:enter_4(),width=3)
btn4.pack(side=LEFT)
btn5 = Button(calc_frame3, text="5", bg="black", fg='black', command=lambda:enter_5(),width=3)
btn5.pack(side=LEFT)
btn6 = Button(calc_frame3, text="6", bg="black", fg='black', command=lambda:enter_6(),width=3)
btn6.pack(side=LEFT)
btnplu = Button(calc_frame3, text="+", bg="black", fg='black', command=lambda:enter_plus(),width=3)
btnplu.pack(side=LEFT)

calc_frame4 = Frame(calc_frame, width=300, height=100, bg="black")
calc_frame4.pack(side=TOP)


btn1 = Button(calc_frame4, text="1", bg="black", fg='black', command=lambda:enter_1(),width=3)
btn1.pack(side=LEFT)
btn2 = Button(calc_frame4, text="2", bg="black", fg='black', command=lambda:enter_2(),width=3)
btn2.pack(side=LEFT)
btn3 = Button(calc_frame4, text="3", bg="black", fg='black', command=lambda:enter_3(),width=3)
btn3.pack(side=LEFT)
btnmin = Button(calc_frame4, text="-", bg="black", fg='black', command=lambda:enter_minus(),width=3)
btnmin.pack(side=LEFT)

calc_frame5 = Frame(calc_frame, width=300, height=100, bg="black")
calc_frame5.pack(side=TOP)

btn0 = Button(calc_frame5, text="0", bg="black", fg='black', command=lambda:enter_0(),width=3)
btn0.pack(side=LEFT)
btn00 = Button(calc_frame5, text="00", bg="black", fg='black', command=lambda:enter_00(),width=3)
btn00.pack(side=LEFT)
btnres = Button(calc_frame5, text="=", bg="black", fg='black', command=lambda:evaluate(),width=10)
btnres.pack(side=LEFT)


calc.mainloop()
