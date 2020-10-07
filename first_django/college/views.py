from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from college.models import Education

# Create your views here.
def index(request):
    return render(request,'index.html')
def reg_details(request):
    if request.session._session:
        data=User.objects.all()
        return render(request,'reg_details.html',{'user_data':data})
    else:
        return redirect(request,'login.html')
        
def login(request):  
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Login Details')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
        if request.method == 'POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            password1=request.POST['password1']
            password2=request.POST['password2']
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request,'Username Taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.error(request,"Email Already Exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save();
                    messages.success(request,'Account Created Successfully')
                    return redirect('login')
            else:
                messages.error(request,'Password And Confirm-Password did not match ')
                return redirect('register')
        else:
            return render(request,'register.html')
    

def contact(request):
    return render(request,'contact.html')
    
def about(request):
    return render(request,'about.html')
    
def dashboard(request):
    if request.session._session:
        return render(request,'dashboard.html')
    else:
        return render(request,'login.html')
def delete_user(request,pk):
    if request.session._session:
        User.objects.filter(id=pk).delete()
        messages.success(request,"User Deleted Successfully")
        return redirect('reg_details')
    else:
        return render(request,'login.html')
def edit_user(request,pk):
    if request.session._session:
        data=User.objects.filter(id=pk).values()
        return render(request,'user_record.html',{'reg_details':data})    
    else:
        return render(request,'login.html')
def update_user(request):
    if request.session._session:
        if request.method=="POST":
            user_id=request.POST['user_id']
            user_data=User.objects.get(id=user_id)
            user_data.first_name=request.POST['first_name']
            user_data.last_name=request.POST['last_name']
            user_data.email=request.POST['email']
            user_data.save();
            messages.success(request,"User Record Updated Successfully")
            return redirect('reg_details')
        else:
            return redirect('reg_details')
    else:
        return render(request,'login.html')
def change_password(request):
    if request.session._session:
        if request.method=='POST':
            form=PasswordChangeForm(request.user,request.POST)
            if form.is_valid():
                user=form.save()
                update_session_auth_hash(request,user)  #important
                messages.success(request,'Your password was succssfully updated')
                return redirect('change_password')
            else:
                messages.error(request,'Please correct the error')
        else:
            form=PasswordChangeForm(request.user)
        return render(request,'change_password.html',{'form':form})
    else:
        return render(request,'login.html')
def user_profile(request):
    if request.session._session:
        return render(request,'user_profile.html')
    else:
        return render(request,'login.html')
def update_user_profile(request):
    if request.session._session:
        if request.method=="POST":
            user_id=request.POST['user_id']
            user_data=User.objects.get(id=user_id)
            user_data.first_name=request.POST['first_name']
            user_data.last_name=request.POST['last_name']
            user_data.email=request.POST['email']
            user_data.save();
            messages.success(request,"User Record Updated Successfully")
            return redirect('user_profile')
        else:
            return redirect('user_profile')
    else:
        return render(request,'login.html')
def logout(request):
    if request.session._session:
        auth.logout(request)
        return redirect('login')
    else:
        return render(request,'login.html')
def education_details(request):
    if request.session._session:
        return render(request,'education_details.html')
    else:
        return render(request,'login.html')
def education(request):
    if request.session._session:
        return render(request,'education.html')
    else:
        return render(request,'login.html')
def insert_edu_details(request):
    if request.session._session:
        if request.method=="POST":
            use_id=request.POST['user_id']
            edu_name=request.POST['education_name']
            edu_univ=request.POST['education_university']
            pass_year=request.POST['passing_year']
            obt_marks=request.POST['obtained_marks']
            maxim_marks=request.POST['max_marks']
            per=request.POST['percentage']
            edu_remark=request.POST['remark']
            user_data=Education(Education_name=edu_name,Education_university=edu_univ,
            Education_year=pass_year,Education_obtainedmarks=obt_marks,
            Educationmaxmarks=maxim_marks,Education_per=per,Education_remarks=edu_remark,Education_user_id=use_id)
            user_data.save();
            messages.success(request,"User Record Updated Successfully")
            return redirect('user_profile')
        else:
            return redirect('user_profile')
    else:
        return render(request,'login.html')
