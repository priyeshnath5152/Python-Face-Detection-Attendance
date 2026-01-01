from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Help:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Registration System")
        self.root.geometry("1600x800+0+0")
        self.root.state("zoomed")
        
        title_lbl=Label(self.root,text="HELP DESK",bg="#912740",bd=3,relief=RIDGE,fg="white",font=("times new roman",20,"bold"),padx=2,pady=10)
        title_lbl.place(x=0,y=0,width=1600,height=50)

        img_top = Image.open(r"Images\laptop-336373__340.jpg")
        img_top=img_top.resize((1600,760),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1600,height=760)

        # =============Help Info========
        info_lbl=Label(f_lbl,text="Email:- priyesht5152@gmail.com\n\n Email:- vinaysingh070697@gmail.com",bg="white",relief=RIDGE,fg="black",font=("times new roman",18,"bold"),padx=2,pady=10)
        info_lbl.place(x=10,y=10,width=410,height=200)

       

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()



    