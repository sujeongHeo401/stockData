import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Create table
cur.execute('''CREATE TABLE stocks (date, side, symbol, qty, price)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2021-01-01','BUY','AAPL',100,148.48)")
cur.execute("INSERT INTO stocks VALUES ('2021-01-02','SELL','AAPL',100,149.11)")
cur.execute("INSERT INTO stocks VALUES ('2021-01-03','BUY','AAPL',75,144.27)")
row = ('2021-01-04', 'SELL', 'AAPL', '75', '146.39')
cur.execute(f"INSERT INTO stocks VALUES {row}")

# Save (commit) the changes
conn.commit()

data = cur.execute('SELECT * FROM stocks').fetchall()
print(data)

# Close the connection
conn.close()