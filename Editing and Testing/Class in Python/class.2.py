class person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello {self.name}!")

adam = person('Adam')
adam.say_hello()
