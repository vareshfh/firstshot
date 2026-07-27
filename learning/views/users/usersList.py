from django.shortcuts import render
from django import views
from django.views.generic import ListView
from learning.models import Users

class UsersList(ListView):
    model = Users
    context_object_name = "users"
    template_name = "learning/userslist.html"

# class UsersList(views):
#     template_name = "learning/userslist.html"
#     def get(self, request, *args, **kwargs):
#         users = Users.objects.all()
#         return render(request,self.template_name,context={"users":users})
#     def post(self, request, *args, **kwargs):
#         pass
#     def put(self, request, *args, **kwargs):
#         pass
#     def patch(self, request, *args, **kwargs):
#         pass
#     def delete(self, request, *args, **kwargs):
#         pass


# def UsersList(request):
#     users = Users.objects.all()
#     return render(request,"learning/userslist.html",context={"users":users})