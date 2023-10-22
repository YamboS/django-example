from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('bp/', views.BpList.as_view()),
    path('bp/create', views.BpCreate.as_view()),
    path('bp/<int:pk>/', views.BpDetail.as_view(),name='bp-detail'),

    path('weight/', views.WeightList.as_view()),
    path('weight/create', views.WeightCreate.as_view()),
    path('weight/<int:pk>/', views.WeightDetail.as_view(), name='weight-detail'),

    path('bg/', views.BloodGlucoseList.as_view()),
    path('bg/create', views.BloodGlucoseCreate.as_view()),
    path('bg/<int:pk>/', views.BloodGlucoseDetail.as_view(), name='bloodGlucose-detail'),
]