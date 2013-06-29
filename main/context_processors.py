from mezzanine.conf import settings

def general_data(request):
    return {
        	'SITE_PHONE': settings.SITE_PHONE,
        	'SITE_EMAIL': settings.SITE_EMAIL,
        	'SITE_ADDRESS': settings.SITE_ADDRESS,
        }
