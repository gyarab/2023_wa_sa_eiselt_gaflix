
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls'), name='movies'),
    path('', TemplateView.as_view(template_name='movies/home.html'), name='home'),
    path('druhy/', TemplateView.as_view(template_name='movies/druhy.html'), name='druhy'),
]
