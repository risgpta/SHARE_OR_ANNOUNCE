
from rest_framework import routers

from .models import Profiles
from .views import ProfileViewSet

router = routers.SimpleRouter()
router.register('profiles', ProfileViewSet, basename='profile')
# router.register('profile_model',Profiles,basename='profile_model')

urlpatterns = router.urls
