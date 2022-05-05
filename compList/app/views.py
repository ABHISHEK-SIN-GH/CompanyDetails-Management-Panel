from urllib import request
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import redirect, render
from .models import companyDetails
from django. views. decorators. csrf import csrf_exempt
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    companyData = companyDetails.objects.all()
    # companyData1 = companyDetails.objects.get(pk=1)
    # print(companyData1.Company_City)
    # print(companyData)
    # print(companyData.filter(Company_Name='TCS'))
    # return HttpResponse('This is compList App')
    return render(request,'index.html',{'Company_Datas':companyData})

def details(request,pk):
    compDetails = companyDetails.objects.get(pk=pk)
    # print(compDetails)
    return render(request,'companyDetails.html',{'Details':compDetails})   

def listCompany(request):
    if request.method == 'POST':
        name = request.POST['name']
        website = request.POST['website']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        industry = request.POST['industry']
        data = companyDetails(Company_Name = name, Company_Website = website, Company_Phone_Number = phone, 
        Company_Address = address, Company_City = city, Company_State = state, Company_Country = country, Industry_List = industry)
        data.save()
    return render(request,'Company.html')

def upCompany(request,pk):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        website = request.POST['website']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        industry = request.POST['industry']
        data = companyDetails(id=id,Company_Name = name, Company_Website = website, Company_Phone_Number = phone, 
        Company_Address = address, Company_City = city, Company_State = state, Company_Country = country, Industry_List = industry)
        data.save()
    company = companyDetails.objects.get(pk=pk)  
    return render(request,'updateCompany.html',{'company':company})    

def delCompany(request,pk):
    data = companyDetails.objects.get(id=pk)
    data.delete()
    companyData = companyDetails.objects.all()
    return redirect('/',{'Company_Datas':companyData})