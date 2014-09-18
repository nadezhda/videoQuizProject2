from django.conf.urls import patterns, include, url
from django.contrib import admin
from equiz import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'equiz.views.homepage', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('equiz.urls')),
)
