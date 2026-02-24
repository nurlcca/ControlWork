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

def delete_user(rowid):   
    cursor.execute(
        "DELETE FROM users WHERE rowid = ?", 
        (rowid,)
    )
    connect.commit()
    print("Deleted")

delete_user(31)
get_users()






