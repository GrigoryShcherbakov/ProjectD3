from django.urls import path, include
from .views import NewsList, NewsDetailView, NewsSearch, AddNews, ChangeNews, DeleteNews
from .views import IndexView

urlpatterns = [


    path('', NewsList.as_view()),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Ссылка на детали новости
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('add/', AddNews.as_view(), name='news_add'),
    path('edit/<int:pk>', ChangeNews.as_view(), name='news_edit'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='news_delete'),
    path('', IndexView.as_view()),
]