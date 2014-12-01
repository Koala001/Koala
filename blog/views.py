from django.shortcuts import render_to_response
from blog.models import User, Blog, Comment
from django import forms
from django.http import HttpResponse, HttpResponseRedirect

class UserForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class BlogForm(forms.Form):
	name = forms.CharField()
	summary = forms.CharField()
	content = forms.CharField()

def blog(req):
	if req.method == 'POST':
		blogform = BlogForm(req.POST)
		if blogform.is_valid():
			name = blogform.cleaned_data['name']
			summary = blogform.cleaned_data['summary']
			content = blogform.cleaned_data['content']
			email = req.session.get('email', '')
			users = User.objects.filter(email__exact=email)
			Blog.objects.create(user_id=users[0].id, user_name=users[0].name, user_image=users[0].image, 
				name=name, summary=summary, content=content)
			return HttpResponseRedirect('/index')
	else:
		blogform = BlogForm()
	return render_to_response('blog.html',{'blogform':blogform})

def regist(req):
	if req.method == 'POST':
		uf = UserForm(req.POST)
		if uf.is_valid():
			email = uf.cleaned_data['email']
			password = uf.cleaned_data['password']
			User.objects.create(email=email, password= password)
			return HttpResponseRedirect('/login')
	else:
		uf = UserForm()
	return render_to_response('regist.html', {'uf':uf})

'''
def login(req):
	if req.method == 'POST':
		uf = UserFormsTest(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			users = UserTest.objects.filter(username__exact=username, password__exact= password)
			if users:
				response = HttpResponseRedirect('/blog/index_test')
				response.set_cookie('username',username, 3600)
				return response
			else:
				return HttpResponseRedirect('/blog/login')
	else:
		uf = UserFormsTest()
	return render_to_response('login.html', {'uf':uf})
'''

def login(req):
	if req.method == 'POST':
		uf = UserForm(req.POST)
		if uf.is_valid():
			email = uf.cleaned_data['email']
			password = uf.cleaned_data['password']
			users = User.objects.filter(email__exact=email, password__exact= password)
			if users:
				req.session['email'] = email
				return HttpResponseRedirect('/index')
			else:
				return HttpResponseRedirect('/login')
	else:
		uf = UserForm()
	return render_to_response('login.html', {'uf':uf})

'''
def logout(req):
	response = HttpResponse('logout')
	response.delete_cookie('username')
	return response
'''
def logout(req):
	del req.session['email']
	return HttpResponseRedirect('/index')


def index(req):
	email = req.session.get('email', '')
	blogs = Blog.objects.all()
	return render_to_response('index.html', {'email':email,'blogs':blogs})


'''
def index(req):
	username = req.session.get('username', 'anybody')
	blogs = Blog.objects.all()
	return render_to_response('index_test.html', {'username':username,'blogs':blogs})
'''

'''
class UserForm(forms.Form):
	username = forms.CharField()
	#headImg = forms.FileField()
'''

def register(req):
	if req.method == 'POST':
		uf = UserForm(req.POST, req.FILES)
		if uf.is_valid():
			print uf.cleaned_data['username']    # hou tai chu li
			#print req.FILES
			return HttpResponse('ok')
		else:
			print 'bind is not valid'
	else:
		uf = UserForm()
	return render_to_response('register.html',{'uf':uf})

'''
def register(req):
	if req.method == 'POST':
		form = UserForm(req.POST)  #bind to form
		if form.is_valid():
			print form.cleaned_data
			return HttpResponse('ok')
	else:                                 #get
		form = UserForm()
	return render_to_response('register.html',{'form':form})
'''

'''
def index(req):
	emps = Employee.objects.all()
	return render_to_response('index.html',{'emps':emps})
'''


'''class Person(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def say(self):
		return 'I am' + self.name


def index(req, id):
	user = {'name':'koala', 'age':1, 'sex':'male'}
	book_list = ['python', 'c++', 'django']
	return render_to_response('index.html', {'title':'koala', 'user':user, 'book':book_list, 'id':id})
	'''