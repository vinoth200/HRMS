# """
# admin.py

# Used to register models on admin site
# """

# from django.contrib import admin

# from payroll.models.models import (
#     Allowance,
#     Contract,
#     Deduction,
#     FilingStatus,
#     LoanAccount,
#     MultipleCondition,
#     Payslip,
#     Reimbursement,
#     ReimbursementrequestComment,
#     WorkRecord,
# )
# from payroll.models.tax_models import PayrollSettings, TaxBracket

# # Register your models here.
# admin.site.register(FilingStatus)
# admin.site.register(TaxBracket)
# admin.site.register([Contract, WorkRecord])
# admin.site.register(Allowance)
# admin.site.register(Deduction)
# admin.site.register(Payslip)
# admin.site.register(PayrollSettings)
# admin.site.register(LoanAccount)
# admin.site.register(Reimbursement)
# admin.site.register(ReimbursementrequestComment)
# admin.site.register(MultipleCondition)
