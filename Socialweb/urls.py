"""
URL configuration for Socialweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_page,register_page,logout_page,login_page,friends_page,other_profile, search_friends
from stepanflow.views import ribbon
from django.conf.urls.static import static
from django.conf import settings
from azamat.views import profile, delete_avatar, create_post, delete_post, post_page, delete_comment
from rest_framework.routers import DefaultRouter
from azamat.views import PostViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page,name = 'home'),
    path('register/', register_page,name = 'register'),
    path('logout/', logout_page,name = 'logout'),
    path('login/', login_page,name = 'login'),
    path('profile/', profile, name='profile'),
    path('friends/', friends_page, name='friends'),
    path('delete-avatar/', delete_avatar, name='delete_avatar'),
    path('flow/', ribbon,name = 'ribbon'),
    path('chat/', include('chat.urls')),
    path('profile/<str:username>/', other_profile, name='other_profile'),
    path('friends/search/', search_friends, name='search_friends'),
    path('createpost/', create_post, name='create_post'),
    path('delete-post/<int:post_id>/', delete_post, name='delete_post'),
    path('post/<slug:post_slug>/', post_page, name='post'),
    path('comments/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
