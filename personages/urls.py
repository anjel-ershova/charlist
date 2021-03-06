from django.urls import path, include  # pylint: disable=unused-import

import personages.views as personages

app_name = 'personages'

urlpatterns = [

    path('details/<int:pk>/', personages.PersonageDetailView.as_view(), name='details'),
    path('create/', personages.PersonageCreateView.as_view(template_name="personages/personage_create.html"), name='create'),
    path('create2/', personages.PersonageCreateView.as_view(template_name="personages/personage_form.html"), name='create2'),
    path('details2/<int:pk>/', personages.personage_details2, name='details2'),
    path('update/<int:pk>/', personages.PersonageUpdateView.as_view(template_name="personages/personage_update.html"), name='update'),


]
