from django.db import models
from django.urls import reverse

# Create your models here.

class Club(models.Model):
    name = models.CharField('NAME', max_length=30)
    location = models.CharField('Location', max_length=30, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('scard:club_detail', args=(self.id,))


class Course(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField('NAME', max_length=30)
    parscore1 = models.SmallIntegerField(default=3, null=False)
    parscore2 = models.SmallIntegerField(default=3, null=False)
    parscore3 = models.SmallIntegerField(default=3, null=False)
    parscore4 = models.SmallIntegerField(default=3, null=False)
    parscore5 = models.SmallIntegerField(default=3, null=False)
    parscore6 = models.SmallIntegerField(default=3, null=False)
    parscore7 = models.SmallIntegerField(default=3, null=False)
    parscore8 = models.SmallIntegerField(default=3, null=False)
    parscore9 = models.SmallIntegerField(default=3, null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('scard:course_detail', args=(self.id,))


class Scorecard(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey('common.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=False)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    myscore1 = models.SmallIntegerField(default=3, null=False)
    myscore2 = models.SmallIntegerField(default=3, null=False)
    myscore3 = models.SmallIntegerField(default=3, null=False)
    myscore4 = models.SmallIntegerField(default=3, null=False)
    myscore5 = models.SmallIntegerField(default=3, null=False)
    myscore6 = models.SmallIntegerField(default=3, null=False)
    myscore7 = models.SmallIntegerField(default=3, null=False)
    myscore8 = models.SmallIntegerField(default=3, null=False)
    myscore9 = models.SmallIntegerField(default=3, null=False)

    class Meta:
        ordering = ('owner',)

    def get_absolute_url(self):
        return reverse('scard:scorecard_detail', args=(self.id,))
    
