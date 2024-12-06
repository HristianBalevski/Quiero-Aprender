from rest_framework import serializers

from .models import WordOfTheDay


class WordOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WordOfTheDay
        fields = "__all__"

