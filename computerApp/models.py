from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine, Personnel
from .forms import AddMachineForm, AddPersonnelForm, DeleteMachineForm, DeletePersonnelForm


# Fonction de vue pour afficher la page d'accueil
def index(request):
    # Récupérer tous les objets du modèle Personnel
    personnels = Personnel.objects.all()
    # Récupérer tous les objets du modèle Machine
    machines = Machine.objects.all()
    context = {
        'personnel': personnels,
        'machines': machines,
    }
    return render(request, 'index.html', context)


# Fonction de vue pour afficher la liste des machines
def machine_list_view(request):
    # Récupérer tous les objets du modèle Machine
    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'computerApp/machines_list.html', context)


# Fonction de vue pour afficher les détails d'une machine
def machine_detail_view(request, pk):
    # Récupérer l'objet Machine correspondant à l'ID donné
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine': machine}
    return render(request, 'computerApp/machines_detail.html', context)


# Fonction de vue pour afficher la liste du personnel
def personnel_list_view(request):
    # Récupérer tous les objets du modèle Personnel
    personnel = Personnel.objects.all()
    context = {'personnels': personnel}
    return render(request, 'computerApp/personnel_list.html', context)


# Fonction de vue pour afficher les détails d'un membre du personnel
def personnel_detail_view(request, pk):
    # Récupérer l'objet Personnel correspondant à l'ID donné
    personnel = get_object_or_404(Personnel, id=pk)
    context = {'personnel': personnel}
    return render(request, 'computerApp/personnel_detail.html', context)


# Fonction de vue pour ajouter une machine
def machine_add_view(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            nom = form.cleaned_data['nom']
            mach = form.cleaned_data['mach']
            etat = form.cleaned_data['etat']
            # Créer une nouvelle instance de Machine avec les données
            new_machine = Machine(nom=nom, mach=mach, etat=etat)
            new_machine.save()
            return redirect('machines')
    else:
        form = AddMachineForm()
    
    context = {'form': form}
    return render(request, 'computerApp/machines_list.html', context)


# Fonction de vue pour ajouter un membre du personnel
def personnel_add_view(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            nom = form.cleaned_data['nom']
            # Créer une nouvelle instance de Personnel avec les données
            new_personnel = Personnel(nom=nom)
            new_personnel.save()
            return redirect('personnels')
    else:
        form = AddPersonnelForm()
    
    context = {'form': form}
    return render(request, 'computerApp/personnel_list.html', context)


# Fonction de vue pour supprimer des membres du personnel
def personnel_delete_view(request):
    if request.method == 'POST':
        # Récupérer les IDs des membres du personnel à supprimer
        personnels_ids = request.POST.getlist('personnels')
        # Filtrer les objets Personnel correspondants aux IDs donnés
        personnels = Personnel.objects.filter(id__in=personnels_ids)
        # Supprimer les objets Personnel
        personnels.delete()
        return redirect('personnels')

    personnels = Personnel.objects.all()
    context = {'personnels': personnels}
    return render(request, 'computerApp/personnel_list.html', context)


# Fonction de vue pour supprimer des machines
def machine_delete_view(request):
    if request.method == 'POST':
        # Récupérer les IDs des machines à supprimer
        machines_ids = request.POST.getlist('machines')
        # Filtrer les objets Machine correspondants aux IDs donnés
        machines = Machine.objects.filter(id__in=machines_ids)
        # Supprimer les objets Machine
        machines.delete()
        return redirect('machines')

    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'computerApp/machines_list.html', context)


# Fonction de vue pour afficher la page de gestion
def gestion_view(request):
    context = {}
    return render(request, 'computerApp/gestion.html', context)
