from django.shortcuts import render
from .models import Title,Features,Kar,ContentsForKar,CTA

def index(request):
    title = Title.objects.get(id=1)
    features = title.features.all()
    kar = Kar.objects.all()
    cta = CTA.objects.get(id=1)
    context = {
        'title': title,
        'features': features,
        'cta': cta,
        'con': kar,
    }
    return render(request, 'blog/index.html', context)

