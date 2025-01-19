from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name="index"),

    # Run page
    path('runs', views.runs, name="runs"),

    # Detail page for a single run
    path('runs/<int:run_id>', views.run, name="run"),

    # Page to add a new Run
    path('runs/new_run', views.new_run, name="new_run"),

    # Page to edit a Run
    path('runs/edit_run/<int:run_id>', views.edit_run, name="edit_run"),

    # Page to delete Run
    path('runs/<int:run_id>/delete_run', views.delete_run, name="delete_run"),
    
    # Page to add Splits
    path('runs/<int:run_id>/add_splits', views.add_splits, name="add_splits"),

    # Page to view schedules
    path('schedules', views.get_schedules, name="schedules"),

    # Page to view schedule
    path('schedule/<int:schedule_id>', views.get_schedule, name="get_schedule"),
]