from django.urls import path,include
from api.views import counts,accounts
urlpatterns = [
    path('course/',counts.CourseView.as_view({'get':'list'})),
    path('course/<int:pk>/',counts.CourseView.as_view({'get':'retrieve'})),
    path('auth/',accounts.LoginView.as_view()),
    path('mirco/',accounts.MicroView.as_view())
]
