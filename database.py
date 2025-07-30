import pymysql
from tkinter import messagebox

#connection

def db_connection():

    global cursor,conn

    try:
        conn=pymysql.connect(host="localhost",user="root",password="your_password")
        cursor=conn.cursor()

    except:
        messagebox.showerror("ERROR","Failed to connect to database")
        return

    cursor.execute("CREATE database IF NOT EXISTS employee")
    cursor.execute("USE employee")
    cursor.execute("CREATE table IF NOT EXISTS employee_data (id VARCHAR(10), name VARCHAR(50), phone VARCHAR(10), role VARCHAR(30), gender VARCHAR(10), salary VARCHAR(10))")
    
db_connection()

def id_exists(id):
    cursor.execute("SELECT COUNT(*) FROM employee_data WHERE id=%s",id)
    result=cursor.fetchone()
    return result[0] > 0

def insert(id,name,phone,role,gender,salary):
    cursor.execute("INSERT INTO employee_data VALUES (%s,%s,%s,%s,%s,%s)",(id,name,phone,role,gender,salary))
    conn.commit()

def fetch_details():
    cursor.execute("SELECT * FROM employee_data")
    result=cursor.fetchall()
    return result

def update(new_id,new_name,new_phone,new_role,new_gender,new_salary):
    cursor.execute("UPDATE employee_data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s",(new_name,new_phone,new_role,new_gender,new_salary,new_id))
    conn.commit()

def delete(id):
    cursor.execute("DELETE FROM employee_data WHERE id=%s",id)
    conn.commit()

def delete_all():
    cursor.execute("TRUNCATE table employee_data")
    conn.commit()

def search_emp(option,value):
    cursor.execute(f"SELECT * FROM employee_data WHERE {option}=%s",value)
    result=cursor.fetchall()
    return result