from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Category, Doctor, Profile
from django.contrib.auth import login, authenticate, logout as django_logout
from .forms import SignupForm, DoctorForm, LoginForm, EnterpriseForm, EditProfileForm
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib import messages



def index(request):
    categories = Category.objects.filter(sort="DOCTOR")
    user=request.user
    context = {'categories': categories, 'user': user}
    return render(request, 'doctor/index.html', context)


def profile(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.filter(user=user)
    context = {'user': user, 'profile': profile}

    return render(request, 'doctor/profile.html', context)


def profile_edit(request, pk):
    instance = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('doctor:profile', pk)
    else:
        form = EditProfileForm()
    return render(request, 'doctor/edit_profile.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {
        'form': form,
    })



def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('doctor:index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def logout(request):
    django_logout(request)
    return render(request, 'doctor/index.html')


def doctor_certification(request, pk):
    user = User.objects.get(pk=pk)
    category = Category.objects.filter(sort='DOCTOR')
    for i in category:
        if user == i.user:
            messages.error(request, '이미 등록!', extra_tags='alert')
            return redirect('doctor:index')
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            # Category 저장

            form.save()
            Category.objects.create(user=user, sort='DOCTOR')
            return redirect('doctor:index')
    else:
        form = DoctorForm()
    return render(request, 'doctor/doctor_certification.html', {
        'form': form,
    })


# def individual_certification(request, pk):
#     user = User.objects.get(pk=pk)
#     category = Category.objects.filter(sort='INDIVIDUAL')
#     for i in category:
#         if user == i.user:
#             messages.warning(request, '이미 등록')
#             return redirect('doctor:index')
#     Category.objects.create(user=user, sort='INDIVIDUAL')
#     messages.success(request, '등록 완료')
#     return redirect('doctor:index')


def enterprise_certification(request, pk):
    user = User.objects.get(pk=pk)
    category = Category.objects.filter(sort='ENTERPRISE')

    if request.method == 'POST':
        form = EnterpriseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user

            # Category 저장
            for i in category:
                if user == i.user:
                    messages.warning(request, '이미 등록')
                    return redirect('doctor:index')
            form.save()
            Category.objects.create(user=user, sort='ENTERPRISE')
            messages.success(request, '등록 완료')
            return redirect('doctor:index')
    else:
        form = EnterpriseForm()
    return render(request, 'doctor/enterprise_certification.html', {
        'form': form,
    })

def doctor_form(request, pk):
    user = User.objects.get(pk=pk)
    doctor_info = Doctor.objects.get(user=user)
    context = {
        'id': user.username,
        'name': doctor_info.name,
        'medical_name': doctor_info.medical_name,
        'address': doctor_info.address,
        'phone_number': doctor_info.phone_number,
        'license_number': doctor_info.license_number,
    }
    return render(request, 'doctor/doctor_form.html', context)


def for_user(request, pk):
    return render(request, 'doctor/for_user.html')





