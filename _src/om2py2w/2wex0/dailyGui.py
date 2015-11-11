# -*- coding: UTF-8 -*-
from Tkinter import *
import tkMessageBox
import sys  #引用sys模块进来，并不是进行sys的第一次加载  
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8') #调用setdefaultencoding函数

root = Tk()
root.geometry('700x50')

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# 写入日记
    def write(self):
        filename = open('diary.txt','a')
        target = self.input.get()
        self.input.delete(0,END) # 保存后清空文字框
        filename.write("\n"+target)
        filename.close()

# 读取日记
    def read(self):
        tkMessageBox.showinfo('读日记',open('diary.txt','r').read())
       
# 清除日记
    def clear(self):
        filename = open('diary.txt','w')
        filename.close()


# 创建组件
    def createWidgets(self):
      
        self.label1 = Label(self, text='输入内容:').pack(side=LEFT)
        self.input = Entry(self, borderwidth = 3,width =50,)
        self.input.pack(side=LEFT)
        
        self.readButton = Button(self, text='查阅',command=self.read)
        self.readButton.pack(side=LEFT)
    

        self.saveButton = Button(self)
        self.saveButton['text'] = '保存'
        self.saveButton['command'] = self.write
        self.saveButton.pack(side=LEFT)
        
        self.quitButton = Button(self)
        self.quitButton['text'] = '退出'
        self.quitButton['command'] = self.quit
        self.quitButton.pack(side=LEFT)
  
        self.clearButton = Button(self)
        self.clearButton['text'] = '清空'
        self.clearButton['command'] = self.clear
        self.clearButton.pack(side=LEFT)
      
        
        

def main():
    app = Application(master = root)
    app.master.title('简易日记')
    app.mainloop()

if __name__ == "__main__":
    main()