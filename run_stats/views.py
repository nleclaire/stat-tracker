from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import inlineformset_factory, modelformset_factory
from .models import Run, Split
from .forms import RunForm, SplitForm

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
            form.save()
            return HttpResponseRedirect(reverse('run_stats:runs'))

    context = {'form': form, 'run': run}
    return render(request, 'run_stats/edit_run.html', context)

def delete_run(request, run_id):
    """Delete an existing run."""
    if Run.objects.filter(id=run_id).delete():
        return HttpResponseRedirect(reverse('run_stats:runs'))

def add_splits(request, run_id):
    """Add splits to an existing run."""
    run = Run.objects.get(id=run_id)
    splits = run.split_set.order_by('-date')
    SplitFormSetFactory = modelformset_factory(Split, form=SplitForm, extra=0)
    formset = SplitFormSetFactory(request.POST or None, queryset=splits)
    if request.method != 'POST':
        if not splits:
            formset = SplitFormSetFactory()
        else:
            formset = SplitFormSetFactory(
                initial=[
                    {
                        'date': split.date, 
                        'time': split.time, 
                        'length': split.length, 
                        'run': split.run
                    } for split in splits
                ]
            )
    else:
        if formset.is_valid():
            for form in formset:
                form.save()

    context = {
        'formset': formset,
        'splits': splits,
        'run': run
    }

    return render(request, 'run_stats/add_splits.html', context)
