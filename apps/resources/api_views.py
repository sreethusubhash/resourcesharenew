from rest_framework.decorators import api_view
from .models import Resources,Category
from rest_framework.response import Response
from . import serializers
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView

from rest_framework import viewsets
from . import mixins

@api_view(['GET'])
def list_resources(request):
    
    queryset = (Resources.objects.select_related#query set is an attribute in DRF's CBV that specifies the set of objs to be returned by the view
    ('user_id','cat_id')
    .prefetch_related('tags').all())
    #build our response ourself
    # response = [
    #     {
    #         'title':query.title,
    #         'links':query.link,
    #         'user':
    #             {
    #                 'id':query.user_id.id,
    #                 'username':query.user_id.username,
    #     },
    #     'category':query.cat_id.cat,
    #     'tags':query.all_tags(),
    #     }
    #     for query in queryset
    
    # ]
    response=serializers.ResourceSerializer(queryset,many=True)
    #transform to json before returning
    #return Response(response)
    return Response(response.data)

@api_view(['GET'])#fun based apiview
def list_category(request):
    
    queryset = Category.objects.all()
    # response = [
    #     {
    #         'id':query.id,
    #         'cat':query.cat,
    #     }
    # for query in queryset
    # ]
    response=serializers.CategorySerializer(queryset,many=True)
    #return Response(response)
    return Response(response.data)

#class based apiview
class ListResource(ListAPIView):
    queryset = (Resources.objects.select_related
    ('user_id','cat_id')
    .prefetch_related('tags').all())
    serializer_class=serializers.ResourceModelSerializer
    
#details of single resource not a group of resources
class DetailResource(RetrieveAPIView):
    lookup_field='id'#u provide a pk ,default look up is pk
    queryset = (Resources.objects.select_related
    ('user_id','cat_id')
    .prefetch_related('tags').all())
    serializer_class=serializers.ResourceModelSerializer
    
#to create viewset-can permit us to perform the CRUD operations in one class based view
class ResourceViewSets(viewsets.ModelViewSet) :#model+ViewSets
    queryset = (Resources.objects.select_related
    ('user_id','cat_id')
    .prefetch_related('tags').all())
    serializer_class=serializers.ResourceModelSerializer
    
    #single end point for object,list.autogenerate the end points by django
# class CategoryViewSets(viewsets.ModelViewSet) :
#     queryset = Category.objects.all()
#     serializer_class=serializers.CategoryModelSerializer
    
#create viewset-can permit us to perform the CRUD operations in
class CategoryViewSets(mixins.DenyDeletionOfDefaultCategoryMixin,viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=serializers.CategoryModelSerializer
    
class DeleteCategory(mixins.DenyDeletionOfDefaultCategoryMixin,DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=serializers.CategoryModelSerializer
# class FilterOutAdminMixin():
#     def get_queryset(self):
#         queryset=super().get_queryset().exclude(user_id__is_superuser__exact=True)
#         return queryset

   
        
    
    
    
    
    
    
