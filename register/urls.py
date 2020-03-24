from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
    path('list/', views.EmployeeList.as_view(), name='employee_list'),
    path('detail/<int:id>', views.EmployeeDetail.as_view(), name='employee_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
