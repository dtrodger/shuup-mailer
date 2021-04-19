from django.views.generic import ListView

from shuup.apps.mailer.models import Company


class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100
