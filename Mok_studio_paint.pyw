
"""
##################################################

   Welcome to Mok_studio_paint
   This project was created in 8/09/2020

   no-copyright-program  
         so you can use it to learn how to coding
       whatever you want :) 

    i hopefully you will enjoy it :) YAEE

################################################
"""

from tkinter import *
from tkinter.ttk import *
import time
from tkinter import colorchooser, filedialog
import pyautogui



color = "#000000"
x_old, y_old = None, None
b_size = 1

class main:

    x_old, y_old = None, None


    def __init__ (self,window):
        self.window = window
        

    def color_Picker():
        global color
        data_color = colorchooser.askcolor()
        color = data_color[1]
    
        print(color)

    def open_file():
        file = filedialog.askopenfilename()
        print(file)
        pass

    def save_file():
        save_canvas()
        filedialog.asksaveasfilename()
        pass

    def Up_Down(event):
        print(event)

        global x_old, y_old 
        x_old, y_old = None, None


    def paint(event):
        
        global color, x_old, y_old 
        if x_old and y_old:
            x1, y1, x2, y2 = (x_old), (y_old),(event.x), (event.y)
            Precious_line = mai_canvas.create_line(x1, y1, x2, y2, fill=color, 
                                               smooth=TRUE, capstyle=ROUND,
                                               joinstyle=MITER ,width=b_size,
                                               )
        x_old = event.x
        y_old = event.y



def menu():
        Main_Menu = Menu(master=window)

        File = Menu(master=Main_Menu, tearoff=0)
        Main_Menu.add_cascade(label="Flie", menu=File)
        File.add_command(label="Open File" ,command=main.open_file)
        File.add_command(label="Save File" ,command=main.save_file)
        File.add_separator()
        File.add_command(label="Exit" ,command=window.destroy)

        Color = Menu(master=Main_Menu, tearoff=0)
        Main_Menu.add_cascade(label="Colors", menu=Color)
        Color.add_command(label="Color Picker" ,command=main.color_Picker)
        Color.add_separator()
        Color.add_command(label="Exit" ,command=window.destroy)

        window.config(menu=Main_Menu)

def mouse_pos():
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
    pass


def Drawing_Area():
    Drawing_Frame = Frame(master=window, width=500)
    Drawing_Frame.grid(row=0, column=1)

    global mai_canvas
    mai_canvas = Canvas(master=Drawing_Frame, bg="snow", height=850, width=1500)
    mai_canvas.bind("<B1-Motion>", main.paint)
    mai_canvas.bind("<Button-1>",main.Up_Down)
    mai_canvas.bind("<Key>",None)
    mai_canvas.pack()

def save_canvas():
    global mai_canvas
    mai_canvas.update()
    mai_canvas.postscript(file="file_test.png", colormode='color')


def Button_Area():
    Button_Frame = Frame(master=window, height=900, width=100, pad=40)
    Button_Frame.configure(relief=GROOVE)
    Button_Frame.grid(row=0, column=0)

    B1 = Button(master=Button_Frame, text="Color Picker", 
                command=main.color_Picker)
    B1.grid(row=0, column=0, pady=50)


    B2 = Button(master=Button_Frame, text="RANDOMM",
                command=None)
    B2.grid(row=1, column=0, pady=50)

    def show_b_size(value):
       global b_size
       b_size = value
       tell_text = "Brush size is : " + str(b_size)[0:2].replace(".","  ") + " px"
       tell_label.config(text=tell_text)
    
    S1 = Scale(master=Button_Frame,from_=1,
               to=99, orient=HORIZONTAL,
               command=show_b_size)
    S1.grid(row=2, column=0, pady=50)
    tell_label = Label(Button_Frame, text="Brush size is : 1    px")
    tell_label.grid(row=3, column=0,)
    




if __name__ == "__main__":

    window = Tk()
    window.geometry("1500x900")
    window.title("Mok Studio Paint")
    window.resizable(False, False)
    window.focus
    main(window)

    menu()
    Button_Area()
    Drawing_Area()



 
    window.mainloop()





