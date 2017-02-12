from django.views.generic import TemplateView
from django.shortcuts import render


class BasicView(TemplateView):
    template_name = "restaurant/templates/base.html"
    kwargs = {}

    def get_context_data(self, **kwargs):
        self.context = super(BasicView, self).get_context_data(**kwargs)
        self.menu = self.context['url_name'] = self.request.resolver_match.url_name
        self.kwargs = kwargs

        return self.context

    def post(self, request, *args, **_kwargs):
        self.context = {}
        self.kwargs = _kwargs
        self.menu = self.context['url_name'] = self.request.resolver_match.url_name

        return render(request, 'restaurant/templates/base.html', self.context)


