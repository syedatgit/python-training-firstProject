
from django.conf.urls import url,include
from third_app import views

app_name = 'relative_url'

urlpatterns=[
    url('other/',views.other,name='other'),
    url('index/',views.index,name='index'),
    url('relativeurl',views.relative,name='relative'),
]
