from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Registration System")
        self.root.geometry("1600x800+0+0")
        self.root.state("zoomed")
        bg_color="#074463"
        #===========================Valriables========================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        #======image==========
        img = Image.open(r"Images\college-students.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=5,y=0,width=800,height=200)

        #======image1==========
        img1 = Image.open(r"Images\student.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        # ***********************Main frame**************************
        mainframe=Frame(self.root,bd=12,relief=RIDGE,padx=15,bg=bg_color)
        mainframe.place(x=0,y=100,width=1600,height=730)

        lbltitle=Label(mainframe,text="ATTENDANCE MANAGEMENT SYSTEM",fg="white",bg="#074463",font=("times new roman",30,"bold"),padx=0,pady=6)
        lbltitle.place(x=0,y=0,width=1500,height=40)

        # left lable frame
        Left_frame=LabelFrame(mainframe,text="Student Attendance",fg="#876a0b",bd=7,relief=RIDGE,font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=75,width=760,height=620)
        
        img_left = Image.open(r"Images\college-students.jpg")
        img_left=img_left.resize((750,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        Left_lbl=Label(Left_frame,image=self.photoimg_left)
        Left_lbl.place(x=5,y=0,width=740,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE)
        left_inside_frame.place(x=5,y=135,width=738,height=350)

        # ====labeled ======
        # Attendance ID
        attendanceId_lbl=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",13,"bold"))
        attendanceId_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_Entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_Entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll
        studroll_lbl=Label(left_inside_frame,text="RollNo:",font=("times new roman",13,"bold"))
        studroll_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studName_Entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",13,"bold"))
        studName_Entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Name
        studName_lbl=Label(left_inside_frame,text="Student Name:",font=("times new roman",13,"bold"))
        studName_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studName_Entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        studName_Entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Department
        studDep_lbl=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"))
        studDep_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studDep_Entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        studDep_Entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Time
        studTime_lbl=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"))
        studTime_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studTime_Entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        studTime_Entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # Date
        studDate_lbl=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"))
        studDate_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studDate_Entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        studDate_Entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Attendence status
        studStatus_lbl=Label(left_inside_frame,text="Attendence Status:",font=("times new roman",13,"bold"))
        studStatus_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studStatus_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly",width=18)
        studStatus_combo["values"]=("Status","Present","Absent")
        studStatus_combo.current(0)
        studStatus_combo.grid(row=3,column=1,padx=10,pady=7,sticky=W)

        # Button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=735,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        # ================Right lable frame==================
        Right_frame=LabelFrame(mainframe,text="student Details",fg="#876a0b",bd=7,relief=RIDGE,font=("times new roman",13,"bold"))
        Right_frame.place(x=780,y=75,width=760,height=620)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=735,height=455)

        #===============scroll bar table====
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attendance ID")
        self.attendanceReportTable.heading("roll",text="Roll")
        self.attendanceReportTable.heading("name",text="Name")
        self.attendanceReportTable.heading("department",text="Department")
        self.attendanceReportTable.heading("time",text="Time")
        self.attendanceReportTable.heading("date",text="Date")
        self.attendanceReportTable.heading("attendance",text="Attendance")

        self.attendanceReportTable["show"]="headings"
        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)

        self.attendanceReportTable.pack(fill=BOTH,expand=1)
        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ===============================fetch Data====================
    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)
    # ===========Import data=========
    def importcsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    # ===========Export data===========
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False 
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)       

    def get_cursor(self,event=""):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()