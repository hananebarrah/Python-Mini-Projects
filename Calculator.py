from tkinter import*

def guiCalculator(source, side):
    s_obj = Frame(source, borderwidth=4, bd=4, bg="slate blue")
    s_obj.pack(side=side, expand=YES, fill=BOTH)
    return s_obj
    
def button(source, side, text, command=None):
    s_obj = Button(source, text=text, command=command)
    s_obj.pack(side=side, expand=YES, fill=BOTH)
    return s_obj
    
class application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')
        display = StringVar()
        Entry(self, relief=RIDGE,
                    textvariable=display,
                    justify='right', bd=30,
                    bg="slate blue").pack(side=TOP, expand=YES, fill=BOTH)
                    
        for clearButton in (["CE"], ["C"]):
            frame = guiCalculator(self, TOP)
            for ichar in clearButton:
                button(frame, LEFT, ichar,
                        lambda s_obj=display, q=ichar: s_obj.set(''))
                        
        for numButton in ("789/", "456*", "123-", "0.+"):
            numFrame = guiCalculator(self, TOP)
            for numChar in numButton:
                button(numFrame, LEFT, numChar,
                        lambda s_obj=display, q=numChar: s_obj.set(s_obj.get() + q))

        equalButton = guiCalculator(self, TOP)
        for equal in "=":
            if equal == '=':
                btnEqual = button(equalButton, LEFT, equal)
                btnEqual.bind('<ButtonRelease-1>',
                        lambda e, s=self, s_obj=display: s.calc(s_obj))
            else:
                btnEqual = button(equalButton, LEFT, equal,
                                lambda s_obj=display, s=' %s '%equal: s_obj.set(s_obj.get()+s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    application().mainloop()