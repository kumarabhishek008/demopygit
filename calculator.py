from tkinter import *
from tkinter import ttk


calculator = Tk()
calculator.geometry("310x300")
calculator.title("CALCULATOR")
calculator.resizable(TRUE,TRUE)
cal_value = StringVar()
cal_value.set("")
cal_box = Entry(calculator,width =25 ,bg = 'white',textvariable = cal_value,font="lucida 15 bold")
cal_box.clipboard_append(cal_value)
cal_box.grid(row=0,column =0,padx = 15,pady = 10)

def button1():
    global cal_value
    text = "1"
    cal_value.set(cal_value.get() + text)

    print("1")
def button2():
    global cal_value
    text = '2'
    cal_value.set(cal_value.get() + text)


def button3():
    global cal_value
    text = '3'
    cal_value.set(cal_value.get() + text)


def button4():
    global cal_value
    text = '4'
    cal_value.set(cal_value.get() + text)

    print("4")
def button5():
    global cal_value
    text = '5'
    cal_value.set(cal_value.get() + text)

def button6():
    global cal_value
    text = '6'
    cal_value.set(cal_value.get() + text)

def button7():
    global cal_value
    text = '7'
    cal_value.set(cal_value.get() + text)

def button8():
    global cal_value
    text = '8'
    cal_value.set(cal_value.get() + text)

def button9():
    global cal_value
    text = '9'
    cal_value.set(cal_value.get() + text)

def button0():
    global cal_value
    text = '0'
    cal_value.set(cal_value.get() + text)

def button_plus():
    global cal_value
    text = '+'
    cal_value.set(cal_value.get() + text)
    cal_box.update()

def button_minus():
    global cal_value
    text = '-'
    cal_value.set(cal_value.get() + text)
    cal_box.update()
def button_mul():
    global cal_value
    text = '*'
    cal_value.set(cal_value.get() + text)

def button_div():
    global cal_value
    text = '/'
    cal_value.set(cal_value.get() + text)

def button_dot():
    global cal_value
    cal_value.set(".")

def button_equal():
    global result
    if cal_value.get().isdigit():
        value = int(cal_value.get())

    else:
        try:
            value = eval(cal_box.get())
        except:
            value = "wrong expression"
    cal_value.set(value)

def _cancel():
    cal_value.set("")
    cal_box.update()
jframe = Frame(calculator)
num1 = Button(jframe,text = 1,bg = "orange",width = 5,height = 2,command = button1)

num2 = Button(jframe,text = 2,bg = 'orange',width = 5,height = 2,command = button2)
num3 = Button(jframe,text = 3,bg = 'orange',width = 5,height = 2,command = button3)
num_plus = Button(jframe, text = '+', bg = 'orange',width = 5, height = 2,command = button_plus)
jframe.grid(row = 2 ,column = 0)
jframe1= Frame(calculator)
num4 = Button(jframe1,text = 4,bg = "orange",width = 5,height = 2,command = button4)
num5 = Button(jframe1,text = 5,bg = 'orange',width = 5,height = 2,command = button5)
num6 = Button(jframe1,text = 6,bg = 'orange',width = 5,height = 2,command = button6)
num_minus = Button(jframe1, text = '-', bg = 'orange',width = 5, height = 2,command = button_minus)
jframe1.grid(row = 3,column = 0,padx = 5,pady = 5)
jframe2 = Frame(calculator)
num7 = Button(jframe2,text = 7,bg = "orange",width = 5,height = 2,command = button7)
num8 = Button(jframe2,text = 8,bg = 'orange',width = 5,height = 2,command = button8)
num9 = Button(jframe2,text = 9,bg = 'orange',width = 5,height = 2,command = button9)
num_mul = Button(jframe2, text = '*', bg = 'orange',width = 5, height = 2,command = button_mul)
jframe2.grid(row = 4 ,column = 0 ,padx = 5,pady =0)
jframe3 = Frame(calculator)
num_dot = Button(jframe3,text = ".",bg = 'orange',width = 5,height = 2,command = button_dot)
num0 = Button(jframe3,text = 0,bg = 'orange',width = 5,height = 2,command = button0)
num_equal = Button(jframe3,text ='=',bg = 'orange',width =5,height = 2 ,command = button_equal)
num_div = Button(jframe3, text = '/', bg = 'orange',width = 5, height = 2,command = button_div)
jframe3.grid(row =5 ,column = 0,padx = 10,pady = 5)
button_cancel = Button(jframe3,width = 5,height = 2,bg = 'orange',text = 'C',command = _cancel)
button_cancel.grid(row = 9,column = 2 ,padx = 5,pady = 5)
num_div.grid(row = 8,column = 4,padx = 5)
num_mul.grid(row = 7,column =4 ,padx = 5)
num_minus.grid(row = 6,column = 4,padx = 5)
num_plus.grid(row = 5,column = 4,padx = 5)
num_equal.grid(row = 8,column = 3,padx = 5)
num_dot.grid(row = 8,column = 1,padx = 5)
num0.grid(row = 8,column = 2,padx = 5)
num9.grid(row = 7,column = 3,padx = 5)
num8.grid(row =7, column = 2,padx = 5)
num7.grid(row = 7,column = 1,padx = 5)
num6.grid(row = 6,column = 3,padx = 5)
num5.grid(row =6, column = 2,padx = 5)
num4.grid(row = 6,column = 1,padx = 5)
num3.grid(row = 5,column = 3,padx = 5)
num2.grid(row =5, column = 2,padx = 5)
num1.grid(row = 5,column = 1,padx = 5)


calculator.mainloop()