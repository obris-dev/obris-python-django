from django.views.generic import TemplateView


class ExampleTemplateView(TemplateView):
    template_name = "templates/index.html"
