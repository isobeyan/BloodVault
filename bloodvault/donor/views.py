from django.shortcuts import render, HttpResponseRedirect
from .forms import MemberReg
from .models import Member

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = MemberReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            gr = fm.cleaned_data['group']
            reg = Member(name=nm, email=em, group=gr)
            reg.save()
            fm = MemberReg()
    else:
        fm = MemberReg()
    mm = Member.objects.all()
    return render(request, 'donor/insertandread.html', {'form':fm, 'mem':mm})


def update_data(request, id):
    if request.method == 'POST':
        pi = Member.objects.get(pk=id)
        fm = MemberReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         pi = Member.objects.get(pk=id)
         fm = MemberReg(instance=pi)

    return render(request, 'donor/update.html', {'form':fm})


def delete_data(request, id):
    if request.method=='POST':
        pi = Member.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')