from django.conf.urls import patterns, include, url
from django.contrib import admin


from django.views.generic import TemplateView

from data_registry import views
from data_registry.views import PaperListView
from data_registry.views import PaperDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dfp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^dfp/',include('dfp.urls')),
    url(r'^$',TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^papers/(?P<paper_id>[0-9]+)/$',PaperDetailView,name='paper-detail'),
    url(r'^papers/',PaperListView.as_view(),name='paper-list'),

)
