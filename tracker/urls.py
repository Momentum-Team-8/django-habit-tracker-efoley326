from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.homepage, name='homepage'),
    path('project/', views.habit_list, name='habit_list'),
    path('project/', views.add_habit, name='add_habit'),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns =[
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
