from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .forms import RunForm, SplitForm
from .models import Run, Split


def index(request):
    """The home page for stat-tracker."""
    return render(request, "run_stats/index.html")


@login_required
def runs(request):
    """Return all runs related to a user."""
    runs = Run.objects.filter(owner=request.user).order_by('-date')
    context = {'runs': runs}
    return render(request, "run_stats/runs.html", context)


@login_required
def run(request, run_id):
    """Show a single run and its splits."""
    run = Run.objects.get(id=run_id)
    validate_user(request, run)
    splits = run.split_set.order_by('-date')
    context = {'run': run, 'splits': splits}
    return render(request, 'run_stats/run.html', context)


@login_required
def new_run(request):
    """Add a new run."""
    if request.method != 'POST':
        form = RunForm(initial={'time': '00:'})
    else:
        form = RunForm(request.POST)
        if form.is_valid():
            new_run = form.save(commit=False)
            new_run.owner = request.user
            new_run.save()
            return HttpResponseRedirect(reverse('run_stats:runs'))

    context = {'form': form}
    return render(request, 'run_stats/new_run.html', context)


@login_required
def edit_run(request, run_id):
    """Edit an existing run."""
    run = Run.objects.get(id=run_id)
    validate_user(request, run)
    if request.method != 'POST':
        form = RunForm(instance=run)
    else:
        form = RunForm(instance=run, data=request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('run_stats:runs'))

    context = {'form': form, 'run': run}
    return render(request, 'run_stats/edit_run.html', context)


@login_required
def delete_run(request, run_id):
    """Delete an existing run."""
    run = Run.objects.filter(id=run_id)
    validate_user(request, run)
    if run.delete():
        return HttpResponseRedirect(reverse('run_stats:runs'))


@login_required
def add_splits(request, run_id):
    """Add splits to an existing run."""
    run = Run.objects.get(id=run_id)
    validate_user(request, run)
    splits = run.split_set.order_by('-date')
    SplitFormsetFactory = modelformset_factory(Split, fields=('date', 'time', 'length', 'run'), form=SplitForm)
    if request.method != 'POST':
        if not splits:
            formset = SplitFormsetFactory()
        else:
            formset = SplitFormsetFactory(queryset=splits)

    else:
        formset = SplitFormsetFactory(request.POST)
        for form in formset:
            if form.is_valid():
                form.save()
        return HttpResponseRedirect(reverse('run_stats:run', kwargs={'run_id': run.id}))

    context = {
        'formset': formset,
        'splits': splits,
        'run': run
    }

    return render(request, 'run_stats/add_splits.html', context)


def validate_user(request, run):
    if run.owner != request.user:
        raise Http404
