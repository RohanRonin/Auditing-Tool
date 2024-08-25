from django.urls import path
from . import views

urlpatterns = [
    path('auto_audit/', views.run_audit, name='auto_audit'),
]
