import sqlite3 as sql
import uuid

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open('images/weihan' + filename, 'rb') as file:
        blobData = file.read()
    return blobData

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open('images_database' + filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

conn = sql.connect('memory')
c = conn.cursor()
c.execute("""DROP TABLE user""")
c.execute("""DROP TABLE family""")

c.execute("""CREATE TABLE user (
    user_id INTEGER PRIMARY KEY,
    user_fname text,
    user_lname text)
""")

conn.commit()

c.execute("""CREATE TABLE family (
    family_id TEXT NOT NULL,
    family_image blob,
    family_fname text,
    family_lname text,
    user_id text NOT NULL,
    PRIMARY KEY (family_id, user_id)
)""")

conn.commit()

def insert_user(fname, lname):
    try:
        conn = sql.connect('memory')
        c = conn.cursor()
        insert_blob = """INSERT INTO family VALUES (id, image, fname, lname) VALUES (?, ?, ?, ?)"""
        new_id = str(uuid.uuid4()).replace('-','')
        data = (new_id, fname, lname)
        c.execute(insert_blob, data)
        print('Sucessful')
        conn.commit()
    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)


def insert_family(id, image, fname, lname):
    try:
        conn = sql.connect('memory')
        c = conn.cursor()
        insert_blob = """INSERT INTO family VALUES (id, image, fname, lname) VALUES (?, ?, ?, ?)"""
        new_id = str(uuid.uuid4()).replace('-','')
        image = convertToBinaryData(image)
        data = (new_id, image, fname, lname, id)
        c.execute(insert_blob, data)
        print('Sucessful')
        conn.commit()
    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)

#Assume names are unique
def get_user_id(gname, fname):
    conn = sql.connect('memory')
    c = conn.cursor()
    query = """SELECT user_id from user where user_fname = ? and user_lname = ?"""
    c.execute(query, (gname, fname, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
        return row

def get_image(id):
    conn = sql.connect('memory')
    c = conn.cursor()
    query = """select family_image from family where user_id = ?"""
    c.execute(query, (id))
    records = c.fetchall()
    records = records[0]
    writeTofile(records, id)
    return records

conn.commit()
c.close()
conn.close()


