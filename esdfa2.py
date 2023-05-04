from flask import Flask, jsonify, request, make_response
import sqlite3
import bcrypt
from flask_cors import cross_origin, CORS
import uuid

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
    user_id = uuid.uuid1()
   
    password=user['password'].encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    print("USER ID TYPE ====>", type(user_id.hex))
    cursor.execute("INSERT INTO user(user_id, email_id, password, fname, lname, phone, address, city, state, pincode, user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id.hex , user['email_id'], hashed, user['fname'], user['lname'],int(user['phone']), user['address'], user['city'], user['state'], int(user['pincode']), user['user_type']))
    print("SUCCESSFULLY")
    conn.commit()
    conn.close()
    conn.close()
    return {'message': 'User created successfully', 'user_id': str(user_id)}

#----------READ/DISPLAY---------------

def validate_user(login_data):
    conn = sqlite3.connect('landd.db')
    cursor = conn.cursor()
    u_name= login_data["u_name"]
    u_password = login_data["u_password"]
    print("data11------>", u_name, u_password)
    try:
        cursor.execute("SELECT * FROM user WHERE fname = ?", (u_name,))
        data=cursor.fetchone()
        u_id=data[0]
        name=data[3]
        pwd=data[2]
        # print("dataaa==========>", name, pwd)
        password = u_password.encode('utf-8')
        if bcrypt.checkpw(password, pwd):
            conn.commit()
            conn.close()
            return {'u_name': name, 'u_id': str(u_id)}
        else:
            conn.commit()
            conn.close()
            return {}
    except:
        return {}
     

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
    pwd=user["pwd"]
    password=pwd.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    cursor.execute("UPDATE userr SET u_pwd=? WHERE u_id =?",(hashed, int(user["u_id"]),))
    conn.commit()
    # demo="sunny"
    # check = demo.encode('utf-8') 
    # if bcrypt.checkpw(check, hashed):
    #     print("pwd ======> login success")
    # else:
    #     print("pwd ======> incorrect password")
    conn.close()

    return jsonify({'message': 'User updated successfully'})

def update_property(property):
    conn = sqlite3.connect('landd.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE property SET status=? WHERE p_id =?",(property["status"], int(property["p_id"]),))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User updated successfully'})

#-----------------DELETE-------------------

def delete_user(user_id):
    message = {}
    conn = sqlite3.connect('landd.db')
    conn.execute("DELETE * from user WHERE u_id = ?",(user_id))
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
    print("USER_ID ==>",msg['user_id'])
    return jsonify({'status': 'User created successfully', 'message': msg['user_id']})

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

@app.route('/login', methods=['POST'])
def get_login_data():
    login_data=request.get_json()
    msg = validate_user(login_data)
    print("message ==>", msg)
    if msg=={}:
        return jsonify({'success': False, 'error': True, 'message': "username or password is incorrect", 'data': {}})
    else:
        return jsonify({'success': True, 'data': msg, 'error': False, 'message': "user logged in successfully"})


@app.route('/showproperties', methods=['GET'])
def get_properties():
    msg=list_properties()
    return jsonify(msg)

@app.route('/updateproperty',  methods = ['PUT'])
def update_properties():
    property = request.get_json()
    msg=update_property(property)
    print(msg)
    return jsonify({'message': 'User updated successfully'})

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




