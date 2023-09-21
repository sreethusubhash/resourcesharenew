from django.test import TestCase, Client
from django.urls import reverse
from apps.user.models import User
from apps.resources import models


# Test Case # Test<view-name>View
class TestResourcesView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        # TODO: CREATE A USER
        self.user = User.objects.create_user(  # .create_user
            username="admin",
            password="admin",)
        #     first_name="tony",
        #     last_name="ralph",
        #     email="tonyralph@gmail.com",
        #     bio="Good at anything Python",
        #     title="Python Developer",
        # )
        # TODO: CREATE A TAG
        self.tag = models.Tag(name="Python")
        self.tag.save()  # save it to the database
        # TODO: CREATE A CATEGORY
        self.cat = models.Category.objects.create(cat="Programming Language")
        # TODO: CREATE RESOURCE
        # create without the tag, so that the id is auto generated
        self.resource = models.Resources.objects.create(
            user_id=self.user,
            cat_id=self.cat,
            title="Python for beginners",
            description="All you need to know...",
            link="https://python.com",
        )
        # set the many to many relationship
        self.resource.tags.add(self.tag)
        # save it, so that the changes are recorded in the database
        self.resource.save()

    # unit test 1
    def test_home_page_return_200_status(self):
        response = self.client.get(
            reverse("home_page"),  # access url using path name
            HTTP_USER_AGENT="Mozilla/5.0",  # set the user agent
            HTTP_CONTENT_TYPE="text/plain",  # set content type
        )
        # Check that the status code of the response is 200
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_user_count(self):
        # ARRANGE
        expected_user_cnt = 1

        # Act
        response = self.client.get(
            reverse("home_page"),  # access url using path name
            HTTP_USER_AGENT="Mozilla/5.0",  # set the user agent
            HTTP_CONTENT_TYPE="text/plain",  # set content type
        )

        # Assert
        self.assertEqual(response.context["user_cnt"], expected_user_cnt)

    def test_home_page_view_resource_count(self):
        # ARRANGE
        expected_resource_count = 1

        # Act
        response = self.client.get(
            reverse("home_page"),  # access url using path name
            HTTP_USER_AGENT="Mozilla/5.0",  # set the user agent
            HTTP_CONTENT_TYPE="text/plain",  # set content type
        )

        # Assert
        self.assertEqual(response.context["cnt"], expected_resource_count)

    def test_home_page_view_resource_per_category_count(self):
        # TODO: Write your test logic
        pass

    def test_resource_detail_view_redirects_to_login_for_non_auth_user(self):
        response = self.client.get(
            reverse("resource-detail", kwargs={"id": 1}),
            HTTP_USER_AGENT="Mozilla/5.0",  # set the user agent
            HTTP_CONTENT_TYPE="text/plain",  # set content type
        )

        # Assert
        # check if the response object is an instance of HttpResponseRedirect
        # check if the status code of response is 302
        self.assertEqual(response.status_code, 302)
        # Check if the url path is equal to 'user/login/?next=/resource/1'
        
    def test_resource_detail_view_status_code_ok_for_auth_user(self):
        # ARRANGE
        login = self.client.login(username="admin", password="admin")

        response = self.client.get(
            reverse("resource-detail", kwargs={"id": self.resource.id}),
            HTTP_USER_AGENT="Mozilla/5.0",  # set the user agent
            HTTP_CONTENT_TYPE="text/plain",  # set content type
        )
        # check if the status code of response is 302
        self.assertEqual(response.status_code, 200)

# # #Test Case #Test<view-name>View
# # class TestResourceView(TestCase):
    
# #     def setUp(self) -> None:
# #         self.client = Client()
    
# #     #unit test 1
# #     def test_home_page_return_200_status(self):
# #         #->name='home_page->urls.py->response = self.client.get('/')
# #         response = self.client.get(
# #             reverse('home_page'),#access url using path name
# #             HTTP_USER_AGENT="Mozilla/5.0",#set the user agent
# #             HTTP_CONTENT_TYPE="text/plain",
# #             ) 
# #         self.assertEqual(response.status_code, 200)
    
# #     def test_home_page_view_user_count(self):
# #         #Arrange
# #         User.objects.create(username="admin", password="admin",)
# #                             #first_name='',last_name='', email='',bio='',title='')
# #         expected_user_cnt=1
# #         #Act
# #         response = self.client.get(
# #             reverse('home_page'),#access url using path name
# #             HTTP_USER_AGENT="Mozilla/5.0",#set the user agent
# #             HTTP_CONTENT_TYPE="text/plain",
# #             ) 
# #         #Assert
# #         self.assertEqual(response.context['user_cnt'], expected_user_cnt)
# #     def test_home_page_view_resource_count(self):
# #         #Arrange
# #         #Create a user
     
# #         user=User.objects.create(username="admin", password="admin",)
# #                             #first_name='',last_name='', email='',bio='',title='')
# #         user.save()
# #         expected_user_cnt=1
       
# #         #create tag
# #         tag=models.Tag(name='Python')
# #         tag.save()
        
# #         #create a category
# #         cat=models.Category.objects.create(cat='Programming Language')
        
# #         #create without the tag,so that id is autogenerated
# #         r=models.Resources.objects.create(
# #             user_id=user,cat_id=cat,title='python one hour',
# #             description='Learning pattern in one hour',
# #             link='https://www.youtube.com/watch?v=kqtD5dpn9C8',
            
# #         )
# #         #set M2M
# #         #breakpoint()
# #         r.tags.add(tag)
# #         r.save()
# #         expected_resource_count=1
        
# #         #Act
# #         response = self.client.get(
# #             reverse('home_page'),#access url using path name
# #             HTTP_USER_AGENT="Mozilla/5.0",#set the user agent
# #             HTTP_CONTENT_TYPE="text/plain",
# #             ) 
# #         #Assert
# #         self.assertEqual(response.context['cnt'], expected_resource_count)
        
# #     def test_home_page_view_per_category_count(self):
# #         #TODO:Write ur test logic
# #         pass#from resources/view.py from home_page()
    
# #     def test_resource_details_redirects_to_login_for_non_auth_user(self):
# #         response = self.client.get(
# #             reverse('resource-detail',kwargs={'id':2}),#access url using path name
# #             HTTP_USER_AGENT="Mozilla/5.0",#set the user agent
# #             HTTP_CONTENT_TYPE="text/plain",
# #             ) 
# #         #Assert
# #         #Check if the response object is an instance of httpresponseredirect
# #         #Check if the status code of response is 302
# #         self.assertEqual(response.status_code, 302)
# #         #check if the url path is equal to 'user/login/?next=/resource/1'
# #     def test_resource_detail_view_status_code_ok_for_auth_user(self):
# #         #Arrange
# #         user=User.objects.create_user(username="admin", password="admin",)
# #                             #first_name='',last_name='', email='',bio='',title='')
# #         user.st_password='admin'
# #         user.save()                  
# #         #Login so that I am authenticated
# #         login=self.client.force_login(username='admin',password='admin')
# #         response = self.client.get(
# #             reverse('resource-detail',kwargs={'id':2}),#access url using path name
# #             HTTP_USER_AGENT="Mozilla/5.0",#set the user agent
# #             HTTP_CONTENT_TYPE="text/plain",
# #             ) 
# #         self.assertEqual(response.status_code,200)
        
        
