from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    emergency_contact = models.CharField(max_length=100)
    emergency_person = models.CharField(max_length=100)
    date_of_employment = models.DateField()
    date_of_resignation = models.DateField(null=True, blank=True)
    affiliation_fiscal_year = models.PositiveIntegerField()
    qualifications = models.TextField()
    work_contents = models.TextField()

    def __str__(self):
        return self.name