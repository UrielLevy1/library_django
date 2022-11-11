from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

from . import settings
from books.views import books
from books.mylogin import mylogin, mylogout, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('mylogin/', mylogin, name="mylogin"), 
    # path('accounts/', include("django.contrib.auth.urls")),  # new
    path('', books),
    path('mylogout/', mylogout, name="logout"), 
    path('register/', register, name="register"), 

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
