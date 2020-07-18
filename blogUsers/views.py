from django.shortcuts import render

# Create your views here.
def registerView(request):
    form = UserCreationForm()
    context = {
        "form" : form
    }    
    return render(request,'blogUsers/userRegister.html', context)