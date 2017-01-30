#! -*- coding=utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def send_first_mail(form):
    plaintext = get_template('app/mail_detail.html')
    b= {'name':form['name'],
        'phone':form['phone'],
        'order':form['order']}
    message_body = plaintext.render(b)
    email = EmailMultiAlternatives('Пришла заявка с сайта ПитЛайн59',
                         message_body,
                         to=['che-email@ya.ru',
                             ])
    email.attach_alternative(message_body, "text/html")
    print email.send()
