from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, HomePageView, signup, MediaFileListView, MediaFileCreateView, PhotoListView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('booklist/', BookListView.as_view(), name='book_list'),
    path('<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('', HomePageView.as_view(), name='home_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('media_files', MediaFileListView.as_view(), name='mediafile_list'),
    path('media_files/new', MediaFileCreateView.as_view(), name='mediafile_create'),
    path('photos/', PhotoListView.as_view(), name='photo_list')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)