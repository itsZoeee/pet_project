from django.shortcuts import render
from plotly.offline import plot
# Create your views here.
def index(request):
    
    #撈出資料庫資料
    return render(request, "index.html", locals())