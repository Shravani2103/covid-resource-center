from django.db import models

# Create your models here.

class Area3(models.Model):
    Area_id = models.CharField(max_length=200, null=True)
    Area_name = models.CharField(max_length=200, null=True)
    Landmark = models.CharField(max_length=200, null=True)
    Street_name = models.CharField(max_length=200, null=True)
    Lane_no = models.CharField(max_length=200, null=True)
    Pincode = models.CharField(max_length=200, null=True)
    def __str__(self) :
        return str(self.Area_name)

class Industry(models.Model):
    Ind_id=models.CharField(max_length=200, null=True)
    Ind_name=models.CharField(max_length=200, null=True)
    Ind_license=models.CharField(max_length=200, null=True)
    Ind_rating=models.CharField(max_length=200, null=True)
    Area_id=models.ForeignKey(Area3, null=True, on_delete=models.SET_NULL)
    def __str__(self) :
        return str(self.Ind_name)


class Resource(models.Model):
    Res_id=models.CharField(max_length=200, null=True)
    Res_name=models.CharField(max_length=200, null=True)
    cost=models.CharField(max_length=200, null=True)
    use=models.CharField(max_length=200, null=True)
    Mfg_date=models.DateTimeField(max_length=200, null=True)
    Exp_date=models.DateTimeField(max_length=200, null=True)
    Ind_id=models.ForeignKey(Industry, null=True,on_delete=models.SET_NULL)
    Man_quantity=models.CharField(max_length=200, null=True)
    def __str__(self) :
        return str(self.Res_name)

class Hospital(models.Model):
    H_id=models.CharField(max_length=200, null=True)
    H_name=models.CharField(max_length=200, null=True)
    Area_id=models.ForeignKey(Area3, null=True,on_delete=models.SET_NULL)
    Total_beds=models.CharField(max_length=200, null=True)
    Beds_avail=models.CharField(max_length=200, null=True)
    H_ph_no=models.CharField(max_length=200, null=True)
    Shots_per_day=models.CharField(max_length=200, null=True)
    def __str__(self) :
       return str(self.H_name)

class Hospital_resource(models.Model):
   AVAILABILITY=(('Available','Available'),('Not Available','Not Available'))
   H_id=models.ForeignKey(Hospital, related_name='hres' , null=True,on_delete=models.SET_NULL)
   Res_name=models.ForeignKey(Resource, null=True, on_delete=models.SET_NULL)
   Res_quantity=models.CharField(max_length=200, null=True)
   Availability=models.CharField(max_length=200, null=True, choices=AVAILABILITY)
   def __str__(self) :
       return str(self.Res_name)

   

class Plasma_Donor(models.Model):
    BLOODGROUP=(('0+','0+'),('0-','0-'),('AB+','AB+'),('AB-','AB-'),('A-','A-'),('A+','A+'),('B-','B-'),('B+','B+'))
    SEX=(('F','F'),('M','M'))
    Don_id=models.CharField(max_length=200, null=True)
    Don_name=models.CharField(max_length=200, null=True)
    Don_age=models.CharField(max_length=200, null=True)
    D_ph_no=models.CharField(max_length=200, null=True)
    Blood_group=models.CharField(max_length=200, null=True, choices=BLOODGROUP)
    Pos_date=models.DateTimeField(max_length=200, null=True)
    Sex=models.CharField(max_length=200, null=True, choices=SEX)
    Hospital_id=models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)
    def __str__(self) :
        return str(self.Don_name)

class Pharmacy(models.Model):
    P_id=models.CharField(max_length=200, null=True)
    P_name=models.CharField(max_length=200, null=True)
    Area_id=models.ForeignKey(Area3, null=True, on_delete=models.SET_NULL)
    P_ph_no=models.CharField(max_length=200, null=True)
    Ratings=models.CharField(max_length=200, null=True)
    def __str__(self) :
        return str(self.P_name), str(self.Area_id)

class Pharm_res(models.Model):
   AVAILABILITY=(('Available','Available'),('Not Available','Not Available'))
   P_id=models.ForeignKey(Pharmacy, null=True, related_name= 'pres', on_delete= models.SET_NULL)
   Res_name=models.ForeignKey(Resource, null=True, on_delete= models.SET_NULL)
   Stock=models.CharField(max_length=200, null=True)
   Availability=models.CharField(max_length=200, null=True, choices=AVAILABILITY)
   def __str__(self) :
       return str(self.Res_name)

class Stockist(models.Model):
    Stockist_id=models.CharField(max_length=200, null=True)
    S_fname=models.CharField(max_length=200, null=True)
    S_mname=models.CharField(max_length=200, null=True)
    S_lname=models.CharField(max_length=200, null=True)
    Area_id=models.ForeignKey(Area3, null=True,on_delete=models.SET_NULL)
    Phno=models.CharField(max_length=200, null=True)
    Email_id=models.CharField(max_length=200, null=True)
    def __str__(self) :
        return str(self.S_fname),str(self.Area_id)
    
class Stockist_resource(models.Model):
   AVAILABILITY=(('Available','Available'),('Not Available','Not Available'))
   Stockist_id=models.ForeignKey(Stockist, null=True, related_name='Sres', on_delete=models.SET_NULL)
   Res_name=models.ForeignKey(Resource, null=True, on_delete=models.SET_NULL)
   Stock_bought=models.CharField(max_length=200, null=True)
   Availability=models.CharField(max_length=200, null=True, choices=AVAILABILITY)
   def __str__(self) :
       return str(self.Res_name)

class vaccination_center(models.Model):
     Vc_id=models.CharField(max_length=200, null=True)
     Vc_name=models.CharField(max_length=200, null=True)
     Area_id=models.ForeignKey(Area3, null=True,on_delete=models.SET_NULL)
     Shots_per_day=models.CharField(max_length=200, null=True)
     def __str__(self) :
        return str(self.Vc_name),str(self.Area_id)
    

class Vac_res(models.Model):
   AVAILABILITY=(('Available','Available'),('Not Available','Not Available'))
   Vc_id=models.ForeignKey(vaccination_center, null=True, related_name='vres', on_delete=models.SET_NULL)
   Res_name=models.ForeignKey(Resource, null=True, on_delete=models.SET_NULL)
   Res_quantity=models.CharField(max_length=200, null=True)
   Availability=models.CharField(max_length=200, null=True, choices=AVAILABILITY)
   def __str__(self) :
       return str(self.Res_name)



     
     