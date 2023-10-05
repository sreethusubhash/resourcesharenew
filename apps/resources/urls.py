from django.urls import path
from . import views
from . import api_views
from rest_framework import routers


router=routers.SimpleRouter()#Default and simple router self study
router.register('api/v3/resource',api_views.ResourceViewSets)#baseurl will be api#no need of.as_view() method#we can see put ,get ,post
router.register('api/v3/category',api_views.CategoryViewSets)

#once register the router include it in url

api_urlpatterns =[
    path('api/v1/resource/',api_views.list_resources,name='list-resources'),
    path('api/v1/category/',api_views.list_category,name='list-category'),
    path('api/v2/resource/',api_views.ListResource.as_view(),name='list-resources-class'),
    path('api/v2/resource/<int:id>',api_views.DetailResource.as_view(),name='detail-resource-class'),
    path('api/v2/category',api_views.DeleteCategory.as_view(),name='delete-category-class')
    
]

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('resource/<int:id>',views.resource_detail,name='resource-detail'),
    path('resource/post/',views.resource_post,name='resource-post'),
    #path('resource/post/',views.resource_post,name='resource-post_old'),
    *api_urlpatterns,
    *router.urls,
]
