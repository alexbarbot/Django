from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine, Personnel
from .forms import AddMachineForm, AddPersonnelForm, DeleteMachineForm, DeletePersonnelForm

# Vue pour la page d'accueil
def index(request):
    # Récupérer tous les objets Personnel et Machine depuis la base de données
    personnels = Personnel.objects.all()
    machines = Machine.objects.all()
    # Passer les objets récupérés au template 'index.html'
    context = {
        'personnel': personnels,
        'machines': machines,
    }
    return render(request, 'index.html', context)

# Vue pour afficher la liste des machines
def machine_list_view(request):
    # Récupérer tous les objets Machine depuis la base de données
    machines = Machine.objects.all()
    # Passer les machines récupérées au template 'computerApp/machines_list.html'
    context = {'machines': machines}
    return render(request, 'computerApp/machines_list.html', context)

# Vue pour afficher les détails d'une machine spécifique
def machine_detail_view(request, pk):
    # Récupérer la machine correspondante à l'ID fourni (ou retourner une erreur 404 si elle n'existe pas)
    machine = get_object_or_404(Machine, id=pk)
    # Passer la machine récupérée au template 'computerApp/machines_detail.html'
    context = {'machine': machine}
    return render(request, 'computerApp/machines_detail.html', context)

# Vue pour afficher la liste du personnel
def personnel_list_view(request):
    # Récupérer tous les objets Personnel depuis la base de données
    personnel = Personnel.objects.all()
    # Passer le personnel récupéré au template 'computerApp/personnel_list.html'
    context = {'personnels': personnel}
    return render(request, 'computerApp/personnel_list.html', context)

# Vue pour afficher les détails d'une personne spécifique
def personnel_detail_view(request, pk):
    # Récupérer la personne correspondante à l'ID fourni (ou retourner une erreur 404 si elle n'existe pas)
    personnel = get_object_or_404(Personnel, id=pk)
    # Passer la personne récupérée au template 'computerApp/personnel_detail.html'
    context = {'personnel': personnel}
    return render(request, 'computerApp/personnel_detail.html', context)

# Vue pour ajouter une nouvelle machine
def machine_add_view(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST)
        if form.is_valid():
            # Récupérer les données valides du formulaire
            nom = form.cleaned_data['nom']
            mach = form.cleaned_data['mach']
            etat = form.cleaned_data['etat']
            # Créer une nouvelle instance de Machine avec les données récupérées
            new_machine = Machine(nom=nom, mach=mach, etat=etat)
            new_machine.save()
            # Rediriger vers la page affichant la liste des machines
            return redirect('machines')
    else:
        # Si la requête n'est pas une requête POST, créer un formulaire vide
        form = AddMachineForm()
    
    # Passer le formulaire au template 'computerApp/machines_list.html'
    context = {'form': form}
    return render(request, 'computerApp/machines_list.html', context)

# Vue pour ajouter une nouvelle personne
def personnel_add_view(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST)
        if form.is_valid():
            # Récupérer les données valides du formulaire
            nom = form.cleaned_data['nom']
            # Créer une nouvelle instance de Personnel avec les données récupérées
            new_personnel = Personnel(nom=nom)
            new_personnel.save()
            # Rediriger vers la page affichant la liste du personnel
            return redirect('personnels')
    else:
        # Si la requête n'est pas une requête POST, créer un formulaire vide
        form = AddPersonnelForm()
    
    # Passer le formulaire au template 'computerApp/personnel_list.html'
    context = {'form': form}
    return render(request, 'computerApp/personnel_list.html', context)

# Vue pour supprimer des personnes
def personnel_delete_view(request):
    if request.method == 'POST':
        # Récupérer les identifiants des personnes sélectionnées dans le formulaire
        personnels_ids = request.POST.getlist('personnels')
        # Filtrer les personnes correspondantes dans la base de données et les supprimer
        personnels = Personnel.objects.filter(id__in=personnels_ids)
        personnels.delete()
        # Rediriger vers la page affichant la liste du personnel
        return redirect('personnels')

    # Récupérer tous les objets Personnel depuis la base de données
    personnels = Personnel.objects.all()
    # Passer le personnel récupéré au template 'computerApp/personnel_list.html'
    context = {'personnels': personnels}
    return render(request, 'computerApp/personnel_list.html', context)

# Vue pour supprimer des machines
def machine_delete_view(request):
    if request.method == 'POST':
        # Récupérer les identifiants des machines sélectionnées dans le formulaire
        machines_ids = request.POST.getlist('machines')
        # Filtrer les machines correspondantes dans la base de données et les supprimer
        machines = Machine.objects.filter(id__in=machines_ids)
        machines.delete()
        # Rediriger vers la page affichant la liste des machines
        return redirect('machines')

    # Récupérer tous les objets Machine depuis la base de données
    machines = Machine.objects.all()
    # Passer les machines récupérées au template 'computerApp/machines_list.html'
    context = {'machines': machines}
    return render(request, 'computerApp/machines_list.html', context)

# Vue pour la gestion
def gestion_view(request):
    context = {}
    return render(request, 'computerApp/gestion.html', context)
