from django.shortcuts import render, get_object_or_404, redirect
from Library.models import Student, Book, Borrowing, Course, Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    context = {
        'name': 'KHALLIS',
    }
    return render(request, 'index.html', context)

def view(request):
    brooo = {
        'LOL': 'HOHOHO',
    }
    return render(request, 'view.html', brooo)

def database(request):
    myCourses = Student.objects.all().values()
    books = Book.objects.all().values()
    borrow = Borrowing.objects.select_related('book_id','student_id').all()
    cont = {
        'Courses': myCourses,
        'Books': books,
        'Borrowings': borrow,
        'greeting' : 0
    }
    return render(request, 'database.html', cont)

def course(request):
    if request.method == 'POST':
        code = request.POST['code']
        description = request.POST['desc']
        
        # Save the course data
        data = Course(code=code, description=description)
        data.save()
        
        # Redirect to avoid resubmission on page refresh
        return redirect('course')  # Redirect to the course page

    else:
        cor = Course.objects.all().values()
        cont = {
            'message': '',
            'course': cor
        }
    return render(request, 'course.html', cont)

def mentor(request):
    # Retrieve all mentor records
    mentor_list = Mentor.objects.all().values()
    
    if request.method == 'POST':
        mentorid = request.POST['mentorid']
        mentorname = request.POST['mentorname']
        mentorroom = request.POST['mentorroom']
        data = Mentor(mentorid=mentorid, mentorname=mentorname, mentorroom=mentorroom)
        data.save()
    
    context = {
        'mentor_list': mentor_list
    }
    
    return render(request, 'newmentor.html', context)

def update_course(request, code):
    course = Course.objects.get(code=code)
    dict = {
        'course': course
    }
    return render(request, 'update_course.html', dict)

def update_course_post(request, code):
    course = Course.objects.get(code=code)
    description = request.POST['desc']
    course.description = description
    course.save()
    return HttpResponseRedirect(reverse('course'))

def delete_course(request, code):
    course = Course.objects.get(code=code)

    if request.method == 'POST':
        course.delete()
        return redirect('course')

    return render(request, 'delete_course.html', {'course': course})

def update_mentor(request, menid):
    data = Mentor.objects.get(menid=menid)
    dist = {
        'mentor': data
    }
    return render(request, 'update_mentor.html', dist)

def save_update_mentor(request,menid):
    data = Mentor.objects.get(menid=menid)
    name = request.POST['mentorname']
    room = request.POST['mentorroom']
    data.menname = name
    data.menroomno = room
    data.save()
    return HttpResponseRedirect(reverse('mentor'))

def search_course(request): 
    if request.method == 'GET':
        code = request.GET.get('code')
        if code:
            data = Course.objects.filter(code=code.upper())
        else: 
            data = None
        context = {
            'data': data
        }
        return render(request, 'search_course.html', context)
    return render(request, 'search_course.html')