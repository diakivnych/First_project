import shelve

from person import Person


def add_person():
    first_name = input('first_name = ')
    last_name = input('last_name = ')
    age = input('age = ')
    job = input('job = ')
    hobby = input('hobby = ')
    new_person = Person(first_name, last_name, int(age), job, hobby)
    db[str(new_person.get_id())] = new_person

def del_person():
    id = input('id person what you need to delete -> ')
    del db[id]

def change_person():
    id = input('id person what you need to change ->')
    first_name = input('first_name = ')
    last_name = input('last_name = ')
    age = input('age = ')
    job = input('job = ')
    hobby = input('hobby = ')
    new_person = Person(first_name, last_name, int(age), job, hobby)
    db[str(id)] = new_person


db = shelve.open('people2')
while True:
    print('All users:')
    mx_id = 0
    mx_len = 0
    for human in db.values():
        mx_len = max(mx_len, len(human.last_name))
        mx_id = max(mx_id, human.get_id())

    for human in db.values():
        print(human.last_name, end='')
        for j in range(mx_len-len(human.last_name)):
            print(end=' ')
        print('->id =', human.get_id())
    Person.max_id = mx_id
    print("\n| 1 - add object | 2 - del object | 3 - change object | 4 - show object | 5 - exit |")

    t = input()
    if t == '1':
        try:
            add_person()
        except BaseException:
            print('ERROR')
        else: 
            print('OK :)')
    if t == '2':
        try:
            del_person()
        except BaseException:
            print('ERROR\n')
        else:
            print('OK :)\n')
    if t == '3':
        try:
            change_person()
        except BaseException:
            print('ERROR')
        else:
            print('OK :)')
    if t == '4':
        try: 
            human = input('What is a person? -> ')
            print(db[human])
            print()
        except BaseException:
            print('ERROR')
        else:
            print('OK :)')

    if t == '5':
        print("That's all")
        break

db.close()