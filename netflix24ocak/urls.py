from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from appMy.views import *
from appUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name="indexPage"),
    path('Netflix/', indexBrowsePage, name="indexBrowsePage"),
    path('netflix/<pid>/', profileLogin, name="indexProfile"),

    # === USER ===
    path('profile/', profileUser, name="profileUser"),
    path('delete-profile/<pid>/', profileDelete, name="profileDelete"),
    path('account/', accountUser, name="accountUser"),
    path('login/', loginUser, name="loginUser"),
    path('register/', registerUser, name="registerUser"),
    path('logoutUser/cıkıs', logoutUser, name="logoutUser"),
    
    # === LISTS ===
    path('Netflix/diziler/', seriesPage, name='seriesPage'),
    path('Netflix/filmler/', moviesPage, name='moviesPage'),
    path('Netflix/yeni-populer/', popularPage, name='popularPage'),
    path('Netflix/listem/', mylistPage, name='mylistPage'),
    # path('Netflix/diziler/', detailPage, name='detailPage'),
    # path('Netflix/diziler/<pid>', detailPage, name='detailPage'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
