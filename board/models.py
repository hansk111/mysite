from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children', db_index=True)
    title = models.CharField(max_length=128)
    # slug = models.SlugField(max_length=250, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['tree_id', 'lft']

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title



class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = RichTextUploadingField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_post')
    voter = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='voter_post')
    # category = models.CharField(max_length=20, unique=True)
    # slug = models.SlugField(max_length=250, unique=False, allow_unicode=True)
    category = TreeForeignKey('Category', null=True, blank=True, db_index=True, on_delete=models.SET_NULL,)
    head_image = models.ImageField(upload_to='board/images/%Y/%m',blank=True, null=True)
    
    def __str__(self):
        return self.subject

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_comment')
    voter = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='voter_comment')