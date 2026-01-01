from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train_data
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os
import tkinter
class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recognition System")
        self.root.geometry("1600x800+0+0")
        self.root.state("zoomed")
        bg_color="#074463"
        lbltitle=Label(self.root,text="FACE & EYES RICOGNITION ATTENDANCE SYSTEM",bg="#912740",fg="white",bd=15,relief=RIDGE,font=("times new roman",35,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

                # ***********************Main frame**************************
        mainframe=Frame(self.root,bd=12,relief=RIDGE,padx=15,bg=bg_color)
        mainframe.place(x=0,y=100,width=1600,height=730)


        btnData1=Button(mainframe,text="STUDENT DETAILS",command=self.student_details,font=("arial",12,"bold"),width=12,height=2,bg="#912740",fg="white",cursor="hand2")
        btnData1.place(x=270, y=150,height=100,width=200)

        btnData2=Button(mainframe,text="FACE DETECTOR",command=self.face_data,font=("arial",12,"bold"),width=12,height=2,bg="#912740",fg="white",cursor="hand2")
        btnData2.place(x=520, y=150,height=100,width=200)

        btnData3=Button(mainframe,text="ATTENDENCE",command=self.attendence_data,font=("arial",12,"bold"),width=12,height=2,bg="#912740",fg="white",cursor="hand2")
        btnData3.place(x=770, y=150,height=100,width=200)

        btnData4=Button(mainframe,text="HELP DESK",font=("arial",12,"bold"),command=self.help_data,width=12,height=2,bg="#912740",fg="white",cursor="hand2")
        btnData4.place(x=1020, y=150,height=100,width=200)

        btnData5=Button(mainframe,text="TRAIN DATA",command=self.train_data,font=("arial",12,"bold"),width=12,height=2,bg="#912740",fg="white",cursor="hand2")
        btnData5.place(x=270, y=300,height=100,width=200)

        btnData2=Button(mainframe,text="PHOTO",command=self.open_img,font=("arial",12,"bold"),width=12,height=2,bg="#912740",fg="white",cursor="hand2")
        btnData2.place(x=520, y=300,height=100,width=200)

        btnData3=Button(mainframe,text="DEVELOPER",font=("arial",12,"bold"),command=self.developer_data,width=12,height=2,bg="#912740",fg="white",cursor="hand2")
        btnData3.place(x=770, y=300,height=100,width=200)

        btnData4=Button(mainframe,text="EXIT",font=("arial",12,"bold"),command=self.iExit,width=12,height=2,bg="#912740",fg="white",cursor="hand2")
        btnData4.place(x=1020, y=300,height=100,width=200)
    
    def open_img(self):
        os.startfile("data")

        # ==========Function button=========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_data(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this portal",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()