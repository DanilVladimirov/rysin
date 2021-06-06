from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rysin import settings
from siterysin.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page, name='startpage'),
    path('pub-create/', pubcreate, name='pub-create'),
    path('pub-del/', pubdel, name='pub-del'),
    path('albums/', albums_page, name='albums-page'),
    path('album/<int:aid>/', album_page, name='album'),
    path('feedback/', feedback_page, name='feedback-page'),
    path('addfeedback/', add_feedback, name='add-feedback'),
    path('caregories/', categories_files, name='categories'),
    path('caregory/<int:categ_id>/', category, name='category'),
    path('file/<int:file_id>', file, name='file'),
    path('search/', search_page, name='search-page'),
    path('login/', login_page, name='login-page'),
    path('register/', register_page, name='register-page'),
    path('logout/', logout_page, name='logout-page')
]
