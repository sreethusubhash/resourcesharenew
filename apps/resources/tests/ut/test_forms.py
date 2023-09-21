from django.test import TestCase
from apps.resources.form import PostResourceForm

#Test Case#Test<form-name>Form
class TestPostResourceForm(TestCase):
    #unit test 1
    def test_form_is_valid_method_return_for_good_data(self):
        data={
            'title':'Python for beginners',
            'link':'http://pythonforbeginners.com',
            'description':'Best Resources',
            #TODO:Add more key-value pairs based on ur form
        }
        #get resource_post()pass to form=postresourceform()
        #since it is testing needs domian value
        #Act
        form=PostResourceForm(data=data)
        
        #Assert
        self.assertTrue(form.is_valid())
def test_form_not_valid_when_link_is_missing(self):

    data={
        'title':'Python for beginners',

        'description':'Best Resources',
        #TODO:Add more key-value pairs based on ur form
     }
    #Act
    form=PostResourceForm(data=data)
    form.is_valid()
     #Assert
    #self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['link'],['This field is require'])        