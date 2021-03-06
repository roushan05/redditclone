from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def signup(request):
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html', {'error':'Username already exists'})
            except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                    login(request, user)

                    return render(request,'accounts/signup.html')
        else:
            return render(request,'accounts/signup.html', {'error':'passwords do not match'})

    else:
        return render(request,'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password= request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next'  in request.POST:
                if request.POST['next'] is not None:
                    return redirect(request.POST['next'])
            return redirect('home')

            # Redirect to a success page.
        else:
            return render(request,'accounts/login.html', {'error':'Username and password do not match'})


    else:
        return render(request,'accounts/login.html')

def logoutview(request) :
    if request.method =='POST':
        logout(request)
        return redirect('home')
