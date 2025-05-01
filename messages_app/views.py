from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
