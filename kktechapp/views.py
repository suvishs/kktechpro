from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from datetime import datetime, time
from pytz import timezone
from kktechapp.models import rawmaterials, ProjectManagement, Attendance, LeaveApplication, Tools
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import Q

# Create your views here.

# ------------------------General------------------------

def Register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirm_password')

            if password == confirmpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already Taken")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Id is already Exists...")
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.info(request, "User Successfuly created...")
                    return redirect('Usrlogin')
            else:
                messages.info(request, "Both password is not matching")
                return redirect('Register')
        return render(request, 'General/Register.html')
    except PermissionDenied as e:
        return render(request, 'General/error_page.html', {'error_message': str(e)})

def Usrlogin(request):
    try:
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.info(request, "Username or Password Is Wrong...")
                return redirect('index')
        return render(request, 'General/Usrlogin.html')
    except PermissionDenied as e:
        return render(request, 'General/error_page.html', {'error_message': str(e)})

def logout(request):
    auth.logout(request)
    return redirect('Usrlogin')

# ------------------------Attendance------------------------

def index(request):
    return render(request, "General/index.html")

def mark_attendance(request):
    user = request.user
    if request.method == 'POST':
        ist = timezone('Asia/Kolkata')
        current_time = datetime.now(ist).time()
        current_date = datetime.now(ist).date()

        # Define time ranges for attendance marking
        morning_start = time(8, 30)
        morning_end = time(9, 30)
        intermediate_time = time(13, 0)
        evening_start = time(18, 0)
        evening_end = time(18, 30)

        punch_stat = ''
        if current_time < morning_start:
            punch_stat = 'Overtime'
        if morning_start <= current_time <= morning_end:
            punch_stat = 'OnTimeMorning'
        elif morning_end < current_time < intermediate_time:
            punch_stat = 'LatePunchMorning'
            
        elif intermediate_time <= current_time < evening_start:
            punch_stat_evening = 'EarlyPunchEvening'
        elif evening_start <= current_time <= evening_end:
            punch_stat_evening  = 'OntimeEvening'
        elif current_time > evening_end:
            punch_stat_evening  = 'Overtime'
        
        if Attendance.objects.filter(usr=request.user, date=current_date).exists():
            attendance = Attendance.objects.filter(usr=request.user, date=current_date).first()
            if current_time > intermediate_time:
                if attendance.evening_time:
                    return JsonResponse({'status': 'already_marked'})
                attendance.evening_time = current_time
                attendance.punch_stat_evening = punch_stat_evening
                attendance.date = current_date
                attendance.save()
                return JsonResponse({'status':'success'})
            else:
                if attendance.morning_time:
                    return JsonResponse({'status': 'already_marked'})
                attendance.morning_time = current_time
                attendance.punch_stat = punch_stat
                attendance.date = current_date
                attendance.save()
                return JsonResponse({'status':'success'})
        else:
            if current_time < intermediate_time:
                new_punch = Attendance(usr=request.user, date=current_date, morning_time=current_time, punch_stat=punch_stat)
                new_punch.save()
                return JsonResponse({'status':'success'})
            else:
                new_punch = Attendance(usr=request.user, date=current_date, evening_time=current_time,punch_stat_evening=punch_stat_evening)
                new_punch.save()
                return JsonResponse({'status':'success'})
    return redirect("index")

def overtime(request):
    attendance = Attendance.objects.filter(Q(punch_stat="overtime") | Q(punch_stat_evening="overtime"))
    users = User.objects.all()
    return render(request, "General/overtime.html", {"attendance":attendance, "users":users})
    
from datetime import datetime, timedelta

def viewallatendancereport(request):
    attendance = Attendance.objects.all()
    users = User.objects.all()
    eight_hours = timedelta(hours=8)
    for i in attendance:
        if i.morning_time and i.evening_time:
            morning_datetime = datetime.combine(datetime.today(), i.morning_time)
            evening_datetime = datetime.combine(datetime.today(), i.evening_time)
            working_hour = evening_datetime - morning_datetime
            difference = working_hour - eight_hours
            print()
            i.working_hour = working_hour
            if working_hour <= eight_hours:
                i.difference = "0Hrs"
            else:
                i.difference = difference
            i.save()
    return render(request, "General/Attendance_Report.html", {"attendance": attendance, "users": users})


def sortattandance(request):
    users = User.objects.all()
    if request.method == "POST":
        start_date = request.POST.get("start_date")
        print(start_date)
        end_date = request.POST.get("end_date")
        print(end_date)
        by_user = request.POST.get("by_user")
        print(by_user)
        if by_user == "all":
            attendance = Attendance.objects.filter(date__gte=start_date, date__lte=end_date)
            return render(request, "General/Attendance_Report.html", {"attendance":attendance, "users":users})
        else:
            usr = User.objects.get(username=by_user)
            attendance = Attendance.objects.filter(date__gte=start_date, date__lte=end_date, usr=usr)
            return render(request, "General/Attendance_Report.html", {"attendance":attendance, "users":users})
        
def sortattandanceovertime(request):
    users = User.objects.all()
    if request.method == "POST":
        start_date = request.POST.get("start_date")
        print(start_date)
        end_date = request.POST.get("end_date")
        print(end_date)
        by_user = request.POST.get("by_user")
        print(by_user)
        if by_user == "all":
            attendance = Attendance.objects.filter(date__gte=start_date, date__lte=end_date)
            return render(request, "General/overtime.html", {"attendance":attendance, "users":users})
        else:
            usr = User.objects.get(username=by_user)
            attendance = Attendance.objects.filter(date__gte=start_date, date__lte=end_date, usr=usr)
            return render(request, "General/overtime.html", {"attendance":attendance, "users":users})

def Applicationforleave(request):
    if request.method == "POST":
        empname = request.POST.get('empname')
        reason = request.POST.get('reason')
        leave = LeaveApplication(empname=empname, reason=reason, usr=request.user)
        leave.save()
        messages.info(request, "Leave application submited successfuly...")
        return redirect('Applicationforleave')
    return render(request, "General/Applicationforleave.html")

def Viewleaveaplications(request):
    applications = LeaveApplication.objects.all()
    return render(request, "General/Viewleaveaplications.html",{"applications":applications})

def ApproveViewleaveaplications(request):
    applications = LeaveApplication.objects.all()
    return render(request, "General/ApproveViewleaveaplications.html",{"applications":applications})

def ApproveViewleaveaplication(request, id):
    application = LeaveApplication.objects.get(id=id)
    application.approval = True
    application.save()
    messages.info(request, f"{application.empname}'s Leave application approved...")
    return redirect('ApproveViewleaveaplications')

# ------------------------Projects------------------------

def Projects(request):
    projects = ProjectManagement.objects.all()
    return render(request, "Projects/projects.html", {"projects":projects})

# ------------------------Tools------------------------

def Addtool(request):
    tools = Tools.objects.all()
    if request.method == "POST":
        tool_image = request.FILES.get("tool_image")
        tool_name = request.POST.get("tool_name")
        tool = Tools(tool_image=tool_image, tool_name=tool_name, usr=request.user)
        tool.save()
        return render(request, "Tools/Addtool.html", {"tools":tools})
    return render(request, "Tools/Addtool.html", {"tools":tools})

def Addrawmaterials(request):
    rawmaterial = rawmaterials.objects.all()
    return render(request, "Rawmaterials/Addrawmaterials.html", {"rawmaterial":rawmaterial})