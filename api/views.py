from django.http import Http404
from django.shortcuts import render
from .models import test, IndexPhotos, Publications, PublicationsYears, PublicationsMembers, IntroduceUs, AlumniPhD, AlumniMs, OurLabTopic
from rest_framework import generics, serializers
from rest_framework.response import Response
from .serializers import TestListSerializer, IndexPhotosListSerializer, PublicationListSerializer, PublicationsYearsListSerializer, PublicationsMebmersListSerializer, IntroduceUsListSerializer, AlumniMsListSerializer, AlumniPhDListSerializer, OurLabTopicSerializer
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


# Create your views here.

@permission_classes((permissions.AllowAny,))
class TestListView(APIView):
    queryset = test.objects.all()
    serializer_class = TestListSerializer

    def get(self, request):
        review = test.objects.all()

        serializer = TestListSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class TestDetail(APIView):
    def get_object(self, pk):
        try:
            return test.objects.get(pk=pk)
        except test.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = TestListSerializer(review)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = TestListSerializer(review, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes((permissions.AllowAny,))
class IndexPhotosListView(APIView):
    queryset = IndexPhotos.objects.all()
    serializer_class = IndexPhotosListSerializer

    def get(self, request):
        review = IndexPhotos.objects.all()

        serializer = IndexPhotosListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = IndexPhotosListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class PublicationListView(APIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationListSerializer

    def get(self, request):
        review = Publications.objects.all()

        serializer = PublicationListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicationListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class PublicationYearsListView(APIView):
    queryset = PublicationsYears.objects.all()
    serializer_class = PublicationsYearsListSerializer

    def get(self, request):
        review = PublicationsYears.objects.all()

        serializer = PublicationsYearsListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class PublicationsMembersListView(APIView):
    queryset = PublicationsMembers.objects.all()
    serializer_class = PublicationsMebmersListSerializer

    def get(self, request):
        review = PublicationsMembers.objects.all()

        serializer = PublicationsMebmersListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class IntroduceUsListView(APIView):
    queryset = IntroduceUs.objects.all()
    serializer_class = IntroduceUsListSerializer

    def get(self, request):
        review = IntroduceUs.objects.all()

        serializer = IntroduceUsListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class IntroduceUsListView(APIView):
    queryset = IntroduceUs.objects.all()
    serializer_class = IntroduceUsListSerializer

    def get(self, request):
        review = IntroduceUs.objects.all()

        serializer = IntroduceUsListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class IntroduceUsListView(APIView):
    queryset = IntroduceUs.objects.all()
    serializer_class = IntroduceUsListSerializer

    def get(self, request):
        review = IntroduceUs.objects.all()

        serializer = IntroduceUsListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class AlumniMsListView(APIView):
    queryset = AlumniMs.objects.all()
    serializer_class = AlumniMsListSerializer

    def get(self, request):
        review = AlumniMs.objects.all()

        serializer = AlumniMsListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class AlumniPhDListView(APIView):
    queryset = AlumniPhD.objects.all()
    serializer_class = AlumniPhDListSerializer

    def get(self, request):
        review = AlumniPhD.objects.all()

        serializer = AlumniPhDListSerializer(
            review, many=True, context={"request": request})
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class OurLabTopicListView(generics.ListCreateAPIView):
    queryset = OurLabTopic.objects.all()
    serializer_class = OurLabTopicSerializer

