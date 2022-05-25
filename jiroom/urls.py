from django.urls import path, include
from jiroom.views import PostList, top_page

urlpatterns = [
    path('', top_page)
    # path('', PostList.as_view(), name='post_list')
]