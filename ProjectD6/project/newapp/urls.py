from django.urls import path, include


from .views import NewsList, NewsDetail, NewsSearch, AddNews, ChangeNews, DeleteNews, add_subscribe, \
    del_subscribe

urlpatterns = [

    # модуль Д4 - вывод инфы из БД, создание новостей, редактирование, удаление и прочее
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),  # Ссылка на детали новости
    path('search/', NewsSearch.as_view(), name='news_search'),

    # модуль Д5 - регистрация пользователей, ограничение прав доступа к сайту (1)
    path('add/', AddNews.as_view(), name='news_add'),
    path('edit/<int:pk>', ChangeNews.as_view(), name='news_edit'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='news_delete'),

    # модуль Д6 - подписка на рассылку на статью
    path('<int:pk>/add_subscribe/', add_subscribe, name='add_subscribe'),
    path('<int:pk>/del_subscribe/', del_subscribe, name='del_subscribe'),

]