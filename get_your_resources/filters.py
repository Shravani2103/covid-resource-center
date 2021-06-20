import django_filters
from .models import *

class ResourceFilter(django_filters.FilterSet):
    class Meta:
        model = Resource
        fields = ['Res_name']

class HospitalFilter(django_filters.FilterSet):
    class Meta:
        model = Hospital
        fields = ['H_name','Area_id']

class HosresFilter(django_filters.FilterSet):
    class Meta:
        model = Hospital_resource
        fields = ['Res_name']

class PharmacyFilter(django_filters.FilterSet):
    class Meta:
        model = Pharmacy
        fields = ['P_name','Area_id']

class PharmresFilter(django_filters.FilterSet):
    class Meta:
        model = Pharm_res
        fields = ['Res_name']

class VaccinationFilter(django_filters.FilterSet):
    class Meta:
        model = vaccination_center
        fields = ['Vc_name','Area_id']

class VacresFilter(django_filters.FilterSet):
    class Meta:
        model = Vac_res
        fields = ['Res_name']

class StockistFilter(django_filters.FilterSet):
    class Meta:
        model = Stockist
        fields = ['S_fname']

class StockresFilter(django_filters.FilterSet):
    class Meta:
        model = Stockist_resource
        fields = ['Res_name']

class PlasmaFilter(django_filters.FilterSet):
    class Meta:
        model = Plasma_Donor
        fields = ['Blood_group']