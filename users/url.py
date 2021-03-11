from django.urls import path
from .views import ListCreateView, ReadUpdateDeleteView

urlpatterns=[
    path('', ListCreateView.as_view()),
    path('/<int:pk>', ReadUpdateDeleteView.as_view())
]
