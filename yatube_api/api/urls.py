from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v2 = routers.DefaultRouter()
router_v2.register('posts', PostViewSet,)
router_v2.register('groups', GroupViewSet,)
router_v2.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
)

urlpatterns = [
    path('v1/', include(router_v2.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
