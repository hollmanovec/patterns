class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        self.subordinates.remove(employee)

    def display_information(self, indentation=0):
        print(" " * indentation + self.name + " - " + self.position)
        for subordinate in self.subordinates:
            subordinate.display_information(indentation + 4)


ceo = Employee("Jan Novak", "CEO")

head_of_development = Employee("Petr Svoboda", "Head of Development")
ceo.add_subordinate(head_of_development)

developer1 = Employee("Lucie Cerna", "Developer")
developer2 = Employee("Tomas Dvorak", "Developer")
head_of_development.add_subordinate(developer1)
head_of_development.add_subordinate(developer2)

ceo.display_information()