# models.py

from django.db import models

class CisRule(models.Model):
    check = models.CharField(max_length=255)
    isSafe = models.BooleanField()
    detail = models.TextField()

class IndustryCheck(models.Model):
    industry = models.CharField(max_length=255)
    checks = models.JSONField()  # Store checks as JSON data
