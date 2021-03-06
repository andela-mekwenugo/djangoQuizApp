"""djangoQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home_view')
]

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login',
        {'template_name': 'main/login.html'},
        name='user_login'
        ),

    url(r'^logout/$', 'logout',
        {'next_page': 'home_view'},
        name='user_logout'
        ),
    url(r'^main/', include('main.urls')),
    url(r'^accounts/',
        include('allauth.urls'),
        name='google_login'),

)

handler404 = 'main.views.custom_404'
handler500 = 'main.views.custom_500'
