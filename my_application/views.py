from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import context


# Create your views here.

Teams = {
    'Management': {
        'team': 'Management',
        'members': ['Brian', 'Tristan', 'Christopher'],
        'description': "The Management team is responsible for overseeing the cleaning tasks for the day is delagated and completed. "
    },
    'Procurement': {
        'team': 'Procurement',
        'members': ['Brian', 'Tristan', 'Christopher'],
        'description': "The Procurement team is responsible for managing the acquisition of supplies and equipment needed for daily meals. "
    },
    'Community': {
        'team': 'Community',
        'members': ['Corey', 'Tyler V', 'Tyle J'],
        'description': "The Community team is responsible for fostering a positive and inclusive environment for all members by planning activites for all at BaseCamp to have time to bond. "
    },
    'Documentation': {
        'team': 'Documentation',
        'members': ['Corey', 'Tyler V', 'Tyle J'],
        'description': "The Documentation team is responsible for creating and maintaining the documentation of BaseCamp on their social media pages. "
    },
}

def index_view(request: HttpRequest) -> HttpResponse:
    context = {'Teams': Teams}
    return render(request, 'index.html', context)

def all_content_view(request: HttpRequest, team_name) -> HttpResponse:
    context = {'Teams': Teams,
               'id': team_name,
               }
    return render(request, 'AllTeamsContent.html', context)


def nav_view(request: HttpRequest) -> HttpResponse:
    context = {'Teams': Teams}
    return render(request, 'NavBar.html', context)
