class VendingMachineState:
    def action(self, vending_machine):
        pass


class WaitingForMoney(VendingMachineState):
    def action(self, vending_machine):
        print("Waiting for money")
        if vending_machine.money >= vending_machine.price_of_drink:
            vending_machine.change_state(SufficientMoney())


class SufficientMoney(VendingMachineState):
    def action(self, vending_machine):
        print("Sufficient money. Drink dispensed.")
        vending_machine.money = 0
        vending_machine.change_state(WaitingForMoney())


class VendingMachine:
    def __init__(self, price_of_drink):
        self.price_of_drink = price_of_drink
        self.state = WaitingForMoney()
        self.money = 0

    def change_state(self, new_state):
        self.state = new_state

    def insert_money(self, amount):
        self.money += amount
        self.state.action(self)


# TODO spravne prepinanie stavov

vending_machine = VendingMachine(20)

vending_machine.insert_money(10)
vending_machine.insert_money(10)
vending_machine.change_state(SufficientMoney())
vending_machine.insert_money(0)