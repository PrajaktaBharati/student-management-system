from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.shortcuts import render, get_object_or_404, redirect

def student_form(request):

    if request.method == 'POST':

        Student.objects.create(
            name=request.POST.get('name'),
            roll_number=request.POST.get('roll_number'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            course=request.POST.get('course'),
            gender=request.POST.get('gender'),
            address=request.POST.get('address')
        )

        return HttpResponse("Student Saved Successfully!")

    return render(request, 'students/student_form.html')


def student_list(request):
    students = Student.objects.all()

    return render(request, 'students/student_list.html' ,{'students': students})

def student_edit(request, id):

    student = get_object_or_404(Student, id = id)

    if request.method == 'POST' :

        student.name = request.POST.get("name")
        student.roll_number = request.POST.get("roll_number")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.course = request.POST.get("course")
        student.gender = request.POST.get("gender")
        student.address = request.POST.get("address")

        student.save()

        return redirect('student_list')
    return render(request, 'students/student_edit.html', {'students': student})

def student_delete(request,id):
    student = get_object_or_404(Student,id=id)

    if request.method == 'POST' :
        student.delete()

        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'students': student})