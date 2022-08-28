class Nikola:
    def __init__(self, name, age):
        self.age = age
        if name != "Николай":
            self.name = f'Я не {name}, а Николай'
        else:
            self.name = name