from django.urls import path,include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView,ArticleViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewset,base_name='article')
urlpatterns = [
    # path('api/', article_list),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('detail/<int:pk>/', article_detail),
    path('api/', ArticleAPIView.as_view()),
    path('articledet/<int:id>/', ArticleDetails.as_view()),
    path('generic/api/<int:id>/', GenericAPIView.as_view()),

]
