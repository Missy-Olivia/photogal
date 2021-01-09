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

class ImageTestClass(TestCase):
    #setup method
    def setUp(self):

        self.categ = Category(name="Art")
        self.categ.save_category()

        self.locate = Location(name="Africa")
        self.locate.save_location()

        self.image = Image(name="image one", description='my image',image_location=self.locate, image_category=self.categ)
        self.image.save_image()

    #Testing Instances
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.categ.delete_category()
        self.locate.delete_location()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        images = Image.search_by_category('art')
        self.assertTrue(len(images)>0)

    def test_filter_by_location(self):
        images = Image.filter_by_location('1')
        print(images)
        self.assertTrue(len(images)>0)

    def test_update_image(self):
        self.image.save_image()
        image = Image.update_image( self.image.id, 'Image update', 'my Image',self.locate, self.categ)
        upimage = Image.objects.filter(id = self.image.id)
        print(upimage)
        self.assertTrue(Image.name == 'Image update')
