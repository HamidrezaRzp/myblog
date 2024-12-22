from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

    class Status(models.TextChoices):
        pUBLISHED = 'PB','Published' 
        DRAFTED = 'DF','drafted'
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    publish = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
            max_length=2,
            choices=Status,
            default=Status.DRAFTED
    )
    authur = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                related_name='post',
                on_delete=models.CASCADE
    )


    class Meta:
        ordering =['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
    
