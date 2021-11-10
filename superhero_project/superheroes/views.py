from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Superhero

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
    if request.method == "POST":
        update_hero.name = request.POST.get('name')
        update_hero.alter_ego = request.POST.get('alter_ego')
        update_hero.primary_ability = request.POST.get('primary_ability')
        update_hero.secondary_ability = request.POST.get('secondary_ability')
        update_hero.catch_phrase = request.POST.get('catch_phrase')
        update_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request,'superheroes/update.html',context)
        
def delete(request,hero_id):
    Superhero.objects.filter(pk= hero_id).delete()
    return HttpResponseRedirect(reverse('superheroes:index'))
