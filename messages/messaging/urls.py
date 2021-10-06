from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name="api-overView"),
    path('show-all/', views.getAllMessages, name="all-messages"),
    path('read-message/<str:pk>', views.readMessage, name="read-message"),
    path('write-message/', views.writeMessage, name="write-message"),
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),
    path('user-messages/<str:user>', views.getUserMessages, name="user-messages"),
    path('user-unread/<str:sender>',
         views.getUserUnreadMessages, name="user-unread-messages"),
    path('user-auth/',
         views.userAuth, name="user-auth"),






]
