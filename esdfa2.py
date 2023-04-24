from flask import Flask, jsonify, request
import sqlite3
from flask_cors import cross_origin, CORS
app = Flask(__name__)
CORS(app, resources={r'*': {'origins': '*'}})


#-----------CREATE/INSERT----------------

def insert_property(property):
    conn = sqlite3.connect('landd.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO property(p_name, p_description, p_type, p_price, p_address, p_pincode) VALUES (?, ?, ?, ?, ?, ?)", (property['name'], property['description'], property['type'], property['price'], property['address'], int(property['pincode'])))
    conn.commit()
    conn.close()
    conn.close()
    return jsonify({'message': 'User created successfully'})

def insert_user(user):
    conn = sqlite3.connect('landd.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO userr(u_name, u_address, u_phone) VALUES (?, ?, ?)", (user['name'], user['address'], int(user['phone'])))
    conn.commit()
    conn.close()
    conn.close()
    return jsonify({'message': 'User created successfully'})

#----------READ/DISPLAY---------------

def list_users():
    conn = sqlite3.connect('landd.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userr")
    data=cursor.fetchall()
    user=[]
    print("dataaaaaaaaaaaa")
    print(data)
    for i in data:
            print(i)
            userdata = {}
            userdata["user_id"] = str(i[0])
            userdata["name"] = i[1]
            userdata["address"] = i[2]
            userdata["phone"] = str(i[3])
            user.append(userdata)

    conn.commit()
    conn.close()
    return user

def list_properties():
    conn = sqlite3.connect('landd.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM property")
    data=cursor.fetchall()
    properties=[]
    print("dataaaaaaaaaaaa")
    print(data)
    for i in data:
            print(i)
            propertydata = {}
            propertydata["p_id"] = str(i[0])
            propertydata["name"] = i[1]
            propertydata["description"] = i[2]
            propertydata["type"] = i[3]
            propertydata["price"] = str(i[4])
            propertydata["address"] = i[5]
            propertydata["pincode"] = str(i[6])
            properties.append(propertydata)

    conn.commit()
    conn.close()
    return properties

#---------------UPADTE-----------------

def update_user(user):
    conn = sqlite3.connect('landd.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE userr SET u_name = ?, u_address = ?, u_phone = ? WHERE u_id =?",(user["name"], 
                                                                                            user["address"], int(user["phone"]), int(user["u_id"]),))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User updated successfully'})

#-----------------DELETE-------------------

def delete_user(user_id):
    message = {}
    conn = sqlite3.connect('landd.db')
    conn.execute("DELETE from userr WHERE u_id = ?",(user_id))
    conn.commit()
    message["status"] = "User deleted successfully"
   
    conn.close()
    return message

def delete_property(property_id):
    message = {}
    conn = sqlite3.connect('landd.db')
    print(property_id)
    conn.execute("DELETE from property WHERE p_id = ?",(property_id))
    conn.commit()
    message["message"] = "Property deleted successfully"
    message["success"] = True
    
   
    conn.close()
    return message
#----------CREATING CRUD API---------------

@app.route('/addusers',  methods = ['POST'])
def add_user():
    user = request.get_json()
    print(user)
    msg=insert_user(user)
    print(msg)
    return jsonify({'message': 'User created successfully'})

@app.route('/addproperty', methods = ['POST'])
def add_property():
    property = request.get_json()
    # print(property)
    msg=insert_property(property)
    print(msg)
    return jsonify({'message': 'User created successfully'})

@app.route('/showusers', methods=['GET'])
# @cross_origin(origins=['http://localhost:3000/'])
def get_users():
    msg=list_users()
    return jsonify(msg)


@app.route('/showproperties', methods=['GET'])
def get_properties():
    msg=list_properties()
    return jsonify(msg)

@app.route('/updateusers',  methods = ['PUT'])
def update_userr():
    user = request.get_json()
    msg=update_user(user)
    print(msg)
    return jsonify({'message': 'User updated successfully'})
    # return jsonify(update_user(user))

@app.route('/deleteusers/<user_id>',  methods = ['DELETE'])
def delete_userr(user_id):
    return jsonify(delete_user(user_id))

@app.route('/deleteproperty/<p_id>',  methods = ['DELETE'])
def delete_propertyy(p_id):
    return jsonify(delete_property(p_id))

if __name__ == '__main__':
    app.run()


# def list_user_by_id(u_id):
#     conn = sqlite3.connect('landd.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM userr WHERE u_id = ?", (u_id))
#     data=cursor.fetchone()
#     user={}
#     user["user_id"] = str(data[0])
#     user["name"] = data[1]
#     user["address"] = data[2]
#     user["phone"] = str(data[3])

#     conn.commit()
#     conn.close()
#     return jsonify(user) 

# @app.route('/showusersid/<user_id>', methods=['GET'])
# def get_user(user_id):
#     msg=list_user_by_id(user_id)
#     print(msg)
#     return jsonify(msg)
