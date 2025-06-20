from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, NoteForm
from .models import Note, COLOR_CHOICES

@login_required(login_url="/login")
def index(request):
    selected_color = request.GET.get('color')

    if selected_color:
        notes = Note.objects.filter(color=selected_color)
    else:
        notes = Note.objects.all()

    if request.method == "POST":
        note_id = request.POST.get("note-id")

        if note_id:
            note = Note.objects.filter(id=note_id).first()
            if note and (note.author == request.user):
                note.delete()
    context = {"notes":notes,
               "selected_color":selected_color,
               "colors_list":COLOR_CHOICES,
    }

    return render(request, "main/index.html", context)

@login_required(login_url="/login")
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect("/index")
    else:
        form = NoteForm()

    return render(request, "main/create_note.html", {"form":form})

@login_required(login_url="/login")
def update_note(request):
    note_id = request.GET.get("update-id")

    if note_id is None:
        return redirect("/404")

    note = get_object_or_404(Note, id=note_id)
    if note.author == request.user:
        if request.method == "POST":
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                updated_note = form.save(commit=False)
                updated_note.author = request.user
                updated_note.save()
                return redirect("/index")
        else:
            form = NoteForm(instance=note)
    else:
        return redirect("/create_note")

    return render(request, "main/update_note.html", {"form":form})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.POST.get("remember-me"):
                request.session.set_expiry(1209600)
            return redirect("index")
        else:
            messages.info(request, "Username OR password is incorrect")
        
    context = {}
    return render(request, "registration/login_page.html", context)

def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + username)
            return redirect("login")

    return render(request, "registration/sign_up.html", {"form":form})

def logout_user(request):
    logout(request)
    return redirect("login")

# def error_page_404(request, exception):
def error_page_404(request):
    return render(request, "main/404.html", status=404)