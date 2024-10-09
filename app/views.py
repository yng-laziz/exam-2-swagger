from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from .serializers import *
# Create your views here.

class AboutListAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(APIView):
    def get(self, request, slug, *args, **kwargs):
        news = get_object_or_404(News, slug=slug)
        news.view_content += 1
        news.save()
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)




class TeamMemberListAPIView(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamMemberDetailAPIView(APIView):
    def get(self, request, slug, *args, **kwargs):
        team_member = get_object_or_404(TeamMember, slug=slug)
        serializer = TeamMemberSerializer(team_member)
        return Response(serializer.data, status=status.HTTP_200_OK)




class PublicationListAPIView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class PublicationDetailAPIView(APIView):
    def get(self, request, slug, *args, **kwargs):
        publication = get_object_or_404(Publication, slug=slug)
        serializer = PublicationSerializer(publication)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# class ModelDetailView(generics.RetrieveAPIView):
#     model = Service
#     serializer_class = ServiceSerializer
#     lookup_field = 'slug'

class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        send_mail(
            subject=f"New Contact: {contact.name}",
            message=f"Message: {contact.message}\n\nContact Details:\nName: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nMode of Contact: {contact.mode_of_contact}\nQuestion Categories: {contact.question_categories}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact.email],
            fail_silently=False,
        )


class ServiceDetailAPIView(APIView):
    def get(self, request, slug, *args, **kwargs):
        service = get_object_or_404(Service, slug=slug)
        service.view_count += 1
        service.save()
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)
    