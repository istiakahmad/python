#basic
def welcome(name):
    print("Welcome {name}".format(name= name))
welcome('ahmad')

#positional arguments
def person(name, age, country): #get 3 parameter
    print(name, age, country, sep='|')
#argument maintain order
person('ahmad', 27, 'bd') #sent 3 arguments
person('Istiak', 25, 'bd')

#keyword arguments:
def person(name, age, country): #get 3 parameter
    print(name, age, country, sep='|')
#argument does not maintain order: after keyword argument, every argument must keyword
person(name='ahmad', age=27, country='bd') #sent 3 arguments
person('Istiak', 25, country='bd')

#Default Value: after defaulr parameter, every parameter  must have default value
def person(name, age, country="BD"): #get 3 parameter
    print(name, age, country, sep='|')
#argument does not maintain order: after keyword argument, every argument must keyword
person(name='ahmad', age=27, country='bd') #sent 3 arguments
person('Istiak', 25, country='bd')
