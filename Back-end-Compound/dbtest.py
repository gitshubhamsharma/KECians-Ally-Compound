import json
import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

# cursor
cur = con.cursor()

# execute query
# cur.execute("INSERT INTO room (pname, arrival, departure) VALUES (%s, %s, %s)")
cur.execute("select pname from room")

rows = cur.fetchall()

for r in rows:
    print(f"pname={(r[0])}")

# con.commit()

# close the cursor
cur.close()

# Close the DB
con.close()
