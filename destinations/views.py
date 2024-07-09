from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import DestinationForm

def destination_list(request):
    destinations = Destination.objects.all()
    print(f"Number of destinations: {destinations.count()}")
    return render(request, 'destination_list.html', {'destinations': destinations})


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'destination_detail.html', {'destination': destination})

def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save()
            print(f"Saved destination: {destination.place_name}")
            return redirect('destination_list')
        else:
            print("Form is not valid")
    else:
        form = DestinationForm()
    return render(request, 'destination_form.html', {'form': form})


def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'destination_form.html', {'form': form})


def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == "POST":
        destination.delete()
        return redirect('destination_list')
    return render(request, 'destination_confirm_delete.html', {'destination': destination})