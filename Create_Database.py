import sqlite3


def create_Database():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    # employee
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text, email text, gender text, contact text, dob text, doj text, password text, usertype text, address text, salary text)")
    con.commit()
    # supplier
    cur.execute(
        "CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,  contact text, discription text)")
    con.commit()
    # category
    cur.execute(
        "CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()
    # product
    cur.execute(
        "CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT ,Category text, Supplier text, name text, price text, qty text, status text)")
    con.commit()


create_Database()
