
class user_model(object):

    def __init__(self, user_id, name, lastname, age):
        self.user_id = user_id
        self.name = name
        self.lastname = lastname
        self.age = age

    def __str__(self):
        print "{} {} {} {}".format(self.user_id, self.name, self.lastname, self.age)


#a = user_model(1, 'Matias', 'Iacono', 39)
#print a.__dict__
