#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from apps.models import Poems, PoemsAuthor, Poetry, PoetryAuthor


class PoemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poems
        fields = ('title', 'author', 'content')


class PoemsAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoemsAuthor
        fields = "__all__"


class PoetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Poetry
        fields = ('title', 'author', 'dynasty', 'content', 'yunlv_rule')


class PoetryAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoetryAuthor
        fields = '__all__'
