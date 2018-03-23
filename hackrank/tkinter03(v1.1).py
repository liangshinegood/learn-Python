import tkinter
root = tkinter.Tk()
root.minsize(500,500)
#创建变量
num = tkinter.StringVar()
num.set(0)

'''
    计算显示

'''
label = tkinter.Label(root,textvariable = num ,bg = 'white',font=('黑体',20),anchor = 'e')
label.place(width = 400,height = 100,x = 50,y = 20)
isArith = False
calcuList = []
'''
    控制面板

'''
def pressno(no):
    global isArith
    if isArith == True:
        num.set(no)
        isArith = False
    else:
        inino = num.get()
        if inino == '0':
             num.set(no)
        else:
            num.set(str(num.get()+no))

def arith(flag):
    global isArith
    global calcuList
    isArith = True
    calcuList.append(num.get())
    calcuList.append(flag)
    print(calcuList)

def getresult(flag):
    global  calcuList
    if(len(calcuList) == 1):
        num.set(calcuList[0])
    else:
        calcuList.append(num.get())
        result = eval(''.join(calcuList))
        num.set(result)
        calcuList.clear()
def setZero():
    global calcuList
    num.set(0)
    calcuList.clear()

btn15 = tkinter.Button(root,text = '清零',command =setZero)
btn15.place(relx=0.05, rely=0.4, relwidth=0.2)

btn1 = tkinter.Button(root,text = '1',command = lambda :pressno('1'))
btn1.place(relx=0.05, rely=0.5, relwidth=0.2)

btn2 = tkinter.Button(root,text = '2',command = lambda :pressno('2'))
btn2.place(relx=0.25, rely=0.5, relwidth=0.2)

btn3 = tkinter.Button(root,text = '3',command = lambda :pressno('3'))
btn3.place(relx=0.45, rely=0.5, relwidth=0.2)

btn10 = tkinter.Button(root,text = '+',command =lambda : arith('+'))
btn10.place(relx=0.75, rely=0.5, relwidth=0.2)

btn4 = tkinter.Button(root,text = '4',command = lambda :pressno('4'))
btn4.place(relx=0.05, rely=0.6, relwidth=0.2)

btn5 = tkinter.Button(root,text = '5',command = lambda :pressno('5'))
btn5.place(relx=0.25, rely=0.6, relwidth=0.2)

btn6 = tkinter.Button(root,text = '6',command = lambda :pressno('6'))
btn6.place(relx=0.45, rely=0.6, relwidth=0.2)

btn11 = tkinter.Button(root,text = '-',command =lambda : arith('-'))
btn11.place(relx=0.75, rely=0.6, relwidth=0.2)

btn7 = tkinter.Button(root,text = '7',command = lambda :pressno('7'))
btn7.place(relx=0.05, rely=0.7, relwidth=0.2)

btn8 = tkinter.Button(root,text = '8',command = lambda :pressno('8'))
btn8.place(relx=0.25, rely=0.7, relwidth=0.2)

btn9 = tkinter.Button(root,text = '9',command = lambda :pressno('9'))
btn9.place(relx=0.45, rely=0.7, relwidth=0.2)

btn12 = tkinter.Button(root,text = '*',command = lambda :arith('*'))
btn12.place(relx=0.75, rely=0.7, relwidth=0.2)

btn0 = tkinter.Button(root,text = '0',command = lambda :pressno('0'))
btn0.place(relx=0.05, rely=0.8, relwidth=0.2)


btn14 = tkinter.Button(root,text = '=',command = lambda:getresult('='))
btn14.place(relx=0.25, rely=0.8, relwidth=0.4)


btn13 = tkinter.Button(root,text = '/',command =lambda :arith(('/')))
btn13.place(relx=0.75, rely=0.8, relwidth=0.2)

root.mainloop()