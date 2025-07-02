from django.contrib import admin

import data_wizard


from .models import Cliente

# Register your models here.
admin.site.register(Cliente)

data_wizard.register(Cliente)


from .models import Table_Est_TecNM

# Register your models here.
admin.site.register(Table_Est_TecNM)

data_wizard.register(Table_Est_TecNM)