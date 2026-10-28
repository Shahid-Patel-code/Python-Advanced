import psycopg2
conn= psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="focus",
    user="postgres",
    password="1445"
    )

print("database connected succesfully")

cursor=conn.cursor()

Table="""create table if not exists course(id integer,
name text,
age integer,
marks integer)"""

insert="""insert into course values(1,'AKhalil',50,46)"""

cursor.execute(Table)
cursor.execute(insert)
conn.commit()
conn.close()


