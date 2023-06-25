# -*- coding: utf-8 -*-
"""gestor_medias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.urls import path
from oauth2_provider import views
from config import settings

# OAuth2 provider endpoints
urlpatterns = [
    path('authorize/', views.AuthorizationView.as_view(), name="authorize"),
    path('token/', views.TokenView.as_view(), name="token"),
    path('revoke-token/', views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    urlpatterns += [
        path('applications/', views.ApplicationList.as_view(), name="list"),
        path('applications/register/', views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<pk>/', views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<pk>/delete/', views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<pk>/update/', views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    urlpatterns += [
        path('introspect/', views.IntrospectTokenView.as_view(), name="introspect"),
        path('authorized-tokens/', views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        path('authorized-tokens/<pk>/delete/', views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]
