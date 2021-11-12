
from django.urls import path
from .views import LikeView,HomeView, ArticleDetailsView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article-detail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('add_category/',AddCategoryView.as_view(), name='add_category'),

    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>/', LikeView, name='like_post'),


    
]
