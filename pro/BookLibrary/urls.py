from django.urls import path
from BookLibrary import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bookform/',views.book_form,name='Book_Form'),
    path('authorform/',views.Author_Form,name='Author_Form'),
    path('updateauthor/<str:pk>/',views.Update_Author,name='Update_Author'),
    path('viewauthor/<str:pk>/',views.single_Author,name='Single_Author'),
    path('deleteauthor/<str:pk>/',views.delete_Author,name='delete_Author'),

    path('singlepost/<str:pk>/',views.Single_Post,name='Single_Post'),
    path('updatepost/<str:pk>/',views.Update_Post,name='Update_Post'),
    path('deletepost/<int:pk>/', views.delete, name='delete'),
    path('aggrigation/',views.Aggrigation,name='Aggrigation'),
]
