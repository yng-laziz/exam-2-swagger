from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/about/', AboutListAPIView.as_view(), name='about-list'),

    path('api/v1/news/', NewsListAPIView.as_view(), name='news-list'),
    path('api/v1/news/<slug:slug>/', NewsDetailAPIView.as_view(), name='news-detail'),

    path('api/v1/team-members/', TeamMemberListAPIView.as_view(), name='team-member-list'),
    path('api/v1/team-members/<slug:slug>/', TeamMemberDetailAPIView.as_view(), name='team-member-detail'),

    path('api/v1/publications/', PublicationListAPIView.as_view(), name='publication-list'),
    path('api/v1/publications/<slug:slug>/', PublicationDetailAPIView.as_view(), name='publication-detail'),

    path('api/v1/reviews/', ReviewListAPIView.as_view(), name='review-list'),

    path('api/v1/services/', ServiceListAPIView.as_view(), name='service-list'),
    path('api/v1/services/<slug:slug>/', ServiceDetailAPIView.as_view(), name='service-detail'),

    path('contacts/create/', ContactCreateAPIView.as_view(), name='contact-create')

]

