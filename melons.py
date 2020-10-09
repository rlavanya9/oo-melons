from random import randint
from datetime import datetime

"""Classes for melon orders."""
class AbstractMelonOrder():

    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
       
    
    is_shipped = False


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.is_shipped = True
    
    def get_base_price(self):
        base_price = randint(5, 9)
        rush_start_time = datetime(2020, 10, 9, 8, 00, 00)
        rush_end_time = datetime(2020, 10, 9, 23, 00, 00 )
        current_time = datetime.now()
        print(current_time)
        print(base_price)
        if current_time > rush_start_time and current_time < rush_end_time :
            base_price = base_price + 4
            print("rush hour- base price:", base_price)

        return base_price


    def get_total(self):
        """Calculate price, including tax."""


        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price = 1.5 * base_price
       

        total = (1 + self.tax) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""


    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)

        self.country_code = country_code
    
    order_type = "international"
    tax = 0.17


    def get_total(self):
        if self.qty < 10:
             return super().get_total() + 3
        else:
            return super().get_total()


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):

        self.passed_inspection = passed





    
