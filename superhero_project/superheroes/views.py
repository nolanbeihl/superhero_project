from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Superhero
# Create your views here.

def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes' : all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego,primary_ability=primary,secondary_ability=secondary,catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request,'superheroes/create.html')

def update(request, hero_id):
    update_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'update_hero': update_hero
    }
    #query for hero, pass it to context
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        update_hero = Superhero(name=name, alter_ego=alter_ego,primary_ability=primary,secondary_ability=secondary,catch_phrase=catchphrase)
        request = update_hero
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request,'superheroes/update.html',context)
        
def delete(request,hero_id):
    remove_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'remove_hero': remove_hero
    }
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        remove_hero = Superhero(name=name, alter_ego=alter_ego,primary_ability=primary,secondary_ability=secondary,catch_phrase=catchphrase)
        remove_hero.delete()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request,'superheroes/update.html',context)