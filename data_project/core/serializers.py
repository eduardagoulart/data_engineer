from rest_framework import serializers
from data_project.core.models import Insurance


class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'
