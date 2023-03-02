from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)

def recipe(request,pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe_output = {
        'recipe': recipe
    }
    return render(request, 'recipe.html', recipe_output)
    
