from django.shortcuts import redirect, render

from user_author.models import UserAuthModel


# Create your views here.
def home(request):
    return render(request, 'home.html')
def regestation(request):
    if request.method== 'POST':
        username=request.POST.get("username")
        full_name=request.POST.get("full_name")
        email=request.POST.get("email")
        contact_number=request.POST.get("contact_number")
        password=request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password==confirm_password:

        
            user_info=UserAuthModel.objects.create(
                username=username,
                full_name=full_name,
                email=email,
                contact_number=contact_number,
                password=password,
            
                
            )
            user_info.save()
        return redirect('login')

            
    else:
        
        print("passwird not match")   
       

    
    return render(request, 'regestation.html')
def login(request):
    return render(request, 'loging.html')