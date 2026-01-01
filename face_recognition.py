from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from random import randrange

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recogniton System")
        self.root.geometry("1600x800+0+0")
        self.root.state("zoomed")
        bg_color="#074463"

        lbl_heading=Label(self.root,text="Face Recognition",bg="#912740",fg="white",bd=20,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=10)
        lbl_heading.pack(side=TOP,fill=X)
        
        mainframe=Frame(self.root,bd=12,relief=RIDGE,padx=15,bg=bg_color)
        mainframe.place(x=0,y=90,width=1600,height=730)

        img_frame=Image.open(r"Images\face-recog.jpg")
        img_frame=img_frame.resize((650,700),Image.ANTIALIAS)
        self.photoimg_frame = ImageTk.PhotoImage(img_frame)

        img_lbl=Label(mainframe,image=self.photoimg_frame)
        img_lbl.place(x=450,y=60,width=660,height=540)

        btnData1=Button(img_lbl,text="FACE RECOGNITION",command=self.face_recog,font=("arial",12,"bold"),width=12,height=2,bg="#821a36",fg="white",cursor="hand2")
        btnData1.place(x=400, y=350,height=100,width=200)
    
    #=============attendance==========================================
    def mark_attendance(self,i,r,n,d):
        with open("Hiray.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    
    # ===============face Recognition===========
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(128,256), randrange(128,256), randrange(128,256)), 2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                # ==============fetch Data from database============
                conn=mysql.connector.connect(host='localhost',username='root',password='',database='face_recognition')
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Name from student where Student_Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Rollno from student where Student_Id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_Id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                
                if confidence>77:
                    # ========try to understand face ===========
                    cv2.putText(img,f"Id: {i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(0,255), randrange(128,256), randrange(128,256)), 2)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        webcam=cv2.VideoCapture(0)

        while True:
            ret, img=webcam.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Hiray",img)
            key = cv2.waitKey(1)

            if key==81 or key==113:
                break
        webcam.release()
        cv2.destroyAllWindows()
           


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()