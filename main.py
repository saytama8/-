from flask import Flask, url_for , redirect
import sqlite3 


def index():
    conn = sqlite3.connect("Artistc.db")
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM artists WHERE "Birth Year" = (?)', [year])
    data = cursor.fetchall()


    if len(data)==0:
        return "У базі немає даних."
    elif len(data)==1:
        return "У цому році народився 1 художник"
    else:
        r = "<h3>Список художників</h3>"
        for person in data:
            r += person[0]
    return r

year = int(input("Введіть рік"))

app = Flask(__name__)
app.add_url_rule("/", "index" , index)

if __name__ == "__main__":
    app.run()