from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddressForm, PenggunaForm, ContentForm, SearchPengguna
from .models import Pengguna, Content
from django.http import JsonResponse

def set_data_entry(request):
    form = AddressForm()
    context ={
        'form':form,
    }
    return render(request, 'data_entry/input_data_1.html', context)

# Create your views here.

def search_pengguna_by_state(request):
    pesan = None
    tampil = None
    form = None
    listpengguna = None
    status = None
    if request.method == 'POST':
        form = SearchPengguna(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            listpengguna = Pengguna.objects.filter(state=state)

            if listpengguna is None:
                pesan = "Data Pengguna tidak ditemukan"
                status = True
            else:
                tampil = True
    else:
        form = SearchPengguna()
        
    context = {
        'form': form,
        'tampil': tampil,
        'pesan': pesan,
        'listpengguna': listpengguna,
        
    }
    return render(request, 'data_entry/list_pengguna.html', context=context)

def set_pengguna(request):
    list_pengguna = Pengguna.objects.all().order_by('-id')
    print(list_pengguna)
    print('ini jalan')
    context = None
    form = PenggunaForm(None)
    if request.method == "POST":
        form = PenggunaForm(request.POST)
        if form.is_valid():
            form.save()
            list_pengguna = Pengguna.objects.all().order_by('-id')
            context = {
                'form' : form,
                'list_pengguna' : list_pengguna,
            }
            return render(request, 'data_entry/input_data_1.html', context)
    
    else:
        context = {
            'form' : form,
            'list_pengguna' : list_pengguna,
        }
        return render(request, 'data_entry/input_data_1.html', context)
    
def view_pengguna(request, id):
    try:
        pengguna = Pengguna.objects.get(pk=id)
        return render(request, 'data_entry/pengguna_detail.html', {'user_id': pengguna.id})
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'User Not Found'}, status=404)
    
def get_pengguna_detail_api(request, user_id):
    try:
        pengguna = Pengguna.objects.get(pk=user_id)
        data = {
            'email' : pengguna.email,
            'address_1' : pengguna.address_1,
            'address_2' : pengguna.address_2,
            'city' : pengguna.city,
            'state' : pengguna.state,
            'zip_code' : pengguna.zip_code,
            'tanggal_join' : pengguna.tanggal_join.strftime('%Y- %m-%d')
        }
        return JsonResponse(data)
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
def set_content(request):
    form = ContentForm(None)
    if request.method =='POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            context ={
                'form' : form,
            }
            return render(request, 'data_entry/content.html', context)
    else:
        context ={
            'form' : form,
        }
        return render(request, 'data_entry/content.html', context)
    
def edit_pengguna(request, id):
    pengguna = get_object_or_404(Pengguna, pk=id)
    form = PenggunaForm(request.POST or None, instance=pengguna)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('data_entry:view_pengguna', id=pengguna.id)
    return render(request, 'data_entry/edit_pengguna.html', {'form': form})

def main_view(request):
    if request.method == "POST":
        search_query = request.POST.get('search')
        pengguna_list = Pengguna.objects.filter(email__icontains=search_query)
    else:
        pengguna_list = Pengguna.objects.all()

    return render(request, 'main.html', {'pengguna_list': pengguna_list})