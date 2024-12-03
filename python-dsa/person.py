class Person:
    def __init__(self,name,job = "none",pay = 0):
        self.name = name
        self.job = job
        self.pay = pay


    bob = Person(name = "Bob marlie",job = "buisness",pay = 1200)
    print(bob)