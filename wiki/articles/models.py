from django.db import models
class Article(models.Model):
    title =models.CharField(max_length=200,primary_key=True)
    body = models.TextField(blank=True)
    user = models.CharField(max_length=25)
    flag = models.CharField(max_length=6)
    
    def __unicode__(self):
        """will call the __unicode__ method of the User class and  to give an object a readable name"""   
        return self.title
