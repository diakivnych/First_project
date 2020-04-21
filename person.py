class Person:
    #max_id = 0
    def __init__(self, id, first_name, last_name, age, job, hobby):
        #Person.max_id += 1
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.hobby = hobby
        self.address = "img"+str(self.id)+".jpg"
    def __str__(self):
        return "first_name = {} \nlast_name = {} \nage = {} \njob = {} \nhobby = {}".format(self.first_name, self.last_name, self.age, self.job, self.hobby)
    def get_id(self):
        return self.id
