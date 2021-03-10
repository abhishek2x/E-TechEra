from django.shortcuts import render
# from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q

from django.views.generic.edit import (UpdateView,
                                        CreateView,
                                        DeleteView )

# Create your views here.

from .models import *


def landing(request):
    context = {}
    return render(request, 'skills/landing.html', context)


def skills(request):
    context = {}
    return render(request, 'skills/skills.html', context)


@method_decorator(login_required, name="dispatch")
class LearnerDetailView(DetailView):
    model = Learner


@method_decorator(login_required, name="dispatch")
class LearnerUpdateView(UpdateView):
    model = Learner
    fields = ["name", "profession", "institution", "description",
              "linkedin_profile", "github_profile", "Other_profile", "profile_pic"]

# @method_decorator(login_required, name="dispatch")
# class LearnerListView(ListView):
#     model = Learner
#     paginate_by = 8
#
#     def get_queryset(self):
#         si = self.request.GET.get("si")
#
#         if si == None:
#             si = ""
#
#         profList = Learner.objects.filter(name__icontains=si)
#
#         return profList


