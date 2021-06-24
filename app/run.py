from flask import Flask, render_template
from pymysql import connect, cursors

app = Flask(__name__)
connection = connect(
    host="db",
    port=3306,
    user="root",
    password="hoge",
    database="test",
    cursorclass=cursors.DictCursor,
)
cursor = connection.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM fruit;")
    return render_template("index.html", data=cursor.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)