from django.urls import path
from blog.views import PostList, PostDetail, top

urlpatterns = [
    path("", top, name="top"),
    path("blog", PostList.as_view(), name="blog"),
    path("article/<int:pk>/", PostDetail.as_view(), name="article"),
]