"""
URL configuration for ART_GALLERY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from MYAPP import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('view_artist', views.view_artist, name='view_artist'),
    path('admin2', views.admin2, name='admin2'),
    path('change_password', views.change_password, name='change_password'),
    path('view_user', views.view_user, name='view_user'),
    path('view_complaints_reply', views.view_complaints_reply, name='view_complaints_reply'),
    path('view_complaints_reply2/<id>', views.view_complaints_reply2, name='view_complaints_reply2'),
    path('review_box', views.review_box, name='review_box'),
    path('view_complaints_reply2post', views.view_complaints_reply2post, name='view_complaints_reply2post0'),
    path('artist_registration', views.artist_registration, name='artist_registration'),
    path('view_accepted_artist', views.view_accepted_artist, name='view_accepted_artist'),
    path('adminHome', views.adminHome, name='adminHome'),
    path('loginPost', views.loginPost, name='loginPost'),

    path('add_design', views.add_design, name='add_design'),
    path('add_post', views.add_post, name='add_post'),
    path('add_product', views.add_product, name='add_product'),
    path('add_schedule', views.add_schedule, name='add_schedule'),
    path('add_schedulepost', views.add_schedulepost, name='add_schedulepost'),
    path('view_booking', views.view_booking, name='view_booking'),
    path('view_comment_and_like/<pid>', views.view_comment_and_like, name='view_comment_and_like'),
    path('view_like/<pid>', views.view_like, name='view_like'),
    path('view_design', views.view_design, name='view_design'),
    path('view_other_work_and_like', views.view_other_work_and_like, name='view_other_work_and_like'),
    path('view_payment_details', views.payment_details, name='view_payment_details'),
    path('view_post', views.view_post, name='view_post'),
    path('view_product', views.view_product, name='view_product'),
    path('view_profile_and_update', views.view_profile_and_update, name='view_profile_and_update'),
    path('view_shedule', views.view_shedule, name='view_shedule'),
    path('artistHome', views.artistHome, name='artistHome'),
    path('review_box', views.review_box, name='review_box'),
    path('accept_artist/<id>', views.accept_artist, name='accept_artist'),
    path('reject_artist/<id>', views.reject_artist, name='reject_artist'),
    path('change_passwordpost', views.change_passwordpost, name='change_passwordpost'),
    path('view_profile_and_updatepost', views.view_profile_and_updatepost, name='view_profile_and_updatepost'),
    path('add_designpost', views.add_designpost, name='add_designpost'),
    path('delete_design/<id>', views.delete_design, name='delete_design'),
    path('edit_schedule/<id>', views.edit_schedule, name='edit_schedule'),
    path('edit_schedulepost', views.edit_schedulepost, name='edit_schedulepost'),
    path('delete_schedule/<id>', views.delete_schedule, name='delete_schedule'),
    path('add_productpost', views.add_productpost, name='add_productpost'),
    path('edit_product/<id>', views.edit_product, name='edit_product'),
    path('edit_productpost', views.edit_productpost, name='edit_productpost'),
    path('delete_product/<id>', views.delete_product, name='delete_product'),
    path('add_postpost', views.add_postpost, name='add_postpost'),
    path('edit_post/<id>', views.edit_post, name='edit_post'),
    path('edit_postpost', views.edit_postpost, name='edit_postpost'),
    path('delete_post/<id>', views.delete_post, name='delete_post'),
    path('artist_registrationpost', views.artist_registrationpost, name='artist_registrationpost'),
    path('artist_change_password', views.artist_change_password, name='artist_change_password'),
    path('artist_change_passwordpost', views.artist_change_passwordpost, name='artist_change_passwordpost'),
    path('artist2', views.artist2, name='artist2'),
    path('reject_design/<id>', views.reject_design, name='reject_design'),
    path('accept_design/<id>', views.accept_design, name='accept_design'),






    path('logincode', views.logincode, name='logincode'),
    path('user_change_password_post', views.user_change_password_post, name='user_change_password_post'),
    path('registrationcode', views.registrationcode, name='registrationcode'),
    path('user_view_design', views.user_view_design, name='user_view_design'),
    path('user_view_product', views.user_view_product, name='user_view_product'),
    path('user_view_schedule', views.user_view_schedule, name='user_view_schedule'),
    path('user_add_booking', views.user_add_booking, name='user_add_booking'),
    path('user_view_booking', views.user_view_booking, name='user_view_booking'),
    path('user_sendfeedback', views.user_sendfeedback, name='user_sendfeedback'),
    path('user_view_post', views.user_view_post, name='user_view_post'),
    path('user_add_comment', views.user_add_comment, name='user_add_comment'),
    path('user_add_like', views.user_add_like, name='user_add_like'),
    path('user_view_profile', views.user_view_profile, name='user_view_profile'),
    path('user_edit_profile', views.user_edit_profile, name='user_edit_profile'),
    path('user_view_artist', views.user_view_artist, name='user_view_artist'),
    path('user_artistsendfeedback', views.user_artistsendfeedback, name='user_artistsendfeedback'),
    path('user_view_rating', views.user_view_rating, name='user_view_rating'),
    path('user_view_post', views.user_view_post, name='user_view_post'),
    path('user_artistsendcomplaint', views.user_artistsendcomplaint, name='user_artistsendcomplaint'),
    path('user_view_complaint', views.user_view_complaint, name='user_view_complaint'),
    path('user_view_comment', views.user_view_comment, name='user_view_comment'),
    path('viewchat', views.viewchat, name='viewchat'),
    path('sendchat', views.sendchat, name='sendchat'),
    path('payment', views.payment, name='payment'),
    path('recomendation', views.recomendation, name='recomendation'),






path('chatwithuser', views.chatwithuser, name='chatwithuser'),
path('chatview', views.chatview, name='chatview'),
path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),

]
