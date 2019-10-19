from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/', views.EmployeeCBV1.as_view()),
    path('json/<int:id>/',views.EmployeeCBV.as_view()),
    path('json1/',views.EmployeelistCBV.as_view()),
    path('json2/',views.EmployeelistCBV1.as_view()),
    path('json3/',views.EmployeelistCBV2.as_view()),
    path('error/<int:id>/',views.EmployeeCBV3.as_view()),
    path('error1/<int:id>/', views.EmployeeCBV4.as_view()),
    # path('api/',views.EmployeecrudCBV.as_view()),

]
