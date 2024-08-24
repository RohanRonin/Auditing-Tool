# views.py

from django.shortcuts import render
from .models import CisRule, IndustryCheck

# Create
def create_rule(request):
    rule = CisRule.objects.create(
        check="Access Control",
        isSafe=True,
        detail="Implement proper access controls for sensitive data."
    )
    rule.save()

# Read
def list_rules(request):
    rules = CisRule.objects.all()
    return render(request, 'list_rules.html', {'rules': rules})

# Update
def update_rule(request, rule_id):
    rule = CisRule.objects.get(id=rule_id)
    rule.detail = "Updated detail text"
    rule.save()

# Delete
def delete_rule(request, rule_id):
    rule = CisRule.objects.get(id=rule_id)
    rule.delete()
