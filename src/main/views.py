from django.shortcuts import render
from django.http import HttpResponse
import requests
import random

# Create your views here.
data = {}
categories = [
    {
        'name': 'Sports',
        'image': '/static/img/categories/sports.jpg',
        'category': '21'
    },
    {
        'name': 'Celebrities',
        'image': '/static/img/categories/celebs.jpg',
        'category': '26'
    }, {
        'name': 'General Knowledge',
        'image': '/static/img/categories/general-knowledge.jpg',
        'category': '9'
    }, {
        'name': 'History',
        'image': '/static/img/categories/history.jfif',
        'category': '23'
    }, {
        'name': 'Movies',
        'image': '/static/img/categories/movies.jpeg',
        'category': '14'
    }, {
        'name': 'Automobiles',
        'image': '/static/img/categories/automobiles.jfif',
        'category': '28'
    }, {
        'name': 'CS & IT',
        'image': '/static/img/categories/cs-it.jpg',
        'category': '18'
    }, {
        'name': 'Mathematics',
        'image': '/static/img/categories/mathematics.jpg',
        'category': '19'
    },
]


def getLandingPage(response):
    return render(response, "main/landingPage.html", {'home_page': 'active'})


def getAboutUsPage(response):
    return render(response, "main/aboutUsPage.html", {})


def getCategoriesPage(response, category_name=None):
    return render(response, "main/CategoriesPage.html", {'categories': categories})


def getQuizPage(response, category_name: str):
    category_id = "1"
    for category in categories:
        if(category['name'].casefold() == category_name.casefold()):
            category_id = category['category']
            break
    if category_id == "19":
        difficulty = ""
    else:
        difficulty = "&difficulty=easy"
    data = requests.get(
        "https://opentdb.com/api.php?amount=10&category="+category_id+difficulty+"&type=multiple", verify=False).json()['results']
    for questions in data:
        questions['incorrect_answers'].append(questions['correct_answer'])
    return render(response, "main/quizPage.html", {'category': category_name, 'data': data})
