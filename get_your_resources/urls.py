from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard , name= "dashboard"),
    path('resources/', views.resources , name="resources"),
    path('hospital/', views.hospital, name="hospital"),
    path('pharmacy/' , views.pharmacy , name= "pharmacy"),
    path('vaccination_centre/', views.vaccination_centre , name="vaccination_centre"),
    path('plasma_donors/',views.plasma_donors , name="plasma_donor"),
    path('stockist/', views.stockist , name= "stockist"),
    path('pharm_res/<str:pk_test>/', views.pharm_res , name ="pharm_res"),
    path('vac_res/<str:pk_test>/' , views.vac_res , name= "vac_res"),
    path('s_res/<str:pk_test>/', views.s_res , name="s_res"),
    path('h_res/<str:pk_test>/', views.h_res , name= "h_res"),
    path('createResources/',views.createResources, name="createResources"),
    path('updateResources/<str:pk>/',views.updateResources, name="updateResources"),
    path('updateResourcesP/<str:pk>/',views.updateResourcesP, name="updateResourcesP"),
    path('updateResourcesV/<str:pk>/',views.updateResourcesV, name="updateResourcesV"),
    path('updateResourcesS/<str:pk>/',views.updateResourcesS, name="updateResourcesS"),
    path('<id>/delete', views.delete_view ,name="delete"),
    path('<id>/deleteH', views.delete_viewH ,name="deleteH"),
    path('<id>/deleteV', views.delete_viewV ,name="deleteV"),
    path('<id>/deleteS', views.delete_viewS ,name="deleteS"),
    path('register/',views.registerPage , name="register"),
    path('login/',views.loginPage , name="login"),
    path('logout/',views.Logoutuser,name="logout"),
    path('tests/',views.error,name="tests"),
    path('industry/',views.industry,name="industry"),
    #path('population-chart/', views.population_chart, name='population-chart'),
    #path('Chart/', views.ChartView.as_view(),name="chart"),
    
    
]


   



