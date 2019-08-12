from django.db import models
from django.conf import settings

class Position(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Profi(models.Model):
    name = models.CharField(verbose_name=u'Instructor name', max_length=255,
                            help_text='This is name', unique=True)
    surname = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    is_active = models.BooleanField(default=True)

    #courses = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField(Course)
    position = models.ForeignKey('Position', on_delete=models.CASCADE, null=True )
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name



