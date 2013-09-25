from django.core.mail import send_mail
from django.conf import settings
from django.contrib.messages import info

from mezzanine.utils.views import render

from main.forms import ContactForm

def contact(request, template_name = 'index.html'):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			post_data = contact_form.cleaned_data
			nom = post_data.get('nom','')
			tel = post_data.get('tel','')
			from_email = post_data.get('email')
			body = post_data.get('message')
			recipient_list = list(settings.RECIPIENT_LIST)

			subject = 'HorizonPlus : Vous avez recu un email de %s' % from_email

			message = body 
			message += '<br />------------------------------------'
			message += '<br />%s (%s)' % (nom, tel)

			send_mail(subject, message, from_email, recipient_list)
			message = 'votre message a bien été envoyé'
			info(request, message, extra_tags='success')
	else:
		contact_form = ContactForm()

	context = {
		'contact_form' : contact_form,
	}

	return render(request, template_name, context)

