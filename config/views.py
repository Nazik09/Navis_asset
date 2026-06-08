from rest_framework import viewsets
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin
)

from .models import Partner, Zaiavka, FAQ, News, Otzyvy, Price
from .serializers import (
    PartnerSerializer,
    ZaiavkaSerializer,
    FAQSerializer,
    NewsSerializer,
    OtzyvySerializer,
    PriceSerializer
)


# Только GET
class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class OtzyvyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Otzyvy.objects.all()
    serializer_class = OtzyvySerializer


class PriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


# GET + POST
class ZaiavkaViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Zaiavka.objects.all()
    serializer_class = ZaiavkaSerializer


class FAQViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class NewsViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = News.objects.all()
    serializer_class = NewsSerializer