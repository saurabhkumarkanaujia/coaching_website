from django.db import models

class Education(models.Model):
    Education_name=models.CharField(max_length=245)
    Education_university=models.CharField(max_length=245)
    Education_year=models.CharField(max_length=245)
    Education_obtainedmarks=models.CharField(max_length=4)
    Education_maxmarks=models.CharField(max_length=4)
    Education_per=models.CharField(max_length=4)
    Education_remarks=models.CharField(max_length=245)
    Education_user_id=models.CharField(max_length=10)


# Create your models here.
