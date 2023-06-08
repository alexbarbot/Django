from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine, Personnel
from .forms import AddMachineForm, AddPersonnelForm, DeleteMachineForm, DeletePersonnelForm
from django.contrib import messages


def index(request):
    personnels = Personnel.objects.all()
    machines = Machine.objects.all()
    # Passer les objets récupérés au template 'index.html'
    context = {
        'personnel': personnels,
        'machines': machines,
    }
    return render(request, 'index.html', context)

def machine_list_view(request):
    machines = Machine.objects.all()
    # Passer les machines récupérées au template 'computerApp/machines_list.html'
    context = {'machines': machines}
    return render(request, 'computerApp/machines_list.html', context)

def machine_detail_view(request, pk):
    # Récupérer la machine correspondante à l'ID fourni (ou retourner une erreur 404 si elle n'existe pas)
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine': machine}
    return render(request, 'computerApp/machines_detail.html', context)

def personnel_list_view(request):
    # Récupérer tous les objets Personnel depuis la base de données
    personnel = Personnel.objects.all()
    context = {'personnels': personnel}
    return render(request, 'computerApp/personnel_list.html', context)

def personnel_detail_view(request, pk):
    # Récupérer la personne correspondante à l'ID fourni (ou retourner une erreur 404 si elle n'existe pas)
    personnel = get_object_or_404(Personnel, id=pk)
    context = {'personnel': personnel}
    return render(request, 'computerApp/personnel_detail.html', context)

def machine_add_view(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST)
        if form.is_valid():
            # Récupérer les données valides du formulaire
            nom = form.cleaned_data['nom']
            mach = form.cleaned_data['mach']
            etat = form.cleaned_data['etat']
            new_machine = Machine(nom=nom, mach=mach, etat=etat)
            new_machine.save()
            messages.success(request, 'La machine a été ajoutée avec succès.')
            return redirect('machines')
    else:
        # Si la requête n'est pas une requête POST, créer un formulaire vide
        form = AddMachineForm()
    
    context = {'form': form}
    return render(request, 'computerApp/machines_list.html', context)

def personnel_add_view(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            new_personnel = Personnel(nom=nom)
            new_personnel.save()
            messages.success(request, 'L\'utilisateur a été ajoutée avec succès.')
            return redirect('personnels')
    else:
        # Si la requête n'est pas une requête POST, créer un formulaire vide
        form = AddPersonnelForm()
    
    context = {'form': form}
    return render(request, 'computerApp/personnel_list.html', context)

def personnel_delete_view(request):
    if request.method == 'POST':
        personnels_ids = request.POST.getlist('personnels')
        # Filtrer les personnes correspondantes dans la base de données et les supprimer
        personnels = Personnel.objects.filter(id__in=personnels_ids)
        personnels.delete()
        messages.success(request, 'L\'utilisateur a suprimée avec succès.')
        return redirect('personnels')

    personnels = Personnel.objects.all()
    context = {'personnels': personnels}
    return render(request, 'computerApp/personnel_list.html', context)

def machine_delete_view(request):
    if request.method == 'POST':
        machines_ids = request.POST.getlist('machines')
        machines = Machine.objects.filter(id__in=machines_ids)
        machines.delete()
        messages.success(request, 'La machine a été suprimée avec succès.')
        return redirect('machines')


    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'computerApp/machines_list.html', context)

def gestion_view(request):
    context = {}
    return render(request, 'computerApp/gestion.html', context)
