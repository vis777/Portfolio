from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Newapp import views

urlpatterns = [
    path('home_page/', views.home_page, name="home_page"),
    path('download/', views.download, name="download"),
    path('upload_resume/', views.upload_resume, name="upload_resume"),
    path('view_resumes/', views.view_resumes, name="view_resumes"),
    path('contact/', views.contact, name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)