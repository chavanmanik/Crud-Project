from io import BytesIO
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        student_id = pythondata.get('id', None)
        if student_id is not None:
            try:
                student = Student.objects.get(id=student_id)
                serializer = StudentSerializer(student)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except Student.DoesNotExist:
                return HttpResponse(status=404)

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
# @csrf_exempt
# def student_api(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)  # Import statement corrected: io.ByteIO -> io.BytesIO
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')


# @csrf_exempt
# def student_api(request):
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)  # Corrected: JSONRenderer().parse() -> JSONParser().parse()
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythondata,)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Update !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
   
 
# @csrf_exempt
# def student_api(request):
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)  # Corrected: JSONRenderer().parse() -> JSONParser().parse()
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg': 'Data Delete !!'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res, safe=False)      