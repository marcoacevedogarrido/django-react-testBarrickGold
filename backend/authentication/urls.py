from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authentication.api.usuario import RegisterView

urlpatterns = [
    # path('api/login', LoginView.as_view()),
    # path('api/logout', LogoutView.as_view()),
    path('api/registro', RegisterView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
