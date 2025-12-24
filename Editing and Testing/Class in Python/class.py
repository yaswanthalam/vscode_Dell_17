class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
        print("hello {} !".format(self.name))   

adam = person('Adam',25)   
adam.say_hello()  