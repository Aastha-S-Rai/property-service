
import sqlite3  
  
conn = sqlite3.connect('landd.db')  
print("Opened database successfully")  
cursor = conn.cursor()
# cursor.execute("INSERT INTO userr (u_name, u_address, u_phone) VALUES (?, ?, ?)", ("Astha", "dhveg", 8776555))

# conn.execute("ALTER TABLE userr ADD COLUMN u_pwd VARCHAR(255)")
# conn.execute("DROP TABLE user_agent")
# conn.execute("create table user(user_id VARCHAR (255) NOT NULL PRIMARY KEY, email_id VARCHAR (50), password VARCHAR (255), fname VARCHAR (20), lname VARCHAR (20), phone INTEGER, address TEXT, city VARCHAR (20), state VARCHAR (20), pincode INTEGER, user_type VARCHAR (20))")
print("successful")
# conn.execute("create table userr(u_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, u_name VARCHAR (20), u_address TEXT, u_phone INTEGER UNIQUE)")
# conn.execute("create table registration (reg_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, p_id INTEGER NOT NULL REFERENCES property(p_id), user_id INTEGER NOT NULL REFERENCES userr(u_id), user_type BOOLEAN NOT NULL)")
# print("Table created successfully")  




conn.close()