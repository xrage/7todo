from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Todo(models.Model):
    todo = models.CharField(max_length=100)
    created_by=models.ForeignKey(User, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    due_date = models.DateTimeField(blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    group = models.IntegerField(max_length=20, choices=(
        (1, "Personal"),
        (2, "Shared")
    ))

    def __unicode__(self):
        return self.todo

class Company(models.Model):
    company = models.CharField(max_length=60)
    website = models.URLField()
    created_by = models.ForeignKey(User, verbose_name="owner", editable=False)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.company

class CompanyUser(models.Model):
    company = models.ForeignKey(Company)
    user = models.ForeignKey(User)
    token = models.CharField(max_length=100, editable=False)
    state = models.BooleanField(default=False, editable=False)

    def __unicode__(self):
        return self.company.company

# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     company = models.ManyToManyField(Company, blank=True, null=True)
#
#     def __unicode__(self):
#         return self.user.username