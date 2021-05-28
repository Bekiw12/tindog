from django.db import models

class Title(models.Model):
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pictures', blank=True)

    class Meta():
        verbose_name_plural = "Users"
        verbose_name = "User"

    def __str__(self):
        return self.name

class Features(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    class_name = models.CharField(max_length=200, blank=True)

    class Meta():
        verbose_name_plural = "Users"
        verbose_name = "User"

    def __str__(self):
        return self.name

class ContentForKar1(models.Model):
    subtitle = models.CharField(max_length=300)
    info = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pictures', blank=True)

    class Meta():
        verbose_name_plural = "Users"
        verbose_name = "User"

    def __str__(self):
        return self.name

class ContentForKar2(models.Model):
    subtitle = models.CharField(max_length=300)
    info = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pictures', blank=True)

    class Meta():
        verbose_name_plural = "Users"
        verbose_name = "User"

    def __str__(self):
        return self.name
