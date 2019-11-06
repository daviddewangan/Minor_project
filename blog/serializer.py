from blog.models import Choice
from rest_framework import serializers
class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ["category", "choice_text","user"]