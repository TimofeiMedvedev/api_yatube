from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from api.views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet,)
router.register('groups', GroupViewSet,)
router.register(
    r'posts/(?P<post_id>.+)/comments',
    CommentViewSet,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
