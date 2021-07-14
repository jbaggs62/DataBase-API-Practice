import pymysql
from app import app
from config import mysql
from flask import jsonify, request


@app.route('/Manu')
def get_Manu():
    try:
        _json = request.json
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM manufacturer")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/shotGiver')
def get_shotGiver():
    try:
        _json = request.json
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select DISTINCT ID, FirstName, LastName from Volunteer")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/shotGiven')
def get_shotGiven():
    try:
        _json = request.json
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "Select Distinct VolunteerID, FirstName, LastName, Count(PatientID) as Shots_Adminstered from Dose inner join Volunteer on Dose.VolunteerID = Volunteer.ID group by VolunteerID")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/doseByManu')
def get_doseByManu():
    try:
        _json = request.json
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "Select Distinct ManufacturerID, MName, Count(PatientID) as Dose_Adminstered from Dose inner join Manufacturer on Dose.ManufacturerID = Manufacturer.ID group by ManufacturerID")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/PatientByLotID')
def get_PatientByLotID():
    try:
        _json = request.json
        _lotID = _json['lotID']
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = f"Select ID, FirstName, LastName from Patient Inner Join Dose on Patient.ID= Dose.PatientID where Dose.LotID='{_lotID}'"
        print(sqlQuery)
        cursor.execute(sqlQuery)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/PatientWithFirstDose')
def get_PatientWithFirstDose():
    try:
        _json = request.json
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "Select ID, FirstName, LastName, DateReceived from Patient Inner Join Dose on Patient.ID= Dose.PatientID where DoseNumber=1")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/AgeAtVaccination')
def get_AgeAtVaccination():
    try:
        _json = request.json
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "Select ID, FirstName, LastName, Floor(DATEDIFF(Dose.DateReceived, DOB ) / 365.25) as age from Patient Inner Join Dose on Patient.ID= Dose.PatientID where DoseNumber=1")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/AvgAgeOfVolunteers')
def get_AvgAgeOfVolunteers():
    try:
        _json = request.json
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT AVG(AGE) as AverageAge from Volunteer")
        row = cursor.fetchone()
        value = str(row)
        resp = jsonify(value)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/INSERT')
def Insert():
    try:
        _json = request.json
        _table = _json['table']
        _columns = _json['columns']
        _values = _json['values']
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        sqlQuery = f"INSERT INTO {_table}({_columns}) VALUES({_values})"
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = (sqlQuery)
        cursor.execute(query)
        conn.commit()
        resp = jsonify(query)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/SELECT')
def Select():
    try:
        _json = request.json
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        _query = _json['query']
        sqlQuery = f"{_query}"
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = (sqlQuery)
        cursor.execute(query)
        row = cursor.fetchall()
        value = str(row)
        resp = jsonify(value)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/DELETE')
def Delete():
    try:

        _json = request.json
        _table = _json['table']
        _where = _json['where']
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        sqlQuery = f"DELETE From {_table} where {_where}"
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = (sqlQuery)
        cursor.execute(query)
        conn.commit()
        resp = jsonify(query)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@app.route('/AdminQuery')
def Query():
    try:

        _json = request.json
        _query = _json['query']
        app.config['MYSQL_DATABASE_USER'] = _json['UserName']
        app.config['MYSQL_DATABASE_PASSWORD'] = _json['Password']
        sqlQuery = f"{_query}"
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = (sqlQuery)
        cursor.execute(query)
        conn.commit()
        resp = jsonify(query)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(debug=True)
