from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def execute_query(query):
  db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0013',
    database='myproject'
  )

  mycursor = db.cursor()
  mycursor.execute(query)
  db.commit()
  myresult = mycursor.fetchall()
  return myresult


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        course = request.form.get('course')

        # q = """INSERT INTO registration(username, password, course)
        #     VALUES
        #     ("username", "password}", "source");"""

        sqlquery = f'insert into registration values("{username}", "{password}", "{course}")'
        
        execute_query(sqlquery)

        return redirect(url_for('success'))

    return render_template('template.html')

@app.route('/success')
def success():
    return render_template('last.html')


if __name__ == '__main__':
    app.run(debug=True)

