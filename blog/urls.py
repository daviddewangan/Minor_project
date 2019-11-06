
from django.urls import path
from blog import views


urlpatterns = [
    path('',views.index,name="index"), 
    path('<int:id>/',views.detail,name="detail"),
    path('<int:id>/result/',views.result,name="result"),
    path('form/',views.addChoice,name="form"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('blog/<int:id>',views.choiceDetail,name = "detail"),
    path('feed', views.PostList.as_view(), name='home'),
    path('<int:pk>/detail', views.PostDetail.as_view(), name='post_detail'),
    ]