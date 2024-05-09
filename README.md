# Face_Recognition_Based_Attendance_System
This project is a part of the course ID1110: Introduction to Programming
Project Report: https://docs.google.com/document/d/1wjwFz1SePWUqcY9E-AOmB7cuslZYx1yhzfnRn0edZFk/edit?usp=sharing

Please install all the required libraries.
Please change username and password of MySQL in each file.

For creating the MySQL tables and database, copy the following code and run it  

pwd='yourpassword'  
conn = mysql.connector.connect(username='root', password=pwd, host='localhost')  
mycursor = conn.cursor()  
mycursor.execute("create database face_recognition")  
mycursor.commit()  
mycursor.close()  

pwd='yourpassword'  
conn = mysql.connector.connect(username='root', password=pwd, host='localhost', database='face_recognition')  
mycursor = conn.cursor()  
mycursor.execute("create table regteach(fname varchar(50), lname varchar(50), email varchar(100), username varchar(100) not null primary key, secu_q varchar(50), secu_ans varchar(50), pwd varchar(50)")  
mycursor.commit()  
mycursor.close()  

pwd='yourpassword'  
conn = mysql.connector.connect(username='root', password=pwd, host='localhost', database='face_recognition')  
mycursor = conn.cursor()  
mycursor.execute("create table student(Roll_No int(11), Name varchar(45), Course varchar(45), Department varchar(45), Year varchar(45), Semester varchar(45), Gender varchar(45), DOB varchar(45), Email varchar(45), Mobile_No bigint(20), Address varchar(45), instructor varchar(50))")  
mycursor.commit()  
mycursor.close()  
