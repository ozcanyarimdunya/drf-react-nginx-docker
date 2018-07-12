from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, CountryViewSet, OperationListView, OperationDetailView, OperationViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'country', CountryViewSet)
router.register(r'operation-viewset', OperationViewSet, base_name='operation')

urlpatterns = [
    path('', include(router.urls)),
    path('operation-api-view/', OperationListView.as_view()),
    path('operation-api-view/<int:pk>', OperationDetailView.as_view()),
]
