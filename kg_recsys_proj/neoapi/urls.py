from django.urls import include, path
from rest_framework import routers
from .views import CardViewSet, RecomendationList, buy_card

router = routers.DefaultRouter()
router.register(r'card', CardViewSet, 'Card')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('recomendedCards/<slug:pid_slug>/', RecomendationList.as_view()),
    path('buy_card/', buy_card
    ),
]