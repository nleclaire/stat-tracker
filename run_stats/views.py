from django.shortcuts import render

def index(request):
    """The home page for stat-tracker."""
    return render(request, "run_stats/index.html")

