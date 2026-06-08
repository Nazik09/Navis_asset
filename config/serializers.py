from rest_framework import serializers

from .models import Partner, Zaiavka  , FAQ, News,   Otzyvy ,   Price

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'





class ZaiavkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zaiavka
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"




class OtzyvySerializer(serializers.ModelSerializer):
    class Meta:
        model = Otzyvy
        fields = '__all__'



class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


