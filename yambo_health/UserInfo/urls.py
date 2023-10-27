from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('BloodPressure/', views.BloodPressureList.as_view()),
    path('BloodPressure/create', views.BloodPressureCreate.as_view()),
    path('BloodPressure/<int:pk>/', views.BloodPressureDetail.as_view(),name='BloodPressure-detail'),

    path('weight/', views.WeightList.as_view()),
    path('weight/create', views.WeightCreate.as_view()),
    path('weight/<int:pk>/', views.WeightDetail.as_view(), name='weight-detail'),

    path('BloodGlucose/', views.BloodGlucoseList.as_view()),
    path('BloodGlucose/create', views.BloodGlucoseCreate.as_view()),
    path('BloodGlucose/<int:pk>/', views.BloodGlucoseDetail.as_view(), name='bloodGlucose-detail'),
]