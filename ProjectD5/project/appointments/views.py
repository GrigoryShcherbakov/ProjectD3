from datetime import datetime

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from .models import Appointment


# обрабатывает запрос и сохраняет новые объекты в БД (в базе данных), models.py
class AppointmentView(View):
    # получаем шаблон для ввода данных
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    # отправляем на сервер нашу информацию и сохраняем в БД
    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # блок для отправки писем из базы данных любому адресату
        # создали объект в БД, и отправляем его поля по почте, то есть сформировать из них само письмо, для удобства
        # имя клиента сделаем темой, выделим ее жирным шрифтом и чтоб показывалось в письме первым, далее идет само
        # сообщение содержащее краткую суть проблемы и в заключении добавить дату записи. И всё это отправлялось на
        # почту любому адресату

        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            # имя клиента и дата записи будут в теме для удобства
            message=appointment.message,  # сообщение с кратким описанием проблемы
            from_email='factoryskill@yandex.ru',  # почта с которой отправляем письма
            recipient_list=['ges1987@list.ru'],  # список получателей, например, секретарь, врач и т. д.
            fail_silently=False,
        )

        return redirect('make_appointment')