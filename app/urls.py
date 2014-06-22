'''
 :author: "Dharmendra Verma"
 :copyright: "Copyright 2013, Shopsense.Co" 
 :created: 22/06/14
 :email: "dharmendraverma@shopsense.co"   
 :github: @xrage 

'''

from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    # Examples:
  url(r'^company/list$', CompanyList.as_view(), name='company_list'),
  url(r'^company/new$', CompanyCreate.as_view(), name='company_new'),
  url(r'^company/edit/(?P<pk>\d+)$', CompanyUpdate.as_view(), name='company_edit'),
  url(r'^company/delete/(?P<pk>\d+)$', CompanyDelete.as_view(), name='company_delete'),
  url(r'^todo/list$', TodoList.as_view(), name='todo_list'),
  url(r'^todo/new$', TodoCreate.as_view(), name='todo_new'),
  url(r'^todo/edit/(?P<pk>\d+)$', TodoUpdate.as_view(), name='todo_edit'),
  url(r'^todo/delete/(?P<pk>\d+)$', TodoDelete.as_view(), name='todo_delete'),
  url(r'^company_user/list$', CompanyUserList.as_view(), name='company_user_list'),
  url(r'^company_user/active/list$', CompanyActiveUserList.as_view(), name='company_user_active_list'),
  url(r'^company_user/new$', CompanyUserCreate.as_view(), name='company_user_new'),
  # url(r'^company_user/edit/(?P<pk>\d+)$', CompanyUserUpdate.as_view(), name='company_user_edit'),
  url(r'^company_user/delete/(?P<pk>\d+)$', CompanyUserDelete.as_view(), name='company_user_delete'),  # url(r'^company_user/delete/(?P<pk>\d+)$', CompanyUserDelete.as_view(), name='company_user_delete'),

)