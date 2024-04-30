#Importing essential modules
import os
import cv2
import numpy as np
import face_recognition as fr
import tkinter as tk
from tkinter import simpledialog
from tkinter import*
import mysql.connector
import threading
from tkinter import messagebox

pwd='root'#SQL local host password

class FaceRecognitionSystem:
    def __init__(self,root,username):
        self.username=username
        self.col_name = None
        self.recognized_name = "Unknown"
        self.consecutive_count = 0
        self.consecutive_count_2 = 0
        self.known_face_encodings = []
        self.known_face_names = []
        self.video_capture = cv2.VideoCapture(0) #Initialising camera
    
    #Load images from folder and encode it
    def load_images_from_folder(self, folder):
        known_face_encodings = []
        known_face_names = []
        try:
            for filename in os.listdir(folder):
                path = os.path.join(folder, filename)
                if os.path.isfile(path):
                    image = fr.load_image_file(path)
                    face_encoding = fr.face_encodings(image)
                    if len(face_encoding) > 0:
                        known_face_encodings.append(face_encoding[0])
                        known_face_names.append(os.path.splitext(filename)[0])  # Use file name as person's name
        except:
            messagebox.showerror("Error", "Add student first")
            exit()

        else:
            self.known_face_encodings = known_face_encodings
            self.known_face_names = known_face_names

    #Attendance marked popup
    def show_popup(self, message):
        def popup_thread():
            popup = tk.Tk()
            popup.title("Attendance")
            popup.geometry("200x100+400+300")
            label = tk.Label(popup, text=message)
            label.pack(pady=10)
            popup.after(2000, popup.destroy)  # Destroy the popup after 2 seconds
            popup.mainloop()

        thread = threading.Thread(target=popup_thread)
        thread.start()

    #Check entered date format
    def validate_date_format(self,date_string):
        # Check if the string length is exactly 10 characters
        if len(date_string) != 10:
            return False
        
        # Check if the format is "DD-MM-YYYY"
        if (date_string[2] != "-" or date_string[5] != "-"):
            return False
        
        # Check if all characters before and after the hyphens are digits
        if not (date_string[:2].isdigit() and date_string[3:5].isdigit() and date_string[6:].isdigit()):
            return False
        
        return True


    #To recognise faces
    def recognize_faces(self):
        #Asking date input
        self.col_name = simpledialog.askstring("Input", "Please enter Date in DD-MM-YYYY")
        if self.col_name is not None:
            if self.validate_date_format(self.col_name):
                self.col_name=self.col_name[:2]+self.col_name[3:5]+self.col_name[6:]
                conn = mysql.connector.connect(username='root', password=pwd,host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("desc instructor"+self.username)
                data=mycursor.fetchall()
                exist=False
                for i in data:
                    if 'date'+self.col_name in i:
                        exist=True
                if exist==False:
                    mycursor.execute("alter table instructor"+self.username+" add date"+self.col_name+" varchar(45) default 'Absent'")
            else:
                messagebox.showerror("Error", "Invalid date format")
                return    

            # Load known face encodings and names from a folder
            self.load_images_from_folder(f"student_data/{self.username}")

            while True: 
                #Caputring real time video
                ret, frame = self.video_capture.read()
                rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])

                fc_locations = fr.face_locations(rgb_frame)
                fc_encodings = fr.face_encodings(rgb_frame, fc_locations)

                for (top, right, bottom, left), face_encoding in zip(fc_locations, fc_encodings):
                    matches = fr.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    fc_distances = fr.face_distance(self.known_face_encodings, face_encoding)
                    match_index = np.argmin(fc_distances)

                    if matches[match_index]:
                        name = self.known_face_names[match_index]

                    if name == self.recognized_name:
                        self.consecutive_count += 1
                    else:
                        self.consecutive_count = 0
                        self.consecutive_count_2=0

                        self.recognized_name = name
                    #To mark attendance only if 5 consecutive frames are properly recognised
                    if self.consecutive_count >= 5:
                        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 0), cv2.FILLED)
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                        cv2.putText(frame, self.recognized_name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 1)
                        if self.recognized_name!='Unknown':
                            mycursor.execute("select date"+self.col_name+" from instructor"+self.username+" where rollno ="+self.recognized_name)
                            data=mycursor.fetchone()
                            if data is not None and "Present" not in data:                        
                                mycursor.execute("update instructor"+self.username+" set date"+self.col_name+"='Present' where rollno="+self.recognized_name)
                                conn.commit()
                                self.show_popup(f"Attendance Marked: {self.recognized_name} ")
                            elif data is None:
                                pass
                            else:
                                self.consecutive_count_2+=1
                                if self.consecutive_count_2<5:
                                    self.show_popup("Attendance Already Marked")
        

                    else:
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.imshow('Face Detection', frame)

                if cv2.waitKey(1) & 0xFF == 27:
                    break

            self.video_capture.release()
            cv2.destroyAllWindows()
        else:
            print('No Column name entered')
            

if __name__ == "__main__":
    root=Tk()
    # Create and call instance of the FaceRecognition class
    face_recognition_instance = FaceRecognitionSystem(root)
    face_recognition_instance.recognize_faces()
