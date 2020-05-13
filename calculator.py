#import addition
#import subtraction
#import multiplication
#import divide

from tkinter import *

calc = Tk()
calc.title("calculator")
calc.geometry("200x200")

w=Entry(calc,bg = 'white',fg = 'black',width = '30' )
w.grid(row = 0,column = 1)
jlabel = Label(calc,width = 4,height = 1)
jlabel.grid(row = 1)
butt1 = Button(calc,text ='1',width = '4')
butt1.grid(row = 2,column = 2,sticky ='E')

butt2 = Button(calc , text = '2',width = '4')
butt2.grid(row = 2,column = 4 )
butt3 = Button(calc , text = '3',width = '4')
butt3.grid(row = 2,column = 6)
butt4 = Button(calc , text = '4',width = '4')
butt4.grid(row = 4,column = 2 )
butt5 = Button(calc , text = '5',width = '4')
butt5.grid(row = 4 , column = 4)
butt6 = Button(calc , text = '6',width = '4')
butt6.grid(row = 4,column = 6)
butt7 = Button(calc , text = '7',width = '4')
butt7.grid(row = 6,column = 2)
but8 = Button(calc,text ='8',width = '4')
but8.grid(row =6,column = 4)
but9 = Button(calc,text ='9',width = '4')
but9.grid(row =6,column = 4)
calc.mainloop()