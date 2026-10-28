import psycopg2
conn= psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="compony_db",
    user="postgres",
    password="1445"
    )
print("database connected succesfully")
cursor=conn.cursor()
while True:
    print("""1. Insert employee details
    2. Update employee salaryl
    3. Delete employee details
    4. Fetch employee details
    5. Modify table structure
    6. Exit
    """)
    choice=int(input("Enter your choice: "))

    if choice==1:
        #compony_db
       
        id=int(input("Enter employee id: "))
        name=input("Enter employee name: ")
        depart=input("Enter department name of employee: ")
        salary=int(input("Enter salary of employee: "))

        table="""create table if not exists employee_detail(
        id integer primary key, 
        name varchar(100), 
        department varchar(50), 
        salary int)"""

        insert=f"""insert into employee_detail values({id},'{name}','{depart}',{salary})"""
        cursor.execute(table)
        cursor.execute(insert)
        print("Value inserted succesfully")
        conn.commit()

    elif choice==2:
        id=int(input("Enter employee id: "))
        cursor.execute(f"select {id} from employee_detail where id ={id}")
        data=cursor.fetchall()
        data=(data[0])
        if id in data[0]:
            salary=int(input("Enter salary to update: "))
            update=f"""update employee_detail set salary={salary} where id={id}"""
            print("Previous data:", data)
            cursor.execute(update)
            conn.commit()
            print("Value updated succesfully")
        else: 
            print("Id Not Found")

    elif choice==3:
        id=int(input("Enter employee id to delete: "))
        cursor.execute(f"select {id} from employee_detail where id={id}")
        data=cursor.fetchall()
        print(data)
        data1=(data[0])
        if id in data[0]:
            delete=f"""delete from employee_detail where id={id}"""
            print("Previous data:", data1)
            cursor.execute(delete)
            conn.commit()
            print("Value deleted succesfully")
        else:
            print("Id Not Found")

    elif choice==4:
        cursor.execute("select *from employee_detail")
        choice1=int(input("""1. fetchone 
        2. fetchmany 
        3. fetchall
        Enter your choice: """))
        if choice1==1:
            data=cursor.fetchone()
            print(data)
        elif choice1==2:
            data1=cursor.fetchmany(3)
            for i in data1:
                print(i)

        elif choice1==3:
            data2=cursor.fetchall()
            for i in data2:
                print(i)
    elif choice==6:
    
        cursor.close()
        conn.close()
        break
    elif choice==5:
        print("""1. add colunm
         2. drop colunm """)
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter Column Name:  ")
            alter=(f"""alter table employee_detail add column {name} varchar(100)""")
            cursor.execute(alter)
            conn.commit()
            print("Column added succesfully")
        elif choice==2:
            name=input("Enter Colunm Name: ")
            alter=(f"""alter table employee_detail drop column {name}""")
            cursor.execute(alter)
            conn.commit()
            print("Column dropped succesfully")