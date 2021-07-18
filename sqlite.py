import sqlite3 as sql
import uuid

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open('images/weihan/' + filename, 'rb') as file:
        blobData = file.read()
    return blobData

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open('images_database/' + str(filename) + '.png', 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

conn = sql.connect('memory.db')
c = conn.cursor()
#c.execute("""DROP TABLE user""")
#c.execute("""DROP TABLE family""")

def create():
    c.execute("""CREATE TABLE user (
    user_id INTEGER PRIMARY KEY,
    user_fname text,
    user_lname text)""")

    conn.commit()

    c.execute("""CREATE TABLE family (
        family_id TEXT NOT NULL,
        family_fname text,
        family_lname text,
        user_id text NOT NULL,
        PRIMARY KEY (family_id, user_id)
    )""")

    conn.commit()

    c.execute(
        """CREATE TABLE family_image (
        family_image_id TEXT NOT NULL,
        family_image_pic blob,
        family_image_descript,
        family_id,
        user_id,
        PRIMARY KEY (family_image_id, family_id, user_id)
        )"""
    )

    conn.commit()

def insert_user(fname, lname):
    try:
        conn = sql.connect('memory.db')
        c = conn.cursor()
        insert_blob = """INSERT INTO user (user_id, user_fname, user_lname) VALUES (?, ?, ?)"""
        data = ('1234', fname, lname)
        c.execute(insert_blob, data)
        print('Sucessful')
        conn.commit()
    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)


def insert_family(id, image, fname, lname):
    try:
        conn = sql.connect('memory.db')
        c = conn.cursor()
        insert_blob = """INSERT INTO family (family_id, family_fname, family_lname, user_id) VALUES (?, ?, ?, ?, ?)"""
        new_id = str(uuid.uuid4()).replace('-','')
        data = (new_id, fname, lname, id)
        c.execute(insert_blob, data)
        print('Sucessful')
        conn.commit()
        insert_image(new_id, id, image, 'first')
    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)

def insert_image(family_id, user_id, image, description):
    try:
        conn = sql.connect('memory.db')
        c = conn.cursor()
        insert_blob = """INSERT INTO family_image (family_image_id, family_image_pic, description, family_id, user_id) VALUES (?, ?, ?, ?)"""
        new_id = str(uuid.uuid4()).replace('-', '')
        image = convertToBinaryData(image)
        data = (new_id, image, description, family_id, user_id)
        c.execute(insert_blob, data)
        print('Sucessful')
        conn.commit()
    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)

#Assume names are unique
def get_user_id(gname, fname):
    conn = sql.connect('memory.db')
    c = conn.cursor()
    query = """SELECT user_id from user where user_fname = ? and user_lname = ?"""
    #query = """SELECT * from user"""
    #c.execute(query)
    c.execute(query, (gname, fname))
    rows = c.fetchall()
    for row in rows:
        print(row)
        return row[0]

def get_family_id(gname, fname, user_id):
    conn = sql.connect('memory.db')
    c = conn.cursor()
    query = """SELECT family_id from family where family_fname = ? and family_lname = ? and user_id = ?"""
    #query = """SELECT * from user"""
    #c.execute(query)
    c.execute(query, (gname, fname, user_id))
    rows = c.fetchall()
    for row in rows:
        print(row)
        return row[0]

def get_image(user_id, family_id):
    conn = sql.connect('memory.db')
    c = conn.cursor()
    query = """select family_image_pic, family_image_description from family_image where user_id = ? and family_id = ?"""
    c.execute(query, (user_id, family_id))
    records = c.fetchall()
    records = records[0][0]
    writeTofile(records, family_id)
    return records

conn.commit()
c.close()
conn.close()


