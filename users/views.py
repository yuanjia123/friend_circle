from django.shortcuts import render,redirect
from users.forms import LoginForm,RegisterForm
from users.models import UserProfile
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.views.generic.base import View
from users.forms import Userdetail

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        msg = "已经完成数据提交"
        if form.is_valid():

            name = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            print("name:   ",name)
            print("age:   ",email)
            print("password:   ",password)

            g1 = UserProfile.objects.filter(username=name).first()
            if g1:
                msg = "您所输入姓名:{} 已经存在".format(name)
                return render(request, 'register.html', {'form': form, 'msg':msg})
            else:
                msg = "注册成功"
                # 手机号是用户名
                user = UserProfile(username=name)

                # 设置密码  加密的形式
                user.set_password(password)
                # 手机号是手机号
                user.email = email
                # 保存
                user.save()
                # 记录登录
                login(request, user)
                # return render(request, 'register.html', {'form': form, 'msg': msg})
                return redirect("main")
                # return HttpResponse("注册成功")

    else:
        form = RegisterForm()
        # msg = "初始化表单"

    return render(request, 'register.html', {'form':form})


def Login_View(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print("*************",name,password)
            user = authenticate(username=name,password=password)
            if user is not None and user.is_active:
                print("登录成功",type(user))
                login(request, user)
                msg = "登录成功"

                #如果登陆成功、跳到答题页面
                #return redirect("question",name)

                return redirect("main")
                # return HttpResponse("登录成功")
            else:
                return HttpResponse("登录失败")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#编写退出接口
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        #退出登录、清空cook
        logout(request)
        #跳转到主页
        return redirect("main")
        # return HttpResponse("退出登录")

def Main_View(request):

    return render(request,'main.html')


def Personal_center(request):

    if request.method == "POST":
        print("来了没222")
        form = Userdetail(request.POST)
        if form.is_valid():
            print("来了没")
            one = UserProfile.objects.filter(username=request.user.username).first()
            sex = form.cleaned_data["sex"]
            phone = form.cleaned_data["phone"]
            address = form.cleaned_data["address"]
            age = form.cleaned_data["age"]
            img_url = request.FILES.get('img_url')
            one.sex = sex
            one.phone = phone
            one.address = address
            one.age = age
            one.img_url = img_url
            one.save()
            return HttpResponse("提交成功")
            # return redirect("main")
        else:
            print("验证没有通过")

    else:
        print("来了没111")
        one = UserProfile.objects.filter(username=request.user.username).first()
        form = Userdetail()
        return render(request, 'personal_center.html', {'form': form, "one": one})

    # one = Friend_Message.objects.filter(username=request.user.username).first()
    # if request.method == "POST":
    #     form = File_Form(request.POST)
    #     if form.is_valid():
    #         content = form.cleaned_data["content"]
    #         img = request.FILES.get('img')
    #         who = request.user.username
    #         Friend_Message.objects.create(content=content,photo=img,who=who)
    #         msg = "上传成功"
    #     return render(request, 'personal_center.html', {'form':form,'msg':msg,"one":one })
    # else:
    #     form = File_Form()
    #
    # return render(request,'personal_center.html',{'form': form,"one":one})