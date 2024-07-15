from django.urls import path
from . import views
urlpatterns = [
    path('categoryAdd/', views.addCategory),
    path('articleAdd/', views.addArticle),
    path('listCategory', views.listCategory),
    path('listArticle', views.listArticle),
    path('getCategoryById/<int:id>', views.getCategoryById),
    path('getArticleById/<int:id>', views.getArticleById),
    path('updateCategory/<int:id>', views.updateCategory),
    path('updateArticle/<int:id>', views.updateArticle),
    path('deleteCategory/<int:id>', views.deleteCategory),
    path('deleteArticle/<int:id>', views.deleteArticle)
]