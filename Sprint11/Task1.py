import sqlite3

con = sqlite3.connect("q1.db")
print("Connected to SQLite")
cur = con.cursor()
res = cur.execute("SELECT * FROM customers WHERE grade > 200 ORDER BY Id")
result = res.fetchall()
print(f"Total rows are:   {len(result)}")
print("Printing each row")
for item in result:
    print(f'Id:  {item[0]}')
    print(f'Name:  {item[1]}')
    print(f'City:  {item[2]}')
    print(f'Grade:  {item[3]}')
    print(f'Seller:  {item[4]}')
    print('\n')
print("The SQLite connection is closed")