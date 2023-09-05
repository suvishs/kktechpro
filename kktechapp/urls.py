from django.urls import path
from kktechapp import views

urlpatterns = [
    # ------------------------General------------------------
    path('', views.Usrlogin, name="Usrlogin"),path('Register', views.Register, name="Register"),
    path('logout', views.logout, name="logout"),
    path('index', views.index, name="index"),
    
    # ------------------------Attendance------------------------
    path('mark_attendance', views.mark_attendance, name="mark_attendance"),
    path('viewallatendancereport', views.viewallatendancereport, name="viewallatendancereport"),
    path('Applicationforleave', views.Applicationforleave, name="Applicationforleave"),
    path('Viewleaveaplications', views.Viewleaveaplications, name="Viewleaveaplications"),
    path('ApproveViewleaveaplications', views.ApproveViewleaveaplications, name="ApproveViewleaveaplications"),
    path('ApproveViewleaveaplication/<int:id>', views.ApproveViewleaveaplication, name="ApproveViewleaveaplication"),
    path('sortattandance', views.sortattandance, name="sortattandance"),
    path('overtime', views.overtime, name="overtime"),
    
    # ------------------------Projects------------------------
    path('Projects', views.Projects, name="Projects"),
    
    # ------------------------Tools------------------------
    path('Addtool', views.Addtool, name="Addtool"),
    
    # ------------------------Rawmatirials------------------------
    path('Addrawmaterials', views.Addrawmaterials, name="Addrawmaterials"),
]