from django.urls import path
from basic_app.views import my_other,my_relative_url

app_name = 'basic_app'

urlpatterns = [path("other/",my_other,name = "other_page_name"),
                path("relurl/",my_relative_url,name = 'relurl_page'),]
