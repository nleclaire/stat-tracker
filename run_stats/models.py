from django.db import models

class Run(models.Model):
    """A run the user wants to track."""
    date = models.DateField()
    time = models.TimeField()
    distance = models.DecimalField(max_digits=4, decimal_places=2)
    average_speed = models.DecimalField(max_digits=3, decimal_places=1)
    calories_burned = models.IntegerField()
    steps = models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.distance) + " miles - " + str(self.time)[3:] + " minutes"

class Split(models.Model):
    """A time split for each mile on the run."""
    date = models.DateField()
    time = models.TimeField()
    length = models.DecimalField(max_digits=3, decimal_places=2)
    run = models.ForeignKey(Run, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.time)[3:]
