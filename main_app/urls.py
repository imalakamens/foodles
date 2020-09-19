from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipe/', views.RecipeList.as_view(), name='recipes_index'),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view(), name='recipes_detail'),
    path('recipe/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('accounts/signup/', views.signup, name='signup'),
]