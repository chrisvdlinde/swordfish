from django.db import models

class Client(models.Model):
    name = models.CharField(max_length = 150, unique=True)

    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(max_length = 150, unique=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length = 150, unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class Issue(models.Model):
    number = models.PositiveBigIntegerField(unique=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    client = models.ForeignKey(Client, related_name='issue_client', on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, related_name='issue_priority', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='issue_type', on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=30)

    def __str__(self):
        return (str(self.number) + ' - ' + self.title)