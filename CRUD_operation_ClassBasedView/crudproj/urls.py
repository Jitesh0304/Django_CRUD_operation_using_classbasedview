from django.contrib import admin
from django.urls import path
from enroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AddShowView.as_view(), name="addshow"),
    path('updt/<int:id>/', views.UpdateData.as_view(), name="update"),
    path('delete/<int:id>/', views.DeleteData.as_view(), name="deleteOne"),
]
