"""define users url patterns"""

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns=[
    #��¼ҳ��
    url(r'^login/$',login,{'template_name':'users/login.html'},
        name='login'),
    #ע��
    url(r'^logout/$',views.logout_view,name='logout'),
    #ע��ҳ��
    url(r'^register/$',views.register,name='register'),
]
