# from django.contrib import admin - до подключения дебаг-функции
from django.urls import path, include  # pylint: disable=unused-import
from charlist.settings import DEBUG  # pylint: disable=unused-import

import personages.views as personages

app_name = 'personages'

urlpatterns = [

    path('details/<int:pk>/', personages.PersonageDetailView.as_view(), name='details'),
    path('create/', personages.PersonageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', personages.PersonageUpdateView.as_view(), name='update'),

]
