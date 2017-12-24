"""define users url patterns"""

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns=[
    #µÇÂ¼Ò³Ãæ
    url(r'^login/$',login,{'template_name':'users/login.html'},
        name='login'),
    #×¢Ïú
    url(r'^logout/$',views.logout_view,name='logout'),
    #×¢²áÒ³Ãæ
    url(r'^register/$',views.register,name='register'),
]
