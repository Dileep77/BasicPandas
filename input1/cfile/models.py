from django.db import models
from adaptor.model import CsvModel
# Create your models here.
class output(CsvModel):
    number= IntegerField()
    Length= IntegerField()
    class Meta:
        delimiter= " "
