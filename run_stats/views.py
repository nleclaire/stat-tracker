from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Run
from .forms import RunForm

def index(request):
    """The home page for stat-tracker."""
    return render(request, "run_stats/index.html")

def runs(request):
    """Return all runs."""
    runs = Run.objects.order_by('-date')
    context = {'runs': runs}
    return render(request, "run_stats/runs.html", context)

def run(request, run_id):
    """Show a single run and its splits."""
    run = Run.objects.get(id=run_id)
    splits = run.split_set.order_by('-date')
    context = {'run': run, 'splits': splits}
    return render(request, 'run_stats/run.html', context)

def new_run(request):
    """Add a new run."""
    if request.method != 'POST':
        form = RunForm(initial={'time': '00:'})
    else:
        form = RunForm(request.POST)
        if form.is_valid():
            new_run = form.save(commit=False)
            new_run.save()
            return HttpResponseRedirect(reverse('run_stats:runs'))
    
    context = {'form': form}
    return render(request, 'run_stats/new_run.html', context)

def edit_run(request, run_id):
    """Edit an existing run."""
    run = Run.objects.get(id=run_id)
    if request.method != 'POST':
        form = RunForm(instance=run)
    else:
        # POST data submitted; process data
        form = RunForm(instance=run, data=request.POST)
        if form.is_valid:
            run_form.save()
            return HttpResponseRedirect(reverse('run_stats:runs'))

    context = {'form': form, 'run': run}
    return render(request, 'run_stats/edit_run.html', context)
