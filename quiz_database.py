import mysql.connector as my
con = my.connect(host = "localhost",port="3306", user="root",password = "User_password",database="Quiz")
cur = con.cursor()
login_status=False
user_id=""
ids=[]
marks=0
uipd={}
out1="select user_id,password from register"
cur.execute(out1)
n=cur.fetchall()

for i in n:
     ud,pd=i
     ids.append(ud)
     uipd[ud]=pd

## This is to create a data base Quiz Which will store the tables

# sql = "create database Quiz"
# cur.execute(sql)

## This is to create dbms table which contain dbms questions and answers

# sql1 = " create table dbms( Que varchar(250) primary key ,option_1 varchar(100),option_2 varchar(100), option_3 varchar(100),option_4 varchar(100),answer int)"
# cur.execute(sql1)
# dbms_que = "insert into dbms (Que , option_1 , option_2 , option_3 , option_4 , answer ) values(%s,%s,%s,%s,%s,%s)"
# val1 = [("Which of the following is a primary key?","A unique identifier for each record in a table","A key that can accept null values","A key that is used to create relationships between tables","A key that allows duplicate values",1),
#      ("What does ACID stand for in the context of database transactions?","Atomicity Consistency Isolation Durability","Accuracy Consistency  Integrity  Durability ","Atomicity Coherence Isolation Data","Availability Consistency  Isolation  Durability",1),
#      ("Which of the following SQL statements is used to create a table?","INSERT INTO","UPDATE","CREATE TABLE","ALTER TABLE",3),
#      ("Which type of join returns all rows when there is a match in either of the tables?","INNER JOIN","LEFT JOIN","RIGHT JOIN" ,"FULL JOIN",4),
#      ("What is the purpose of normalization in a database?","To reduce redundancy and improve data integrity","To increase data redundancy","To ensure data is stored in a single table","To reduce the complexity of queries",1)
#      ]
# cur.executemany(dbms_que,val1)

## This is to create dbms table which contain dsa questions and answers

# sql2="create table dsa(Que varchar(250) primary key ,option_1 varchar(100),option_2 varchar(100), option_3 varchar(100),option_4 varchar(100),answer int)"
# cur.execute(sql2)
# dsa_que = "insert into dsa ( Que , option_1 , option_2 , option_3 , option_4 , answer ) values(%s,%s,%s,%s,%s,%s)"
# val2 =[("What is the full form of DSA?","Data Structure and algorithm","Data Science Algorithm","Data Sort Algorithm ","Domain Search Algorithm",1),
#      ("What is the average time complexity of searching for an element in a balanced binary search tree (BST)?","O(1)","O(log n)","O(n)","O(n log n)",4),
#      ("Which data structure uses LIFO (Last In First Out) principle?","Queue","Stack","Array","Linkedlist",2),
#      ("What is the time complexity of accessing an element in an array?","O(n)","O(1)","O(log n)","O(n log n)",2),
#      ("Which algorithm is used to find the shortest path in a graph?","Depth-First Search","Breadth-First Search","Dijkstra's Algorithm","Kruskal's Algorithm",3)
#      ]
# cur.executemany(dsa_que,val2)

# ## This is to create Python table which contain dsa questions and answers

# sql3="create table python(Que varchar(250) primary key ,option_1 varchar(100),option_2 varchar(100), option_3 varchar(100),option_4 varchar(100),answer int)"
# cur.execute(sql3)
# python_que = "insert into python ( Que , option_1 , option_2 , option_3 , option_4 , answer ) values(%s,%s,%s,%s,%s,%s)"
# val3 =[("Which of the following is a mutable data type in Python?","Tuple","List","String","integer",2),
#      ("Which keyword is used to create a function in Python?","func","define","function","def",4),
#      ("Which of the following functions can be used to get the length of a string in Python?","length()","strlen()","len()","size()",3),
#      ("Which of the following is the correct way to declare a variable and assign the value 5 to it?","int x = 5","x = 5","declare x=5" ,"x:=5",2),
#      ("What is the data type of print(type(3.14)) in Python?","int","float","double","string",3)
#      ]
# cur.executemany(python_que,val3)

def register():
    
## This is for creating registration table which hold the user information
    #  sql4="create table register(Name varchar(25),enrollment varchar(15),user_id varchar(15) primary key,password varchar(15),marks int );"
    #  cur.execute(sql4)
    #  sql5="insert into register(Name,enrollment,user_id,password,marks) values(%s,%s,%s,%s,%s)"
    #  val5=[("Divya","102","d06","12",12),("sarthak","109","s06","12",12)]
    # cur.executemany(sql5,val5)
     l=False
     global ids
     global uipd
     while l!=True:
          val6=[]
          print("Enter the information\n")
          name=input("Enter your name= ")
          val6.append(name)
          enroll=input("Enter your enrollment= ")
          val6.append(enroll)
          uid=input("Create user id for account= ") 
          
          
          # print(ids)
          # print(uipd)
          
          if uid in ids:
            print("\nUser already exist go to login or enter new userid")
            val6=[]
          #   print(val6)
            
           
          else:
            val6.append(uid)
            pas=input("Create Password= ")
            val6.append(pas)
            mar=0
            val6.append(mar)
            sql6="insert into register(Name,enrollment,user_id,password,marks) value(%s,%s,%s,%s,%s)"
           
            cur.execute(sql6,val6)
          #   print(val6)
          out1="select user_id,password from register"
          cur.execute(out1)
          n=cur.fetchall()
        #   print(n)
          for i in n:
              ud,pd=i
              ids.append(ud)
              uipd[ud]=pd
          l=True
          

def login():
   global ids
   global user_id
   global login_status
   
   print("Enter your details")
   m=False
   while m!=True:
     user_id=input("Enter your user id: ")
     if user_id in ids:
         p=input("Enter your password: ")
         k=False
         while k!=True:
             if uipd[user_id]==p:
                 login_status=True
                
                 m=True
                 k=True
             else:
                 p=input("Enter your password: ")
                 m=False
                 k=False
     else:
         print("\nUser not exist go to register")
         m=True
       



def profile():
     if login_status==True:
          out2="select * from register;"
          cur.execute(out2)
          o=cur.fetchall()
         
          for i in o:
            
              
              if user_id in i:
                  print(f"\nThe {user_id} information are")
                  print("Name=",i[0])
                  print("Enrollment=",i[1])
                  print("User ID=",i[2])
                  print("Password=*****")
                  print("Marks=",i[4])
                  print("\n")
             

     else:
         print("\nFirst login or register")


def attemp_quiz():
    global marks
    if login_status==True:
        j=False
        while j!=True:
            print("\nChoose Subject \n1.DBMS \n2.DSA \n3.Python \n0.Exit\n")
            ch=int(input("Enter your choice: "))
            if ch==1:
               out3="select * from dbms;"
               cur.execute(out3)
               o1=cur.fetchall()
            elif ch==2:
               out3="select * from dsa;"
               cur.execute(out3)
               o1=cur.fetchall()
               
            elif ch==3:
               out3="select * from python;"
               cur.execute(out3)
               o1=cur.fetchall()
            elif ch==0:
                print("\nMarks=",marks)
                break
            else:
                n=False
            print("\n")
            for i in range(0,len(o1)):
               
                for j in range(0,len(o1[i])-1):
                    if j==0:
                        print(f"\nQue{i+1}:{o1[i][j]}")
                    else:
                        print(f"{j}. {o1[i][j]}")
                ans=int(input("Enter your answer:"))
                # print("\n")
                # print(o1[i][-1])
                

                if ans==o1[i][-1]:
                    marks=marks+1
                   
            # print("Marks=",marks)
            sql6=f"update register set marks={marks} where user_id=\"{user_id}\";"
            cur.execute(sql6)


                    
    else:
        print("First login ")
def exit():
    print("Logging out...")

def main():
    print("---------Welcome to Python Programing Quiz Application---------")
   
    l=False
    while l!=True:
        if login_status==True:
            print("Choose form below\n")
            print("3.Profile")
            print("4.Attempt Quiz")
            print("5.Exit")
            choice=int(input("Enter your choice: "))

            if choice==3:
                profile()
               
    
            elif choice==4:
                attemp_quiz()
               
            elif choice==5:
                exit()
                l=True
            else:
                print("Invalid choice")
                l=False
        else:
            print("\n---Welcome---")
            print("1.Register")
            print("2.Login")
            print("3.Profile")
            print("4.Attempt Quiz")
            print("5.Exit")
            choice=int(input("\nEnter your choice: "))
    
            if choice==1:
                register()
            elif choice==2:
                login()
            elif choice==3:
                profile()
                

            elif choice==4:
                attemp_quiz()
               
    
            elif choice==5:
                exit()
                l=True
            else:
                print("Invalid choice")
                l=False
        

main()


con.commit()
con.close()
