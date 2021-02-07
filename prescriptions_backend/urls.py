from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import PrescriptionViewSet

router = routers.DefaultRouter()
router.register(r'prescriptions', PrescriptionViewSet)
# router.register(r'assigs', AssigViewSet)
# router.register(r'memberassigs', MemberAssigSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]