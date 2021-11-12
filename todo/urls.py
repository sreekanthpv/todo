from django.urls import path
from todo import views


urlpatterns=[
    path('todos',views.TodoMixinList.as_view()),
    path('todos/<int:id>',views.TodoDetailMixin.as_view()),
    path('todos/accounts/signup',views.UserRegistrationView.as_view()),
    path('todos/accounts/signin',views.UserSigninView.as_view()),
]
