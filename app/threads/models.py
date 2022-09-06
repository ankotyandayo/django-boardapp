from django.db import models
 
 
class Post(models.Model):
    post_content = models.CharField(max_length=100)
 
    def __str__(self):
        return self.post_content
 
 
class Coment(models.Model):
    coment_content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.coment_content + ' ' + self.club.post