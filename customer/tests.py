from django.test import TestCase
from customer.models import Customer
from django.contrib.auth.models import User


class CustomerTestCases(TestCase):
    def createCustomer(self, name="testName", country="Ireland", phone="0876842345"):
        u1 = User(username=name)
        u1.save()
        return Customer.objects.create(user=u1, country=country, phone=phone)

    def test_Customer_creation(self):
        c1 = self.createCustomer()
        # success - c1 is a customer instance
        # fail - c1 is not a customer instance
        self.assertTrue(isinstance(c1, Customer))

        # success - returns a string
        # fail - returns non string
        self.assertTrue(isinstance(c1.__str__(), str))

    def testPhoneNumber(self):
        c1 = self.createCustomer()
        phoneNumber = str(c1).split()[2]
        # success - length of phone number is 10
        # fail - length of phone number is less than or greater than 10
        self.assertTrue(len(phoneNumber),10)

