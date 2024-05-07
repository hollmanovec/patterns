# Create a class that performs the following operations on an array:
# -- display data in a file or on the screen
# -- flip data
# -- find maximum and minimum
# The class can get a set of values from a keyboard. Use the Strategy pattern and other necessary patterns

class ActionStrategy():
    def action(self, data):
        pass


class DisplayStrategy(ActionStrategy):
    def action(self, data, choice=None):
        if choice == None:
            choice = input("Zadejte volbu: [soubor]/[obrazovka]")

        if choice == "soubor":
            with open("StrategyTask.txt", "w") as file:
                file.writelines(data)

        if choice == "obrazovka":
            for i in data:
                print(i)

class FlipStrategy(ActionStrategy):
    def action(self, data):
        pass