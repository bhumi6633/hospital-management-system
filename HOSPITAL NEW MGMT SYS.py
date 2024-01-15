import sys
import mysql.connector as sql
mydb=sql.connect(host="localhost",user="root",passwd="bhumi",database="d1")
mycur=mydb.cursor()

def create_table():
    mycur.execute('create table hosp_details(g_bed int(2), icu_room int(2), special_room int(2))')
    mycur.execute('create table patient_details(p_id varchar(4) primary key,p_name varchar(25) ,p_age int(3),p_problems varchar(40),\
    p_phono int(15),t_type varchar(6),days int(2),Total_Bill float(10))')
    mycur.execute('create table doctor_details(d_name varchar(25) primary key,d_age int(3),d_department varchar(40),d_phono int(15))')
    mycur.execute('create table worker_details(w_name varchar(25) primary key,w_age int(3),w_workname varchar(40),w_phono int(15))')
    print('tables created')  
    mycur.close()

def Insert_Hopsital():
      g_bed=int(input('Enter no.of beds in general ward:'))
      icu_room=int(input('Enter no of ICU rooms:'))
      special_room=int(input('Enter no of Special rooms:'))
      mycur.execute("insert into hosp_details values({},{},{})".format(g_bed,icu_room,special_room)) 
      mydb.commit()
      print(mycur.rowcount,"Record(s) inserted successfully")


def Insert_Doctors():
      d_name=input('Enter Doctor Name:')
      d_age=int(input('Enter Age:'))
      d_department=input('Enter the Department:')
      d_phono=int(input('Enter Phone number:'))
      mycur.execute("insert into doctor_details values('{}',{},'{}',{})".format(d_name,d_age,d_department,d_phono)) 
      mydb.commit()
      print(mycur.rowcount,"Record(s) inserted successfully")

def Insert_Patient(tabl=None):
      p_id=input('Enter PatientID:')
      p_name=input('Enter Patient Name:')
      p_age=int(input('Enter Age:'))
      p_problems=input('Enter the Problem/Disease:')
      p_phono=int(input('Enter Phone number:'))
      t_type=input("Enter OPD/Admit:")
      if t_type=='OPD' or t_type=='opd':
          c=float(input("consultant charge:"))
          m=float(input("medicine charge:"))
          Total_Bill=c+m
          days=int(input('Enter number of days:'))
      if t_type=='ADMIT'  or t_type=='admit' or t_type=='Admit':
          days=int(input('Enter number of days:'))
          print("Type of room 1. Special   2. ICU   3. General")
          room=int(input('Enter Room Type:'))
          if room==1:
              r_cost=5000*days
              c=float(input("consultant charge:"))
              m=float(input("medicine charge:"))
              Total_Bill=r_cost+c+m
              
          if room==2:
              r_cost=10000*days
              c=float(input("consultant charge:"))
              m=float(input("medicine charge:"))
              Total_Bill=r_cost+c+m
              
          if room==3:
              if tabl=='hosp_details':
                  g_bed=g_bed-1
                  mycur.execute("update hosp_details set g_bed={}".format(g_bed))
                  mydb.commit()
                  print(mycur.rowcount,"Record(s) modified")
                  for x in mycur:
                      if x[0]>0:
                          r_cost=1000*days
                          c=float(input("consultant charge:"))
                          m=float(input("medicine charge:"))
                          Total_Bill=r_cost+c+m
                      else:
                          print("General ward full")
         
      mycur.execute("insert into patient_details values('{}','{}',{},'{}',{},'{}',{},{})".format(p_id,p_name,p_age,p_problems,p_phono,t_type,days,Total_Bill)) 
      mydb.commit()
      print(mycur.rowcount,"Record(s) inserted successfully")
              
              
def Insert_Workers():
      w_name=input('Enter Worker Name:')
      w_age=int(input('Enter Age:'))
      w_workname=input('Enter type of work:')
      w_phono=int(input('Enter Phone number:'))
      mycur.execute("insert into worker_details values('{}',{},'{}',{})".format(w_name,w_age,w_workname,w_phono)) 
      mydb.commit()
      print(mycur.rowcount,"Record(s) inserted successfully")

def Display_Hosp():
    mycur.execute("Select * from hosp_details")
    for x in mycur:
            print("General Bed: ",x[0])
            print("ICU ROOMS: ",x[1])
            print("Special ROOMS: ",x[2])


def DispAllPatients():
    mycur.execute("Select * from patient_details")
    for x in mycur:
            print("Patient Id: ",x[0])
            print("Patient Name: ",x[1])
            print("Age:",x[2])
            print("Problem :",x[3])
            print("Phone no.:",x[4])
            print("T_Type[OPD/Admit]:",x[5])
            print("Days  :",x[6])
            print("Total_Bill :",x[7])
            print("-"*20)

def DispAllDoctors():
    mycur.execute("Select * from doctor_detail")
    for x in mycur:
            print("Doctor Name : ",x[0])
            print("Age : ",x[1])
            print("Department :",x[2])
            print("Phone No.:",x[3])
            print("-"*20)
            
def DispAllWorkers():
    mycur.execute("Select * from worker_details")
    print("Worker_Name     Age      Work Type      Phone No.")
    for x in mycur:
        print(x[0],x[1],x[2],x[3])
            
            
def Search_Records():
    print("Find from 1. Patient File     2. Doctor File    3. Worker File")
    choice=int(input("enter choice from above"))
    if choice ==1:
            P_Nm=input("Enter Patient Name: ")
            mycur.execute("select * from patient_details where p_name = '{}'".format(P_Nm))
            for x in mycur:
                print("Patient Id: ",x[0])
                print("Patient Name: ",x[1])
                print("Age :",x[2])
                print("Problem :",x[3])
                print("Phone No.:",x[4])
                print("T_Type[OPD/Admit]:",x[5])
                print("Days  :",x[6])
                print("Total_Bill :",x[7])
                
    if choice ==2:
            D_Nm=input("Enter Doctors Name: ")
            mycur.execute("select * from doctor_details where d_name='{}'".format(D_Nm))
            for x in mycur:
                print("Doctor Name : ",x[0])
                print("Age : ",x[1])
                print("Department :",x[2])
                print("Phone No.:",x[3])

    if choice ==3:
            W_Nm=input("Enter Workers Name: ")
            mycur.execute("select * from worker_details where w_name='{}'".format(W_Nm))
            for x in mycur:
                print("Worker Name : ",x[0])
                print("Age : ",x[1])
                print("Work Type  :",x[2])
                print("Phone No.:",x[3])
                print("-"*20)  
                

def DeleteSpecific_Records():
    print("delete from 1. Patient File     2. Doctor File    3. Worker File")
    choice=int(input("enter choice from above"))
    if choice ==1:
        p_id=input("Enter Patient code to Delete")
        mycur.execute("select * from patient_details where p_id='{}'".format(p_id))
        data=mycur.fetchall()
        if mycur.rowcount>0:
            cf=input("Are you Confirm to Delete this Record")
            if cf=='Y' or cf=='y':
                mycur.execute("delete from patient_details where p_id='{}'".format(p_id))
                mydb.commit()
                print(mycur.rowcount,"Record(s) Deleted")
        else:
            print("No Record Found")

    if choice ==2:
        d_nm=input("Enter Doctors Name to Delete")
        cf=input("Are you Confirm to Delete this Record")
        if cf=='Y' or cf=='y':
            mycur.execute("delete from doctor_details where d_name='{}'".format(d_nm))
            mydb.commit()
            print(mycur.rowcount,"Record(s) Deleted")

    if choice ==3:
        w_nm=input("Enter worker Name to Delete")
        cf=input("Are you Confirm to Delete this Record")
        if cf=='Y' or cf=='y':
            mycur.execute("delete from worker_details where w_name='{}'".format(w_nm))
            mydb.commit()
            print(mycur.rowcount,"Record(s) Deleted")        

def Delete_Records():
    print("delete from 1. Patient File     2. Doctor File    3. Worker File")
    choice=int(input("enter choice from above"))
    if choice ==1:
        cf=input("Are you Confirm to Delete all Record")
        if cf=='Y' or cf=='y':
            mycur.execute("delete from patient_details")
            mydb.commit()
            print(mycur.rowcount,"Record(s) Deleted")
          
    if choice ==2:
        cf=input("Are you Confirm to Delete all Record")
        if cf=='Y' or cf=='y':
            mycur.execute("delete from doctor_details")
            mydb.commit()
            print(mycur.rowcount,"Record(s) Deleted")
          
    if choice ==3:
        cf=input("Are you Confirm to Delete all Record")
        if cf=='Y' or cf=='y':
            mycur.execute("delete from workerr_details")
            mydb.commit()
            print(mycur.rowcount,"Record(s) Deleted")
          
def Modify_Records():
     print("Modify from 1. Patient File     2. Doctor File    3. Worker File")
     choice=int(input("enter choice from above"))

     if choice==1:
        p_id=input("Enter Patient code to edit")
        mycur.execute("select * from patient_details where p_id='{}'".format(p_id))
        data=mycur.fetchall()
        if mycur.rowcount>0:
            p_nm=input("Enter New Name")
            p_no=int(input("Enter new phone number: "))
            cf=input("Are you Confirm to Modify ")
            if cf=='Y' or cf=='y':
                mycur.execute("update patient_details set p_name='{}', p_phono={} where p_id='{}'".format(p_nm,p_no,p_id))
                mydb.commit()
                print(mycur.rowcount,"Record(s) modified")
        else:
            print("No Record Found")

     if choice==2:
        d_nm=input("Enter Doctors Name to edit")
        mycur.execute("select * from doctor_details where d_nm='{}'".format(d_nm))
        data=mycur.fetchall()
        if mycur.rowcount>0:
            d_nm=input("Enter New Name")
            d_dept=input("Enter New department")
            d_no=int(input("Enter new phone number: "))
            cf=input("Are you Confirm to Modify ")
            if cf=='Y' or cf=='y':
                mycur.execute("update doctors_details set d_name='{}', d_department='{}',d_phono={} where d_name='{}'".format(d_nm,d_dept,d_no))
                mydb.commit()
                print(mycur.rowcount,"Record(s) modified")
        else:
            print("No Record Found")

#---------------Menu -------------
while True:
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("1: Create Tables")
    print("2. Insert Records")
    print("3: Search Record(s)")
    print("4: Delete Record(s)")
    print("5: Modify Record(s)")
    print("6: Display All Records")
    print("7: Delete Specific Record(s)")
    print("0: Exit")
    ch=int(input("Enter Your Choice: "))
    if ch==1:
        create_table()
    elif ch==2:
        c=int(input("insert:\n 1 - hospital \n 2 -patience \n 3 - doctors\n 4 - workers: "))
        if c==1:
            Insert_Hopsital()
        if c==2:
            Insert_Patient()
        if c==3:
            Insert_Doctors()
        if c==4:
            Insert_Workers()
    elif ch==3:
        Search_Records()
    elif ch==4:
        Delete_Records()
    elif ch==5:
        Modify_Records()
    elif ch==6:
         c=int(input("insert:\n 1 - hospital\n 2 - patience\n 3 - doctors \n 4 - workers :"))
         if c==1:
            Display_Hosp()
         if c==2:
            DispAllPatients()
         if c==3:
            DispAllDoctors()
         if c==4:
            DispAllWorkers()
    elif ch==7:
        DeleteSpecific_Records()
    elif ch==0:
        sys.exit()
