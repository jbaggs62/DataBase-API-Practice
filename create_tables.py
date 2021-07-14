import mysql.connector
from mysql.connector import Error

#create connection using root to
connection = mysql.connector.connect(
    host="localhost",
    database="vaccineDB",
    user="root",
    password="password"
)

cursor=connection.cursor()

#create Tables
cursor.execute("create table IF NOT EXISTS Manufacturer("
               "ID          INT NOT NUll PRIMARY KEY,"
               "MName       VARCHAR(255),"
               "StreetNum   INT,"
               "StreetName  VARCHAR(255),"
               "Zip         VARCHAR(10),"
               "City        VARCHAR(255),"
               "State       VARCHAR(255));")

cursor.execute("create table IF NOT EXISTS Patient("
               "ID                  INT NOT NUll PRIMARY KEY,"
               "DOB                 DATE,"
               "FirstName           VARCHAR(255),"
               "LastName            VARCHAR(255),"
               "StreetNum           INT,"
               "StreetName          VARCHAR(255),"
               "City                VARCHAR(255),"
               "State               VARCHAR(255),"
               "Zip                 VARCHAR(10),"
               "Gender              VARCHAR(15));")
cursor.execute("CREATE TABLE Clinic("
               "ID                  INT NOT NULL PRIMARY KEY,"
               "CName              VARCHAR(255),"
               "StreetNum           INT,"
               "StreetName          VARCHAR(255),"
               "City                VARCHAR(255),"
               "State               VARCHAR(255),"
               "Zip                 VARCHAR(10));")
cursor.execute("CREATE TABLE Volunteer("
               "ID          INT NOT NULL PRIMARY KEY,"
               "FirstName   VARCHAR(255),"
               "LastName    VARCHAR(255),"
               "Age         Int(3),"
               "ClinicID    INT, FOREIGN KEY (ClinicID) REFERENCES Clinic(ID));")
cursor.execute("create table Dose ("
               "ManufacturerID      INT, FOREIGN KEY (ManufacturerID) REFERENCES Manufacturer(ID),"
               "LotID               VARCHAR(255),"
               "DoseNumber          INT,"
               "DateReceived        DATE,"
               "VolunteerID         INT, FOREIGN KEY (VolunteerID) REFERENCES Volunteer(ID),"
               "PatientID           INT, FOREIGN KEY (PatientID) REFERENCES Patient(ID),"
               "ClinicID            INT, FOREIGN KEY (ClinicID) REFERENCES Clinic(ID),"
               "PRIMARY KEY         (DoseNumber,PatientID,ManufacturerID));")



