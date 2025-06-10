import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def reminder_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            date = data.get('date')
            time = data.get('time')
            message = data.get('message')
            remind_by = data.get('remind_by')

            # For demo, return what you received:
            return JsonResponse({
                'status': 'success',
                'data': {
                    'date': date,
                    'time': time,
                    'message': message,
                    'remind_by': remind_by
                }
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'message': 'Only POST allowed'}, status=405)
