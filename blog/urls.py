from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.post_list,name='post-list'),
    path('<int:pk>',views.post_detail,name='post-detail'),
    path('delete/<int:id>',views.delete_post,name='delete-post'),
    path('update/<int:id>',views.update_post,name='update-post'),
   

]
