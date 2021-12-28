while True:
 
    import mysql.connector
 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1122",
    database="LIBRARY"
    )
 
    cur=mydb.cursor()
    a=int(input('select a option: \n 1.Create an entry \n 2.Modify entry \n 3.View entry \n 4.Delete entry :'))
    if (a==1):
        book_no=int(input("Enter book no : "))
        book_name=input("Enter book name : ")
        sql="insert into library(book_no,book_name) values (%s,%s)"
        val= (book_no,book_name)
        cur.execute(sql,val)
        mydb.commit()
    
    
    elif(a==2):
        h=input("is this book taken(T) or returned(R) (press R/T) : ")
        if (h=='T' or h=='t'):
            book_no=int(input("Enter book no to modify entry : "))
            dot=input("date of taken : ")
            availability="no"
            sql="UPDATE library SET dot = %s WHERE book_no = %s "
            val=(dot,book_no)
            cur.execute(sql,val)
            mydb.commit()
            sql="UPDATE library SET availability = %s WHERE book_no = %s "
            val=(availability,book_no)
            cur.execute(sql,val)
            mydb.commit()
            details=input("Enter details of student here : ")
            sql="update library SET details = %s WHERE book_no = %s "
            val=(details,book_no)
            cur.execute(sql,val)
            mydb.commit()
      
 
        elif (h=='R' or h=='r'):
            book_no=int(input("Enter book no to modify entry : "))
            dor=input("date of return :")
            detail=input("enter details of student returned :")
            availability="yes"
            sql="UPDATE library SET dor = %s WHERE book_no = %s "
            val=(dor,book_no)
            cur.execute(sql,val)
            mydb.commit()
            sql="UPDATE library SET availability = %s WHERE book_no = %s "
            val=(availability,book_no)
            cur.execute(sql,val)
            mydb.commit()
            details=input("Enter details of student here : ")
            sql="update library SET details = %s WHERE book_no = %s "
            val=(details,book_no)
            cur.execute(sql,val)
            mydb.commit()
      
 
    elif (a==3):
        book_no=int(input("enter book n.o you want to search : "))
        sql="SELECT * FROM library WHERE book_no = %s "
        cur.execute(sql, (book_no,)) 
        myresult = cur.fetchall()
        print(myresult)
    
    elif (a==4):
        book_no=int(input("enter book n.o of the book you want to delete : "))
        sql="DELETE FROM library WHERE book_no = %s "
        cur.execute(sql, (book_no,))
        mydb.commit()
  
  x=input("Do you want to continue or not (Y/N) :")
  if (x=='N' or x=='n'):
    break





