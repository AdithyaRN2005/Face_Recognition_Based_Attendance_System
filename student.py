#Importing all essential modules
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import dlib

pwd='root'

class Student:
    def __init__(self,root,username):
        self.root=root
        self.root.geometry("1540x900")
        self.root.resizable(width=False, height=False)
        self.root.title("Student Panel")
        self.username=username

        #Variables for sql
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_name=StringVar()
        self.var_rollno=StringVar()
        self.var_gen=StringVar()
        self.var_DOB=StringVar()
        self.var_mail=StringVar()
        self.var_num=StringVar()
        self.var_address=StringVar()

        # first header image  
        bnrimg=Image.open(r"student_images\banner.png")
        bnrimg=bnrimg.resize((1600,200),Image.LANCZOS)
        self.photobnrimg=ImageTk.PhotoImage(bnrimg)

        # set image as label
        bnr_lb = Label(self.root,image=self.photobnrimg)
        bnr_lb.place(x=0,y=0,width=1600,height=200)

        # backgrund image 
        bgimg=Image.open(r"student_images\bg3.png")
        bgimg=bgimg.resize((1600,768),Image.LANCZOS)
        self.photobgimg=ImageTk.PhotoImage(bgimg)

        #set image as label
        bg_lb = Label(self.root,image=self.photobgimg)
        bg_lb.place(x=0,y=200,width=1600,height=768)


        #title section
        title_lb = Label(bg_lb,text="STUDENT DETAILS",font=("verdana",36,"bold"),bg="white",fg="#260e75")
        title_lb.place(x=0,y=-5,width=1600,height=61)

        # Creating Frame 
        main_frame = Frame(bg_lb,bd=2,bg="white")  
        main_frame.place(x=0,y=50,width=1600,height=590)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="#260e75")
        left_frame.place(x=10,y=10,width=800,height=570)

        # Current Course 
        current_course = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="#260e75")
        current_course.place(x=10,y=5,width=800,height=150)

        #label Department
        dept_label=Label(current_course,text="Department",font=("verdana",12,"bold"),bg="white",fg="#260e75")
        dept_label.grid(row=0,column=2,padx=5,pady=15)

        #combo box department
        dept_combo=ttk.Combobox(current_course,textvariable=self.var_dept,width=15,font=("verdana",12,"bold"),state="readonly")
        dept_combo["values"]=("Select Department","CSE","DSE","EE","ME","CE","Other")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=3,padx=0,pady=15,sticky=W)

        #label Course
        course_label=Label(current_course,text="Course",font=("verdana",12,"bold"),bg="white",fg="#260e75")
        course_label.grid(row=0,column=0,padx=50,pady=15)

        #combo box 
        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,width=15,font=("verdana",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","B-Tech","Msc","M-Tech","Phd","Other")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=0,pady=15,sticky=W)


        #label Year
        year_label=Label(current_course,text="Year",font=("verdana",12,"bold"),bg="white",fg="#260e75")
        year_label.grid(row=1,column=0,padx=50,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-24","2021-25","2022-26","2023-27","Other")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=0,pady=15,sticky=W)

        #label Semester 
        sem_label=Label(current_course,text="Semester",font=("verdana",12,"bold"),bg="white",fg="#260e75")
        sem_label.grid(row=1,column=2,padx=50,sticky=W)

        #combo box 
        sem_combo=ttk.Combobox(current_course,textvariable=self.var_sem,width=15,font=("verdana",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=0,pady=15,sticky=W)

        #Student Information
        Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Personal Details",font=("verdana",12,"bold"),fg="#260e75")
        Student_frame.place(x=10,y=160,width=800,height=300)

     
        #Student name
        name_label = Label(Student_frame,text="Name:",font=("verdana",12,"bold"),fg="#260e75",bg="white")
        name_label.grid(row=0,column=2,padx=50,pady=5,sticky=W)

        name_entry = ttk.Entry(Student_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        name_entry.grid(row=0,column=3,padx=25,pady=5,sticky=W)

  

        #Roll No
        student_rollno_label = Label(Student_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="#260e75",bg="white")
        student_rollno_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        student_rollno_entry = ttk.Entry(Student_frame,textvariable=self.var_rollno,width=15,font=("verdana",12,"bold"))
        student_rollno_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Gender
        gender_label = Label(Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="#260e75",bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=20,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(Student_frame,textvariable=self.var_gen,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Choose","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=40,sticky=W)

        #Date of Birth
        dob_label = Label(Student_frame,text="DOB:",font=("verdana",12,"bold"),fg="#260e75",bg="white")
        dob_label.grid(row=2,column=2,padx=60,pady=40,sticky=W)

        student_dob_entry = ttk.Entry(Student_frame,textvariable=self.var_DOB,width=15,font=("verdana",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=25,pady=40,sticky=W)

        #Email
        email_label = Label(Student_frame,text="Email:",font=("verdana",12,"bold"),fg="#260e75",bg="white")
        email_label.grid(row=4,column=0,padx=5,pady=20,sticky=W)

        email_entry = ttk.Entry(Student_frame,textvariable=self.var_mail,width=15,font=("verdana",12,"bold"))
        email_entry.grid(row=4,column=1,padx=5,pady=20,sticky=W)

        #Phone Number
        mobno_label = Label(Student_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="#260e75",bg="white")
        mobno_label.grid(row=4,column=2,padx=60,pady=20,sticky=W)

        student_mob_entry = ttk.Entry(Student_frame,textvariable=self.var_num,width=15,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=4,column=3,padx=25,pady=20,sticky=W)

        #Address
        address_label = Label(Student_frame,text="Address:",font=("verdana",12,"bold"),fg="#260e75",bg="white")
        address_label.grid(row=6,column=0,padx=5,pady=50,sticky=W)

        address_entry = ttk.Entry(Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        address_entry.grid(row=6,column=1,padx=5,pady=50,sticky=W)

        #Button Frame
        bton_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        bton_frame.place(x=10,y=470,width=800,height=70)

        #save button
        save_bton=Button(bton_frame,command=self.add_data,text="Save & Take Photo",width=18,height=2,font=("verdana",12,"bold"),fg="white",bg="#260e75")
        save_bton.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_bton=Button(bton_frame,command=self.update_data,text="Update",width=15,height=2,font=("verdana",12,"bold"),fg="white",bg="#260e75")
        update_bton.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_bton=Button(bton_frame,command=self.delete_data,text="Delete",width=15,height=2,font=("verdana",12,"bold"),fg="white",bg="#260e75")
        del_bton.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_bton=Button(bton_frame,command=self.reset_data,text="Reset",width=15,height=2,font=("verdana",12,"bold"),fg="white",bg="#260e75")
        reset_bton.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #  Label Frame 
        std_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="#260e75")
        std_frame.place(x=800,y=10,width=720,height=640)

        #Searching System in student Label Frame 
        search_frame = LabelFrame(std_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="#260e75")
        search_frame.place(x=10,y=5,width=700,height=80)

        
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="#260e75",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll-No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=20,pady=15,sticky=W)
        #entry box

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=15,pady=5,sticky=W)

        #Search button

        search_bton=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="#260e75")
        search_bton.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #showall button

        showAll_bton=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="#260e75")
        showAll_bton.grid(row=0,column=4,padx=10,pady=10,sticky=W)

        #Table Frame 
        #Searching System in std Label Frame 
        table_frame = Frame(std_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=700,height=452)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.std_table = ttk.Treeview(table_frame,column=("Roll-No","Name","Course","Dep","Year","Sem","Gender","DOB","Email","Mob-No","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.std_table.xview)
        scroll_y.config(command=self.std_table.yview)

        self.std_table.heading("Roll-No",text="Roll-No")
        self.std_table.heading("Name",text="Name")
        self.std_table.heading("Course",text="Course")
        self.std_table.heading("Dep",text="Department")
        self.std_table.heading("Year",text="Year")
        self.std_table.heading("Sem",text="Semester")
        self.std_table.heading("Gender",text="Gender")
        self.std_table.heading("DOB",text="DOB")
        self.std_table.heading("Email",text="Email")
        self.std_table.heading("Mob-No",text="Mob-No")
        self.std_table.heading("Address",text="Address")
        self.std_table["show"]="headings"


        # Set Width of Colums 
        self.std_table.column("Roll-No",width=100)
        self.std_table.column("Name",width=100)
        self.std_table.column("Course",width=100)
        self.std_table.column("Dep",width=100)
        self.std_table.column("Year",width=100)
        self.std_table.column("Sem",width=100)   
        self.std_table.column("Gender",width=100)
        self.std_table.column("DOB",width=100)
        self.std_table.column("Email",width=100)
        self.std_table.column("Mob-No",width=100)  
        self.std_table.column("Address",width=100)
       
        self.std_table.pack(fill=BOTH,expand=1)
        self.std_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_name.get()=="" or self.var_rollno.get()=="" or self.var_gen.get()=="Choose" or self.var_DOB.get()=="" or self.var_mail.get()=="" or self.var_num.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                try:

                    #Capturing Image to add to student data
                    cap = cv2.VideoCapture(0)
                    cv2.namedWindow("Face Detection")
                    detector = dlib.get_frontal_face_detector()

                    if not cap.isOpened():
                        print("Error: Unable to open camera.")
                        return

                    while True:
                        # Capture frame-by-frame
                        ret, frame = cap.read()

                        # Convert the frame to grayscale
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        
                        # Detect faces in the grayscale frame
                        faces = detector(gray)
                        


                        key = cv2.waitKey(1) & 0xFF
                        if key == 32:  # Check if spacebar is pressed
                           
                            if not os.path.exists(f"student_data/{self.username}"):
                                os.makedirs(f"student_data/{self.username}")
                            cv2.imwrite(f"student_data/{self.username}/{self.var_rollno.get()}.jpg", frame)
                            print("Image captured.")
                            break

                        # Draw rectangles around the detected faces
                        for face in faces:
                            x, y, w, h = (face.left(), face.top(), face.width(), face.height())
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                        # Display the frame
                        cv2.imshow("Capture Image", frame)
                        
                        # Exit loop if 'q' key is pressed
                        if key == ord('q') or key==27:
                            print("Forced Exit. Data Not Saved")
                            break
                except:
                        pass
                finally:

                        # Release the camera and close all OpenCV windows
                        cap.release()
                        cv2.destroyAllWindows()

                #Saving data to sql
                conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("select rollno from instructor"+self.username)
                dataroll=mycursor.fetchall()
                if (str(self.var_rollno.get()),) not in dataroll:
                    mycursor.execute("insert into instructor"+self.username+"(rollno,student) values(%s,%s)", (
                                 self.var_rollno.get(),
                                 self.var_name.get()
                    ))
                    conn.commit()
                    mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                    self.var_rollno.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_dept.get(),                
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_gen.get(),
                    self.var_DOB.get(),
                    self.var_mail.get(),
                    self.var_num.get(),
                    self.var_address.get(),
                    self.username
                    ))

                    conn.commit()

                

                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #To fetch data from a table
    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        mycursor.execute("select * from student where instructor=%s",(self.username,))
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.std_table.delete(*self.std_table.get_children())
            for i in data[:len(data)]:
                self.std_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get values from table
    def get_cursor(self,event=""):
        cursor_focus = self.std_table.focus()
        content = self.std_table.item(cursor_focus)
        data = content["values"]

        self.var_rollno.set(data[0]),
        self.var_name.set(data[1]),
        self.var_course.set(data[2]),
        self.var_dept.set(data[3]),
        self.var_year.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_gen.set(data[6]),
        self.var_DOB.set(data[7]),
        self.var_mail.set(data[8]),
        self.var_num.set(data[9]),
        self.var_address.set(data[10])

    #Update student data     
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_name.get()=="" or self.var_rollno.get()=="" or self.var_gen.get()=="Choose" or self.var_DOB.get()=="" or self.var_mail.get()=="" or self.var_num.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
                    mycursor = conn.cursor()
                    mycursor.execute("show tables")
                    data=mycursor.fetchall()
                    for i in data:
                        if "instructor"+self.username in i[0]:
                            mycursor.execute("select rollno from instructor"+self.username)
                            dataroll=mycursor.fetchall()
                            if (str(self.var_rollno.get()),) not in dataroll:
                                mycursor.execute("update instructor"+self.username+" set student=%s where rollno=%s",(self.var_name.get(),self.var_rollno.get(),))
                                conn.commit()

                                mycursor.execute("update student set Name=%s,Course=%s,Department=%s,Year=%s,Semester=%s,Gender=%s,DOB=%s,Email=%s,Mobile_No=%s,Address=%s where Roll_No=%s and instructor=%s",( 
                                        
                                self.var_name.get(),
                                self.var_course.get(),
                                self.var_dept.get(),                
                                self.var_year.get(),
                                self.var_sem.get(),
                                self.var_gen.get(),
                                self.var_DOB.get(),
                                self.var_mail.get(),
                                self.var_num.get(),
                                self.var_address.get(),
                                self.var_rollno.get(),
                                self.username
                                ))
                                conn.commit()
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #To delete data of student from database
    def delete_data(self):
        if self.var_rollno.get()=="":
            messagebox.showerror("Error","Student ROll No is Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
                    mycursor = conn.cursor() 
                    sql="delete from student where Roll_No=%s and instructor=%s"
                    val=(self.var_rollno.get(),
                         self.username)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                mycursor.execute("delete from instructor"+self.username+" where rollno=%s",(self.var_rollno.get(),))
                if os.path.exists(f'student_data/{self.username}/{self.var_rollno.get()}.jpg'):
                    os.remove(f'student_data/{self.username}/{self.var_rollno.get()}.jpg')

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_name.set(""),
        self.var_dept.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_gen.set("Choose"),
        self.var_DOB.set(""),
        self.var_num.set(""),
        self.var_address.set(""),
        self.var_rollno.set(""),
        self.var_mail.set("")
      
    
    #To search data in the table
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
                my_cursor = conn.cursor()
                sql = "SELECT Roll_No,Name,Course,Department,Year,Semester,Gender,DOB,Email,Mobile_No,Address FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.std_table.delete(*self.std_table.get_children())
                    for i in rows:
                        self.std_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
