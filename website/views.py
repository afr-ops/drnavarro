from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import EmailMultiAlternatives

def send_user_mail(user):
    subject = 'Titulo del correo'
    template = get_template('templates/mi_template_correo.html')

    content = template.render({
        'user': user,
    })

    message = EmailMultiAlternatives(subject, #Titulo
                                    ''",
                 						settings.EMAIL_HOST_USER, #Remitente
                                    [user.email]) #Destinatario

    message.attach_alternative(content, 'text/html')
    message.send()





def home(request):
	return render(request, 'home.html', {})
'''
def contact(request):
	if request.method == 'POST':
		#do stuff

		message_name =	request.POST['message-name']	
		message_email = request.POST['message-email']	
		message = request.POST['message'] 	
		email_from = settings.EMAIL_HOST_USER
		#send mail
		

		send_mail(
			message_name,	
			message_email, 
			message,
			['nbmalnero@gmail.com'],
			fail_silently=False,
			)


		return render(request, 'contact.html', {'message_name': message_name}) 

	else:
		return render(request, 'contact.html', {}) 	


	'''