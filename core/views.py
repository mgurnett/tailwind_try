from django.views.generic import TemplateView

colors = [
    {"function": "primary",             "hex": "#6686b9", "name": "Ship Cove", "notes": "Dark accent"},
    # {"function": "primary-content",     "hex": "#6686b9", "name": "", "notes": ""},
    {"function": "secondary",           "hex": "#2b4881", "name": "", "notes": ""},
    # {"function": "secondary-content",   "hex": "#2b4881", "name": "", "notes": ""},
    {"function": "accent",              "hex": "#39c1f0", "name": "", "notes": ""},
    # {"function": "accent-content",      "hex": "#39c1f0", "name": "Bay of Many", "notes": "text"},
    {"function": "neutral",             "hex": "#39c1f0", "name": "Picton Blue", "notes": "Primary - highlights"},
    # {"function": "neutral-content",     "hex": "#39c1f0", "name": "", "notes": ""},
    {"function": "base-100",            "hex": "#f1eff0", "name": "Bon Jour", "notes": "page background"},
    {"function": "base-200",            "hex": "#d2d0d1", "name": "", "notes": "slightly darker than base-100"},
    {"function": "base-300",            "hex": "#b3b1b2", "name": "", "notes": "slightly darker than base-200"},
    # {"function": "base-content",        "hex": "#141414", "name": "", "notes": ""},
    {"function": "info",                "hex": "#7fbed9", "name": "Bermuda", "notes": "Light accent"},
    # {"function": "info-content",        "hex": "#7fbed9", "name": "", "notes": ""},
    {"function": "success",             "hex": "#46b480", "name": "Ocean Green", "notes": "Good"},
    # {"function": "success-content",     "hex": "#46b480", "name": "", "notes": ""},
    {"function": "warning",             "hex": "#c4a448", "name": "Roti", "notes": "Warning"},
    # {"function": "warning-content",     "hex": "#c4a448", "name": "", "notes": ""},
    {"function": "error",               "hex": "#f44336", "name": "Pomegranate", "notes": "Danger"},
    # {"function": "error-content",       "hex": "#f44336", "name": "", "notes": ""},
    {"function": "unknown",             "hex": "#999999", "name": "", "notes": "alt text or basic button"},
    {"function": "unknown2",            "hex": "#677AAF", "name": "Wild Blue Yonder", "notes": "Main text color"},
    {"function": "goofy",               "hex": "#FF10F0", "name": "Pink", "notes": "Test color"},
]


class HomeView(TemplateView):
    template_name = "home.html"


class TemplateView(TemplateView):
    template_name = "template_sheet.html"

    def get_context_data(self, **kwargs):
 
        context = super(TemplateView, self).get_context_data(**kwargs)
        # print (colors)
        context['colors'] = colors
        return context