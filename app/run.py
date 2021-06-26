from flask import Flask, render_template
from pymysql import connect, cursors
from time import sleep

app = Flask(__name__)
while True:
    try:
        connection = connect(
            host="db",
            port=3306,
            user="root",
            password="hoge",
            database="test",
            cursorclass=cursors.DictCursor,
        )
        break
    except:
        print("Couldn't connect to database. trying to reconnect in 3 seconds")
        sleep(3)
cursor = connection.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM fruit;")
    return render_template("index.html", data=cursor.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)