from django.db import models

class AuditResult(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    result = models.TextField()

    def __str__(self):
        return f"Audit Result {self.id} at {self.timestamp}"
