"""course_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# from courses import views as views1
# from instances import views as views2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('courses.urls'))
    # path('courses/',views1.CourseListCreateView.as_view(),name='course-list-create'),
    # path('courses/<int:pk>/',views1.CourseDetailView.as_view(),name='course-detail'),
    # path('instances/',views2.InstanceListCreateView.as_view(),name='instance-list-create'),
    # path('instances/<int:pk>/',views2.InstanceDetailView.as_view(),name='instance-detail'),
]
