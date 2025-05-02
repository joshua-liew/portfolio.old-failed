from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .models import ENProject
from .forms import ContactForm

# Create your views here.
def home(request):
    template = "en/home.html"
    context = {'current_page': 'home'}
    return render(request, template, context)


def about(request):
    template = "en/about.html"
    context = {'current_page': 'about'}
    return render(request, template, context)


def work(request):
    try:
        featured = ENProject.objects.filter(featured=True).order_by('-date')[:5]
    except:
        featured = None
    
    template = "en/work.html"
    context = {'current_page': 'work', 'projects': featured}
    return render(request, template, context)


def work_all(request):
    all_realworld_count = ENProject.objects.filter(category='RW').count()
    all_personal_count = ENProject.objects.filter(category='PS').count()
    all_challenge_count = ENProject.objects.filter(category='CH').count()
    realworld = get_projects('RW')
    personal = get_projects('PS')
    challenge = get_projects('CH')

    template = "en/work_all.html"
    context = {
        'current_page': 'work_all', 
        'realworld_projects': realworld,
        'personal_projects': personal,
        'challenge_projects': challenge,
        'current_RW_count': realworld.count(),
        'current_PS_count': personal.count(),
        'current_CH_count': challenge.count(),
        'all_RW_count': all_realworld_count,
        'all_PS_count': all_personal_count,
        'all_CH_count': all_challenge_count,
        }
    return render(request, template, context)

def get_realworld(request):
    if request.method == "POST":
        try:
            count = int(request.POST.get('count'))
        except:
            raise TypeError("Bad data - 'count' must be int")
        RW_projects = get_projects('RW', count, count + 5)
        all_realworld_count = ENProject.objects.filter(category='RW').count()

        template = "partials/load_projects.html"
        context = {
            'projects': RW_projects, 
            'all_count': all_realworld_count,
            'current_count': count + RW_projects.count(),
            'section': 'RW',
            'id': 'realworld',
            }
        return render(request, template, context)
    
def get_personal(request):
    if request.method == "POST":
        try:
            count = int(request.POST.get('count'))
        except:
            raise TypeError("Bad data - 'count' must be int")
        PS_projects = get_projects('PS', count, count + 5)
        all_personal_count = ENProject.objects.filter(category='PS').count()

        template = "partials/load_projects.html"
        context = {
            'projects': PS_projects, 
            'all_count': all_personal_count,
            'current_count': count + PS_projects.count(),
            'section': 'PS',
            'id': 'personal',
            }
        return render(request, template, context)

def get_challenge(request):
    if request.method == "POST":
        try:
            count = int(request.POST.get('count'))
        except:
            raise TypeError("Bad data - 'count' must be int")
        CH_projects = get_projects('CH', count, count + 5)
        all_challenge_count = ENProject.objects.filter(category='CH').count()

        template = "partials/load_projects.html"
        context = {
            'projects': CH_projects, 
            'all_count': all_challenge_count,
            'current_count': count + CH_projects.count(),
            'section': 'CH',
            'id': 'challenge',
            }
        return render(request, template, context)

def get_projects(project_category: str, slice_start: int = 0, slice_end: int = 3) -> object:
    try:
        objects = ENProject.objects.filter(category=project_category).order_by('-date')[slice_start:slice_end]
    except:
        objects = None
    return objects


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        template = "partials/_contact.html"

        if not form.is_valid():
            return render(request, template, {'status': 'invalid_field'})

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['text']
        try:
            send_mail(
                "Mail from your portfolio website!", 
                f"[{subject}]\n\n{text}", 
                f"{name} | {email}", 
                ["liqshann@gmail.com"])
        except BadHeaderError:
            return render(request, template, {'status': 'invalid_header'})
        
        return render(request, template, {'status': 'success'})

    template = "en/contact.html"
    form = ContactForm()
    context = {'current_page': 'contact', 'form': form}
    return render(request, template, context)