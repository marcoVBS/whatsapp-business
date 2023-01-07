from .views import MessageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/messages', MessageViewSet, basename='message')
urlpatterns = router.urls