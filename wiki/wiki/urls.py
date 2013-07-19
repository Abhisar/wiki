from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search/$','articles.views.search'),
    url(r'^wiki/$','articles.views.all_articles'),
    url(r'^wiki/(?P<page_name>[^/]+)/$','articles.views.view_page'),
    url(r'^wiki/(?P<page_name>[^/]+)/edit/$','articles.views.edit_page'),
    url(r'^wiki/(?P<page_name>[^/]+)/save/$','articles.views.save_page'),
    url('accounts/login/$','wiki.views.login'),
    url('accounts/logout/$','wiki.views.logout'),
    url('accounts/auth/$','wiki.views.auth_view'),
    url('accounts/loggedin/$','wiki.views.loggedin'),
    url('accounts/invalid/$','wiki.views.invalid_login'),
    url('accounts/register/$','wiki.views.register_user'),
    url('accounts/register_success/$','wiki.views.register_success'),
    url(r'^hello_template/$','articles.views.hello_template'),
    url(r'^hello_template_simple/$','articles.views.hello_template_simple'),
    # url(r'^$', 'wiki.views.home', name='home'),
    # url(r'^wiki/', include('wiki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
