from django.shortcuts import render
from plotly.offline import plot
from mysite.models import Lost,Adopt
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .form import AdoptForm,LostForm
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, "index.html", locals())

def adoptPets(request):
    if request.method == "POST":
        keywords = request.POST.get("keywords")
        adoptPets = Adopt.objects.filter(breed__contains=keywords)
        # .order_by('-id')
    else :
        adoptPets = Adopt.objects.all()

    p = Paginator(adoptPets,12)
    page = request.GET.get('page')
    adopts = p.get_page(page)

    speciesInDataBase = Adopt.objects.values('species').distinct()
    breedsInDataBase = Adopt.objects.values('breed').distinct()
    return render(request, "adoptPets.html", locals())

def lostPets(request):
    if request.method == "POST":
        keywords = request.POST.get("keywords")
        lostPets = Lost.objects.filter(species__contains=keywords)
    else :
        lostPets = Lost.objects.all()

    p = Paginator(lostPets,12)
    page = request.GET.get('page')
    losts = p.get_page(page)

    speciesInDataBase = Lost.objects.values('species').distinct()

    return render(request, "lostPets.html", locals())

def fancyCard(request):
    lostPets = Lost.objects.all()
    return render(request, "fancyCard.html", locals())

def dogBreed(request):
    return render(request, "dogBreed.html", locals())

def upload(request):
    submitted = False
    if request.method == "POST":
        form = AdoptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/upload?submitted=True')
    else :
        form = AdoptForm
        if 'submitted' in request.GET:
            submitted = True
    form = AdoptForm

    adoptPets = Adopt.objects.all()
    p = Paginator(adoptPets,12)
    page = request.GET.get('page')
    adopts = p.get_page(page)

    return render(request, "upload.html", locals())

def uploadLost(request):
    submitted = False
    if request.method == "POST":
        form = LostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/uploadLost?submitted=True')
    else :
        form = AdoptForm
        if 'submitted' in request.GET:
            submitted = True
    form = LostForm

    lostPets = Lost.objects.all()
    p = Paginator(lostPets,12)
    page = request.GET.get('page')
    losts = p.get_page(page)

    return render(request, "uploadLost.html", locals())

def analysisBreed(request):
    return render(request, "analysisBreed.html", locals())

def analysis(request):
    return render(request, "analysis.html", locals())