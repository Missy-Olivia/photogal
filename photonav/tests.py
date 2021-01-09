from django.test import TestCase
from .models import Image, Category, Location
import datetime as date

# Create your tests here.
class LocationTestCLass(TestCase):

    #setup method
    def setUp(self):
        self.locate = Location(name="Africa")
        self.locate.save_location()
        
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.locate,Location))

