from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train_data:
    def __init__(self,root):
        self.root=root
        self.root.title("Train Data Set")
        self.root.geometry("1600x800+0+0")
        self.root.state("zoomed")
        bg_color="#074463"
                
        lbl_heading=Label(self.root,text="TRAIN DATA SET",bg="#912740",fg="white",bd=15,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=10)
        lbl_heading.pack(side=TOP,fill=X)

        img_top=Image.open(r"Images\college-students.jpg")
        img_top=img_top.resize((1600,320),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        top_lbl=Label(self.root,image=self.photoimg_top)
        top_lbl.place(x=0,y=75,width=1600,height=320)

        btnData1=Button(self.root,text="TRAIN DATA",font=("arial",25,"bold"),command=self.train_classifier,width=12,height=2,bg="red",fg="white",cursor="hand2")
        btnData1.place(x=0,y=395,height=60,width=1600)

        img_bottom=Image.open(r"Images\student.jpg")
        img_bottom=img_bottom.resize((1600,320),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bottom_lbl=Label(self.root,image=self.photoimg_bottom)
        bottom_lbl.place(x=0,y=450,width=1600,height=320)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scall image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
       
        # ===============Train the classifier and save===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Train_data(root)
    root.mainloop()