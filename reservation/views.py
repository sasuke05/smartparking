from django.shortcuts import render,redirect
from .forms import PostForm
from Adafruit_IO import Client,Data
from time import strftime
from django.http import HttpResponse
# Create your views here.
def home(request):
    aio = Client('sem6', 'aio_tkWz44qALyafHtu6EWTLfQNgSf0y')
    slot1_available = strftime(aio.receive('entryslot1').created_at) < strftime(aio.receive('exitslot1').created_at)
    slot2_available = strftime(aio.receive('entryslot2').created_at) < strftime(aio.receive('exitslot2').created_at)
    slot3_available = strftime(aio.receive('entryslot3').created_at) < strftime(aio.receive('exitslot3').created_at)
    arr=[slot1_available, slot2_available, slot3_available]
    available_spaces = arr.count(True)

    if request.method == 'POST':
        form =PostForm(request.POST)
        if form.is_valid():
            d=request.POST.copy()
            d1=[d.get('hour'),d.get('minutes'),d.get('slot')]
            if arr[int(d.get('slot'))-1]:
                s=str(d.get('slot'))+ ',' +str(d.get('hour')) + ':' +str(d.get('minutes'))
                data = Data(value=s)
                aio.create_data('reservation',data)
                s1="successful"
                form.save(commit=True)  #
            else:
                s1="unsuccessful"
        else:
            s1="unsuccessful"  # return redirect('home')
        return HttpResponse(render(request, 'reservation/home.html', {'form':form, 's1': slot1_available,'s2':slot2_available,'s3':slot3_available,'available':available_spaces,'s': s1}))
        # return redirect('home',{})
    else:
        form= PostForm()
        return render(request, 'reservation/home.html', {'form':form, 's1': slot1_available,'s2':slot2_available,'s3':slot3_available,'available':available_spaces})

