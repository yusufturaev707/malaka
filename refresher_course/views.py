from datetime import datetime
from io import BytesIO

import qrcode
import urllib3
from PIL import Image, ImageDraw
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db.models import Max, Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from print_pdf import paint_pdf, paint_pdf_gn
from refresher_course.constants import *
from .decorators import unauthenticated_user
from .forms import CreateCertificateForm, CreateCourseForm, CreateNationForm, CourseCompleteForm
from .models import Certificate, Course, CourseComplete, Nation
from .utils import qr_code_function, read_data_excell

urllib3.disable_warnings()


@login_required(login_url='login')
def statistics(request):
    return render(request, "refresher_course/mydtm.html")


@login_required(login_url='login')
def mydtm(request):
    Users_1 = []
    Users_2 = []
    Users_4 = []
    Users_5 = []
    Users_7 = []
    Users_8 = []
    Users_9 = []
    Users_10 = []
    Users_11 = []
    Users_12 = []
    Users_13 = []
    Users_18 = []
    Users_20 = []
    Users_21 = []
    Users_28 = []

    Course = []

    # for page in range(1, get_page(url=f"{URL}service_id=1", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=1&page={page}", HEADERS)
    #     for data in response:
    #         Users_1.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_1, course_name, 1))
    #
    # for page in range(1, get_page(url=f"{URL}service_id=2", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=2&page={page}", HEADERS)
    #     for data in response:
    #         Users_2.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_2, course_name, 2))

    for page in range(1, get_page(url=f"{URL}service_id=4", headers=HEADERS) + 1, 1):
        response = get_all_data(f"{URL}service_id=4&page={page}", HEADERS)
        for data in response:
            Users_4.append(data)

    test_day = "2023-02-13"
    course_name = "Chet tilini bilish darajasining “yozish” va “gapirish” koʼnikmalarini baholash boʼyicha malaka oshirish kursi (24 soat)"

    Course.append(get_data(test_day, Users_4, course_name, 4))

    # for page in range(1, get_page(url=f"{URL}service_id=5", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=5&page={page}", HEADERS)
    #     for data in response:
    #         Users_5.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_2, course_name, 2))

    # for page in range(1, get_page(url=f"{URL}service_id=7", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=7&page={page}", HEADERS)
    #     for data in response:
    #         Users_7.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_2, course_name, 2))
    #
    # for page in range(1, get_page(url=f"{URL}service_id=8", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=8&page={page}", HEADERS)
    #     for data in response:
    #         Users_8.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_2, course_name, 2))
    #
    # for page in range(1, get_page(url=f"{URL}service_id=9", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=9&page={page}", HEADERS)
    #     for data in response:
    #         Users_9.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_2, course_name, 2))

    for page in range(1, get_page(url=f"{URL}service_id=10", headers=HEADERS) + 1, 1):
        response = get_all_data(f"{URL}service_id=10&page={page}", HEADERS)
        for data in response:
            Users_10.append(data)

    test_day = "2023-03-17"
    course_name = "Barcha chet tillari bo‘yicha 'Multilevel' repetitsion (mock) test sinovi"

    Course.append(get_data(test_day, Users_10, course_name, 10))

    for page in range(1, get_page(url=f"{URL}service_id=11", headers=HEADERS) + 1, 1):
        response = get_all_data(f"{URL}service_id=11&page={page}", HEADERS)
        for data in response:
            Users_11.append(data)

    test_day = "2023-02-24"
    course_name = "TOEFL ITP"

    Course.append(get_data(test_day, Users_11, course_name, 11))

    for page in range(1, get_page(url=f"{URL}service_id=12", headers=HEADERS) + 1, 1):
        response = get_all_data(f"{URL}service_id=12&page={page}", HEADERS)
        for data in response:
            Users_12.append(data)

    test_day = "2023-02-24"
    course_name = "TOEIC® Listening and Reading Test"

    Course.append(get_data(test_day, Users_12, course_name, 12))

    for page in range(1, get_page(url=f"{URL}service_id=13", headers=HEADERS) + 1, 1):
        response = get_all_data(f"{URL}service_id=13&page={page}", HEADERS)
        for data in response:
            Users_13.append(data)

    test_day = "2023-02-24"
    course_name = "TOEIC® Speaking and Writing Test"

    Course.append(get_data(test_day, Users_13, course_name, 13))

    # for page in range(1, get_page(url=f"{URL}service_id=18", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=18&page={page}", HEADERS)
    #     for data in response:
    #         Users_18.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_2, course_name, 2))

    # for page in range(1, get_page(url=f"{URL}service_id=20", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=20&page={page}", HEADERS)
    #     for data in response:
    #         Users_20.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_2, course_name, 2))
    #
    # for page in range(1, get_page(url=f"{URL}service_id=21", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=21&page={page}", HEADERS)
    #     for data in response:
    #         Users_21.append(data)
    #
    # test_day = "2023-02-15"
    # course_name = "Ona tili va adabiyot fani ( O‘zbek tili) Milliy sertifikat uchun test topshiriqlarini shakllantirish malaka oshirish kursi (36 soat)"
    #
    # Course.append(get_data(test_day, Users_2, course_name, 2))

    # for page in range(1, get_page(url=f"{URL}service_id=28", headers=HEADERS) + 1, 1):
    #     response = get_all_data(f"{URL}service_id=28&page={page}", HEADERS)
    #     for data in response:
    #         Users_28.append(data)
    #
    # test_day = "2023-02-27"
    # course_name = "Ona (O‘zbek, Rus va Qoraqalpoq) tilidan yozish ko‘nikmasini baholash bo‘yicha malaka oshirish kursi"

    # Course.append(get_data(test_day, Users_28, course_name, 28))

    for page in range(1, get_page(url=f"{URL}service_id=28", headers=HEADERS) + 1, 1):
        response = get_all_data(f"{URL}service_id=28&page={page}", HEADERS)
        for data in response:
            Users_28.append(data)

    test_day = "2023-03-06"
    course_name = "Ona (O‘zbek, Rus va Qoraqalpoq) tilidan yozish ko‘nikmasini baholash bo‘yicha malaka oshirish kursi"

    Course.append(get_data(test_day, Users_28, course_name, 28))

    data = {
        "data": Course
    }
    return JsonResponse(data)


@login_required(login_url='login')
def change_qrcode(request):
    data = "https://dtm.uz/page/ilmiy_markaz"
    qrcode_img = qrcode.make(data=data)

    persons = Certificate.objects.all()

    for person in persons:
        canvas = Image.new("RGB", (500, 500), "white")
        ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        filename = f'qr_{person.cer_nomer}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        person.qr_code.save(filename, File(buffer))
        canvas.close()
    return HttpResponse("ok")


@login_required(login_url='login')
def a_print(request, pk):
    course = CourseComplete.objects.get(pk=pk)
    persons = Certificate.objects.filter(start_date=course.start_date).filter(month=course.month).order_by('id')
    # persons = Certificate.objects.filter(cer_nomer=532)
    for p in persons:
        if p.middle_name is None:
            p.middle_name = ''
            p.save()

    context = {
        "persons": persons,
    }
    return render(request, "refresher_course/print_certificate.html", context=context)


@login_required(login_url='login')
def a_print_one(request, pk):
    persons = Certificate.objects.filter(pk=pk)
    for p in persons:
        if p.middle_name is None:
            p.middle_name = ''
            p.save()

    context = {
        "persons": persons,
    }
    return render(request, "refresher_course/print_certificate.html", context=context)


def home(request):
    all_certificates = Certificate.objects.all()
    get_certificates = Certificate.objects.filter(status=True)
    notget_certificates = Certificate.objects.filter(status=False)
    courses = CourseComplete.objects.count

    kurslar = Course.objects.all()
    A = []
    for kurs in kurslar:
        t = []
        t.append(str(kurs.name).upper())
        total = Certificate.objects.filter(course__id=kurs.id)
        t.append(total)
        A.append(t)

    context = {
        'all_certificates': all_certificates,
        'get_certificates': get_certificates,
        'notget_certificates': notget_certificates,
        'courses': courses,
        'kurslar': A,
    }
    return render(request, "refresher_course/home.html", context=context)


@login_required(login_url='login')
def certificates(request):
    search = request.GET.get('search')
    n_show = request.GET.get('n_show')

    if search is None:
        get_certificates = Certificate.objects.all().order_by('-id')
        search = ''
    else:
        get_certificates = Certificate.objects.filter(
            Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(middle_name__icontains=search) | Q(
                cer_nomer__icontains=search)
        ).order_by('-id')

    if n_show is None:
        n_show = 15

    if n_show == '0':
        n_show = get_certificates.count()

    paginator = Paginator(get_certificates, int(n_show))
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    p_n = paginator.count
    page_count = page.paginator.page_range

    if n_show == p_n:
        n_show = 0

    context = {
        'certificates': get_certificates,
        'page_count': page_count,
        'page': page,
        'p_n': p_n,
        'search': search,
        'n_show': int(n_show),
    }
    return render(request, "refresher_course/certificates.html", context=context)


@login_required(login_url='login')
def complete_course(request, page=1):
    complete_courses = CourseComplete.objects.all()
    # page = request.GET.get('page')
    paginator = Paginator(complete_courses, per_page=15)
    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    p_n = paginator.count
    context = {
        'page_obj': page_object,
        'p_n': p_n,
    }
    return render(request, "refresher_course/complete_courses.html", context=context)


@login_required(login_url='login')
def fill_form(request):
    if request.method == 'POST':
        form = CourseCompleteForm(request.POST, request.FILES)
        if form.is_valid():
            ob = form.save(commit=False)
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            ob.save()
            course = form.cleaned_data['course']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            month = form.cleaned_data['month']
            begin_cer_nomer = form.cleaned_data['begin_cer_nomer']
            nationality = form.cleaned_data['nationality']
            certificate_turi = form.cleaned_data['certificate_turi']

            users = read_data_excell(excel_file)

            current_date = f'{datetime.today():%d.%m.%Y}'
            current_year = current_date.split('.')[-1]

            global max_reg_num
            max_reg_num = None
            data = "https://dtm.uz/page/ilmiy_markaz"

            cc = Certificate.objects.filter(year=current_year)
            if cc.count() == 0:
                max_reg_num = 0
            else:
                dict = cc.aggregate(Max('registered_number'))
                max_reg_num = int(dict['registered_number__max'])

            for user in users:
                begin_cer_nomer += 1
                max_reg_num += 1
                ob = Certificate.objects.create(
                    first_name=user[0],
                    last_name=user[1],
                    middle_name=user[2],
                    jshshr=user[3],
                    # invoice=user[4],
                    course=course,
                    start_date=start_date,
                    end_date=end_date,
                    month=month,
                    cer_nomer=begin_cer_nomer,
                    nationality=nationality,
                    registered_number=max_reg_num,
                    registered_day=current_date
                )
                if int(certificate_turi) == 1:
                    code = qr_code_function(ob)
                    ob.qr_code = "qr_codes/" + code + ".png"
                    ob.pdf_certificate = generate_obj_pdf(ob.id, code)
                    paint_pdf(ob, code)
                    ob.save()
                else:
                    code = qr_code_function(ob)
                    ob.qr_code = "qr_codes/" + code + ".png"
                    ob.pdf_certificate = generate_obj_pdf(ob.id, code)
                    paint_pdf_gn(ob, code)
                    ob.save()
            return redirect('certificates')
        else:
            return HttpResponse("Form isn't valid")
    else:
        form = CourseCompleteForm()
        # ob = Certificate.objects.latest('cer_nomer')
        # if not ob:
        #     end_cer_num = 0
        # else:
        #     end_cer_num = ob.cer_nomer
        return render(request, "refresher_course/import_file_form.html", {'form': form})


@login_required(login_url='login')
def searching(request):
    if request.method == "POST":
        year = request.POST.get('year')
        numbers = str(request.POST.get('cer_numbers')).strip().split(',')
        # registered_numbers = str(request.POST.get('registered_numbers')).strip().split(',')

        if year is not None and numbers is not None:
            persons = Certificate.objects.filter(year=year, cer_nomer__in=numbers).order_by('updated_at')

            # n = len(numbers)
            # for i in range(n):
            #     person = get_object_or_404(Certificate, cer_nomer=int(numbers[i]))
            #     print(person.id)
            #     person.registered_day = "21.11.2022"
            #     person.registered_number = int(registered_numbers[i])
            #     person.save()
        else:
            persons = None

        for p in persons:
            if p.middle_name is None:
                p.middle_name = ''
                p.save()

        context = {
            "persons": persons,
        }
        return render(request, "refresher_course/print_certificate.html", context=context)

    # fam = request.GET.get('fam')
    # ism = request.GET.get('ism')
    # sharf = request.GET.get('sharf')
    # course_id = request.GET.get('course')
    #
    # if fam is not None and ism is not None and sharf is not None and course_id is not None and course_id.isnumeric():
    #     ob = CourseComplete.objects.get(id=int(course_id))
    #     persons = Certificate.objects.filter(first_name__icontains=fam, last_name__icontains=ism,
    #                                          middle_name__icontains=sharf, course=ob.course)
    # else:
    #     persons = None
    #
    # finish_courses = CourseComplete.objects.all()

    context = {
        # 'courses': finish_courses,
        'persons': None,
    }
    return render(request, "refresher_course/searchone_form.html", context)


@login_required(login_url='login')
def courses(request):
    courses = Course.objects.all().order_by('id')
    context = {
        'courses': courses,
    }
    return render(request, "refresher_course/courses.html", context=context)


@login_required(login_url='login')
def nations(request):
    nations = Nation.objects.all()
    context = {
        'nations': nations,
    }
    return render(request, "refresher_course/nations.html", context=context)


@login_required(login_url='login')
def create_certificate(request):
    if request.method == 'POST':
        data = "https://dtm.uz/page/ilmiy_markaz"
        qrcode_img = qrcode.make(data=data)
        form = CreateCertificateForm(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            canvas = Image.new("RGB", (500, 500), "white")
            ImageDraw.Draw(canvas)
            canvas.paste(qrcode_img)
            filename = f'qr_{ob.cer_nomer}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            ob.qr_code.save(filename, File(buffer))
            canvas.close()
            ob.save()
            return redirect('certificates')

    else:
        form = CreateCertificateForm()
        return render(request, "refresher_course/create_certificate.html", {'form': form})


@login_required(login_url='login')
def create_course(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.save()
            return redirect('courses')

    else:
        form = CreateCourseForm()
        return render(request, "refresher_course/create_course.html", {'form': form})


@login_required(login_url='login')
def create_nation(request):
    if request.method == 'POST':
        form = CreateNationForm(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.save()
            return redirect('nations')

    else:
        form = CreateNationForm()
        return render(request, "refresher_course/create_nation.html", {'form': form})


@login_required(login_url='login')
def view_certificate(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    context = {
        'certificate': certificate,
    }
    return render(request, "refresher_course/view_certificate.html", context=context)


@login_required(login_url='login')
def edit_certificate(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        form = CreateCertificateForm(request.POST, instance=certificate)
        form.save()
        return redirect('certificates')

    else:
        form = CreateCertificateForm(instance=certificate)
        return render(request, "refresher_course/edit_certificate.html", {"certificate": certificate, 'form': form})


@login_required(login_url='login')
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CreateCourseForm(request.POST, instance=course)
        form.save()
        return redirect('courses')

    else:
        form = CreateCourseForm(instance=course)
        return render(request, "refresher_course/edit_course.html", {"course": course, 'form': form})


@login_required(login_url='login')
def edit_nation(request, pk):
    nation = get_object_or_404(Nation, pk=pk)
    if request.method == 'POST':
        form = CreateNationForm(request.POST, instance=nation)
        form.save()
        return redirect('nations')

    else:
        form = CreateNationForm(instance=nation)
        return render(request, "refresher_course/edit_nation.html", {"nation": nation, 'form': form})


# Delete
@login_required(login_url='login')
def delete_certificate(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == "POST":
        certificate.delete()
        return redirect('certificates')
    else:
        return render(request, 'refresher_course/delete_sertificate.html', {'certificate': certificate})


@login_required(login_url='login')
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect('courses')
    else:
        return render(request, 'refresher_course/delete_course.html', {'course': course})


@login_required(login_url='login')
def delete_nation(request, pk):
    nation = get_object_or_404(Nation, pk=pk)
    if request.method == "POST":
        nation.delete()
        return redirect('nations')
    else:
        return render(request, 'refresher_course/delete_nation.html', {'nation': nation})


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, "refresher_course/register/login.html")


def logout(request):
    auth_logout(request)
    return redirect('login')


from django.http import HttpResponse

from .utils import render_to_pdf  # created in step 4


def generate_obj_pdf(instance_id, code):
    obj = Certificate.objects.get(id=instance_id)
    context = {'instance': obj}
    pdf_certificate = render_to_pdf('pdfs/invoice.html', context)
    filename = f"{code}.pdf"
    obj.pdf_certificate.save(filename, File(BytesIO(pdf_certificate.content)))
    return "pdfs/" + filename
