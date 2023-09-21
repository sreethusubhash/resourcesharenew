from django.db import models

class CreatedModifiedDateTimeBase(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True) #changed False to True
    
    class Meta:
        abstract=True