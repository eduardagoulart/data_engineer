from rest_framework import serializers
from data_project.core.models import Insurance, Months, Year, State, AgencyId


class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class MonthsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Months
        fields = '__all__'


class YearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class AgencyIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgencyId
        fields = '__all__'
