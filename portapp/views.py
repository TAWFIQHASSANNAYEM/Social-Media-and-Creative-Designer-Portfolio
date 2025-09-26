from django.shortcuts import render
from hitcount.views import HitCountMixin
from hitcount.models import HitCount

def home(request):

    hit_count = HitCount.objects.get_for_object(HitCount.objects.get_or_create(pk=1)) 
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    
    # You can now access hit_count_response.hit_counted to see if the count was successful
    # and hit_count_response.hit_count.hits to get the total number of hits.

    return render(request, 'portapp/home.html') 