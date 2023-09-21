from django.test import TestCase
from apps.resources import models

#Test Case class #Test<model-name>Model
class TestTagModel(TestCase):
    
    def setUp(self) -> None:
        self.tag_name='Python'
        self.tag=models.Tag(name=self.tag_name)#check obj created correctly
        
    #unit test 1#test_<logic-name>
    def test_create_tag_object_successful(self):
        #Check if the obj created is of the instance Tag
        self.assertIsInstance(self.tag,models.Tag)
        
    #unit test 2
    def test_dunder_str(self):
        #str(self.tag)  or self.tag.__str__()
        self.assertEqual(str(self.tag),self.tag_name)
        
#Unit Test For Category Model
class TestCategoryModel(TestCase):
    
    def setUp(self) -> None:
        self.cat_name='Python for beginners'
        self.cat=models.Category(cat=self.cat_name)
    
    #unit test 1   
    def test_create_category_object_successful(self):
        self.assertIsInstance(self.cat,models.Category)
    
    #unit test 2   
    def test_dunder_str(self):
        self.assertEqual(str(self.cat),self.cat_name)
        
    #unit test 3
    def test_verbose_name_plural(self):
        #self.assertEqual('Categories',self.cat._meta.verbose_name_plural)
        name='Categories' #in verbose of category model
        self.assertEqual(name,self.cat._meta.verbose_name_plural)
    
        
        
        
        