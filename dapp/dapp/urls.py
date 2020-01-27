from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api_auth/', include('rest_framework.urls')),
   ]