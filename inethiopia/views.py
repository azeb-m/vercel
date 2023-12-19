from django.shortcuts import render
from datetime import datetime
import pytz

# Create your views here.
def show(request):
    #TIME_ZONE = Africa/Addis_Ababa
    ethTz = pytz.timezone('Africa/Addis_Ababa') 
    timeIneth = datetime.now(ethTz)
    currentTimeIneth = timeIneth.strftime("%H:%M:%S")
    context = {'message': currentTimeIneth}
    return render(request, 'showtime.html', context)
    


