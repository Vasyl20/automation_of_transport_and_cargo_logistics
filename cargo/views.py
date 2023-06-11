

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Cargo, Car, Fuel
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
class CargoListView(ListView):
    model = Cargo
    template_name = 'cargo_list.html'
    context_object_name = 'cargos'


class CargoCreateView(CreateView):
    model = Cargo
    template_name = 'cargo/cargo_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cargo-list')


# class CargoDetailView(DetailView):
#     model = Cargo
#     template_name = 'cargo_detail.html'
#     context_object_name = 'cargo'
#
#
# class CargoUpdateView(UpdateView):
#     model = Cargo
#     template_name = 'cargo_form.html'
#     fields = '__all__'
#     context_object_name = 'cargo'
#     success_url = reverse_lazy('cargo-list')
#
#
# class CargoDeleteView(DeleteView):
#     model = Cargo
#     template_name = 'cargo_confirm_delete.html'
#     context_object_name = 'cargo'
#     success_url = reverse_lazy('cargo-list')



class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'cars'

def create_car(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        special_code = data.get('special_code')
        registration_number = data.get('registration_number')
        year = data.get('year')
        brand = data.get('brand')
        model = data.get('model')
        commercial_description = data.get('commercial_description')
        vehicle_identification_number = data.get('vehicle_identification_number')
        total_weight = data.get('total_weight')
        unloaded_weight = data.get('unloaded_weight')
        engine_volume = data.get('engine_volume')
        fuel_type_id = data.get('fuel_type_id')
        color = data.get('color')

        if (
            special_code and registration_number and year and brand and model and
            commercial_description and vehicle_identification_number and total_weight and
            unloaded_weight and engine_volume and fuel_type_id and color
        ):
            try:
                fuel_type = Fuel.objects.get(id=fuel_type_id)
                car = Car.objects.create(
                    special_code=special_code,
                    registration_number=registration_number,
                    year=year,
                    brand=brand,
                    model=model,
                    commercial_description=commercial_description,
                    vehicle_identification_number=vehicle_identification_number,
                    total_weight=total_weight,
                    unloaded_weight=unloaded_weight,
                    engine_volume=engine_volume,
                    fuel_type=fuel_type,
                    color=color
                )
                return JsonResponse({'message': 'Car created successfully'})
            except Fuel.DoesNotExist:
                return JsonResponse({'error': 'Fuel type not found'}, status=404)
        else:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




class FuelListView(ListView):
    model = Fuel
    template_name = 'fuel/fuel_list.html'
    context_object_name = 'fuel_list'

class FuelCreateView(CreateView):
    model = Fuel
    template_name = 'fuel/fuel_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cargo:fuel-list')




