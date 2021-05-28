from django.shortcuts import render
from .models import Title,Features,ContentForKar1,ContentForKar2

def index(request):
    title = Title.objects.get(id=1)
    features = Features.objects.get(id=1)
    contentforkar1 = ContentForKar1.objects.get(id=1)
    contentforkar2 = ContentForKar2.objects.get(id=1)
    context = {

    }
    return render(request, 'blog/index.html')

