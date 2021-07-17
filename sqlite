import sqlite3 as sql
import uuid

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

conn = sql.connect('memory')
c = conn.cursor()
c.execute("""CREATE TABLE user (
    user_id INTEGER PRIMARY KEY,
    user_fname text,
    user_lname text
""")

conn.commit()

c.execute("""CREATE TABLE family (
    family_id TEXT NOT NULL,
    family_image blob,
    family_fname text,
    family_lname text,
    PRIMARY KEY (family_id)
)""")

conn.commit()

def insert_user(fname, lname):
    try:
        insert_blob = """INSERT INTO family VALUES (id, image, fname, lname) VALUES (?, ?, ?, ?)"""
        new_id = str(uuid.uuid4()).replace('-','')
        data = (new_id, fname, lname)
        c.execute(insert_blob, data)
        print('Sucessful')
        conn.commit()
    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sql:
            sql.close()
            print("the sqlite connection is closed")


def insert_family(image, fname, lname):
    try:
        insert_blob = """INSERT INTO family VALUES (id, image, fname, lname) VALUES (?, ?, ?, ?)"""
        new_id = str(uuid.uuid4()).replace('-','')
        image = convertToBinaryData(image)
        data = (new_id, image, fname, lname)
        c.execute(insert_blob, data)
        print('Sucessful')
        conn.commit()
    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sql:
            sql.close()
            print("the sqlite connection is closed")

c.close()
conn.close()


