class person:
    def __init__(self, speak, age):
        self.speak = speak
        self.age = age

class student(person):
    def __init__(self, name):
        super. __init__()
        self.speak = name

class teacher(person):
    def __init__(self, LastName):
        super. __init__()
        self.speak = LastName

a_person = person("hoi", 20)
a_student= student("hallo", 19)
a_teacher= teacher("Gutentag", 40)

print ()



