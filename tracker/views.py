from django.shortcuts import render
from .forms import TrackForm

# Create your views here.
from django.views.generic import CreateView


def home(request):
    return render(request, "tracker/home.html")


def contactview(request):
    return render(request, "tracker/contact.html")


class TrackView(CreateView):
    template_name = "tracker/track_page.html"
    form_class = TrackForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)