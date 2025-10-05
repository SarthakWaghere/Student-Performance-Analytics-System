from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_data, name='upload_data'),
    path('api/predict/', views.predict_performance, name='predict_performance'),
    path('association-rules/', views.association_rules, name='association_rules'),
    path('clustering/', views.clustering_results, name='clustering_results'),
]
