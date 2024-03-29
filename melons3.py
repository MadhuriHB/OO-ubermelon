"""This file should have our order classes in it."""
import random
import datetime

class TooManyMelonsError(ValueError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)  
            
           
class AbstractMelonOrder(object):
    
    def __init__(self, species, qty):
        self.species = species
        if qty > 100:
            raise TooManyMelonsError("Too many melons!")
        
        self.qty = qty
        self.shipped = False

    def get_total(self, tax):
        """return the total amount"""
        base_price = self.get_base_price()
        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        """calculate random base price"""
        order_time = datetime.datetime.now()
        hour = order_time.hour
        day = order_time.weekday()
        
        base_price = random.randint(5, 10)

        if hour >= 8 and hour <= 11 and day >= 0 and day <= 4:
            base_price += 4
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
    """A government melon order""" 

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
