from django.urls import path
from . import views as screening_views

urlpatterns = [
    path('', screening_views.login_user, name='login_user'),
    path('login_client', screening_views.login_client, name='login_client'),
    path('logout', screening_views.logout_user, name='logout'),
    # path('self_assessment_1', screening_views.self_assessment_1, name='self_assessment_1'),
    path('index_user', screening_views.home1, name='index_user'),
    path('index_client', screening_views.home2, name='index_client'),
    path('selection', screening_views.selection, name='selection'),
    path('self_assessment_1', screening_views.self_assessment_1, name='self_assessment_1'),
    path('self_assessment_scoring', screening_views.self_assessment_scoring, name='self_scoring'),
    path('environment1_1', screening_views.environment1_1, name='environment1_1'),
    path('environment1_2', screening_views.environment1_2, name='environment1_2'),
    path('environment1_3', screening_views.environment1_3, name='environment1_3'),
    path('environment1_4', screening_views.environment1_4, name='environment1_4'),
    path('environment1_5', screening_views.environment1_5, name='environment1_5'),
    path('environment1_6', screening_views.environment1_6, name='environment1_6'),
    path('environment1_7', screening_views.environment1_7, name='environment1_7'),
    path('environment1_8', screening_views.environment1_8, name='environment1_8'),
    path('environment1_9', screening_views.environment1_9, name='environment1_9'),
    path('environment1_10', screening_views.environment1_10, name='environment1_10'),
    path('environment_2', screening_views.environment_2, name='environment_2'),
    path('social_1', screening_views.social_1, name='social_1'),
    path('social_screening', screening_views.social_screening, name='social_screening'),
    path('governance', screening_views.governance, name='governance'),
    path('governance_scoring', screening_views.governance_scoring, name='governance_scoring'),
    path('final_scoring', screening_views.final_scoring, name='final_scoring'),
    path('final_scoring_client', screening_views.final_scoring_client, name='final_scoring_client'),
]