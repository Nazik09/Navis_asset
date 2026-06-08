from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet,ZaiavkaViewSet, FAQViewSet ,NewsViewSet , OtzyvyViewSet ,PriceViewSet

router = DefaultRouter()

router.register(r'partners', PartnerViewSet)
router.register(r'zaiavka', ZaiavkaViewSet)
router.register(r'faq', FAQViewSet)
router.register(r'news', NewsViewSet)
router.register(r'otzyvy', OtzyvyViewSet)

router.register(r'price', PriceViewSet)
urlpatterns = [
    path('', include(router.urls)),
]