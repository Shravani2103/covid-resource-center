from django.contrib import admin

# Register your models here.
from .models import Area3
from .models import Industry
from .models import Resource
from .models import Hospital_resource
from .models import Hospital
from .models import Plasma_Donor
from .models import Pharm_res
from .models import Pharmacy
from .models import Stockist_resource
from .models import Stockist
from .models import Vac_res
from .models import vaccination_center






admin.site.register(Area3)
admin.site.register(Industry)
admin.site.register(Resource)
admin.site.register(Hospital_resource)
admin.site.register(Hospital)
admin.site.register(Plasma_Donor)
admin.site.register(Pharm_res)
admin.site.register(Pharmacy)
admin.site.register(Stockist_resource)
admin.site.register(Stockist)
admin.site.register(Vac_res)
admin.site.register(vaccination_center)




