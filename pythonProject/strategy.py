from typing import List


class BillingStrategy:
    def sum(self, drinks: List[int]) -> float:
        pass


class NormalStrategy(BillingStrategy):
    def sum(self, drinks: List[int]) -> float:
        return sum(drinks)


class HappyHourStrategy(BillingStrategy):
    def sum(self, drinks: List[int]) -> float:
        return sum(drinks) * 0.9

# Pokladňa (Context)
class CashDesk:
    def __init__(self):
        self.drinks = []
        self.strategy = NormalStrategy()

    def add(self, price):
        self.drinks.append(price)

    def print_bill(self):
        total_price = self.strategy.sum(self.drinks)
        print(f"Celkem k zaplaceni: {total_price}")
        print("Dekujeme za navstevu, vratte se znovu!")
        self.drinks = []

    def set_strategy(self, strategy):
        self.strategy = strategy


if __name__ == "__main__":
    cash_desk = CashDesk()

    # Happy Hour
    cash_desk.set_strategy(HappyHourStrategy())
    cash_desk.add(20)
    cash_desk.add(80)
    cash_desk.print_bill()

    # Koniec Happy Hour

    # Normálna stratégia
    cash_desk.set_strategy(NormalStrategy())
    cash_desk.add(20)
    cash_desk.add(80)
    cash_desk.print_bill()