from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify
import string
from random import SystemRandom

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    # Here start the fields for generic relations
    # Represents the model that wants put here 
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)

    # Represents the id of row of the model described above
    object_id = models.CharField(max_length=255)
    # This field represents the relation between this model and the model described above
    
    content_object = GenericForeignKey('content_type', 'object_id')


    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(SystemRandom().choices(
                string.ascii_letters + string.digits, k=5))

            self.slug = slugify(f'{self.name}-{rand_letters}')
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

   
   