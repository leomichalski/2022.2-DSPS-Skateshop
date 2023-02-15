from django.urls import path

from .views import HomePageView, FaqPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('faq/', FaqPageView.as_view(), name='faq')
]
