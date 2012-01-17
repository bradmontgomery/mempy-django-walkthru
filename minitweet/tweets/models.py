from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    posted_on = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ['-posted_on',]
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

