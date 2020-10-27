from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import auth
from .models import *

# Create your views here.

def login_page(request):
    template_name = 'app/login.html'
    return render(request, template_name)


def logout(request):
        auth.logout(request)
        return redirect('app:login')

def profile(request):
    template_name = 'app/profile.html'
    context = {''}
    return render(request, template_name)


def profile_type(request):
    if request.method == 'POST':
        profiletype = request.POST.get('profiletype')
        user_data = User.objects.get(id=request.user.id)
        user_data.role = profiletype
        user_data.save()

        return redirect('app:dashboard')
    return redirect('app:profile')


def dashboard(request):
    template_name = 'app/dashboard.html'
    return render(request, template_name)


def exercise(request):
    template_name = 'app/videos.html'
    return render(request, template_name)


def patients(request):
    template_name = 'app/patients.html'
    data = User.objects.filter(role='patient')

    # user.socialaccount_set.filter(provider='google')[0].extra_data

    context = {
        'patients': data
    }
    return render(request, template_name, context)


def therapy(request, id):
    template_name = 'app/therapy.html'

    therapy = None
    try:
        therapy = Therapy.objects.filter(patient=id)

    except Exception as e:
        therapy = None

    context = {
        'therapy': therapy
    }
    return render(request, template_name, context)


def tests(request, test_id, p_id):
    template_name = 'app/tests.html'

    tests = None
    therapy = None
    test_session = request.GET.get('testSession')

    try:
        therapy = Therapy.objects.filter(patient=p_id)
        tests = Test.objects.filter(therapys=test_id)

        if test_session:
            test_session = TestSession.objects.filter(tests=test_session)
            


    except Exception as e:
        tests = None

    context = {
        'therapy': therapy,
        'tests': tests,
        'test_session': test_session
    }
    return render(request, template_name, context)

def feeds(request):
    template_name = 'app/feeds.html'

    feed = None
    try:
        feed = News.objects.all()

    except Exception as e:
        feed = None

    context = {
        'feed': feed
    }
    return render(request, template_name, context)




def chart(request, name):
    template_name = 'app/testChart.html'

    chart = None
    data_x = []
    data_y = []
    time = []
    try:
        print(name)
        chart = DataFileOne.objects.filter(filename=name)

        if chart:
            for x in chart:
                data_x.append(x.x)
                data_y.append(x.y)
                time.append(x.time)

    except Exception as e:
        chart = None

    context = {
        'x': data_x,
        'y': data_y,
        'time': time
    }
    return render(request, template_name, context)