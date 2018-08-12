from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from apps.models import Poems, PoetryAuthor, Poetry, PoemsAuthor
from apps.serializers import PoemsAuthorSerializer, PoetryAuthorSerializer, PoemsSerializer, PoetrySerializer


class MyPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'size'
    max_page_size = 1500


# 全部宋词
class PoemsList(APIView):
    def get(self, request, format=None):
        poems = Poems.objects.all()
        serializer = PoemsSerializer(poems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 全部宋词词人
class PoemsAuthorList(APIView):
    def get(self, request, format=None):
        poems = PoemsAuthor.objects.all()
        serializer = PoemsAuthorSerializer(poems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 全部唐诗
class PoetryList(APIView):
    def get(self, request, format=None):
        poems = Poetry.objects.all()
        serializer = PoetrySerializer(poems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 全部唐诗诗人
class PoetryAuthorList(APIView):
    def get(self, request, format=None):
        poems = PoetryAuthor.objects.all()
        serializer = PoetryAuthorSerializer(poems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 词人生平
class PoemsAuthorDetail(APIView):
    def get_author(self, name):
        try:
            return PoemsAuthor.objects.get(name=name)
        except PoemsAuthor.DoesNotExist:
            return Http404

    def get(self, request, name, format=None):
        author = self.get_author(name)
        serializer = PoemsAuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 诗人生平
class PoetryAuthorDetail(APIView):
    def get_author(self, name):
        try:
            return PoetryAuthor.objects.get(name=name)
        except PoetryAuthor.DoesNotExist:
            return Http404

    def get(self, request, name, format=None):
        author = self.get_author(name)
        serializer = PoetryAuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 词人作品
class AuthorPoems(APIView):
    def get_poems(self, name):
        try:
            return Poems.objects.filter(author=name)
        except Exception:
            return Http404

    def get(self, request, name, format=None):
        poems = self.get_poems(name)
        serializer = PoemsSerializer(poems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 诗人作品
class AuthorPoetry(APIView):
    def get_poetry(self, name):
        return Poetry.objects.filter(author=name)

    def get(self, request, name, format=None):
        poetry = self.get_poetry(name)
        serializer = PoetrySerializer(poetry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
