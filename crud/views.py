from django.shortcuts import render, get_object_or_404, redirect
from .models import TitanicPassenger
from .forms import TitanicPassengerForm, UploadFileForm
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            
            for _, row in df.iterrows():
                # Check if the passenger already exists
                if not TitanicPassenger.objects.filter(passenger_id=row['PassengerId']).exists():
                    TitanicPassenger.objects.create(
                        passenger_id=row['PassengerId'],
                        survived=row['Survived'],
                        pclass=row['Pclass'],
                        name=row['Name'],
                        sex=row['Sex'],
                        age=row['Age'],
                        sibsp=row['SibSp'],
                        parch=row['Parch'],
                        ticket=row['Ticket'],
                        fare=row['Fare'],
                        cabin=row['Cabin'],
                        embarked=row['Embarked']
                    )
            return redirect('passenger_list')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
def passenger_list(request):
    passengers = TitanicPassenger.objects.all()
    form = TitanicPassengerForm()
    return render(request, 'passenger_list.html', {'passengers': passengers, 'form': form})

# Create or update passenger
def passenger_create_update(request, passenger_id=None):
    if passenger_id:
        passenger = get_object_or_404(TitanicPassenger, pk=passenger_id)
    else:
        passenger = TitanicPassenger()
    
    if request.method == 'POST':
        form = TitanicPassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('passenger_list')
    else:
        form = TitanicPassengerForm(instance=passenger)

    return render(request, 'passenger_form.html', {'form': form})

# Delete passenger
def passenger_delete(request, passenger_id):
    passenger = get_object_or_404(TitanicPassenger, pk=passenger_id)
    passenger.delete()
    return redirect('passenger_list')

def passenger_grid(request):
    passengers = TitanicPassenger.objects.all()
    return render(request, 'passenger_grid.html', {'passengers': passengers})

def delete_all_passengers(request):
    if request.method == 'POST':
        TitanicPassenger.objects.all().delete()
        return redirect('passenger_list')
    return render(request, 'passenger_confirm_delete_all.html')