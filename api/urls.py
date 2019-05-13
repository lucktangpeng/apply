from django.conf.urls import url, include
from api import views

urlpatterns = [
    # url(r"course/$", views.course.as_view({"get": "list"})),
    url(r'course/$', views.CourseViewSet.as_view({"get": "list", "post": "create"}), name="course_list"),
    url(r'course/(?P<pk>\d+)$', views.CourseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name="course_detail"),
    url(r"phone/$", views.phone.as_view()),
    url(r"record/$", views.record.as_view()),
]
