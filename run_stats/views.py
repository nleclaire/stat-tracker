from django.shortcuts import render
from .models import Run

def index(request):
    """The home page for stat-tracker."""
    return render(request, "run_stats/index.html")

def runs(request):
    """Return all runs."""
    runs = Run.objects.all()
    context = {'runs': runs}
    return render(request, "run_stats/runs.html", context)

def run(request, run_id):
    """Show a single run and its splits."""
    run = Run.objects.get(id=run_id)

    splits = run.split_set.order_by('-date')

    context = {'run': run, 'splits': splits}
    return render(request, 'run_stats/run.html', context)
