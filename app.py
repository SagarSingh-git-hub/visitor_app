from flask import Flask, render_template, request, redirect, session
from db import get_db

app = Flask(__name__)
app.secret_key = "secret123"

# 🔐 LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        db = get_db()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (u,p))
        user = cur.fetchone()

        if user:
            session['user'] = u
            return redirect('/')
        else:
            return render_template("login.html", error="Invalid Login")

    return render_template("login.html")


# 🚪 LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# 🏠 HOME (Protected)
@app.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM visitors")
    data = cursor.fetchall()
    return render_template("index.html", visitors=data)


# ➕ ADD VISITOR
@app.route('/add', methods=['GET','POST'])
def add():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        purpose = request.form['purpose']
        meet = request.form['meet']

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO visitors(name,phone,purpose,meet_person) VALUES(%s,%s,%s,%s)",
            (name, phone, purpose, meet)
        )
        db.commit()
        return redirect('/')

    return render_template("add.html")


# ✏ EDIT VISITOR
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        purpose = request.form['purpose']
        meet = request.form['meet']

        cursor.execute(
            "UPDATE visitors SET name=%s, phone=%s, purpose=%s, meet_person=%s WHERE id=%s",
            (name, phone, purpose, meet, id)
        )
        db.commit()
        return redirect('/')

    cursor.execute("SELECT * FROM visitors WHERE id=%s", (id,))
    visitor = cursor.fetchone()
    return render_template("edit.html", visitor=visitor)


# ❌ DELETE
@app.route('/delete/<int:id>')
def delete(id):
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM visitors WHERE id=%s", (id,))
    db.commit()
    return redirect('/')


# 🚪 EXIT TIME
@app.route('/exit/<int:id>')
def exit_visitor(id):
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE visitors SET exit_time = NOW() WHERE id=%s", (id,))
    db.commit()
    return redirect('/')


app.run(debug=True)
