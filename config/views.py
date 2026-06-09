from rest_framework import viewsets
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin
)

from drf_yasg.utils import swagger_auto_schema

from .models import (
    Partner,
    Zaiavka,
    FAQ,
    News,
    Otzyvy,
    Price
)

from .serializers import (
    PartnerSerializer,
    ZaiavkaSerializer,
    FAQSerializer,
    NewsSerializer,
    OtzyvySerializer,
    PriceSerializer
)


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    @swagger_auto_schema(
        operation_summary="Получить список партнеров",
        operation_description="Возвращает список партнеров компании."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class OtzyvyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Otzyvy.objects.all()
    serializer_class = OtzyvySerializer

    @swagger_auto_schema(
        operation_summary="Получить отзывы",
        operation_description="Возвращает список отзывов клиентов."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    @swagger_auto_schema(
        operation_summary="Получить тарифы",
        operation_description="Возвращает тарифы и проценты восстановления."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ZaiavkaViewSet(
    CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Zaiavka.objects.all()
    serializer_class = ZaiavkaSerializer

    @swagger_auto_schema(
        operation_summary="Создать заявку",
        operation_description="Отправка заявки на восстановление активов."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class FAQViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    @swagger_auto_schema(
        operation_summary="Получить список FAQ",
        operation_description="Возвращает все вопросы и ответы."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить FAQ",
        operation_description="Возвращает один FAQ по ID."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class NewsViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @swagger_auto_schema(
        operation_summary="Получить новости",
        operation_description="Возвращает список новостей."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получить новость",
        operation_description="Возвращает новость по ID."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)