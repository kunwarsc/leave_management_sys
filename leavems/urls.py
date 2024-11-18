
from django.contrib import admin

from django.urls import path,include
from django.views.generic import TemplateView


from accounts.views import employee_login
from employee_panel.views import logout
from myadmin.views import dashboard, admin_login, user_logout

urlpatterns = [
    path('', employee_login, name='employee_login'),
    path('user_logout/', user_logout, name='logout'),
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),
    path('myadmin/', include('myadmin.urls')),
    path('employee_panel/', include('employee_panel.urls')),
]
