from django.shortcuts import render, redirect
from Newapp.forms import ResumeForm
from Newapp.models import Resume,contactmedb
from django.http import FileResponse,HttpResponse
# Create your views here.
def home_page(request):
    return render(request, "Home.html")

def download(request):
    resume = Resume.objects.first()
    if resume is not None:
        response = FileResponse(resume.file)
        return response
    else:
        return HttpResponse("NO FILE IS FOUND")
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Resume uploaded successfully!')
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})
def view_resumes(request):
    resumes = Resume.objects.all()
    return render(request, 'view_resumes.html', {'resumes': resumes})
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        ema = request.POST.get('email')
        msg = request.POST.get('message')
        obj = contactmedb(name=name, email=ema, message=msg)
        obj.save()
        return redirect(home_page)