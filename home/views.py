from django.shortcuts import render, redirect
from .forms import OldLinkForm
import random
import string
from .models import Convertion
# Create your views here.


def index(request):
    return render(request, "home/index.html")

def conversion_page(request):
    context = {}
    formulaire = OldLinkForm()
    context['formulaire'] = formulaire
    context['new_link'] = ""
    if request.method == 'POST':
        old_link = request.POST.get('old_link')
        new_link ="".join(random.choices(string.ascii_letters + string.digits, k= 7))
        context['new_link'] = new_link
        obj = Convertion(old_link = old_link, new_link=new_link)
        obj.save()
        return redirect('resultat_page', id=obj.id)
        
    return render(request, "home/conversion.html", context)

def resultat(request, id):
    context = {}
    try:
        r = Convertion.objects.get(id=id)
        context['r'] = r
        context['id'] = id
    except:
        context['r'] = False
        context['id'] = id
    return render(request, "home/resultat.html", context)

def redirection(request, new_link):

    context = {}
    try:
        r = Convertion.objects.get(new_link=new_link)
        context['r'] = r
        context['new_link'] = new_link
    except:
        context['r'] = False
        context['new_link'] = new_link
    return render(request, "home/redirection.html",context)