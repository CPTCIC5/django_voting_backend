from django.urls import path
from . import views

app_name='app1'

urlpatterns = [
    path('',views.index,name='index'),
     path('detail/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
