from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    AddCommentView,
)
from . import views, urls
from cal import views as cal_views
from mailer import views as mail_views



urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('shopping/', views.shopping, name='shopping'),
    path('shopping/<int:product_id>/', views.product_detail, name='product_detail'),
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),   
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
    path('receipt/', views.receipt, name = "receipt"),
    path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('all_sales/', views.all_sales, name = 'all_sales'),
    path('health/', views.health, name='health'),
    path('add_health/', views.add_health, name='add_health'),
    path('calendar/', cal_views.CalendarView.as_view(), name='calendar'),
    path('event/new/', cal_views.event, name='event_new'),
    path('event/<int:pk>/', cal_views.EventUpdateView.as_view(), name='event_edit'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('mail/', mail_views.sendMail, name='send_mail'),

    ]