from django.db import models

# Create your models here.
class Article(models.Model):
    title =models.CharField(max_length=200,primary_key=True)
    body = models.TextField(blank=True)
    #pub_date =models.DateTimeField('date published')
    #likes=models.IntegerField()
    
    def __unicode__(self):
        return self.title
