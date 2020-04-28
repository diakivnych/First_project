from flask import Flask, request, render_template
from person import Person

app = Flask(__name__)
import shelve
db = shelve.open('people3')

@app.route('/users/<int:id>')
def index(id):
    max_id = int(db['0'].id)
    human = db[str(id)] 
    return render_template("index.html", 
                            first_name = human.first_name,
                            last_name = human.last_name,
                            age = human.age,
                            job = human.job,
                            hobby = human.hobby,
                            id = id,
                            address = human.address,
                            max_id = max_id)

@app.route('/users')
def all_users():
    max_id = int(db['0'].id)
    return render_template("all_users.html", 
                            human = db,
                            max_id = max_id)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/users/new_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        next_id = str(int(db['0'].id) + 1)
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        job = request.form['job']
        hobby = request.form['hobby']
        human = Person(next_id, first_name, last_name, age, job, hobby)
        db[next_id] = human
        db['0']= Person(str(int(db['0'].id) + 1), '', '', '', '', '')
        #picture = request.files['picture']
        #picture.save('/home/dima/Study/Flask/Db/static/img100.jpg')
        return render_template("new_user.html")

    return render_template("new_user.html")

@app.route('/users/author')
def author():
    return render_template("author.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

db.close()