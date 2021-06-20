import datetime
from django.shortcuts import render
from .models import Details
from .serializers import formSerializer
import django.contrib.messages as messages
from datetime import date
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def submit_details(request):
    print("hi")
    if request.method == "POST":
        name = request.POST["name"]
        dob = request.POST["dob"]
        email = request.POST["email"]
        number = request.POST["number"]
        today = date.today()
        date_str = dob
        format_str = '%Y%m%d'
        datetime_obj = datetime.datetime.strptime(
            date_str.replace('-', ''), format_str)
        s = today-datetime_obj.date()
        if(s > datetime.timedelta(18*365) and len(number) == 10):
            details = Details(name=name, dob=dob, email=email, number=number)
            details.save()
            stu = Details.objects.all()
            print(stu)
            serializer = formSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            send_mail(
                'Form | Django',
                'Hi '+name+'\nThis is a test mail',
                'innoventixsolutionsbot@gmail.com',
                [email],
                fail_silently=False,
            )
            return HttpResponse(json_data, content_type='application/json')

        else:
            messages.error(
                request, "Age is less than 18 and/or number length should be equal to 10")
            return render(request, 'home.html')

    else:
        messages.error(request, 'Something went wrong!')
        return render(request, 'home.html')
