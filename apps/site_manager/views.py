from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from .tasks import createBulkMail
from django.contrib.sites.shortcuts import get_current_site

from .models import UnsubscribeMassiveMail
from .forms import MassiveEmailForm



class SendMassiveEmail(LoginRequiredMixin, generic.edit.FormView):
    form_class = MassiveEmailForm
    template_name = 'site_manager/massive_mail.html'

    def form_valid(self, form):
        header = self.request.POST['headerMail']
        content = self.request.POST['contentMail']
        category = self.request.POST['category']
        to = self.request.POST['to']
        if self.request.user.is_staff:
            current_site = get_current_site(self.request)
            createBulkMail.s(header, content, category, to, str(current_site)).apply_async()
            return redirect(reverse_lazy('site_manager:send_mass_mail'))
        else:
            return redirect('/')

class Unsubscribe(generic.View):
    pass