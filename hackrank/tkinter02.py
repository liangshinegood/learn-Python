import tkinter
import tkinter.messagebox
import tkinter.filedialog
import zipfile
root = tkinter.Tk()
root.maxsize(300,300)
root.minsize(300,300)
'''
    添加功能按钮
    
'''
frametop = tkinter.Frame(root,width = 300,height = 100)
frametop.pack(side = 'top')
def addfile():
    path = tkinter.filedialog.askopenfilename()
    txt.insert('end', path)#这里面必须要用小写end
    return path

btn1 = tkinter.Button(frametop,text = '添加文件',command = addfile)
btn1.place(relx=0.15, rely=0.2, relwidth=0.2)

def compressfile():
    savepath = tkinter.filedialog.asksaveasfilename()
    openfile = txt.get("1.0", "end-1c")
    if openfile == '':
        tkinter.messagebox.showerror(title= '信息提示',message='请添加文件')
    else:
        zp = zipfile.ZipFile(savepath,'w')
        zp.write(openfile,compress_type= zipfile.ZIP_DEFLATED)
        zp.close()
        tkinter.messagebox.showinfo(title='信息提示',message='压缩文件成功')

btn2 = tkinter.Button(frametop,text = '压缩文件',command = compressfile)
btn2.place(relx=0.45, rely=0.2, relwidth=0.2)
def discompressfile():
    tkinter.messagebox.showinfo(title='信息提示', message='请选择要解压的文件')
    openpath = tkinter.filedialog.askopenfilename()
    tkinter.messagebox.showinfo(title='信息提示', message='请选择要保存的路径')
    savepath = tkinter.filedialog.asksaveasfilename()
    disp = zipfile.ZipFile(openpath)
    disp.extractall(savepath)
    disp.close()
    tkinter.messagebox.showinfo(title='信息提示', message='解压文件成功')
btn3 = tkinter.Button(frametop,text = '解压缩',command = discompressfile)
btn3.place(relx=0.75, rely=0.2, relwidth=0.2)

'''
    添加显示面板

'''
framebottom = tkinter.Frame(root,bg = 'blue',width = 300,height = 200)
framebottom.pack(side = 'bottom')
txt = tkinter.Text(framebottom,width = 200,height = 160)
txt.pack()

root.mainloop()