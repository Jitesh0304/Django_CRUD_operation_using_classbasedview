from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Student
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View




class AddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = Student()
        stud = User.objects.all()
        context={'FORM':fm, 'data':stud}
        return context

    def post(self, request):
        fm = Student(request.POST)
        if fm.is_valid():
            # fm.save()                                         # By this way also we can save data.... OR
            nm = fm.cleaned_data['name']
            eml = fm.cleaned_data['email']
            psw = fm.cleaned_data['password']
            registation = User(name= nm, email= eml, password= psw)
            registation.save()
            return HttpResponseRedirect('/')



class UpdateData(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = Student(instance=pi)
        return render(request, 'enroll/update.html', {'FORM':fm})
    
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')



class DeleteData(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        # print(kwargs)
        # print(kwargs['id'])   ## from here you will get the user id
        dlt_id = kwargs['id']
        User.objects.get(id= dlt_id).delete()
        return super().get_redirect_url(*args, **kwargs)