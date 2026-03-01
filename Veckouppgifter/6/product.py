class Product:
    """Representerar produkter som kan visas i en webbshop."""

    name = ""
    price = 0
    count_in_stock = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.count_in_stock = 0


    def print_info(self):
        #print(f"{self.name} kostar {self.price} och det finns {self.count_in_stock} stycken i lager.")
        print(self.__str__())

    def set_stock(self, count):
        self.count_in_stock = count

    def __str__(self):
        return f"{self.name} kostar {self.price} och det finns {self.count_in_stock} stycken i lager."

skis = Product(name="Skidor", price=600)
ski_boots = Product(name="Pjäxor", price=800)

skis.set_stock(10)

skis.print_info()
ski_boots.print_info()

print(skis)
