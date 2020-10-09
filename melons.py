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
    

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            base_price = 7.5
        else:
            base_price = 5

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





    
