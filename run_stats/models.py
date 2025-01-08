from django.contrib.auth.models import User
from django.db import models


class Schedule(models.Model):
    """A schedule to track your progress over time"""
    created_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.start_date) + " to " + str(self.end_date)


class Run(models.Model):
    """A run the user wants to track."""
    date = models.DateField()
    time = models.TimeField()
    distance = models.DecimalField(max_digits=4, decimal_places=2)
    average_speed = models.DecimalField(max_digits=3, decimal_places=1)
    calories_burned = models.IntegerField()
    steps = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.distance) + " miles - " + str(self.time)[3:] + " minutes"


class Split(models.Model):
    """A time split for each mile on the run."""
    created_date = models.DateField(auto_now_add=True)
    time = models.TimeField()
    length = models.DecimalField(max_digits=3, decimal_places=2)
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.time)[3:]
