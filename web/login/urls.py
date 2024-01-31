from django.urls import path, include
from . import views

urlpatterns = [
    #path("", views.landingpageview.as_view(), name="landing"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.UzduotisListView.as_view(),name='uzrasai'),

]