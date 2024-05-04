#Import all essential modules and class
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from face_recognition_file import FaceRecognitionSystem
from attendance import Attendance
from about import About
from help import Support

class Face_Recognition_System:
    def __init__(self,root,username):
        #Setting window parameter
        self.root=root
        self.root.geometry("1540x900")
        self.root.title("Face_Recognition_System")
        self.root.resizable(width=False, height=False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.username=username
        
        # Load the background image file
        bg_image = Image.open(r'main_images\bg.jpg')  
        bg_image = bg_image.resize((1600, 900), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(bg_image)

        # Creating a Canvas 
        canvas = Canvas(root, width=1300, height=768)
        canvas.pack(fill='both', expand=True)

        # Adding the background image
        canvas.create_image(0, 0, image=self.background_image, anchor='nw')

        #heading image

        heading = Image.open("main_images/heading.png").resize((1000,70))

        self.tk_image = ImageTk.PhotoImage(heading)

        image_label = Label(root, image=self.tk_image,borderwidth=0)

        image_label.pack()
        image_label.place(x=474, y=3)




        # Create the button image files
        button_image_face_detection = Image.open('main_images/facedetection.png').resize((700, 360), Image.LANCZOS)
        self.button_photo_face_detection = ImageTk.PhotoImage(button_image_face_detection, format='RGBA')


        # Add a button for Face Detection
        button_face_detection = Button(root,image=self.button_photo_face_detection)
        button_face_detection.config(image=self.button_photo_face_detection, command= self.face_rec, cursor="hand2")  # Set the button image
        button_face_detection.place(x=650, y=90, width=700, height=360)

        #effects for button
        def on_enter(event):
            button_face_detection.config(relief="sunken")

        def on_leave(event):
            button_face_detection.config(relief="raised")

        def on_click(event):
            button_face_detection.config(borderwidth=2)

        def on_release(event):
            button_face_detection.config(borderwidth=1)

        button_face_detection.bind("<Enter>", on_enter)
        button_face_detection.bind("<Leave>", on_leave)
        button_face_detection.bind("<Button-1>", on_click)
        button_face_detection.bind("<ButtonRelease-1>", on_release)


        # Add a button for Student Details
        button_image_student_details = Image.open('main_images/studentdetails.png').resize((350, 260), Image.LANCZOS)
        self.button_photo_student_details = ImageTk.PhotoImage(button_image_student_details)


        button_student_details = Button(root)
        button_student_details.config(image=self.button_photo_student_details, command=self.student_panel, cursor="hand2")
        button_student_details.place(x=650, y=450, width=350, height=260)
        #effects for button

        def on_enter(event):
            button_student_details.config(relief="sunken")

        def on_leave(event):
            button_student_details.config(relief="raised")

        def on_click(event):
            button_student_details.config(borderwidth=2)

        def on_release(event):
            button_student_details.config(borderwidth=1)

        button_student_details.bind("<Enter>", on_enter)
        button_student_details.bind("<Leave>", on_leave)
        button_student_details.bind("<Button-1>", on_click)
        button_student_details.bind("<ButtonRelease-1>", on_release)

        # Add a button for Attendance Record
        button_image_attendance_record = Image.open('main_images/attendance.png').resize((350, 260), Image.LANCZOS)
        self.button_photo_attendance_record = ImageTk.PhotoImage(button_image_attendance_record)
        

        button_attendance_record = Button(root,image=self.button_photo_attendance_record, command=self.attendance_panel, cursor="hand2")
        button_attendance_record.place(x=1000, y=450, width=350, height=260)
        #effects for button

        def on_enter(event):
            button_attendance_record.config(relief="sunken")

        def on_leave(event):
            button_attendance_record.config(relief="raised")

        def on_click(event):
            button_attendance_record.config(borderwidth=2)

        def on_release(event):
            button_attendance_record.config(borderwidth=1)

        button_attendance_record.bind("<Enter>", on_enter)
        button_attendance_record.bind("<Leave>", on_leave)
        button_attendance_record.bind("<Button-1>", on_click)
        button_attendance_record.bind("<ButtonRelease-1>", on_release)

        #help button

        button_help_image = Image.open('main_images/help.png').resize((85,80), Image.LANCZOS)
        self.button_photo_help = ImageTk.PhotoImage(button_help_image)

        button_help = Button(root, image=self.button_photo_help,command=self.support,cursor="hand2")
        button_help.place(x=1329, y=735)
        
        #effects for button

        def on_enter(event):
            button_help.config(relief="sunken")

        def on_leave(event):
            button_help.config(relief="raised")

        def on_click(event):
            button_help.config(borderwidth=2)

        def on_release(event):
            button_help.config(borderwidth=1)

        button_help.bind("<Enter>", on_enter)
        button_help.bind("<Leave>", on_leave)
        button_help.bind("<Button-1>", on_click)
        button_help.bind("<ButtonRelease-1>", on_release)

        #about button

        button_about_image = Image.open('main_images/about.png').resize((80,80), Image.LANCZOS)
        self.button_photo_about = ImageTk.PhotoImage(button_about_image)

        button_about = Button(root,image=self.button_photo_about, command=self.about, cursor="hand2")
        button_about.place(x=1229, y=735)
        
        #effects for button

        def on_enter(event):
            button_about.config(relief="sunken")

        def on_leave(event):
            button_about.config(relief="raised")

        def on_click(event):
            button_about.config(borderwidth=2)

        def on_release(event):
            button_about.config(borderwidth=1)

        button_about.bind("<Enter>", on_enter)
        button_about.bind("<Leave>", on_leave)
        button_about.bind("<Button-1>", on_click)
        button_about.bind("<ButtonRelease-1>", on_release)

        #logout button
        
        button_logout_image = Image.open('main_images/logout.png').resize((80,80), Image.LANCZOS)
        self.button_photo_logout = ImageTk.PhotoImage(button_logout_image)

        button_logout = Button(root,image=self.button_photo_logout,command=self.logout, cursor="hand2")
        button_logout.place(x=1429, y=735)
        
        #effects for button

        def on_enter(event):
            button_logout.config(relief="sunken")

        def on_leave(event):
            button_logout.config(relief="raised")

        def on_click(event):
            button_logout.config(borderwidth=2)

        def on_release(event):
            button_logout.config(borderwidth=1)

        button_logout.bind("<Enter>", on_enter)
        button_logout.bind("<Leave>", on_leave)
        button_logout.bind("<Button-1>", on_click)
        button_logout.bind("<ButtonRelease-1>", on_release)


    #To open student panel
    def student_panel(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window,self.username)
    
    #To open face recognizer
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_window,self.username)
        self.new_window.withdraw()
        # Create an instance of the FaceRecognition class
        face_recognition_instance = FaceRecognitionSystem(self.root,self.username)
        # Call the recognize_faces method
        face_recognition_instance.recognize_faces()
        
    #To open Attendance Panel
    def attendance_panel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window,self.username)

    #To open support panel
    def support(self):
        self.new_window=Toplevel(self.root)
        self.app=Support(self.new_window)

    #To open About window
    def about(self):
        self.new_window=Toplevel(self.root)
        self.app=About(self.new_window)

    #To logout
    def logout(self):
        from login import Login
        self.root.destroy()
        root = Tk()
        app = Login(root)
        root.mainloop()

    #Redifining Close button
    def on_closing(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
