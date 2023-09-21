from django.db import models
from apps.resources import validators
#from apps.resources.models import Resources

# Create your models here.

from django.contrib.postgres.fields import ArrayField

from apps.core.models import CreatedModifiedDateTimeBase
#from apps.user.models import User
#res=Resources.objects.only('description','link')
# Create your models here.

class Tag(CreatedModifiedDateTimeBase):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)
    class Meta:#change the table name in dashboard
        verbose_name_plural="Categories"
    def __str__(self):
        return self.cat
    
class Resources(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    cat_id = models.ForeignKey("resources.Category",default = 1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    tags = models.ManyToManyField("resources.Tag", through="ResourcesTag")
    #rate = ArrayField(base_field=models.IntegerField()) # INT ARRAY
    class Meta:
        verbose_name_plural = "Resources"
    def __str__(self):
    	return f'{self.user_id.username}-{self.title}'
    @property
    def username(self):
        return self.user_id.username
    
    def user_title(self):
        return self.user_id.title
    #doubt
    def all_tags(self):
        return ','.join([tag.name for tag in self.tags.all()])
    

class ResourcesTag(CreatedModifiedDateTimeBase):
    modified_at = None
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    tag_id = models.ForeignKey("resources.Tag", on_delete=models.CASCADE)
    class Meta:
        constraints=[
            models.UniqueConstraint(
                'resources_id',
                name='resource_tag_unique',
                violation_error_message=f'Tag already exist for resources'
            )
        ]
    def title(self):
        return self.resources_id.title
    def tag(self):
        return f'{self.tag_id.name}'
    def __str__(self) -> str:
        return f'{self.resources_id.title}:{self.tag_id.name}'
    
class Review(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    body = models.TextField(max_length=100)
    
    def __str__(self):
        return f"{self.user_id.username} - {self.resources_id.title}"
    def username(self):
        return self.user_id.username
    def title(self):
        return self.resources_id.title
    def get_body(self):
        return self.body[:50]
        
class Rating(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    rate=models.IntegerField(validators=[validators.check_rating_range])#CHECK(rate>o and rate)
    def username(self):
        return self.user_id.username
    def title(self):
        return self.resources_id.title
    def __str__(self):
        return f'{self.user_id.username}:{self.rate}'
    from apps.resources import validators
