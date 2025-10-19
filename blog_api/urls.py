from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CategoryViewSet, TagViewSet, UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("posts", PostViewSet, basename="posts")
router.register("categories", CategoryViewSet, basename="category")
router.register("tags", TagViewSet, basename="tags")


urlpatterns = router.urls