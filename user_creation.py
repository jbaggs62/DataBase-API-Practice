import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
    host="localhost",
    database="vaccineDB",
    user="root",
    password="password"
)


# Function to create user

def createUser(cursor, userName, password):
    try:
        sqlCreateUser = "CREATE USER IF NOT EXISTS '%s'@'localhost' IDENTIFIED BY '%s';" % (userName, password)
        cursor.execute(sqlCreateUser)
    except Exception as e:
        print("Error creating MySQL User: %s" % (e))


cursor = connection.cursor();

# create users one power and one test user to represent a user of our application
createUser(cursor, "powerUser", "pass123")
createUser(cursor, 'testUser1', "pass456")
createUser(cursor, 'jacobbaggs1', 'password')
# make sure we have the users
mySqlListUsers = "select host, user from mysql.user;";
cursor.execute(mySqlListUsers)

# Fetch all the rows
userList = cursor.fetchall()
# Print all the users
print("List of users:")
for user in userList:
    print(user)


def grantPrivs(cursor, privs, dataBase, userName):
    try:
        sqlGrantPowers = "GRANT %s on %s.* TO %s@localhost;" % (privs, dataBase, userName)
        print(sqlGrantPowers)
        cursor.execute(sqlGrantPowers)
    except Exception as e:
        print("Error Grant Privileges to : %s" % (e))


grantPrivs(cursor, "SELECT, INSERT, DELETE, UPDATE", "vaccineDB", "powerUser")
grantPrivs(cursor, "SELECT, INSERT, DELETE, UPDATE", "vaccineDB", "jacobbaggs")


if connection.is_connected():
    cursor.close()
    connection.close()
    print("Mysql connection is closed")
