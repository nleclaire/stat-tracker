from django.db import models

class Run(models.Model):
    """A run the user wants to track."""
    date = models.DateTimeField()
    time = models.TimeField()
    distance = models.DecimalField(max_digits=3, decimal_places=2)
    average_speed = models.DecimalField(max_digits=3, decimal_places=1)
    steps = models.IntegerField()
    calories_burned = models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.distance + " miles in " + self.time + " minutes"

class Split(models.Model):
    """A time split for each mile on the run."""
    date = models.DateTimeField()
    time = models.TimeField()
    full_mile = models.BooleanField()
    run = models.ForeignKey(Run, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.time