from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from apps.users.models import NewsletterSubscriber
import json

@csrf_exempt
@require_POST
def subscribe_newsletter(request):
    try:
        # Since it's going to be a JSON fetch request
        data = json.loads(request.body)
        email = data.get('email')
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)
        
        subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
        if created:
            return JsonResponse({'message': 'Successfully subscribed to the newsletter!'})
        else:
            return JsonResponse({'message': 'You are already subscribed!'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
