from rest_framework import serializers
from web.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'line_nos', 'language', 'style')
