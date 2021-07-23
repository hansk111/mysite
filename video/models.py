from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class VideoPost(models.Model):
    user = models.ForeignKey('common.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    video_file = models.FileField(upload_to='videos/%Y/%m')
    thumbnail = models.ImageField(upload_to='videos/%Y/%m', default='none')
    category = models.CharField(max_length=50, default='none')
    pub_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField('common.User', related_name='likes')
    video_views = models.ManyToManyField('common.User', related_name='video_views')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(VideoPost, on_delete=models.CASCADE)
    user = models.ForeignKey('common.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username