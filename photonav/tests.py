from django.test import TestCase
from .models import Image, Category, Location
import datetime as date

# Create your tests here.
class LocationTestCLass(TestCase):

    #setup method
    def setUp(self):
        self.locate = Location(name="Africa")
        self.locate.save_location()

    #Testing Instances
    def test_instance(self):
        self.assertTrue(isinstance(self.locate,Location))

    def test_save_method(self):
        self.locate.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.locate.save_location()
        self.locate.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.get_location_id(self.locate.id)
        location.update_location('Glasgow')
        location = Location.get_location_id(self.locate.id)
        self.assertTrue(location.name == 'Glasgow')

class CategoryTestClass(TestCase):

    #setup method
    def setUp(self):
        self.categ = Category(name="Art")
        self.categ.save_category()

    #Testing Instances
    def test_instance(self):
        self.assertTrue(isinstance(self.categ, Category))

    def test_save_method(self):
        self.categ.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.categ.save_category()
        self.categ.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.categ.id)
        category.update_category('Photography')
        category = Category.get_category_id(self.categ.id)
        self.assertTrue(category.name == 'Photography')
