from django.urls import path
from api.views import business, accounts

urlpatterns = [
    path('course/', business.CourseView.as_view({'get': 'list'})),
    path('course/<int:pk>/', business.CourseView.as_view({'get': 'retrieve'})),
    path('article/', business.ArticleView.as_view({'get': 'list'})),
    path('article/<int:pk>/', business.ArticleView.as_view({'get': 'retrieve'})),
    path('shopping/', business.Shopping.as_view({'get':'list','post':'create','delete':'destroy','put':'retrieve'})),
    path('buy/', business.Buy.as_view({'get':'list','post':'create','put':'retrieve'})),
    path('auth/', accounts.LoginView.as_view()),
    path('mirco/', accounts.MicroView.as_view()),
]
