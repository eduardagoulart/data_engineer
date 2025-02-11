"""data_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from data_project.core import views

router = routers.DefaultRouter()
router.register(r'insurance', views.InsuranceViewSet)
router.register(r'summarize_by_months', views.MonthsViewSet)
router.register(r'summarize_by_year', views.YearViewSet)
router.register(r'summarize_by_agencyid', views.AgencyIdViewSet)
router.register(r'summarize_by_state', views.StateViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('search/', views.SearchList.as_view()),
    path('report/', views.ReportDataView.as_view()),
]


