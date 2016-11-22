

#from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf.urls import include, url


from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^signup', views.signupPage, name='signup'),
    url(r'^$', views.index, name='index'),
    url(r'^auth/$', views.auth_view, name='authenticate'),

    url(r'^register/$', views.register_user),

    url(r'^register_success/$', views.register_success),
    url(r'^register_invalid/$', views.register_invalid),

    url(r'^loggedin/$', views.loggedin),
    url(r'^invalid/$', views.invalid_login),
    url(r'^home/$', views.guest_home),

    url(r'^logout/$', views.logout),

]



# Uncomment the next two lines to enable the admin:
"""
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_test.views.home'),

    # url(r'^django_test/', include('django_test.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django_test.views.login'),
    url(r'^accounts/auth/$', 'django_test.views.auth_view'),
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),

    url(r'^accounts/register/$', 'django_test.views.register_user'),
    url(r'^accounts/register_success/$', 'django_test.views.register_success'),
    url(r'^accounts/register_invalid/$', 'django_test.views.register_invalid'),

    url(r'^accounts/reset_password/$', 'django_test.views.reset_password'),
    url(r'^accounts/reset_auth/$', 'django_test.views.reset_password_form'),

    url(r'^accounts/delete_user/$', 'django_test.views.delete_user'),
    url(r'^accounts/delete_auth/$', 'django_test.views.delete_auth'),


    url(r'^signup', views.signupPage, name='signup'),
    url(r'^$', views.index, name='index'),
)"""
