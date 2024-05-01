#Importing all essential modules
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

pwd='root'

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1540x900")
        self.root.resizable(width=False, height=False)

        # Variables for sql
        self.var_firstname=StringVar()
        self.var_lastname=StringVar()
        self.var_mail=StringVar()
        self.var_username=StringVar()
        self.var_secq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_confirmpwd=StringVar()
        self.var_check=IntVar()

        # Load  and resize the image
        bgimg= Image.open(r"Register_images\bg.jpg")
        bgimg= bgimg.resize((1600,900))

        # convert it to ImageTk format
        self.bgimg = ImageTk.PhotoImage(bgimg)

        lb_bg=Label(self.root,image=self.bgimg)
        lb_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#EBEDE7")
        frame.place(x=100,y=80,width=900,height=580)
        
        img=Image.open(r"Register_images\reg.png")
        img=img.resize((450,100))
        self.photoimage=ImageTk.PhotoImage(img)
        lbimg = Label(self.root,image=self.photoimage,bg="#EBEDE7")
        lbimg.place(x=300,y=100, width=500,height=100)
        
        #Heading Label
        lbl_head= Label(frame,text="Instructor Registration",font=("Courier",30,"bold"),fg="#276069",bg="#EBEDE7")
        lbl_head.place(x=180,y=130)

        #fstname label 
        firstname = Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#276069",bg="#EBEDE7")
        firstname.place(x=100,y=200)

        #entry1
        self.txtname=ttk.Entry(frame,textvariable=self.var_firstname,font=("times new roman",15,"bold"))
        self.txtname.place(x=103,y=225,width=270)


        #lastname label 
        lastname = Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#276069",bg="#EBEDE7")
        lastname.place(x=100,y=270)

        #entry2 
        self.txtlastname=ttk.Entry(frame,textvariable=self.var_lastname,font=("times new roman",15,"bold"))
        self.txtlastname.place(x=103,y=295,width=270)

        #Email label
        mail= Label(frame,text="E-mail:",font=("times new roman",15,"bold"),fg="#276069",bg="#EBEDE7")
        mail.place(x=530,y=200)

        #entry3
        self.txtmail=ttk.Entry(frame,textvariable=self.var_mail,font=("times new roman",15,"bold"))
        self.txtmail.place(x=533,y=225,width=270)


        #Username label 
        username = Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="#276069",bg="#EBEDE7")
        username.place(x=530,y=270)

        #entry4
        self.txtusername=ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",15,"bold"))
        self.txtusername.place(x=533,y=295,width=270)


        #sec qstn label
        secq = Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#276069",bg="#EBEDE7")
        secq.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_secq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)

        #seq answer label 
        sans = Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#276069",bg="#EBEDE7")
        sans.place(x=100,y=420)

        #entry5
        self.txtsans=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtsans.place(x=103,y=445,width=270)

        #password label
        passwd = Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#276069",bg="#EBEDE7")
        passwd.place(x=530,y=350)

        #entry6
        self.txtpasswd=ttk.Entry(frame,show="*",textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtpasswd.place(x=533,y=375,width=270)

        #conf pwd label 
        cpasswd= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#276069",bg="#EBEDE7")
        cpasswd.place(x=530,y=420)

        #entry7
        self.txtcpasswd=ttk.Entry(frame,show="*",textvariable=self.var_confirmpwd,font=("times new roman",15,"bold"))
        self.txtcpasswd.place(x=533,y=445,width=270)

        # Create Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#276069",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=300,y=510,width=350,height=35)

    #Action upon reg button click
    def reg(self):
        if (self.var_firstname.get()=="" or self.var_lastname.get()=="" or self.var_mail.get()=="" or self.var_username.get()=="" or self.var_secq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_confirmpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_confirmpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        else:
            try:
                #MySQL Connection
                conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                query=("select * from regteach where username=%s")  
                value=(self.var_username.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                a=self.var_firstname.get()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another username")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_firstname.get(),
                    self.var_lastname.get(),
                    self.var_mail.get(),
                    self.var_username.get(),
                    self.var_secq.get(),
                    self.var_sa.get(),
                    self.var_pwd.get()
                    ))
                    conn.commit()

                    mycursor.execute("create table instructor" +self.var_username.get()+ "(rollno int not null primary key, student varchar(50))")
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
                    self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()