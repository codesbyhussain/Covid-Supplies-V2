from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Donor, BloodGroup
from .forms import DonorForm, Eligible, appointment, loginform
from django.core.mail import send_mail, mail_admins
import datetime
# Create your views here.
def index(request):
    return render(request, 'bldon/index.html')

def donorregister(request):
    if request.method == 'POST':
        form=DonorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            donor= Donor.objects.last()
            return redirect('login')

    else:
        form = DonorForm()

    return render(request, 'bldon/register.html', {'form':form})

#useless
def eligible (request):
    if request.method == 'POST':
        form1=Eligible(request.POST)
        if form1.is_valid():
            obj=form1.cleaned_data['donated']
            if obj == 'yes':
                return render(request,'bldon/donated.html')
            obj=form1.cleaned_data['age']
            if obj == 'no':
                return render(request,'bldon/age.html')
            obj=form1.cleaned_data['disease']
            if obj == 'yes':
                return render(request,'bldon/disease.html')

            return redirect('login')
    else:
        form1=Eligible()

    return render(request,'bldon/eligible.html', {'form1': form1})

def app(request, donor_id):
    if request.method == 'POST':
        form=appointment(request.POST)
        if form.is_valid():
            obj=form.cleaned_data['setdate']
            try:
                don=Donor.objects.get(pk = donor_id)
                don.reward+=1
                don.last_donate= datetime.date.today()
                don.save()
                email_val= getattr(don, 'email')
                send_mail(don, str(obj), 'avenger.hussain14@gmail.com', [email_val])
                return render(request, 'bldon/Emailsent.html')
            except Donor.DoesNotExist:
                raise Http404("Donor does not exist")
    else:
        form=appointment()

    return render(request, 'bldon/appointment.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form=loginform(request.POST)
        if form.is_valid():
            lname = form.cleaned_data['name']
            try:
                don= Donor.objects.get(name = lname)
                passw = form.cleaned_data['password']
                datedays = datetime.date.today() - don.last_donate
                agedays = (datetime.date.today() - don.date_of_birth)
                if passw == don.retpass():
                    context = {'donor' : don,
                    'agereq': (datetime.date.today() - don.date_of_birth) > datetime.timedelta(days=18*365),
                    'healthreq': (datetime.date.today() - don.last_donate) > datetime.timedelta(days=95),
                    'aval' : (18*365-agedays.days), 'hval': ( 95 - datedays.days)}
                    return render(request, 'bldon/showinfo.html', context)
            except Donor.DoesNotExist:
                raise Http404("Donor does not exist")


    else:
        form =loginform()

    return render(request, 'bldon/login.html', {'form': form})
