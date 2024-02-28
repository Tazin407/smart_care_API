from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views

router = DefaultRouter()
router.register('doctorlist/',views.DoctorViewset)
router.register('specializations/',views.SpecializationViewset)
router.register('designations/',views.DesignationViewset)
router.register('availabletime/',views.AvailableTimeViewset)
router.register('review/',views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls))
]
