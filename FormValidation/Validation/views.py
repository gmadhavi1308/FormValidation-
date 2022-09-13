from django.shortcuts import render
from Validation.forms import *
# Create your views here.
def regform(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['first_name']
            context={"message":"Hello {}, your Registration completed successfully..".format(fname)}
            return render(request,'success.html',{'context':context});
        else:
            return render(request,'reg.html',{'form':form});
    else:
        form = Registration()
        return render(request,'reg.html',{'form':form});
# Create your views here.
