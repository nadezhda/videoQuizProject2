from django.conf.urls import patterns, url, include
from equiz import views
from rest_framework.routers import DefaultRouter


# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'sections', views.SectionViewSet)
# router.register(r'mysections', views.MySectionViewSet)
# router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
    # url(r'^', include(router.urls)),
    # url(r'^index/$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^categories/$', views.CategoryList.as_view(), name='category-list'),
    url(r'^categories/(?P<pk>[\d]+)/$', views.CategoryDetail.as_view(), name='category-detail'),
    url(r'^sections/$', views.SectionList.as_view(), name='section-list'),
    url(r'^sections/(?P<pk>[\d]+)/$', views.SectionDetail.as_view(), name='section-detail'),
    url(r'^owner/sections/$', views.OwnerSectionList.as_view(), name='owner-section-list'),
    url(r'^owner/sections/(?P<pk>[\d]+)/$', views.OwnerSectionDetail.as_view(), name='owner-section-detail'),
    url(r'^owner/sections/create/$', views.OwnSectionCreate.as_view(), name='section_create'),
    url(r'^owner/sections/edit/(?P<pk>\d+)$', views.OwnSectionUpdate.as_view(), name='section_edit'),
    url(r'^owner/sections/delete/(?P<pk>\d+)$', views.OwnSectionDelete.as_view(), name='section_delete'),
    url(r'^owner/sections/(?P<pk>\d+)/questions/create/$', views.QuestionCreate.as_view(), name='question_create'),
    url(r'^owner/sections/questions/(?P<pk>\d+)/delete/$', views.QuestionDelete.as_view(), name='question_delete'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
)
# Login and logout views for the browsable API
urlpatterns += patterns('',
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += patterns('',
    url(r'^tests/$', views.qtests, name='qunit-tests'),
)