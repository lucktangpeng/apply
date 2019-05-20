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
    # url(r"record/$", views.record.as_view()),
    url(r"record/$", views.RecordViewSet.as_view({"get": "list", "post": "create"}),name="record_list"),
    url(r'record/(?P<pk>\d+)$', views.RecordViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
        }), name="record_detail"),
    url(r'sum/(?P<pk>\d+)$', views.Sum_view.as_view()),
    url(r'many_about/$', views.Many_about.as_view()),
    url(r'time_restrict/$', views.time_restrict.as_view())
]
