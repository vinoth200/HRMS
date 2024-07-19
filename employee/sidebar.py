"""
employee/sidebar.py

To set Horilla sidebar for employee
"""

from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

from base.templatetags.basefilters import is_reportingmanager

MENU = trans("Employee")
IMG_SRC = "images/ui/employees.svg"

SUBMENUS = [
    {
        "menu": trans("Profile"),
        "redirect": reverse("employee-profile"),
        "accessibility": "employee.sidebar.profile_accessibility",
    },
    {
        "menu": trans("Employees"),
        "redirect": reverse("employee-view"),
    },
    {
        "menu": trans("Document Requests"),
        "redirect": reverse("document-request-view"),
        "accessibility": "employee.sidebar.document_accessibility",
    },
    {
        "menu": trans("Shift Requests"),
        "redirect": reverse("shift-request-view"),
    },
    {
        "menu": trans("Work Type Requests"),
        "redirect": reverse("work-type-request-view"),
    },
    {
        "menu": trans("Rotating Shift Assign"),
        "redirect": reverse("rotating-shift-assign"),
        "accessibility": "employee.sidebar.rotating_shift_accessibility",
    },
    {
        "menu": trans("Rotating Work Type Assign"),
        "redirect": reverse("rotating-work-type-assign"),
        "accessibility": "employee.sidebar.rotating_work_type_accessibility",
    },
    
    {
        "menu": trans("Policies"),
        "redirect": reverse("view-policies"),
    },
    {
        "menu": trans("Organization Chart"),
        "redirect": reverse("organisation-chart"),
    },
]


def profile_accessibility(request, submenu, user_perms, *args, **kwargs):
    accessible = False
    try:
        accessible = getattr(
            request.session, "selected_company", "all"
        ) == "all" or request.user.employee_get.employee_work_info.company_id.id == getattr(
            request.session, "selected_company", -1
        )
    finally:
        return accessible


def document_accessibility(request, submenu, user_perms, *args, **kwargs):
    return request.user.has_perm(
        "horilla_documents.view_documentrequest"
    ) or is_reportingmanager(request.user)


def rotating_shift_accessibility(request, submenu, user_perms, *args, **kwargs):
    return request.user.has_perm(
        "base.view_rotatingshiftassign"
    ) or is_reportingmanager(request.user)


def rotating_work_type_accessibility(request, submenu, user_perms, *args, **kwargs):
    return request.user.has_perm(
        "base.view_rotatingworktypeassign"
    ) or is_reportingmanager(request.user)
