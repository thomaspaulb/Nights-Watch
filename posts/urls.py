from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[   
    url(r'^$', views.PostList.as_view(), name='all'),
    url(r'new/$', views.CreatePost.as_view(), name='create'),
    url(r'by/(?P<username>[-\w]+)', views.UserPost.as_view(), name='for_user'),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetails.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
]