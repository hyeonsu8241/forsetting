from django.urls import path
from django.views.generic import TemplateView

app_name = 'calendarapp'

urlpatterns = [
path('main/', TemplateView.as_view(template_name='calendarapp/main.html'), name='main')
]