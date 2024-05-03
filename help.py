#Import modules
from tkinter import*
from PIL import Image,ImageTk


class Support:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x900")
        self.root.title("Face_Recogonition_System")
       


        # first header 
        header_img=Image.open(r"help_images\banner.jpeg")

        header_img=header_img.resize((1570,190),Image.LANCZOS)
        self.photoheader_img=ImageTk.PhotoImage(header_img)

        # set image as label
        header_lb1 =Label(self.root,image=self.photoheader_img)
        header_lb1.place(x=0,y=0,width=1566,height=180)

        # backgorund image 
        bg_help=Image.open(r"help_images\bg.PNg")
        bg_help=bg_help.resize((1600,700),Image.LANCZOS)
        self.photobg_help=ImageTk.PhotoImage(bg_help)

        # set image as label
        bg_header_lbl = Label(self.root,image=self.photobg_help)
        bg_header_lbl.place(x=0,y=100,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_header_lbl,text="SUPPORT",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=45)


if __name__ == "__main__":
    root=Tk()
    obj=Support(root)
    root.mainloop()