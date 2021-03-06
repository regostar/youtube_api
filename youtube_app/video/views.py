from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Video

# class DashboardView(ListView):
    
#     paginate_by = 6
#     model = Video
#     template_name = "index.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)
#         # context['now'] = timezone.now()
#         return context

from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

def dashboard(request):
    # print()
    search = request.GET.get('search', '')
    if search:
        videos_list = Video.objects.filter(Q(title__icontains=search) | Q(description__icontains=search)).order_by('publishing_datetime')
        res = "Search results for "+ search
    else:
        videos_list = Video.objects.all().order_by('publishing_datetime')
        res = ""
    paginator = Paginator(videos_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'index.html', {'page_obj': page_obj, "res": res})