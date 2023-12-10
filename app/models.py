from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    def __str__(self):
        return self.dname

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    deptno=models.OneToOneField(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename

class SalGrade(models.Model):
    grade=models.IntegerField()
    losal=models.IntegerField()
    hisal=models.IntegerField()

class Bonus(models.Model):
    id=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    comm=models.IntegerField()
    def __str__(self):
        return self.ename
