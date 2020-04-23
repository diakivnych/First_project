from flask import Flask, render_template
from person import Person

app = Flask(__name__)
import shelve
db = shelve.open('people3')

@app.route('/users/<int:id>')
def index(id):
    human = db[str(id)] 
    return render_template("index.html", 
                            first_name = human.first_name,
                            last_name = human.last_name,
                            age = human.age,
                            job = human.job,
                            hobby = human.hobby,
                            id = id,
                            address = human.address)

@app.route('/users')
def all_users():
    return render_template("all_users.html", 
                            human = db)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/users/new_user')
def add_user():
    return render_template("new_user.html")

@app.route('/users/author')
def author():
    return render_template("author.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

db.close()