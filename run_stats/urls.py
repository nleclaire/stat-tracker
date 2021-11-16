from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name="index"),

    # Run page
    path('runs', views.runs, name="runs"),

    # Detail page for a single run
    path('runs/<int:run_id>', views.run, name="run"),
]