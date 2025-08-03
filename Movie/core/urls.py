from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('movies',views.MoiveListCreateView,basename='movie_list')
router.register('reviews',views.ReviewListCreateView,basename='review_list')
urlpatterns = [
    path('',include(router.urls))
    # path('',Movielists ),
    # path('<pk>/',MovieUpdate ),
    # path('movie',views.MoiveListCreateView.as_view() ),
    # path('movie/<pk>/',views.MovieDetailsview.as_view() ),

    # path('reviews/',views.ReviewListCreateView.as_view(),name='movie_list' ),
    # path('<pk>/',views.ReviewsDetailsview.as_view(), name='movie_details' ),
]
