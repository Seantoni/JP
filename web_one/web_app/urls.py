from django.urls import path
from web_app import views
from django.conf import settings
from django.conf.urls.static import static

#for TEMPLATE TAGGING
app_name = "web_app"

urlpatterns = [
    path("other/", views.other, name="other"),
    path("relative/", views.relative, name="relative"),
    path("register/",views.register, name= "register"),
    path("login/",views.user_login,name="user_login"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
