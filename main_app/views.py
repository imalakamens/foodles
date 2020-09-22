import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal, Recipe, MAIN_INGREDIENT


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class RecipeList(ListView):
  model = Recipe

class RecipeDetail(DetailView):
  model = Recipe

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name', 'source', 'main_ingredient', 'instructions']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = ['name', 'source', 'main_ingredient', 'instructions']

class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  success_url = '/recipe/'

class MealList(ListView):
  model = Meal

class MealDetail(DetailView):
  model = Meal

class MealCreate(LoginRequiredMixin, CreateView):
  model = Meal
  fields = ['date', 'recipe']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/meals/'

class MealUpdate(LoginRequiredMixin, UpdateView):
  model = Meal
  fields = ['date', 'recipe']

class MealDelete(LoginRequiredMixin, DeleteView):
  model = Meal
  success_url = '/meals/'

def recipes_make_favorite(request, pk):
  current_recipe = Recipe.objects.get(id=pk)
  current_recipe.favorite = True
  current_recipe.save()
  return redirect('view_favorites')

class FavoriteList(LoginRequiredMixin, ListView):
  context_object_name = 'favorites'
  queryset = Recipe.objects.filter(favorite=True)
  template_name = 'main_app/view_favorites.html'

class MainList(LoginRequiredMixin, ListView):
  template_name = 'view_by_main.html'
  from django import forms
  choice_field = MAIN_INGREDIENT
  context_object_name = 'main'
  queryset = Recipe.objects.all()

  def get_queryset(self):
    self.main_ingredient = get_object_or_404(Recipe, name=self.kwargs['recipe'])
    return Recipe.objects.filter(main_ingredient=self.main_ingredient)