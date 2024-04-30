#Importing all essential modules and classes
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from main import Face_Recognition_System

pwd='root' #SQL local host password


class Login:
    def __init__(self,root):
        #Defining window parameters
        self.root=root
        self.root.title("Login")
        self.root.geometry("1540x900")
        self.root.resizable(width=False, height=False)

        # variables for sql
        self.var_secq=StringVar()
        self.var_sec_ans=StringVar()
        self.var_pwd=StringVar()

        #background images
        bg=Image.open(r"login_images\bg.jpg")
        bg=bg.resize((1600,900),Image.LANCZOS)
        self.bg=ImageTk.PhotoImage(bg)
        
        lb_bg=Label(self.root,image=self.bg)
        lb_bg.place(x=0,y=0, width=1600,height=900)

        login_frame= Frame(self.root,bg="black")
        login_frame.place(x=760,y=170,width=340,height=450)

        img_person=Image.open(r"login_images\person.png")
        img_person=img_person.resize((100,100),Image.LANCZOS)
        self.photoimg_person=ImageTk.PhotoImage(img_person)
        lblimg_person = Label(image=self.photoimg_person,bg="#002B53")
        lblimg_person.place(x=885,y=175, width=100,height=100)

        #For login GUI
        get_str_label = Label(login_frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str_label.place(x=140,y=100)

        #label username
        username_label =lb1= Label(login_frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_label.place(x=30,y=160)

        #entry username 
        self.txtuser=ttk.Entry(login_frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label password
        pwd_label =lb1= Label(login_frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        pwd_label.place(x=30,y=230)

        #entry password
        self.txtpwd=ttk.Entry(login_frame,show='*',font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(login_frame,command=self.login,cursor='hand2',text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="black",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(login_frame,command=self.reg,cursor='hand2',text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(login_frame,command=self.forget_pwd,cursor='hand2',text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  To open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

     
    def login(self):
        #To check if all datas are correctly entered
        if self.txtuser.get() == "" or self.txtpwd.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                #Connecting to SQL
                conn = mysql.connector.connect(username='root', password=pwd, host='localhost', database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM regteach WHERE username=%s AND pwd=%s", (self.txtuser.get(), self.txtpwd.get()))
                row = mycursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username and Password!")
                else:
                    user = self.txtuser.get()
                    self.root.destroy()     
                    self.open_main(user)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}")
            except:
                print("Error")
            finally:
                if 'conn' in locals() and conn.is_connected():
                    conn.close()
                if 'mycursor' in locals():
                    mycursor.close()
    #To Reset Password 
    def reset_pass(self):
        #check if security questions are answered properly
        if self.var_secq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sec_ans.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
            mycursor = conn.cursor()
            query=("select * from regteach where username=%s and secu_q=%s and secu_ans=%s")
            value=(self.txtuser.get(),self.var_secq.get(),self.var_sec_ans.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where username=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                self.root.destroy()
                self.open_login()


    def open_login(self):
        self.root=Tk()
        app=Login(self.root)
        self.root.mainloop()
               
# To open Forget Password window
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Username ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
            mycursor = conn.cursor()
            query=("select * from regteach where username=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Username!")
            else:
                conn.close()
                self.root2=Toplevel(self.root)
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                self.root2.protocol("WM_DELETE_WINDOW", self.on_closing)
           
                #Label for forget pwd and security questions
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)

                secq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                secq.place(x=70,y=80)

                #Combo Box/Drop down box
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_secq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)

                #Label and entry box for forget pwd
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sec_ans,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)
 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)

    #to open Main window
    def open_main(self,username):
        self.root=Tk()
        app=Face_Recognition_System(self.root,username)
        self.root.mainloop()
    
    #Redefining Closing function
    def on_closing(self):
        self.root2.destroy()
        self.root.destroy()
        root = Tk()
        app = Login(root)
        root.mainloop()
        
            
if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()