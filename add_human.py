from person import Person

from test import db

import shelve
print(db['1'].age)
db.close()