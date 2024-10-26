from typing import Self


class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, name: str, price: float, quantity: int = 1) -> Self:

        if price <= 0 or quantity <= 0:
            raise ValueError("Ціна та кількість повинні бути більшими за 0")
        if name not in self.__items:
            self.__items[name] = {}
        if price in self.__items[name]:
            self.__items[name][price] += quantity
        else:
            self.__items[name][price] = quantity

        return self

    def __len__(self) -> int:
        return len(self.__items)

    def __str__(self) -> str:
        result = "Кошик покупок:\n"
        total = 0.0
        for name, prices in self.__items.items():
            for price, quantity in prices.items():
                result += f"{name}: {quantity} шт. по {price:.2f} грн\n"
                total += price * quantity
        result += f"Загальна вартість: {total:.2f} грн"
        return result

    @property
    def total_cost(self) -> float:
        total = 0.0
        for prices in self.__items.values():
            for price, quantity in prices.items():
                total += price * quantity
        return total
