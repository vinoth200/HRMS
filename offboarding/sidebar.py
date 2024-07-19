"""
offboarding/sidebar.py
"""

from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

from base.context_processors import resignation_request_enabled
from offboarding.templatetags.offboarding_filter import (
    any_manager,
    is_offboarding_employee,
)

MENU = trans()
IMG_SRC = 
ACCESSIBILITY = 


SUBMENUS = [
    # {
    #     "menu": trans("Exit Process"),
    #     "redirect": reverse("offboarding-pipeline"),
    # },
    # {
    #     "menu": trans("Resignation Letters"),
    #     "redirect": reverse("resignation-request-view"),
    #     "accessibility": "offboarding.sidebar.resignation_letter_accessibility",
    # },
]


def offboarding_accessibility(request, menu, user_perms, *args, **kwargs):
    accessible = False
    try:
        accessible = (
            request.user.has_perm("offboarding.view_offboarding")
            or any_manager(request.user.employee_get)
            or is_offboarding_employee(request.user.employee_get)
        )
    finally:
        return accessible


def resignation_letter_accessibility(request, menu, user_perms, *args, **kwargs):
    return resignation_request_enabled(request)[
        "enabled_resignation_request"
    ] and request.user.has_perm("offboarding.view_resignationletter")
