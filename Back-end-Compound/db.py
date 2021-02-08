import psycopg2 

#Connect the DB
con = psycopg2.connect(
    host = "localhost",
    database = "test",
    user = "postgres",
    password = "postgres"

)


#cursor
cur = con.cursor()


#cur.execute("insert into employees(id, name, age, salary) values (%s, %s, %s, %s)",
#            (6, "Aman", 29, 90000))

#execute query
cur.execute("select id, name, age, salary from employees")

rows = cur.fetchone()

for r in rows:
    print(f"id={str(r[0])} name={r[1]} age={r[2]} salary={r[3]}")


#con.commit()


#close the cursor
#cur.close()

#Close the DB
con.close()
