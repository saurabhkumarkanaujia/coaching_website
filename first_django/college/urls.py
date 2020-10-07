from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('reg_details/',views.reg_details,name='reg_details'),
    path('delete_user/<pk>',views.delete_user,name='delete_user'),
    path('edit_user/<pk>',views.edit_user,name='edit_user'),
    path('update_user/',views.update_user,name='update_user'),
    path('change_password/',views.change_password,name='change_password'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('update_user_profile/',views.update_user_profile,name='update_user_profile'),
    path('logout/',views.logout,name='logout'),
    path('education_details/',views.education_details,name='education_details'),
    path('education/',views.education,name='education'),
    path('insert_edu_details/',views.insert_edu_details,name='insert_edu_details'),
]
