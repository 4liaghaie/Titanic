from django.db import models

class TitanicPassenger(models.Model):
    passenger_id = models.IntegerField(primary_key=True)
    survived = models.BooleanField()
    pclass = models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')])
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    age = models.FloatField(null=True, blank=True)
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    ticket = models.CharField(max_length=20)
    fare = models.FloatField()
    cabin = models.CharField(max_length=20, blank=True, null=True)
    embarked = models.CharField(max_length=1, choices=[('C', 'Cherbourg'), ('S', 'Southampton'), ('Q', 'Queenstown')])

    def __str__(self):
        return self.name
