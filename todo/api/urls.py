from django.urls import path, include
from rest_framework import routers
from api.views import TodoModelViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'todos', TodoModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
