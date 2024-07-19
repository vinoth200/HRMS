"""
horilla_automations/views/cbvs.py
"""

from typing import Any

from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _trans

from horilla_automations import models
from horilla_automations.filters import AutomationFilter
from horilla_automations.forms import AutomationForm
from horilla_views.generic.cbv import views


class AutomationSectionView(views.HorillaSectionView):
    """
    AutomationSectionView
    """

    nav_url = reverse_lazy("mail-automations-nav")
    view_url = reverse_lazy("mail-automations-list-view")
    view_container_id = "listContainer"

    script_static_paths = [
        "static/automation/automation.js",
    ]

    template_name = "horilla_automations/section_view.html"


class AutomationNavView(views.HorillaNavView):
    """
    AutomationNavView
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.create_attrs = f"""
            hx-get="{reverse_lazy("create-automation")}"
            hx-target="#genericModalBody"
            data-target="#genericModal"
            data-toggle="oh-modal-toggle"
        """

    nav_title = _trans("Automations")
    search_url = reverse_lazy("mail-automations-list-view")
    search_swap_target = "#listContainer"


class AutomationFormView(views.HorillaFormView):
    """
    AutomationFormView
    """

    form_class = AutomationForm
    model = models.MailAutomation
    new_display_title = _trans("New Automation")
    template_name = "horilla_automations/automation_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        instance = models.MailAutomation.objects.filter(pk=self.kwargs["pk"]).first()
        kwargs["instance"] = instance

        return kwargs

    def form_valid(self, form: AutomationForm) -> views.HttpResponse:
        if form.is_valid():
            message = "New automation added"
            if form.instance.pk:
                message = "Automation updated"
            form.save()

            messages.success(self.request, _trans(message))
            return self.HttpResponse()
        return super().form_valid(form)


class AutomationListView(views.HorillaListView):
    """
    AutomationListView
    """

    row_attrs = """
            hx-get="{detailed_url}?instance_ids={ordered_ids}"
            hx-target="#genericModalBody"
            data-toggle="oh-modal-toggle"
            data-target="#genericModal"
        """

    model = models.MailAutomation
    search_url = reverse_lazy("mail-automations-list-view")
    filter_class = AutomationFilter

    actions = [
        {
            "action": "Edit",
            "icon": "create-outline",
            "attrs": """
                class="oh-btn oh-btn--light-bkg w-100"
                hx-get="{edit_url}"
                hx-target="#genericModalBody"
                data-target="#genericModal"
                data-toggle="oh-modal-toggle"
            """,
        },
        {
            "action": "Delete",
            "icon": "trash-outline",
            "attrs": """
            class="oh-btn oh-btn--light-bkg w-100 tex-danger"
            onclick="
                event.stopPropagation();
                confirm('Do you want to delete the automation?','{delete_url}')
            "
            """,
        },
    ]

    columns = [
        ("Title", "title"),
        ("Model", "model"),
        ("Email Mapping", "get_mail_to_display"),
    ]


class AutomationDetailedView(views.HorillaDetailedView):
    """
    AutomationDetailedView
    """

    model = models.MailAutomation
    title = "Detailed View"
    header = {
        "title": "title",
        "subtitle": "title",
        "avatar": "get_avatar",
    }
    body = [
        ("Model", "model"),
        ("Mail Templates", "mail_template"),
        ("Mail To", "get_mail_to_display"),
        ("Trigger", "trigger_display"),
    ]
    actions = [
        {
            "action": "Edit",
            "icon": "create-outline",
            "attrs": """
            hx-get="{edit_url}"
            hx-target="#genericModalBody"
            data-toggle="oh-modal-toggle"
            data-target="#genericModal"
            class="oh-btn oh-btn--info w-50"
            """,
        },
        {
            "action": "Delete",
            "icon": "trash-outline",
            "attrs": """
            class="oh-btn oh-btn--danger w-50"
            onclick="
                confirm('Do you want to delete the automation?','{delete_url}')
            "
            """,
        },
    ]
