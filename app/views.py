from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from app.mixins import LoginRequiredMixin, AjaxableResponseMixin

from app.models import Company, Todo, CompanyUser
from app.utils import TokenGenerator


class HomeView(TemplateView):
    template_name = "app/index.html"

class CompanyList(LoginRequiredMixin, ListView):
    template_name = "company/company_list.html"
    model = Company

    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user)


class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "company/company_form.html"
    success_url = reverse_lazy('company_list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(CompanyCreate, self).form_valid(form)

class CompanyUpdate(AjaxableResponseMixin, UpdateView):
    model = Company
    template_name = "company/company_form.html"
    success_url = reverse_lazy('company_list')

    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user)

class CompanyDelete(LoginRequiredMixin, DeleteView ):
    model = Company
    template_name = "company/company_confirm_delete.html"
    success_url = reverse_lazy('company_list')

    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user)

class TodoList(LoginRequiredMixin, ListView):
    template_name = "todo/todo_list.html"
    model = Todo

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.created_by = self.request.user
        object.save()
        return super(TodoCreate, self).form_valid(form)

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = "todo/todo_form.html"
    success_url = reverse_lazy('todo_list')

    def dispatch(self, *args, **kwargs):
        print self.request
        return super(TodoUpdate, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)

class TodoDelete(LoginRequiredMixin, DeleteView ):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = reverse_lazy('todo_list')

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)

class CompanyUserList(LoginRequiredMixin, ListView):
    template_name = "company_user/company_user_list.html"
    model = CompanyUser

    def get_queryset(self):
        return CompanyUser.objects.filter(company__created_by=self.request.user)

class CompanyActiveUserList(LoginRequiredMixin, ListView):
    template_name = "company_user/company_user_list.html"
    model = CompanyUser

    def get_queryset(self):
        return CompanyUser.objects.filter(company__created_by=self.request.user, state=True)


class CompanyUserCreate(LoginRequiredMixin, CreateView):
    model = CompanyUser
    template_name = "company_user/company_user_form.html"
    success_url = reverse_lazy('company_user_list')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.token = TokenGenerator.__get_random_token_lower__(16)
        object.save()
        return super(CompanyUserCreate, self).form_valid(form)

# class CompanyUserUpdate(LoginRequiredMixin, UpdateView):
#     model = CompanyUser
#     template_name = "company_user/company_user_form.html"
#     success_url = reverse_lazy('company_user_list')

class CompanyUserDelete(LoginRequiredMixin, DeleteView ):
    model = CompanyUser
    template_name = "company_user/company_user_confirm_delete.html"
    success_url = reverse_lazy('company_user_list')

    def get_queryset(self):
        return CompanyUser.objects.filter(company__created_by=self.request.user)

class UserCompanyList(LoginRequiredMixin, ListView):
    template_name = "company/company_list.html"
    model = CompanyUser

    def get_queryset(self):
        return CompanyUser.objects.filter(user=self.request.user)