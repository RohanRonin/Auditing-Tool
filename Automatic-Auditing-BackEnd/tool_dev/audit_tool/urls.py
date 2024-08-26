from django.urls import path
from .views import run_audit

urlpatterns = [
    path('run_audit/', run_audit, name='run_audit'),
]
