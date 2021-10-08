from django.urls import path
from . import views

urlpatterns = [
    path("", views.getLandingPage, name="landingPage"),
    path("categories/", views.getCategoriesPage, name="CategoriesPage"),
    path("about-us/", views.getAboutUsPage, name="aboutUs"),
    path("category/<str:category_name>",
         views.getQuizPage, name="quizPage"),
    path("category/<str:category_name>/results",
         views.getResultsPage, name="results")
]
