from django.db import models

class Title(models.Model):
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pictures', blank=True)
    features = models.ManyToManyField('Features')

    class Meta:
        verbose_name_plural = "Titles"
        verbose_name = "Title"


class Features(models.Model):
    title1 = models.CharField(max_length=200,)
    subtitle = models.CharField(max_length=300)
    class_name = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Features"
        verbose_name = "Feature"

    def __str__(self):
        return self.title1

class Kar(models.Model):
    contentsforkar = models.ManyToManyField('ContentsForKar')

class ContentsForKar(models.Model):
    subtitle = models.CharField(max_length=300)
    info = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pictures', blank=True)

    class Meta:
        verbose_name_plural = "Contents For Kar"
        verbose_name = "Content For Kar"


class CTA(models.Model):
    text = models.TextField(max_length=500)

    class Meta():
        verbose_name_plural = "CTAs"
        verbose_name = "CTA"