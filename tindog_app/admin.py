from django.contrib import admin
from .models import Title, Features, Kar, ContentsForKar, CTA

admin.site.register(Title)
admin.site.register(Features)
admin.site.register(Kar)
admin.site.register(ContentsForKar)
admin.site.register(CTA)