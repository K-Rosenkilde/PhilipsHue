
# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk

# class Navbar(tk.Frame): ...
# class Toolbar(tk.Frame): ...
class Statusbar(tk.Frame): ...
# class Main(tk.Frame): ...

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.parent = parent
        self.parent.geometry('600x600')
 #       self.parent.statusbar.set("Hello, world")
        
        
#         self.statusbar = Statusbar(self, ...)
#         self.toolbar = Toolbar(self, ...)
#         self.navbar = Navbar(self, ...)
#         self.main = Main(self, ...)

#        self.statusbar.pack(side="bottom", fill="x")
#         self.toolbar.pack(side="top", fill="x")
#         self.navbar.pack(side="left", fill="y")
#         self.main.pack(side="right", fill="both", expand=True)
        def toggleLight1():
            print("Toggle Light Stairs1") 
            activeBulb = 1
 #       getLightInfo(activeBulb)
 #       onOff(activeBulb)

        btnQuit = tk.Button(parent, text="Quit", command=quit).grid(column=5 , row=11)
        
        btn1 = tk.Button(parent, text="1. Stairs 1", command=toggleLight1).grid(column=1, row=1)
        btn2 = tk.Button(parent, text="2. Stairs 2", command=toggleLight1).grid(column=2, row=1)
        btn3 = tk.Button(parent, text="3. Stairs 3", command=toggleLight1).grid(column=3, row=1)
# 
#         btn4 = Button(window, text="4. Entre", command=toggleLight4)
#         btn4.grid(column=1, row=2)
#         btn6 = Button(window, text="6. Altan", command=toggleLight6)
#         btn6.grid(column=2, row=2)
#         btn7 = Button(window, text="7. Bedroom", command=toggleLight7)
#         btn7.grid(column=3, row=2)
#         btn5  = Button(window, text="5. Billed Spot", command=toggleLight5)
#         btn5.grid(column=1, row=3)
#         btn8  = Button(window, text="8. Kuppel", command=toggleLight8)
#         btn8.grid(column=2, row=3)
#         btn10 = Button(window, text="10. Kip Light", command=toggleLight10)
#         btn10.grid(column=3, row=3)
#         btn15 = Button(window, text="15. Desks", command=toggleLight15)
#         btn15.grid(column=5, row=3)
#         btn9  = Button(window, text="9.  Hall 1", command=toggleLight9)
#         btn9.grid(column=1, row=5)
#         btn11 = Button(window, text="11. Hall 2", command=toggleLight11)
#         btn11.grid(column=2, row=5)
#         btn17 = Button(window, text="17. Hall 3", command=toggleLight17)
#         btn17.grid(column=3, row=5)
#         btn12 = Button(window, text="12. Entre", command=toggleLight12)
#         btn12.grid(column=1, row=6)
#         btn13 = Button(window, text="13. Dinner UP", command=toggleLight13)
#         btn13.grid(column=1, row=6)
#         btn14 = Button(window, text="14. Dinner Down", command=toggleLight14)
#         btn14.grid(column=2, row=6)
#         btn19 = Button(window, text="19. Balcony 1", command=toggleLight19)
#         btn19.grid(column=1, row=7)
#         btn18 = Button(window, text="18. Balcony 2", command=toggleLight18)
#         btn18.grid(column=2, row=7)
#         btn20 = Button(window, text="20. Balcony 3", command=toggleLight20)
#         btn20.grid(column=3, row=7)
#         btn16 = Button(window, text="16. Hue Ambiance Spot test", command=toggleLight16)
#         btn16.grid(column=1, row=8)
#         lbl1 = Label(window, text="Test") 
#         lbl1.grid(column=1, row=11)
#         btn21 = Button(window, text="21. Up", command=Up21)
#         btn21.grid(column=1, row=10)
#         btn21 = Button(window, text="22. Down", command=Down21)
#         btn21.grid(column=2, row=10)

 


    def Up21():
        print("Up21")
        activeBulb = 3
        upDown(activeBulb, True)

    def Down21():
        print("Down21")
        activeBulb = 3
        upDown(activeBulb, False)
         


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    
    