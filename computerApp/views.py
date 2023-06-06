from django.shortcuts import render, get_object_or_404, redirect
from computerApp.models import Machine, Personnel
from .forms import AddMachineForm, AddPersonnelForm, DeleteMachineForm, DeletePersonnelForm


# Create your views here.

def index(request) :
	personnels = Personnel.objects.all()
	machines = Machine.objects.all()
	context = {
		'personnel' : personnels,
		'machines' : machines, 
	}
	return render(request, 'index.html', context)

def machine_list_view(request) :
	machines = Machine.objects.all()
	context = {'machines': machines}
	return render(request, 'computerApp/machines_list.html', context)

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk)
	context={'machine': machine}
	return render(request , 'computerApp/machines_detail.html',context)

def personnel_list_view(request) :
	personnel = Personnel.objects.all()
	context={'personnels': personnel}
	return render(request, 'computerApp/personnel_list.html',context)

def personnel_detail_view(request, pk):
	personnel = get_object_or_404(Personnel, id=pk)
	context={'personnel': personnel}
	return render(request, 'computerApp/personnel_detail.html', context)

def machine_add_view(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            mach = form.cleaned_data['mach']
            etat = form.cleaned_data['etat']
            new_machine = Machine(nom=nom,mach=mach,etat=etat)
            new_machine.save()
            return redirect('machines')
    else:
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
            return redirect('personnels')
    else:
        form = AddPersonnelForm()
    
    context = {'form': form}
    return render(request, 'computerApp/personnel_list.html', context)

def personnel_delete_view(request):
    if request.method == 'POST':
        personnels_ids = request.POST.getlist('personnels')
        personnels = Personnel.objects.filter(id__in=personnels_ids)
        personnels.delete()
        return redirect('personnels')

    personnels = Personnel.objects.all()
    context = {'personnels': personnels}
    return render(request, 'computerApp/personnel_list.html', context)

def machine_delete_view(request):
    if request.method == 'POST':
        machines_ids = request.POST.getlist('machines')
        machines = Machine.objects.filter(id__in=machines_ids)
        machines.delete()
        return redirect('machines')

    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'computerApp/machines_list.html', context)

def gestion_view(request):
    context = {}
    return render(request, 'computerApp/gestion.html', context)