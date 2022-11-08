from django.db import models



# Create your models here.
class Issue(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=30, primary_key=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    client = models.CharField(max_length=30, blank=True, null=True)
    Priority = models.CharField(max_length=500)
    type = models.CharField(max_length=200, blank=True, null=True)
    assigned_to = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.title