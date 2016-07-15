"""This file should have our order classes in it."""
import random
class AbstractMelonOrder(object):
    
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self, tax):
        base_price = self.get_base_price()
        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        base_price = random.randint(5, 10)
        return base_price
        
class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.tax = 0.08

    def get_total(self):
        """Calculate price."""
        return super(DomesticMelonOrder, self).get_total(self.tax)
        
    
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self,species, qty, country_code):
        """Initialize melon order attributes"""
        
        self.country_code = country_code
        self.tax = 0.17
        super(InternationalMelonOrder, self).__init__(species, qty)
        

    def get_total(self):
        """Calculate price."""
        total = super(InternationalMelonOrder, self).get_total(self.tax)
        if self.qty<10:
            return total+3
        else:
            return total

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
      
    def __init__(self, species, qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty)
    
    def mark_inspection(self):
        self.passed_inspection = True

    def get_total(self):
        if self.passed_inspection == True:
            self.tax = 0
            total = super(GovernmentMelonOrder, self).get_total(self.tax)
            return total 
        else:
            print "You did not pass Inspection."
