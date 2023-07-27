# Code Consultation in VetsApp Project
import datetime

"""
    create table Customer(
        cid int primary key auto_increment,
        name text,
        phone text unique key,
        email text,
        age int,
        gender text,
        address text,
        createdon datetime
    );
    
    create table Pet(
        pid int primary key auto_increment,
        name text,
        age int,
        weight int,
        breed text,
        gender text,
        cid int,
        createdon datetime,
        FOREIGN KEY (cid) REFERENCES Customer(cid)
    );
    
     create table Consultation(
        cnid int primary key auto_increment,
        cid int,
        pid int,
        problem text,
        heartrate int,
        temperature float,
        medicines text,        
        createdon datetime,
        FOREIGN KEY (cid) REFERENCES Customer(cid),
        FOREIGN KEY (pid) REFERENCES Pet(pid)
    );
    
    
"""


class Consultation:

    def __init__(self):
        self.cnid = 0
        self.cid = 0
        self.pid = 0
        self.problem = ""
        self.heartrate = 0
        self.temperature = 98.4
        self.medicines = ""
        self.createdon = ""

    def read_consultation_data(self):
        self.problem = input("Enter Problem: ")
        self.heartrate = int(input("Enter Heart Rate: "))
        self.temperature = float(input("Enter Temperature: "))
        self.medicines = input("Enter Medicines: ")

        # Get the date and time
        self.createdon = str(datetime.datetime.today())
        # Eliminate Milli Seconds
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = "insert into Consultation values(null, {cid}, {pid}, '{problem}'," \
              "{heartrate}, {temperature}, '{medicines}', '{createdon}');".format_map(vars(self))
        return sql

    def get_consultation_sql_query(self, cid="", pid=""):
        sql = "select * from Consultation"

        if len(cid) != 0:
            sql = "select * from Consultation where cid = {}".format(cid)

        if len(pid) != 0:
            sql = "select * from Consultation where pid = {}".format(pid)

        return sql


    def get_consultation_sql_query_by_date(self, date=""):
        sql = "select * from Consultation where createdon = '{}'".format(date)
        return sql


    def get_delete_sql_query(self):
        sql = "delete from Consultation where cnid = {}".format(self.cnid)
        return sql