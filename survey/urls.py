from survey import views
from django.urls import path

urlpatterns = [
    path('', views.survey_home),
    path('save_survey', views.save_survey),
    path('show_result', views.show_result),
    path('list', views.list),
    path('write', views.write),
    path('insert', views.insert),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
]