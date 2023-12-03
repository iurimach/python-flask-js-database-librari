from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'I123456m@'
app.config['MYSQL_DB'] = 'sys'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Home route - Display all persons
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM person")
    persons = cur.fetchall()
    print(persons)
    cur.close()
    return render_template('index.html', persons=persons)

# Add data route
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        age = request.form['age']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO person (firstName, lastName, age) VALUES (%s, %s, %s)", (firstName, lastName, age))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    return render_template('add.html')

# Delete data route
@app.route('/delete/<int:person_id>')
def delete(person_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM person WHERE id = %s", (person_id,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))
#აბდეითი

@app.route('/update/<int:person_id>', methods=['GET', 'POST'])
def update(person_id):
    if request.method == 'POST':
        
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        age = request.form['age']
        print(firstName,'es aris formidan')
        cur = mysql.connection.cursor()
        cur.execute("UPDATE person SET FirstName=%s, LastName=%s, age=%s WHERE id=%s", (firstName, lastName, age, person_id))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM person WHERE id = %s", (person_id,))
    person = cur.fetchone()
    cur.close()

    return render_template('update.html', person=person)
# Search data route
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        column = request.form['column']

        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM person WHERE {column} LIKE %s", ('%' + keyword + '%',))
        persons = cur.fetchall()
        cur.close()

        return render_template('index.html', persons=persons)

    return render_template('search.html')

# Global search route
@app.route('/global_search', methods=['GET', 'POST'])
def global_search():
    if request.method == 'POST':
        keyword = request.form['keyword']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM person WHERE firstName LIKE %s OR lastName LIKE %s OR age LIKE %s",
                    ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        persons = cur.fetchall()
        cur.close()

        return render_template('index.html', persons=persons)

    return render_template('global_search.html')

if __name__ == '__main__':
    app.run(debug=True)
