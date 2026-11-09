from django.urls import path
from my_application.views import *

urlpatterns = [
    path('', index_view),
    path('<str:team_name>/', all_content_view, name='team.detail'),

]
