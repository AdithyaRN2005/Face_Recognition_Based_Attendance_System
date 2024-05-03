#Importing essential modules
from tkinter import*
from PIL import Image,ImageTk


class About:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x900")
        self.root.title("Face_Recogonition_System")
        self.root.resizable(width=False, height=False)

        # background image 
        about_bg=Image.open(r"about_images\bg.jpg")
        about_bg=about_bg.resize((1600,900),Image.LANCZOS)
        self.photoabout_bg=ImageTk.PhotoImage(about_bg)

        # set image as lable
        about_bg_img = Label(self.root,image=self.photoabout_bg)
        about_bg_img.place(x=0,y=0,width=1600,height=850)

        #Heading about

        heading = Image.open("about_images/heading.png").resize((350,85))

        self.photo_heading=ImageTk.PhotoImage(heading)

        image_label = Label(about_bg_img, image=self.photo_heading)

        image_label.pack()
        image_label.place(x=604, y=90)

        #Our name and images
        std_img_1=Image.open(r"about_images\akshath.jpg")
        std_img_1=std_img_1.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_1)

        std_img_btn_1 = Button(about_bg_img,image=self.std_img1,cursor="hand2")
        std_img_btn_1.place(x=441,y=262,width=180,height=180)

        std_btn_1 = Button(about_bg_img,text="Akshath J",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_btn_1.place(x=441,y=442,width=180,height=45)

        std_img_2=Image.open(r"about_images\adithya.jpg")
        std_img_2=std_img_2.resize((180,180),Image.LANCZOS)
        self.std_img_2=ImageTk.PhotoImage(std_img_2)

        std_img_btn_2 = Button(about_bg_img,image=self.std_img_2,cursor="hand2",)
        std_img_btn_2.place(x=681,y=262,width=180,height=180)

        std_btn_2 = Button(about_bg_img,text="Adithya Ramesh",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_btn_2.place(x=681,y=442,width=180,height=45)

        std_img_3=Image.open(r"about_images\gazal.jpg")
        std_img_3=std_img_3.resize((180,180),Image.LANCZOS)
        self.std_img_3=ImageTk.PhotoImage(std_img_3)

        std_img_btn_3 = Button(about_bg_img,image=self.std_img_3,cursor="hand2",)
        std_img_btn_3.place(x=921,y=262,width=180,height=180)

        std_btn_3 = Button(about_bg_img,text="Gazal S",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_btn_3.place(x=921,y=442,width=180,height=45)

        #Text

        text = Image.open("about_images/info.png").resize((1400,120))

        self.tk_image = ImageTk.PhotoImage(text)

        image_label= Label(about_bg_img,image=self.tk_image,borderwidth=0)

        image_label.place(x=54,y=650)


if __name__ == "__main__":
    root=Tk()
    obj=About(root)
    root.mainloop()