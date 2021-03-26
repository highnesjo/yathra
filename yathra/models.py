from django.db import models

# Create your models here.
class story(models.Model):
    title= models.CharField(max_length=150,default=None,blank=False)
    Img = models.ImageField(upload_to='images/')
    storytext = models.TextField(default=None,blank=False)
    
    def __str__(self):
        return str(self.title)

class review(models.Model):
    storyid = models.IntegerField(default=None,blank=False)
    user = models.CharField(max_length=150,default=None,blank=False)
    review = models.TextField(default=None,blank=False)

    def __str__(self):
        return str(self.storyid)