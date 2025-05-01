from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WorldCup
from .forms import WorldCupForm, SearchForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class WorldCupListView(ListView):
    model = WorldCup
    template_name = 'blog_list.html'
    context_object_name = 'worldcups'

    def get_queryset(self):
        return WorldCup.objects.all()

class WorldCupDetailView(DetailView):
    model = WorldCup
    template_name = 'blog_detail.html'
    context_object_name = 'worldcup'

class WorldCupCreateView(LoginRequiredMixin, CreateView):
    model = WorldCup
    form_class = WorldCupForm
    template_name = 'blog_form.html'
    success_url = reverse_lazy('worldcup_list')

class WorldCupUpdateView(LoginRequiredMixin, UpdateView):
    model = WorldCup
    form_class = WorldCupForm
    template_name = 'blog_form.html'
    success_url = reverse_lazy('worldcup_list')

class WorldCupDeleteView(LoginRequiredMixin, DeleteView):
    model = WorldCup
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('worldcup_list')

@login_required
def search_worldcup(request):
    form = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        q = form.cleaned_data['query']
        results = WorldCup.objects.filter(year__icontains=q) | WorldCup.objects.filter(host__icontains=q)
    return render(request, 'blog_list.html', {'worldcups': results, 'form': form})
