from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def getLandingPage(response):
    return render(response, "main/landingPage.html", {'home_page': 'active'})


def getCategoriesPage(response, category_name=None):
    categories = [
        {
            'name': 'Sports',
            'image': '/static/img/categories/sports.jpg',
            'category': '17'
        },
        {
            'name': 'Celebrities',
            'image': '/static/img/categories/celebs.jpg',
            'category': '17'
        }, {
            'name': 'General Knowledge',
            'image': '/static/img/categories/general-knowledge.jpg',
            'category': '17'
        }, {
            'name': 'History',
            'image': '/static/img/categories/history.jfif',
            'category': '17'
        }, {
            'name': 'Movies',
            'image': '/static/img/categories/movies.jpeg',
            'category': '17'
        }, {
            'name': 'Automobiles',
            'image': '/static/img/categories/automobiles.jfif',
            'category': '17'
        }, {
            'name': 'CS & IT',
            'image': '/static/img/categories/cs-it.jpg',
            'category': '17'
        }, {
            'name': 'Mathematics',
            'image': '/static/img/categories/mathematics.jpg',
            'category': '17'
        },
    ]
    return render(response, "main/CategoriesPage.html", {'categories': categories})


def getAboutUsPage(response):
    return render(response, "main/aboutUsPage.html", {})
