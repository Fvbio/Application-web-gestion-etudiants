from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.

#Afficher/Ajouter informations des etudiants 
def show_view(request): 
    if request.method == 'POST':
        fm  = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email = em, password = pw)
            reg.save()
            fm = StudentRegistration()
    else: 
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'etudiant/addAndShow.html' , {'form':fm, 'stu':stud})    


#Supprimer etudiants 
def delete_data(request, id): 
    if request.method == 'POST':
        pk = User.objects.get(pk=id) 
        pk.delete()
        return HttpResponseRedirect('/')

#Modifier informations etudiants
def update_data(request, id):
    if request.method == 'POST':
        pk = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pk)
        if fm.is_valid():
            fm.save()
    else: 
        pk = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pk)
    return render(request, 'etudiant/updateStudent.html', {'form':fm})

