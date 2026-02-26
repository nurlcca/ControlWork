import sqlite3

connect = sqlite3.connect("users.db")

cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT NOT NULL
    );
""")

connect.commit()

#CRUD - CREATE, READ, UPDATE, DELETE
def create_user(name, age, hobby):
   # cursor.execute(f'INSERT INTO users (name, age, hobby) VALUES ("{name}", {age}, "{hobby}")')
    cursor.execute(
        "INSERT INTO users (name, age, hobby) VALUES (?, ?, ?)", 
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} added to users table")

#create_user("John", 40, "Football")

def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)

#get_users()

#def update_user(name, rowid):
    #cursor.execute(
        #"UPDATE users SET name = ? WHERE rowid = ?", 
        #(name, rowid)
    #)
    #connect.commit()
   # print("Updated")

#update_user(Ronaldo, 10)
#get_users()

#def delete_user(rowid):   
    #cursor.execute(
        #"DELETE FROM users WHERE rowid = ?", 
        #(rowid,)
    #)
    #connect.commit()
    #print("Deleted")

#delete_user(31)
#get_users()
def update_users(ids, name=None, age=None, hobby=None):
    if isinstance(ids, int):
        ids = [ids]

    for user_id in ids:
        if name is not None:
            cursor.execute("UPDATE users SET name = ? WHERE rowid = ?", (name, user_id))
        if age is not None:
            cursor.execute("UPDATE users SET age = ? WHERE rowid = ?", (age, user_id))
        if hobby is not None:
            cursor.execute("UPDATE users SET hobby = ? WHERE rowid = ?", (hobby, user_id))

    connect.commit()
    print("Users updated")

def delete_users(ids):
    if isinstance(ids, int):
        ids = [ids]

    for user_id in ids:
        cursor.execute("DELETE FROM users WHERE rowid = ?", (user_id,))

    connect.commit()
    print("Users deleted")


update_users([1, 2, 3], name="Alex")
update_users(range(4, 7), hobby="Chess")
update_users(8, age=30)

delete_users([10, 11])
delete_users(range(20, 25))
delete_users(30)

get_users()





