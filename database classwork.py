import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="example_database"
)

# Create a cursor
cursor = conn.cursor()

# Create a table (similar to a collection in MongoDB)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
""")

# Insert data
user_data = [
    ("Ayomide Ogunsona", 25),
    ("Paul Shags", 30),
    ("Daniel Lucky", 20),
]

cursor.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", user_data)
conn.commit()
print("Data inserted successfully.")

# Read data
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
print("\nAll Users:")
for user in all_users:
    print(user)

# Update data
update_query = "UPDATE users SET age = %s WHERE name = %s"
update_data = (26, "Ayomide Ogunsona")
cursor.execute(update_query, update_data)
conn.commit()
print("\nUser 'Ayomide Ogunsona' updated.")

# Modify data
modify_query = "UPDATE users SET name = %s WHERE name = %s"
modify_data = ("Ayomide Michaelson", "Ayomide Ogunsona")
cursor.execute(modify_query, modify_data)
conn.commit()
print("\nUser 'Ayomide Ogunsona' modified to 'Johnathan Doe'.")

# Read data after modification
cursor.execute("SELECT * FROM users")
all_users_after_update = cursor.fetchall()
print("\nAll Users After Update:")
for user in all_users_after_update:
    print(user)

# Delete data
delete_query = "DELETE FROM users WHERE name = %s"
delete_data = ("Daniel Lucky",)
cursor.execute(delete_query, delete_data)
conn.commit()
print("\nUser 'Daniel Lucky' deleted.")

# Read data after deletion
cursor.execute("SELECT * FROM users")
all_users_after_deletion = cursor.fetchall()
print("\nAll Users After Deletion:")
for user in all_users_after_deletion:
    print(user)

# Close the cursor and connection
cursor.close()
conn.close()
