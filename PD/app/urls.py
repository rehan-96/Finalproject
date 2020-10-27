from django.urls import path
from . import views, feed

app_name = 'app'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', views.logout, name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('profile/type/', views.profile_type, name='profile_type'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/exercise/', views.exercise, name='exercise'),
    path('dashboard/patients/', views.patients, name='patients'),
    path('dashboard/patients/therapy/<int:id>/', views.therapy, name='therapy'),
    path('dashboard/patients/tests/<int:test_id>/<int:p_id>/', views.tests, name='tests'),
    path('dashboard/chart/<str:name>/', views.chart, name='chart'),

    path('dashboard/feed/', views.feeds, name='feeds'),
    path('feed/rss/', feed.NewsFeed(), name='news_feed'),
]



# 1045131371485-urd7akdp49pf7q911l6u8625h2863faa.apps.googleusercontent.com
# gTBqxoKLtbc0BwGMjfgMF6uO