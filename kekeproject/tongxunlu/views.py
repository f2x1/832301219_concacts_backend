from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt # 导入 @csrf_exempt
from .models import Contact
import json

@csrf_exempt # 禁用 CSRF 保护，方便 JS 直接 POST（作业允许）
def contact_list(request):
    """ 处理 /api/contacts/ 的 GET (读取) 和 POST (新建) """
    if request.method == "GET":
        contacts = Contact.objects.all()
        data = list(contacts.values('id', 'name', 'phone'))
        return JsonResponse({'contacts': data})

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            new_contact = Contact.objects.create(
                name=data['name'],
                phone=data['phone']
            )
            return JsonResponse({'message': '添加成功', 'id': new_contact.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt # 同样禁用
def contact_detail(request, pk):
    """ 处理 /api/contacts/<id>/ 的 PUT (修改) 和 DELETE (删除) """
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return JsonResponse({'error': '联系人不存在'}, status=404)

    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            contact.name = data.get('name', contact.name)
            contact.phone = data.get('phone', contact.phone)
            contact.save()
            return JsonResponse({'message': '修改成功'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == "DELETE":
        contact.delete()
        return JsonResponse({'message': '删除成功'}, status=204)