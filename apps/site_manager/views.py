from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from .tasks import createBulkMail
from django.contrib.sites.shortcuts import get_current_site

from .models import Category
from .forms import MassiveEmailForm

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from apps.users.models import CustomUser
from apps.users.models import UserProfile

from .token import account_activation_token


class SendMassiveEmail(LoginRequiredMixin, generic.edit.FormView):
    form_class = MassiveEmailForm
    template_name = 'site_manager/massive_mail.html'

    def form_valid(self, form):
        header = self.request.POST['headerMail']
        content = self.request.POST['contentMail']
        category = self.request.POST['category']
        to = self.request.POST['to']
        if self.request.user.is_staff:
            domain = get_current_site(self.request).domain
            createBulkMail.s(header, content, category, to, domain).apply_async()
            return redirect(reverse_lazy('site_manager:send_mass_mail'))
        else:
            return redirect('/')

class Unsubscribe(generic.TemplateView):
    template_name = 'site_manager/unsubscribe_done.html'

    def get(self, request, uidb64, uidb64cat, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            userProfile = UserProfile.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            userProfile = None
        if userProfile is not None and account_activation_token.check_token(userProfile.pk, token):
            catid = force_text(urlsafe_base64_decode(uidb64cat))
            objCat = get_object_or_404(Category, pk=catid)
            userProfile.cat_unsubscribed.add(objCat)
            userProfile.save()
        return super().get(self, request, uidb64, uidb64cat, token)
