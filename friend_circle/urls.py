from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from users import views
from users.views import LogoutView
#关于静态文件图片的访问
from django.views.static import serve
from friend_circle.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.Register,name = "register"),
    path('hello/', views.hello),
    path('login/', views.Login_View,name = "login"),
    path('logout/', LogoutView.as_view(), name="logout"),  # name其别名
    path('', views.Main_View, name='main'),
    path('personal_center/', views.Personal_center, name='personal_center'),
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),

    path('edit/', views.edit, name='edit'),

]
