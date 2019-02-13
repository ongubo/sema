
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views as user_views
from django.conf.urls import url
from . import settings
from  blog.views import logout_view
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'posts', user_views.PostViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='blog/login.html'),
    ),
    path(
        '',
        auth_views.LoginView.as_view(
            template_name='blog/login.html'),
    ),
    # path('logout', user_views.logout, name="logout"),
    url(r'^logout/$', logout_view,
        {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path(
        'accounts/',
        include('django.contrib.auth.urls')
    ),
    path(
        'dashboard/',
        include('blog.urls')
    ),
    path('api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


# JWT 
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('hello/', user_views.HelloView.as_view(), name='hello'),

]
