from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Registration System")
        self.root.geometry("1600x800+0+0")
        self.root.state("zoomed")
        
        title_lbl=Label(self.root,text="DEVELOPER",bg="#912740",bd=3,relief=RIDGE,fg="white",font=("times new roman",20,"bold"),padx=2,pady=10)
        title_lbl.place(x=0,y=0,width=1600,height=50)

        img_top = Image.open(r"Images\108171721-abstract.jpg")
        img_top=img_top.resize((1600,760),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1600,height=760)

        # ===Frame==
        mainframe=Frame(f_lbl,bd=5,relief=RIDGE,padx=12,bg="#912740")
        mainframe.place(x=1000,y=0,width=460,height=500)

        # =============Developer Info========
        info_lbl=Label(mainframe,text="Develop By- Priyesh Tiwari \n\nDevelop By- Vinay Singh \n\nFYMCA",bg="#074463",relief=RIDGE,fg="white",font=("times new roman",18,"bold"),padx=2,pady=10)
        info_lbl.place(x=30,y=10,width=350,height=200)

        info_lbl=Label(mainframe,text="Language - Python Project \n\nFramework - Tkinter GUI \n\nDatabase - MYSQL",bg="#074463",relief=RIDGE,fg="white",font=("times new roman",18,"bold"),padx=2,pady=10)
        info_lbl.place(x=30,y=220,width=350,height=200)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()