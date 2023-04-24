
import sqlite3  
  
conn = sqlite3.connect('landd.db')  
print("Opened database successfully")  
cursor = conn.cursor()
# cursor.execute("INSERT INTO userr (u_name, u_address, u_phone) VALUES (?, ?, ?)", ("Astha", "dhveg", 8776555))
print("successful")
# conn.execute("create table property(p_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, p_name VARCHAR (20), p_description TEXT, p_type VARCHAR(20), p_price INTEGER, p_address TEXT, p_pincode INTEGER)")  

# conn.execute("create table userr(u_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, u_name VARCHAR (20), u_address TEXT, u_phone INTEGER UNIQUE)")
# conn.execute("create table registration (reg_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, p_id INTEGER NOT NULL REFERENCES property(p_id), user_id INTEGER NOT NULL REFERENCES userr(u_id), user_type BOOLEAN NOT NULL)")
# print("Table created successfully")  




conn.close()