from rest_framework import serializers
from . import models
from apps.user.serializers import UserModelSerializer


class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    cat=serializers.CharField()
    created_at=serializers.DateTimeField()
    modified_at=serializers.DateTimeField()
    

class TagSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    created_at=serializers.DateTimeField()
    modified_at=serializers.DateTimeField()

class ResourceSerializer(serializers.Serializer):# modelname+serializer->naming convention
    id=serializers.IntegerField()
    title=serializers.CharField()
    description=serializers.CharField()
    link=serializers.URLField()
    #user=UserSerializer()
    cat_id=CategorySerializer()
    tags=TagSerializer(many=True)
    
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields  = '__all__' # special argument to serialize all model's attribute
    
class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields  = '__all__'
        
class ResourceModelSerializer(serializers.ModelSerializer):
    cat_id = CategoryModelSerializer()
    tags = TagModelSerializer(many=True)
    class Meta:
        model=models.Resources
        #2option
        #specify the fields we want our serializer to serialize
        #Omit fields that our serializer should not serialize
        fields=('id','title','description','link','user_id','cat_id','tags'
                )

    
