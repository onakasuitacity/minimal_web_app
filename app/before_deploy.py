from pymysql import connect, cursors

connection = connect(
    host="db",
    user="root",
    port=3306,
    cursorclass=cursors.DictCursor,
    password="hoge"
)

with connection.cursor() as cursor:
    cursor.execute("CREATE DATABASE IF NOT EXISTS test;")
    cursor.execute("USE test;")
    cursor.execute("CREATE TABLE IF NOT EXISTS fruit(id int auto_increment, name varchar(10), index(id));")
    cursor.execute("TRUNCATE fruit;")
    cursor.execute("INSERT INTO fruit(name) VALUES ('apple'), ('orange'), ('banana');")

connection.commit()
connection.close()