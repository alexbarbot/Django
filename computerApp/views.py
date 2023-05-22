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
	context={'machines': machines}
	return render(request, 'computerApp/machine_list.html', context)

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk)
	context={'machine': machine}
	return render(request , 'computerApp/machine_detail.html',context)

def personnel_list_view(request) :
	personnel = Personnel.objects.all()
	context={'personnels': personnel}
	return render(request,
	'computerApp/personnel_list.html',
	context)

def personnel_detail_view(request, pk):
	personnel = get_object_or_404(Personnel, id=pk)
	context={'personnel': personnel}
	return render(request , 'computerApp/personnel_detail.html',context)

def machine_add_form(request):
	if request.method == 'POST':
		form = AddMachineForm(request.POST or None)
		if form.is_valid():
			nom = form.cleaned_data['nom']
			new_machine = Machine(nom=nom)
			new_machine.save()
			return redirect('machines')
	else:
		form = AddMachineForm()
		context = {'form': form}
		return render(request, 'computerApp/machines_add.html',context)

def personnel_add_form(request):
	if request.method == 'POST':
		form = AddPersonnelForm(request.POST or None)
		if form.is_valid():
			new_personnel = Personnel(nom=form.cleaned_data['nom'])
			new_personnel.save()
			return redirect('personnels')
	else:
		form = AddPersonnelForm()
		context = {'form': form}
		return render(request, 'computerApp/personnel_add.html',context)

def machine_delete_form(request):
    if request.method == 'POST':
        form = DeleteMachineForm(request.POST)
        if form.is_valid():
            machines = form.cleaned_data['machines']
            for machine in machines:
                machine.delete()
            return redirect('machines')
    else:
        form = DeleteMachineForm()
    context = {'form': form}
    return render(request, 'computerApp/machines_delete.html', context)

def personnel_delete_form(request):
    if request.method == 'POST':
        form = DeletePersonnelForm(request.POST)
        if form.is_valid():
            personnels = form.cleaned_data['personnels']
            for personnel in personnels:
                personnel.delete()
            return redirect('personnels')
    else:
        form = DeletePersonnelForm()
    context = {'form': form}
    return render(request, 'computerApp/personnels_delete.html', context)
