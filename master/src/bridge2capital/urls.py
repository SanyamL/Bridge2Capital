"""bridge2capital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from django_otp.admin import OTPAdminSite
# admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path(r'', include('favicon.urls')),
    path('', include('english.urls')),
    path('hi/', include('hindi.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from django.contrib import admin
admin.site.site_header = 'XTRACAP - Bridge2Capital Administration'                    # default: "Django Administration"
admin.site.index_title = 'Bridge2Capital'                 # default: "Site administration"
admin.site.site_title = 'Admin' # default: "Django site admin"