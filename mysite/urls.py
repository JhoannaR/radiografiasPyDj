from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dicom),
    path('dynalog/', views.dynalog),


]
# las rutas son Apis
