
## this is where i will add and test the basic gui
try:
    # for Python2
    from Tkinter import *
    import Tkinter as tk
except ImportError:
    # for Python3
    from tkinter import *
    import tkinter as tk

##These are classes for each step in the QuoteR program

##general page class    
class Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
    def show(self):
        self.lift()
        
class WelcomePage(Page):
    def __init__(self, master):
        Page.__init__(self, master)
        label = tk.Label(self, text="Welcome to QuoteR")
        label.config(font=("Courier", 44))
        label.pack(side="top", fill="both", expand=True)
        
class InputPage(Page):
    def __init__(self, master):
        Page.__init__(self, master)
        label = tk.Label(self, text="Input your text to memorize: ")
        label.config(font=("Courier", 32))
        label.pack(side="top", fill="both", expand=True)

class ReadyPage(Page):
    def __init__(self, master):
        Page.__init__(self, master)
        label = tk.Label(self, text="Ready?\n Click the button below to start reciting ")
        label.config(font=("Courier", 32))
        label.pack(side="top", fill="both", expand=True)

class TimerPage(Page):
    def __init__(self, master):
        Page.__init__(self,master)
        label = tk.Label(self, text="Press button when finished")
        label.config(font=("Courier", 32))
        label.pack(side="top", fill="both", expand=True)
        
class ProcessingPage(Page):
    def __init__(self,master):
        Page.__init__(self,master)
        label = tk.Label(self, text="Processing... ")
        label.config(font=("Courier", 32))
        label.pack(side="top", fill="both", expand=True)
        
class ComparisonPage(Page):
    def __init__(self,master):
        Page.__init__(self,master)
        label = tk.Label(self, text="Your input       Time         Your voice")
        label.config(font=("Courier", 32))
        label.pack(side="top", fill="both", expand=True)
       
class MyFirstGUI(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.centerWindow()  
        tk.Frame.__init__(self,master)
        ## make pages
        p0 = WelcomePage(self)
        p1 = InputPage(self)
        p2 = ReadyPage(self)
        p3 = TimerPage(self)
        p4 = ProcessingPage(self)
        p5 = ComparisonPage(self)
        
        ##make button frames
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        ##place all the pages in the program
        p0.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1) 
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
         
        ##place all the buttons      
        b0 = tk.Button(buttonframe, text="Welcome", command=p0.lift)
        b1 = tk.Button(buttonframe, text="Input", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Ready", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Timer", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Processing", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Comparison", command=p5.lift)
        
        b0.pack(side="left")
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
                        
        ## show welcome page that will link to others
        p0.show()
        
        master.title("QuoteR")

## centers the window based on 1280 x 720 size, might change based on
## users screen later
    def centerWindow(self):
        
        w = 1280
        h = 720

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        
        
        x = (sw - w)/2
        y = (sh - h)/2
                
        
              
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
        

   
        
        

root = tk.Tk()

my_gui = MyFirstGUI(root)
my_gui.pack(side="top", fill="both", expand=True)
##root.wm_geometry("1024x768")
root.mainloop()