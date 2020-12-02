from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static 
from images import views

urlpatterns = [
    path('', views.home, name="home"),
    path('images/', views.All_Images, name="images"),
    path('success', views.success, name='success'),
    path('displayimages',views.display_images, name='displayimages'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
  
