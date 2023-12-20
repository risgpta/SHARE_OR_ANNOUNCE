# myapp/urls.py
from rest_framework.routers import DefaultRouter
from .views import LearningViewSet

router = DefaultRouter()
router.register(r'learning', LearningViewSet)

urlpatterns = router.urls

