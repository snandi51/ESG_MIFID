from django.urls import path
from . import views as screening_views

urlpatterns = [
    path('', screening_views.home, name='screening_home'),
    path('environment_1', screening_views.environment_1, name='screening_environment_1'),
    path('environment_2', screening_views.environment_2, name='screening_environment_2'),
    path('social_1', screening_views.social_1, name='screening_social_1'),
]