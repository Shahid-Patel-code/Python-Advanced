import psycopg2
conn= psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="user_db",
    user="postgres",
    password="1445"
    )

print("database connected succesfully")
cursor=conn.cursor()


query="""select name,Extract(year from joining_date) from employee """
cursor.execute(query)
data=cursor.fetchall()
print(data)
print("---------------------------------------------------")
query="""select joining_date + interval '90 days' from employee"""
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")

query="""select name,EXTRACT(month from joining_date) from employee"""
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")

query="""select name,EXTRACT(day from joining_date) from employee"""
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")

query="""select EXTRACT(year from joining_date),count(*) AS DATA from employee group by EXTRACT(year from joining_date)  """
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")

query="""select name, EXTRACT(year from joining_date) AS DATA from employee where EXTRACT(year from joining_date)='2023'"""
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")

query="""SELECT name,EXTRACT(year from joining_date) from employee where (current_date - joining_date) > '1795'"""
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")

query="""Select name, EXTRACT(hours from joining_time) from employee where EXTRACT(hours from joining_time)='9'"""
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")

query="""select name, Extract(DOW from joining_date) from employee where Extract(DOW from joining_date)='0'"""
print("Sunday Employees:")
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")

query="""select * from employee where joining_date > '2023-01-01'"""
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)

query="""select max(joining_date)from employee """
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
print("---------------------------------------------------")
conn.commit()
conn.close()

