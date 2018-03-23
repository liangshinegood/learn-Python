import tkinter
import time
import threading
root = tkinter.Tk()
root.minsize(500,400)
studentname = ['王云','张恒','李琦','王鑫','张目','马琦','闫明','胡丽','祁门','仪器','玉田']
labKey =['lab01','lab02','lab03','lab04','lab05','lab06','lab07','lab08','lab09','lab10','lab11']
for theNumLab in range(len(studentname)):
    labKey[theNumLab] = tkinter.Label(root,text=studentname[theNumLab])
    labKey[theNumLab].place(x = 20,y=30 +theNumLab*30,width=120,height=25)
j = 0
i=0
pressend = False  # 标志符  为了确定结束键被按下
bg1 = False  # 标志符  为了确保开始按键 在第一次按下时才有效果
bg2 = False  # 标志符  只有按下开始键时,结束见按下才能起作用

def isbegin():
    global bg1
    global bg2
    if bg1 == False:
        st = threading.Thread(target=selectName)
        st.start()
    bg1 = True
    bg2 = True

def selectName():
    global pressend
    while True:
        if pressend == True:
            pressend = False
            break
        time.sleep(0.05)
        setLabColor()
        isOutTheLab()

def stop():
    global pressend,bg1,bg2
    if bg2 == True:  # 开始按键被按下,可以按结束键
        bg1 = False  # 开始键被按下,并且只第一次被按下使有效果
        pressend = True  # 结束键被按下
    bg2 = False  # 结束键被按下,返回标识符(只有开始键被按下时,结束键才有效果)

def isOutTheLab():
    global j
    if j < theNumberBoundary() :
        j += 1
    else:
        j = 0

def theNumberLab():
    return len(labKey)

def theNumberBoundary():
    return theNumberLab()-1

def setLabColor():
    global j
    i = 0
    while i < theNumberLab():
        if i==j:
            labKey[i]['bg'] = 'red'
        else:
            labKey[i]['bg'] = 'white'
        # time.sleep(0.1)
        i += 1

btn1 = tkinter.Button(root, text='开始点名', command=isbegin)
btn1.place(relx=0.55, rely=0.3, relwidth=0.2)

btn2 = tkinter.Button(root,text = '结束点名',command=stop )
btn2.place(relx = 0.55,rely = 0.6,relwidth = 0.2)
#
root.mainloop()