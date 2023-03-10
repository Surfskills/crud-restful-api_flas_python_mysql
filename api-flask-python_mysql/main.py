import pymysql

from app import app

from config import mysql

from flask import jsonify

from flask import flash, request



@app.route('/create', methods=['POST'])

def create_experiolearn():

    try:        

        _json = request.json

        _name = _json['name']

        _email = _json['email']

        _phone = _json['phone']	

        if _name and _email and _phone and _address and request.method == 'POST':

            conn = mysql.connect()

            cursor = conn.cursor(pymysql.cursors.DictCursor)		

            sqlQuery = "INSERT INTO emp(name, email, phone, address) VALUES(%s, %s, %s, %s)"

            bindData = (_name, _email, _phone, _address)            

            cursor.execute(sqlQuery, bindData)

            conn.commit()

            respone = jsonify('Employee added successfully!')

            respone.status_code = 200

            return respone

        else:

            return showMessage()

    except Exception as e:

        print(e)

    finally:

        cursor.close() 

        conn.close()          

     

@app.route('/experiolearn')

def experiolearn():

    try:

        conn = mysql.connect()

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT id, name, email, phone, address FROM experiolearn")

        empRows = cursor.fetchall()

        respone = jsonify(empRows)

        respone.status_code = 200

        return respone

    except Exception as e:

        print(e)

    finally:

        cursor.close() 

        conn.close()  



@app.route('/experiolearn/')

def experiolearn_details(experiolearn_id):

    try:

        conn = mysql.connect()

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT id, name, email, phone, address FROM emp WHERE id =%s", experiolearn_id)

        experiolearnRow = cursor.fetchone()

        respone = jsonify(experiolearnRow)

        respone.status_code = 200

        return respone

    except Exception as e:

        print(e)

    finally:

        cursor.close() 

        conn.close() 



@app.route('/update', methods=['PUT'])

def update_experiolearn():

    try:

        _json = request.json

        _id = _json['id']

        _name = _json['name']

        _email = _json['email']

        _phone = _json['phone']

        if _name and _email and _phone and _address and _id and request.method == 'PUT':			

            sqlQuery = "UPDATE experiolearn SET name=%s, email=%s, phone=%s, WHERE id=%s"

            bindData = (_name, _email, _phone, _id,)

            conn = mysql.connect()

            cursor = conn.cursor()

            cursor.execute(sqlQuery, bindData)

            conn.commit()

            respone = jsonify('Employee updated successfully!')

            respone.status_code = 200

            return respone

        else:

            return showMessage()

    except Exception as e:

        print(e)

    finally:

        cursor.close() 

        conn.close() 



@app.route('/delete/', methods=['DELETE'])

def delete_experiolearn(id):

	try:

		conn = mysql.connect()

		cursor = conn.cursor()

		cursor.execute("DELETE FROM experiolearn WHERE id =%s", (id,))

		conn.commit()

		respone = jsonify('Employee deleted successfully!')

		respone.status_code = 200

		return respone

	except Exception as e:

		print(e)

	finally:

		cursor.close() 

		conn.close()

        

       

@app.errorhandler(404)

def showMessage(error=None):

    message = {

        'status': 404,

        'message': 'Record not found: ' + request.url,

    }

    respone = jsonify(message)

    respone.status_code = 404

    return respone

        

if __name__ == "__main__":

    app.run()
